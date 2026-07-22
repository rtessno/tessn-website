#!/usr/bin/env python3
"""Verify the deployed Tessn GitHub Pages preview over HTTP."""

from __future__ import annotations

import argparse
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin
from urllib.request import Request, urlopen


@dataclass(frozen=True)
class Check:
    path: str
    expected_status: int
    expected_content_type: str | None = None
    required_text: tuple[str, ...] = ()


CHECKS = (
    Check("", 200, "text/html", ('name="robots" content="noindex,nofollow"',)),
    Check("current/", 200, "text/html", ('name="robots" content="noindex,nofollow"',)),
    Check("pilot/", 200, "text/html", ('name="robots" content="noindex,nofollow"',)),
    Check("about/", 200, "text/html", ('name="robots" content="noindex,nofollow"',)),
    Check("privacy/", 200, "text/html", ('name="robots" content="noindex,nofollow"',)),
    Check("terms/", 200, "text/html", ('name="robots" content="noindex,nofollow"',)),
    Check("assets/css/site.css", 200, "text/css"),
    Check("assets/js/site.js", 200, ("javascript", "text/plain")),
    Check("assets/images/tessn-mark.svg", 200, "image/svg+xml"),
    Check("assets/images/current-workflow.svg", 200, "image/svg+xml"),
    Check("robots.txt", 200, "text/plain", ("Disallow: /",)),
    Check(
        "missing-route/nested/",
        404,
        "text/html",
        ("This investigation reached a dead end.", '<base href="/tessn-website/">'),
    ),
)


@dataclass
class Result:
    url: str
    expected_status: int
    actual_status: int | None
    content_type: str
    ok: bool
    detail: str


def content_type_matches(actual: str, expected: str | tuple[str, ...] | None) -> bool:
    if expected is None:
        return True
    normalized = actual.lower()
    if isinstance(expected, tuple):
        return any(candidate in normalized for candidate in expected)
    return expected.lower() in normalized


def fetch(url: str, timeout: float) -> tuple[int, str, str]:
    request = Request(url, headers={"User-Agent": "Tessn-Pages-Verification/1.0"})
    try:
        with urlopen(request, timeout=timeout) as response:
            body = response.read().decode("utf-8", errors="replace")
            return response.status, response.headers.get("Content-Type", ""), body
    except HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")
        return error.code, error.headers.get("Content-Type", ""), body


def run_checks(base_url: str, timeout: float) -> list[Result]:
    results: list[Result] = []
    for check in CHECKS:
        url = urljoin(base_url, check.path)
        try:
            status, content_type, body = fetch(url, timeout)
        except (TimeoutError, URLError, OSError) as error:
            results.append(
                Result(url, check.expected_status, None, "", False, f"request failed: {error}")
            )
            continue

        problems: list[str] = []
        if status != check.expected_status:
            problems.append(f"expected HTTP {check.expected_status}, received {status}")
        if not content_type_matches(content_type, check.expected_content_type):
            problems.append(
                f"unexpected content type {content_type!r}; expected {check.expected_content_type!r}"
            )
        for required in check.required_text:
            if required not in body:
                problems.append(f"response is missing required text {required!r}")

        results.append(
            Result(
                url=url,
                expected_status=check.expected_status,
                actual_status=status,
                content_type=content_type,
                ok=not problems,
                detail="; ".join(problems) if problems else "passed",
            )
        )
    return results


def build_report(base_url: str, results: list[Result], attempt: int, attempts: int) -> str:
    passed = sum(result.ok for result in results)
    status = "PASS" if passed == len(results) else "FAIL"
    lines = [
        "<!-- tessn-pages-verification -->",
        f"## GitHub Pages deployment verification: {status}",
        "",
        f"Base URL: `{base_url}`",
        f"Attempt: {attempt}/{attempts}",
        f"Checks passed: {passed}/{len(results)}",
        "",
        "| URL | Expected | Actual | Result |",
        "| --- | ---: | ---: | --- |",
    ]
    for result in results:
        actual = "request failed" if result.actual_status is None else str(result.actual_status)
        outcome = "PASS" if result.ok else f"FAIL — {result.detail}"
        lines.append(
            f"| `{result.url}` | {result.expected_status} | {actual} | {outcome} |"
        )
    lines.extend(
        [
            "",
            "Preview indexing controls and the no-public-download gate remain required after deployment.",
        ]
    )
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", required=True)
    parser.add_argument("--attempts", type=int, default=12)
    parser.add_argument("--delay", type=float, default=10.0)
    parser.add_argument("--timeout", type=float, default=20.0)
    parser.add_argument("--report-file", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    base_url = args.base_url.rstrip("/") + "/"
    final_results: list[Result] = []

    for attempt in range(1, args.attempts + 1):
        final_results = run_checks(base_url, args.timeout)
        if all(result.ok for result in final_results):
            report = build_report(base_url, final_results, attempt, args.attempts)
            args.report_file.write_text(report, encoding="utf-8")
            print(report)
            return 0
        if attempt < args.attempts:
            time.sleep(args.delay)

    report = build_report(base_url, final_results, args.attempts, args.attempts)
    args.report_file.write_text(report, encoding="utf-8")
    print(report, file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
