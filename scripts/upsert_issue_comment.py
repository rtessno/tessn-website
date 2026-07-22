#!/usr/bin/env python3
"""Create or update a marker-based GitHub issue comment using the REST API."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any
from urllib.error import HTTPError
from urllib.request import Request, urlopen

API_ROOT = "https://api.github.com"


def request_json(
    method: str,
    path: str,
    token: str,
    payload: dict[str, Any] | None = None,
) -> Any:
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    request = Request(
        f"{API_ROOT}{path}",
        data=data,
        method=method,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "Tessn-Pages-Verification/1.0",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    try:
        with urlopen(request, timeout=30) as response:
            body = response.read().decode("utf-8")
            return json.loads(body) if body else None
    except HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub API {method} {path} failed: {error.code} {detail}") from error


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", required=True, help="owner/name")
    parser.add_argument("--issue", required=True, type=int)
    parser.add_argument("--body-file", required=True, type=Path)
    parser.add_argument("--marker", required=True)
    parser.add_argument("--open-only", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        print("GITHUB_TOKEN is required", file=sys.stderr)
        return 1

    issue = request_json(
        "GET", f"/repos/{args.repository}/issues/{args.issue}", token
    )
    if args.open_only and issue.get("state") != "open":
        print(f"Issue #{args.issue} is closed; verification comment not updated.")
        return 0

    body = args.body_file.read_text(encoding="utf-8")
    if args.marker not in body:
        body = f"{args.marker}\n{body}"

    comments = request_json(
        "GET", f"/repos/{args.repository}/issues/{args.issue}/comments?per_page=100", token
    )
    existing = next(
        (comment for comment in comments if args.marker in comment.get("body", "")),
        None,
    )

    if existing:
        request_json(
            "PATCH",
            f"/repos/{args.repository}/issues/comments/{existing['id']}",
            token,
            {"body": body},
        )
        print(f"Updated verification comment on issue #{args.issue}.")
    else:
        request_json(
            "POST",
            f"/repos/{args.repository}/issues/{args.issue}/comments",
            token,
            {"body": body},
        )
        print(f"Created verification comment on issue #{args.issue}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
