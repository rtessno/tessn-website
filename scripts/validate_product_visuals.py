#!/usr/bin/env python3
"""Enforce the public evidence gate for Current product screenshots."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
VISUAL_ROOT = REPO_ROOT / "site" / "assets" / "images" / "current"
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp"}
COMMIT_PATTERN = re.compile(r"^[0-9a-f]{40}$")
ALLOWED_SURFACES = {
    "case-overview",
    "evidence-workspace",
    "deterministic-findings",
    "timeline",
    "engineering-handoff",
    "publisher-gateway-outcome",
}
REQUIRED_SANITIZATION_CHECKS = {
    "customer_names_removed",
    "email_addresses_removed",
    "ticket_identifiers_removed",
    "sensitive_ip_addresses_removed",
    "internal_urls_removed",
    "credentials_and_tokens_removed",
    "proprietary_logs_removed",
    "employee_names_removed",
    "contract_and_pricing_removed",
}


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"invalid JSON: {error}") from error
    if not isinstance(data, dict):
        raise ValueError("manifest root must be an object")
    return data


def require_string(data: dict[str, Any], field: str, errors: list[str]) -> str:
    value = data.get(field)
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{field} must be a non-empty string")
        return ""
    return value.strip()


def require_datetime(value: str, field: str, errors: list[str]) -> None:
    if not value:
        return
    normalized = value.replace("Z", "+00:00")
    try:
        datetime.fromisoformat(normalized)
    except ValueError:
        errors.append(f"{field} must be an ISO-8601 date or datetime")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_manifest(image: Path, manifest: Path) -> list[str]:
    errors: list[str] = []
    try:
        data = load_json(manifest)
    except ValueError as error:
        return [str(error)]

    if data.get("schema_version") != 1:
        errors.append("schema_version must equal 1")
    if data.get("status") != "approved_public":
        errors.append("status must equal approved_public")

    source_repository = require_string(data, "source_repository", errors)
    if source_repository and source_repository != "rtessno/support-copilot":
        errors.append("source_repository must equal rtessno/support-copilot")

    source_commit = require_string(data, "source_commit", errors)
    if source_commit and not COMMIT_PATTERN.fullmatch(source_commit):
        errors.append("source_commit must be a full 40-character lowercase commit SHA")

    require_string(data, "capture_id", errors)
    surface = require_string(data, "surface", errors)
    if surface and surface not in ALLOWED_SURFACES:
        errors.append(f"surface must be one of {sorted(ALLOWED_SURFACES)}")

    fixture_mode = require_string(data, "fixture_mode", errors)
    if fixture_mode and fixture_mode not in {"synthetic", "sanitized"}:
        errors.append("fixture_mode must be synthetic or sanitized")
    require_string(data, "fixture_id", errors)

    captured_at = require_string(data, "captured_at", errors)
    reviewed_at = require_string(data, "reviewed_at", errors)
    require_datetime(captured_at, "captured_at", errors)
    require_datetime(reviewed_at, "reviewed_at", errors)
    require_string(data, "reviewer", errors)

    alt_text = require_string(data, "alt_text", errors)
    if alt_text and len(alt_text) > 240:
        errors.append("alt_text must be 240 characters or fewer")
    require_string(data, "caption", errors)

    viewport = data.get("viewport")
    if not isinstance(viewport, dict):
        errors.append("viewport must be an object")
    else:
        for dimension in ("width", "height"):
            value = viewport.get(dimension)
            if not isinstance(value, int) or value <= 0:
                errors.append(f"viewport.{dimension} must be a positive integer")

    claims = data.get("claims_supported")
    if not isinstance(claims, list) or not claims or not all(
        isinstance(claim, str) and claim.strip() for claim in claims
    ):
        errors.append("claims_supported must be a non-empty array of strings")

    sanitization = data.get("sanitization")
    if not isinstance(sanitization, dict):
        errors.append("sanitization must be an object")
    else:
        missing = sorted(REQUIRED_SANITIZATION_CHECKS - sanitization.keys())
        if missing:
            errors.append(f"sanitization is missing checks: {missing}")
        failed = sorted(
            key
            for key in REQUIRED_SANITIZATION_CHECKS
            if sanitization.get(key) is not True
        )
        if failed:
            errors.append(f"sanitization checks must all be true: {failed}")

    expected_hash = require_string(data, "sha256", errors)
    actual_hash = sha256(image)
    if expected_hash and expected_hash != actual_hash:
        errors.append(f"sha256 does not match image bytes; expected {actual_hash}")

    if data.get("filename") != image.name:
        errors.append(f"filename must equal {image.name}")

    return errors


def main() -> int:
    if not VISUAL_ROOT.exists():
        print("No Current public product visuals are present; evidence gate has nothing to validate.")
        return 0

    images = sorted(
        path for path in VISUAL_ROOT.iterdir() if path.is_file() and path.suffix.lower() in IMAGE_SUFFIXES
    )
    orphan_manifests = sorted(
        path
        for path in VISUAL_ROOT.glob("*.json")
        if not any((VISUAL_ROOT / f"{path.stem}{suffix}").exists() for suffix in IMAGE_SUFFIXES)
    )

    errors: list[str] = []
    for manifest in orphan_manifests:
        errors.append(f"{manifest.relative_to(REPO_ROOT)}: manifest has no matching image")

    for image in images:
        manifest = image.with_suffix(".json")
        if not manifest.exists():
            errors.append(f"{image.relative_to(REPO_ROOT)}: missing sidecar manifest {manifest.name}")
            continue
        for error in validate_manifest(image, manifest):
            errors.append(f"{manifest.relative_to(REPO_ROOT)}: {error}")

    if errors:
        print("Product visual evidence validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(images)} approved Current public product visual(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
