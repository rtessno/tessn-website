#!/usr/bin/env python3
"""Validate the dependency-free Tessn static site before Pages deployment."""

from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

SITE_ROOT = Path(__file__).resolve().parents[1] / "site"
EXPECTED_FILES = {
    "index.html",
    "404.html",
    "current/index.html",
    "pilot/index.html",
    "about/index.html",
    "trust/index.html",
    "privacy/index.html",
    "terms/index.html",
    "assets/css/site.css",
    "assets/css/pilot.css",
    "assets/js/site.js",
    "assets/images/current-workflow.svg",
    "assets/images/tessn-mark.svg",
    "robots.txt",
    ".nojekyll",
}
INSTALLER_SUFFIXES = {
    ".appimage",
    ".deb",
    ".dmg",
    ".exe",
    ".msi",
    ".pkg",
    ".rpm",
    ".tar",
    ".tgz",
    ".zip",
}


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.references: list[tuple[str, str]] = []
        self.robots_content: str | None = None
        self.nav_labels: list[str | None] = []
        self.has_header = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "header":
            self.has_header = True
        if tag == "nav":
            self.nav_labels.append(attributes.get("aria-label"))
        if tag == "meta" and attributes.get("name", "").lower() == "robots":
            self.robots_content = attributes.get("content")
        for attribute in ("href", "src"):
            value = attributes.get(attribute)
            if value:
                self.references.append((attribute, value))


def resolve_internal_reference(page: Path, value: str) -> Path | None:
    parts = urlsplit(value)
    if parts.scheme or parts.netloc or value.startswith(("mailto:", "tel:", "data:")):
        return None
    if not parts.path:
        return None

    path = unquote(parts.path)
    if path.startswith("/"):
        # Project Pages is hosted under /tessn-website/. Treat that prefix as site root.
        prefix = "/tessn-website/"
        if not path.startswith(prefix):
            return SITE_ROOT / path.lstrip("/")
        path = path[len(prefix) :]
        target = SITE_ROOT / path
    else:
        target = page.parent / path

    target = target.resolve()
    try:
        target.relative_to(SITE_ROOT.resolve())
    except ValueError:
        raise ValueError(f"reference escapes site root: {value}") from None

    if path.endswith("/") or target.is_dir():
        target = target / "index.html"
    return target


def validate_page(page: Path) -> list[str]:
    errors: list[str] = []
    parser = PageParser()
    parser.feed(page.read_text(encoding="utf-8"))

    robots = (parser.robots_content or "").lower()
    if "noindex" not in robots:
        errors.append(f"{page.relative_to(SITE_ROOT)}: missing preview noindex directive")

    if parser.has_header and not parser.nav_labels:
        errors.append(f"{page.relative_to(SITE_ROOT)}: header has no primary navigation")
    for label in parser.nav_labels:
        if not label:
            errors.append(f"{page.relative_to(SITE_ROOT)}: nav is missing aria-label")

    for attribute, value in parser.references:
        suffix = Path(urlsplit(value).path).suffix.lower()
        if attribute == "href" and suffix in INSTALLER_SUFFIXES:
            errors.append(
                f"{page.relative_to(SITE_ROOT)}: public download link is prohibited ({value})"
            )
        try:
            target = resolve_internal_reference(page, value)
        except ValueError as exc:
            errors.append(f"{page.relative_to(SITE_ROOT)}: {exc}")
            continue
        if target is not None and not target.exists():
            errors.append(
                f"{page.relative_to(SITE_ROOT)}: broken {attribute}={value!r} "
                f"(expected {target.relative_to(SITE_ROOT)})"
            )

    return errors


def validate_pilot_boundary() -> list[str]:
    errors: list[str] = []
    pilot_path = SITE_ROOT / "pilot/index.html"
    privacy_path = SITE_ROOT / "privacy/index.html"
    if not pilot_path.exists() or not privacy_path.exists():
        return errors

    pilot = pilot_path.read_text(encoding="utf-8")
    privacy = privacy_path.read_text(encoding="utf-8")

    if "github.com/rtessno" in pilot:
        errors.append("pilot/index.html: public GitHub profile must not be used as pilot intake")
    if "Do not submit customer evidence" not in pilot:
        errors.append("pilot/index.html: missing initial-intake sensitive-evidence warning")
    if "Dedicated email pending" not in pilot:
        errors.append("pilot/index.html: pending contact state is not explicit")
    if "Do not submit customer evidence" not in privacy:
        errors.append("privacy/index.html: missing sensitive-information prohibition")
    if "does not include an intake form" not in privacy:
        errors.append("privacy/index.html: direct-collection behavior is not documented")

    return errors


def validate_trust_boundary() -> list[str]:
    errors: list[str] = []
    trust_path = SITE_ROOT / "trust/index.html"
    if not trust_path.exists():
        return errors

    trust = trust_path.read_text(encoding="utf-8")
    required = (
        "No certification claim",
        "No outcome guarantee",
        "Tessn is an umbrella brand",
        "not a security assessment",
        "Initial outreach must not include",
    )
    for text in required:
        if text not in trust:
            errors.append(f"trust/index.html: missing required boundary text {text!r}")

    return errors


def main() -> int:
    errors: list[str] = []

    if not SITE_ROOT.is_dir():
        print(f"ERROR: site root not found: {SITE_ROOT}", file=sys.stderr)
        return 1

    for relative_path in sorted(EXPECTED_FILES):
        if not (SITE_ROOT / relative_path).exists():
            errors.append(f"missing required file: {relative_path}")

    html_pages = sorted(SITE_ROOT.rglob("*.html"))
    if not html_pages:
        errors.append("no HTML pages found")
    for page in html_pages:
        errors.extend(validate_page(page))

    errors.extend(validate_pilot_boundary())
    errors.extend(validate_trust_boundary())

    robots = SITE_ROOT / "robots.txt"
    if robots.exists() and "Disallow: /" not in robots.read_text(encoding="utf-8"):
        errors.append("robots.txt must keep preview crawling disabled")

    if errors:
        print("Static site validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(html_pages)} HTML pages and {len(EXPECTED_FILES)} required files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
