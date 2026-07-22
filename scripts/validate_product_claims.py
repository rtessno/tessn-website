#!/usr/bin/env python3
"""Validate public product claims against exact reviewed source metadata."""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = REPO_ROOT / "docs/product-claims/current.json"
SITE_PAGE = REPO_ROOT / "site/current/index.html"
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
ALLOWED_MATURITY = {"alpha", "beta", "release-candidate", "generally-available"}
ALLOWED_AVAILABILITY = {"internal", "private-preview", "public-preview", "available"}
ALLOWED_SURFACE_STATUS = {"implemented", "development-preview", "planned"}
REQUIRED_SURFACES = {"web", "cli", "desktop"}
REQUIRED_DEPLOYMENTS = {"docker-compose", "kubernetes-helm"}
REQUIRED_SOURCE_PATHS = {
    "README.md",
    "cli-site/README.md",
    "cli-site/src/pages/index.astro",
    "docs-site/README.md",
}
REQUIRED_PAGE_TEXT = {
    "Private beta · Design-partner stage",
    "Authenticated web workspace",
    "Current CLI",
    "Current Desktop",
    "Development preview",
    "Docker Compose",
    "Kubernetes with Helm",
    "No public download",
    "requires a separately running Current Server",
}


def _nonempty_strings(value: Any) -> bool:
    return isinstance(value, list) and bool(value) and all(
        isinstance(item, str) and item.strip() for item in value
    )


def validate_manifest(data: dict[str, Any], root: Path = REPO_ROOT) -> list[str]:
    errors: list[str] = []

    if data.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if data.get("product") != "Current":
        errors.append("product must be Current")
    if data.get("source_repository") != "rtessno/support-copilot":
        errors.append("source_repository must be rtessno/support-copilot")
    source_commit = data.get("source_commit")
    if not isinstance(source_commit, str) or not SHA_RE.fullmatch(source_commit):
        errors.append("source_commit must be a full lowercase 40-character SHA")

    reviewed_on = data.get("reviewed_on")
    try:
        reviewed_date = date.fromisoformat(reviewed_on)
        if reviewed_date > date.today():
            errors.append("reviewed_on must not be in the future")
    except (TypeError, ValueError):
        errors.append("reviewed_on must be an ISO date")

    if not isinstance(data.get("reviewed_by"), str) or not data["reviewed_by"].strip():
        errors.append("reviewed_by is required")
    if data.get("maturity") not in ALLOWED_MATURITY:
        errors.append("maturity is invalid")
    if data.get("availability") not in ALLOWED_AVAILABILITY:
        errors.append("availability is invalid")
    if data.get("availability") != "private-preview":
        errors.append("Current availability must remain private-preview in this website state")
    if data.get("public_downloads") is not False:
        errors.append("public_downloads must remain false")
    if data.get("public_safety") != "public-safe-with-caveats":
        errors.append("public_safety must be public-safe-with-caveats")

    source_paths = data.get("source_paths")
    if not isinstance(source_paths, list) or set(source_paths) != REQUIRED_SOURCE_PATHS:
        errors.append("source_paths must contain the exact reviewed source inventory")

    surfaces = data.get("surfaces")
    if not isinstance(surfaces, list):
        errors.append("surfaces must be a list")
    else:
        ids = {surface.get("id") for surface in surfaces if isinstance(surface, dict)}
        if ids != REQUIRED_SURFACES:
            errors.append("surfaces must contain exactly web, cli, and desktop")
        for surface in surfaces:
            if not isinstance(surface, dict):
                errors.append("each surface must be an object")
                continue
            if surface.get("status") not in ALLOWED_SURFACE_STATUS:
                errors.append(f"surface {surface.get('id')}: invalid status")
            if not isinstance(surface.get("label"), str) or not surface["label"].strip():
                errors.append(f"surface {surface.get('id')}: label is required")
            if not _nonempty_strings(surface.get("claims")):
                errors.append(f"surface {surface.get('id')}: claims are required")
        desktop = next((item for item in surfaces if item.get("id") == "desktop"), None)
        if desktop and desktop.get("status") != "development-preview":
            errors.append("desktop surface must remain development-preview")

    deployments = data.get("deployment_models")
    if not isinstance(deployments, list):
        errors.append("deployment_models must be a list")
    else:
        ids = {item.get("id") for item in deployments if isinstance(item, dict)}
        if ids != REQUIRED_DEPLOYMENTS:
            errors.append("deployment_models must contain Docker Compose and Kubernetes/Helm")
        for item in deployments:
            if not isinstance(item, dict) or item.get("status") != "implemented":
                errors.append(f"deployment {getattr(item, 'get', lambda *_: None)('id')}: must be implemented")
            elif not isinstance(item.get("claim"), str) or not item["claim"].strip():
                errors.append(f"deployment {item.get('id')}: claim is required")

    for field, minimum in (("trust_boundaries", 3), ("limitations", 3), ("prohibited_claims", 4)):
        values = data.get(field)
        if not _nonempty_strings(values) or len(values) < minimum:
            errors.append(f"{field} must contain at least {minimum} non-empty entries")

    page = root / "site/current/index.html"
    if not page.exists():
        errors.append("site/current/index.html is missing")
    else:
        page_text = page.read_text(encoding="utf-8")
        for required in sorted(REQUIRED_PAGE_TEXT):
            if required not in page_text:
                errors.append(f"current page is missing required reviewed text: {required!r}")

    return errors


def main() -> int:
    if not MANIFEST_PATH.exists():
        print(f"ERROR: missing manifest: {MANIFEST_PATH}", file=sys.stderr)
        return 1
    try:
        data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"ERROR: invalid JSON: {exc}", file=sys.stderr)
        return 1

    errors = validate_manifest(data)
    if errors:
        print("Product claim validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Current product claims are pinned, bounded, and internally consistent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
