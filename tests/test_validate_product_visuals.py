from __future__ import annotations

import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = REPO_ROOT / "scripts" / "validate_product_visuals.py"
SPEC = importlib.util.spec_from_file_location("validate_product_visuals", MODULE_PATH)
assert SPEC and SPEC.loader
visuals = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(visuals)


class ProductVisualManifestTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.image = self.root / "current__case-overview__1440x1000__abc123def456.png"
        self.image.write_bytes(b"synthetic-image-fixture")
        self.manifest = self.image.with_suffix(".json")
        self.data = {
            "schema_version": 1,
            "status": "approved_public",
            "filename": self.image.name,
            "sha256": hashlib.sha256(self.image.read_bytes()).hexdigest(),
            "capture_id": "CUR-WEB-CASE-OVERVIEW-001",
            "surface": "case-overview",
            "source_repository": "rtessno/support-copilot",
            "source_commit": "a" * 40,
            "fixture_mode": "synthetic",
            "fixture_id": "acme-relay-INC-1042",
            "viewport": {"width": 1440, "height": 1000},
            "captured_at": "2026-07-21T20:00:00-05:00",
            "reviewed_at": "2026-07-21T20:30:00-05:00",
            "reviewer": "reviewer",
            "alt_text": "Current case overview with synthetic escalation context.",
            "caption": "A synthetic escalation organized in Current.",
            "claims_supported": [
                "Current structures case context and investigation status."
            ],
            "sanitization": {
                key: True for key in visuals.REQUIRED_SANITIZATION_CHECKS
            },
        }

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def write_manifest(self) -> None:
        self.manifest.write_text(json.dumps(self.data), encoding="utf-8")

    def test_accepts_complete_approved_manifest(self) -> None:
        self.write_manifest()
        self.assertEqual(visuals.validate_manifest(self.image, self.manifest), [])

    def test_rejects_unapproved_status(self) -> None:
        self.data["status"] = "draft"
        self.write_manifest()
        errors = visuals.validate_manifest(self.image, self.manifest)
        self.assertIn("status must equal approved_public", errors)

    def test_rejects_digest_mismatch(self) -> None:
        self.data["sha256"] = "0" * 64
        self.write_manifest()
        errors = visuals.validate_manifest(self.image, self.manifest)
        self.assertTrue(any(error.startswith("sha256 does not match") for error in errors))

    def test_rejects_incomplete_sanitization(self) -> None:
        self.data["sanitization"]["credentials_and_tokens_removed"] = False
        self.write_manifest()
        errors = visuals.validate_manifest(self.image, self.manifest)
        self.assertTrue(any("sanitization checks must all be true" in error for error in errors))

    def test_rejects_non_public_fixture_mode(self) -> None:
        self.data["fixture_mode"] = "approved_real"
        self.write_manifest()
        errors = visuals.validate_manifest(self.image, self.manifest)
        self.assertIn("fixture_mode must be synthetic or sanitized", errors)


if __name__ == "__main__":
    unittest.main()
