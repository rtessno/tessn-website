from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = REPO_ROOT / "scripts" / "validate_product_claims.py"
SPEC = importlib.util.spec_from_file_location("validate_product_claims", MODULE_PATH)
assert SPEC and SPEC.loader
claims = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(claims)


class ProductClaimTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        (self.root / "site/current").mkdir(parents=True)
        required_page_text = "\n".join(sorted(claims.REQUIRED_PAGE_TEXT))
        (self.root / "site/current/index.html").write_text(required_page_text, encoding="utf-8")
        self.data = {
            "schema_version": 1,
            "product": "Current",
            "source_repository": "rtessno/support-copilot",
            "source_commit": "a" * 40,
            "reviewed_on": "2026-07-22",
            "reviewed_by": "rtessno",
            "maturity": "beta",
            "availability": "private-preview",
            "public_downloads": False,
            "public_safety": "public-safe-with-caveats",
            "source_paths": sorted(claims.REQUIRED_SOURCE_PATHS),
            "surfaces": [
                {"id": "web", "status": "implemented", "label": "Web", "claims": ["Web claim"]},
                {"id": "cli", "status": "implemented", "label": "CLI", "claims": ["CLI claim"]},
                {
                    "id": "desktop",
                    "status": "development-preview",
                    "label": "Desktop",
                    "claims": ["Desktop claim"],
                },
            ],
            "deployment_models": [
                {
                    "id": "docker-compose",
                    "status": "implemented",
                    "label": "Docker Compose",
                    "claim": "Compose claim",
                },
                {
                    "id": "kubernetes-helm",
                    "status": "implemented",
                    "label": "Kubernetes with Helm",
                    "claim": "Helm claim",
                },
            ],
            "trust_boundaries": ["one", "two", "three"],
            "limitations": ["one", "two", "three"],
            "prohibited_claims": ["one", "two", "three", "four"],
        }

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_accepts_bounded_private_preview(self) -> None:
        self.assertEqual(claims.validate_manifest(self.data, self.root), [])

    def test_rejects_short_source_commit(self) -> None:
        self.data["source_commit"] = "abc123"
        errors = claims.validate_manifest(self.data, self.root)
        self.assertIn("source_commit must be a full lowercase 40-character SHA", errors)

    def test_rejects_public_downloads(self) -> None:
        self.data["public_downloads"] = True
        errors = claims.validate_manifest(self.data, self.root)
        self.assertIn("public_downloads must remain false", errors)

    def test_rejects_desktop_as_implemented_release(self) -> None:
        self.data["surfaces"][2]["status"] = "implemented"
        errors = claims.validate_manifest(self.data, self.root)
        self.assertIn("desktop surface must remain development-preview", errors)

    def test_rejects_missing_page_boundary(self) -> None:
        (self.root / "site/current/index.html").write_text("Current CLI", encoding="utf-8")
        errors = claims.validate_manifest(self.data, self.root)
        self.assertTrue(any("No public download" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
