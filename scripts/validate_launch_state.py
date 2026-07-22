#!/usr/bin/env python3
"""Validate Tessn preview and launch metadata state."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

REPO_ROOT = Path(__file__).resolve().parents[1]
SITE_ROOT = REPO_ROOT / "site"
STATE_PATH = REPO_ROOT / "docs" / "launch" / "launch-state.json"
ALLOWED_STATUSES = {"preview", "launch_candidate", "launched"}


def read_html_pages(site_root: Path) -> list[Path]:
    return sorted(site_root.rglob("*.html"))


def validate_https_url(value: str, expected_domain: str) -> list[str]:
    errors: list[str] = []
    parsed = urlsplit(value)
    if parsed.scheme != "https":
        errors.append("canonical_base_url must use https")
    if parsed.netloc != expected_domain:
        errors.append("canonical_base_url host must match custom_domain")
    if parsed.path != "/" or parsed.query or parsed.fragment:
        errors.append("canonical_base_url must end at the domain root with a trailing slash")
    return errors


def validate_state(data: dict, repo_root: Path = REPO_ROOT) -> list[str]:
    errors: list[str] = []
    site_root = repo_root / "site"
    status = data.get("status")

    if data.get("schema_version") != 1:
        errors.append("schema_version must equal 1")
    if status not in ALLOWED_STATUSES:
        errors.append(f"status must be one of {sorted(ALLOWED_STATUSES)}")
        return errors

    pages = read_html_pages(site_root)
    robots_path = site_root / "robots.txt"
    robots = robots_path.read_text(encoding="utf-8") if robots_path.exists() else ""
    cname_path = site_root / "CNAME"
    sitemap_path = site_root / "sitemap.xml"

    draft_path = data.get("social_preview", {}).get("draft_path")
    if not isinstance(draft_path, str) or not draft_path:
        errors.append("social_preview.draft_path is required")
    else:
        draft_asset = repo_root / draft_path
        if not draft_asset.exists():
            errors.append(f"social preview draft asset does not exist: {draft_path}")
        elif draft_asset.suffix.lower() == ".svg":
            content = draft_asset.read_text(encoding="utf-8")
            prohibited = ("Tessn Solutions LLC", "generally available", "guaranteed root cause")
            for phrase in prohibited:
                if phrase.lower() in content.lower():
                    errors.append(f"social preview contains prohibited phrase: {phrase}")

    if status == "preview":
        for field in ("custom_domain", "canonical_base_url", "approved_by", "approved_on"):
            if data.get(field) is not None:
                errors.append(f"{field} must be null in preview status")
        for field in (
            "indexing_approved",
            "legal_entity_approved",
            "structured_data_approved",
            "analytics_approved",
        ):
            if data.get(field) is not False:
                errors.append(f"{field} must be false in preview status")
        if cname_path.exists():
            errors.append("site/CNAME must not exist in preview status")
        if sitemap_path.exists():
            errors.append("site/sitemap.xml must not exist in preview status")
        if "Disallow: /" not in robots:
            errors.append("robots.txt must disallow crawling in preview status")
        for page in pages:
            html = page.read_text(encoding="utf-8").lower()
            relative = page.relative_to(site_root)
            if "noindex" not in html:
                errors.append(f"{relative}: preview page must contain noindex")
            if 'rel="canonical"' in html or "rel='canonical'" in html:
                errors.append(f"{relative}: canonical link is prohibited in preview status")
            if 'property="og:url"' in html or "property='og:url'" in html:
                errors.append(f"{relative}: og:url is prohibited in preview status")
            if "application/ld+json" in html:
                errors.append(f"{relative}: structured data is prohibited in preview status")
        social = data.get("social_preview", {})
        if social.get("public_url") is not None:
            errors.append("social_preview.public_url must be null in preview status")
        if social.get("platform_ready_raster") is not False:
            errors.append("social_preview.platform_ready_raster must be false in preview status")
        return errors

    custom_domain = data.get("custom_domain")
    canonical = data.get("canonical_base_url")
    if not isinstance(custom_domain, str) or not re.fullmatch(r"[A-Za-z0-9.-]+", custom_domain):
        errors.append("custom_domain must be a hostname in launch_candidate or launched status")
    if not isinstance(canonical, str):
        errors.append("canonical_base_url is required in launch_candidate or launched status")
    elif isinstance(custom_domain, str):
        errors.extend(validate_https_url(canonical, custom_domain))

    for field in ("umbrella_name_screened", "product_name_screened"):
        if data.get(field) is not True:
            errors.append(f"{field} must be true in launch_candidate or launched status")
    if not data.get("approved_by") or not data.get("approved_on"):
        errors.append("approved_by and approved_on are required in launch_candidate or launched status")
    if not cname_path.exists():
        errors.append("site/CNAME is required in launch_candidate or launched status")
    elif isinstance(custom_domain, str) and cname_path.read_text(encoding="utf-8").strip() != custom_domain:
        errors.append("site/CNAME must match custom_domain")

    social = data.get("social_preview", {})
    if social.get("platform_ready_raster") is not True:
        errors.append("social_preview.platform_ready_raster must be true before launch candidate")
    public_url = social.get("public_url")
    if not isinstance(public_url, str) or not public_url.startswith("https://"):
        errors.append("social_preview.public_url must be an absolute HTTPS URL before launch candidate")

    if status == "launch_candidate":
        if data.get("indexing_approved") is not False:
            errors.append("indexing_approved must remain false in launch_candidate status")
        if "Disallow: /" not in robots:
            errors.append("robots.txt must remain blocked in launch_candidate status")
        for page in pages:
            html = page.read_text(encoding="utf-8").lower()
            if "noindex" not in html:
                errors.append(f"{page.relative_to(site_root)}: launch candidate must remain noindex")
    else:
        if data.get("indexing_approved") is not True:
            errors.append("indexing_approved must be true in launched status")
        if "Disallow: /" in robots:
            errors.append("robots.txt must not block all crawling in launched status")
        for page in pages:
            html = page.read_text(encoding="utf-8").lower()
            if "noindex" in html:
                errors.append(f"{page.relative_to(site_root)}: launched page must not contain noindex")
            if 'rel="canonical"' not in html and "rel='canonical'" not in html:
                errors.append(f"{page.relative_to(site_root)}: launched page requires canonical link")

    return errors


def main() -> int:
    if not STATE_PATH.exists():
        print(f"Launch state validation failed:\n- missing {STATE_PATH.relative_to(REPO_ROOT)}", file=sys.stderr)
        return 1
    try:
        data = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        print(f"Launch state validation failed:\n- cannot read launch state: {exc}", file=sys.stderr)
        return 1

    errors = validate_state(data)
    if errors:
        print("Launch state validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated launch state: {data['status']}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
