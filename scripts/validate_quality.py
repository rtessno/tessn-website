#!/usr/bin/env python3
"""Validate static accessibility, asset budgets, and external-request boundaries."""

from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

REPO_ROOT = Path(__file__).resolve().parents[1]
SITE_ROOT = REPO_ROOT / "site"

MAX_HTML_BYTES = 80_000
MAX_CSS_BYTES = 120_000
MAX_JS_BYTES = 50_000
MAX_SVG_BYTES = 250_000
ALLOWED_EXTERNAL_HOSTS: set[str] = set()


class QualityParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.skip_targets: list[str] = []
        self.images: list[dict[str, str | None]] = []
        self.references: list[tuple[str, str]] = []
        self.heading_levels: list[int] = []
        self.main_count = 0
        self.footer_count = 0
        self.html_lang: str | None = None
        self.title_text = ""
        self.in_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "html":
            self.html_lang = attributes.get("lang")
        if tag == "title":
            self.in_title = True
        if tag == "main":
            self.main_count += 1
        if tag == "footer":
            self.footer_count += 1
        if tag in {f"h{level}" for level in range(1, 7)}:
            self.heading_levels.append(int(tag[1]))
        element_id = attributes.get("id")
        if element_id:
            self.ids.add(element_id)
        if tag == "a":
            href = attributes.get("href")
            classes = (attributes.get("class") or "").split()
            if href:
                self.references.append(("href", href))
            if "skip-link" in classes and href:
                self.skip_targets.append(href)
        if tag == "img":
            self.images.append(attributes)
        if tag in {"script", "link", "source", "iframe"}:
            for attribute in ("src", "href", "srcset"):
                value = attributes.get(attribute)
                if value:
                    self.references.append((attribute, value))

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_text += data


def validate_page(page: Path) -> list[str]:
    errors: list[str] = []
    parser = QualityParser()
    parser.feed(page.read_text(encoding="utf-8"))
    relative = page.relative_to(SITE_ROOT)

    if not parser.html_lang:
        errors.append(f"{relative}: html element is missing lang")
    if not parser.title_text.strip():
        errors.append(f"{relative}: title is empty")
    if parser.main_count != 1:
        errors.append(f"{relative}: expected exactly one main landmark")
    if parser.footer_count != 1:
        errors.append(f"{relative}: expected exactly one footer landmark")
    if not parser.heading_levels or parser.heading_levels[0] != 1:
        errors.append(f"{relative}: first heading must be h1")
    if parser.heading_levels.count(1) != 1:
        errors.append(f"{relative}: expected exactly one h1")
    for previous, current in zip(parser.heading_levels, parser.heading_levels[1:]):
        if current > previous + 1:
            errors.append(f"{relative}: heading level jumps from h{previous} to h{current}")

    for target in parser.skip_targets:
        if not target.startswith("#") or target[1:] not in parser.ids:
            errors.append(f"{relative}: skip link target {target!r} does not exist")
    if parser.main_count and not parser.skip_targets:
        errors.append(f"{relative}: missing skip link")

    for image in parser.images:
        if "alt" not in image:
            errors.append(f"{relative}: image is missing alt attribute ({image.get('src')})")
        if image.get("width") and not str(image["width"]).isdigit():
            errors.append(f"{relative}: image width must be numeric")
        if image.get("height") and not str(image["height"]).isdigit():
            errors.append(f"{relative}: image height must be numeric")

    for attribute, value in parser.references:
        parts = urlsplit(value)
        if parts.scheme in {"http", "https"} and parts.netloc not in ALLOWED_EXTERNAL_HOSTS:
            errors.append(f"{relative}: unexpected external {attribute} reference {value!r}")
        if parts.scheme == "//":
            errors.append(f"{relative}: protocol-relative reference is prohibited ({value!r})")

    return errors


def validate_asset_budgets() -> list[str]:
    errors: list[str] = []
    limits = {
        ".html": MAX_HTML_BYTES,
        ".css": MAX_CSS_BYTES,
        ".js": MAX_JS_BYTES,
        ".svg": MAX_SVG_BYTES,
    }
    for path in sorted(SITE_ROOT.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in limits:
            continue
        size = path.stat().st_size
        limit = limits[path.suffix.lower()]
        if size > limit:
            errors.append(
                f"{path.relative_to(SITE_ROOT)}: {size} bytes exceeds {limit}-byte budget"
            )
    return errors


def main() -> int:
    errors: list[str] = []
    for page in sorted(SITE_ROOT.rglob("*.html")):
        errors.extend(validate_page(page))
    errors.extend(validate_asset_budgets())

    if errors:
        print("Static quality validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Static accessibility, asset budgets, and external-request boundaries passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
