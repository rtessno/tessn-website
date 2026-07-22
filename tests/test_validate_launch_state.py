from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = REPO_ROOT / "scripts" / "validate_launch_state.py"
SPEC = importlib.util.spec_from_file_location("validate_launch_state", MODULE_PATH)
assert SPEC and SPEC.loader
launch = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(launch)


class LaunchStateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        site = self.root / "site"
        (site / "assets/images").mkdir(parents=True)
        (site / "index.html").write_text(
            '<meta name="robots" content="noindex,nofollow">', encoding="utf-8"
        )
        (site / "robots.txt").write_text("User-agent: *\nDisallow: /\n", encoding="utf-8")
        (site / "assets/images/social-preview.svg").write_text(
            "<svg><title>Tessn Current preview</title></svg>", encoding="utf-8"
        )
        self.data = {
            "schema_version": 1,
            "status": "preview",
            "umbrella_brand": "Tessn",
            "product_name": "Current",
            "custom_domain": None,
            "canonical_base_url": None,
            "indexing_approved": False,
            "legal_entity_approved": False,
            "umbrella_name_screened": False,
            "product_name_screened": False,
            "social_preview": {
                "draft_path": "site/assets/images/social-preview.svg",
                "public_url": None,
                "platform_ready_raster": False,
            },
            "structured_data_approved": False,
            "analytics_approved": False,
            "approved_by": None,
            "approved_on": None,
        }

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_accepts_fail_closed_preview(self) -> None:
        self.assertEqual(launch.validate_state(self.data, self.root), [])

    def test_rejects_preview_canonical_url(self) -> None:
        self.data["canonical_base_url"] = "https://example.com/"
        errors = launch.validate_state(self.data, self.root)
        self.assertIn("canonical_base_url must be null in preview status", errors)

    def test_rejects_preview_cname(self) -> None:
        (self.root / "site/CNAME").write_text("example.com\n", encoding="utf-8")
        errors = launch.validate_state(self.data, self.root)
        self.assertIn("site/CNAME must not exist in preview status", errors)

    def test_rejects_preview_indexing(self) -> None:
        self.data["indexing_approved"] = True
        errors = launch.validate_state(self.data, self.root)
        self.assertIn("indexing_approved must be false in preview status", errors)

    def test_launch_candidate_requires_screening_and_domain(self) -> None:
        self.data["status"] = "launch_candidate"
        errors = launch.validate_state(self.data, self.root)
        self.assertIn(
            "custom_domain must be a hostname in launch_candidate or launched status", errors
        )
        self.assertIn(
            "umbrella_name_screened must be true in launch_candidate or launched status",
            errors,
        )

    def test_launched_rejects_noindex(self) -> None:
        self.data.update(
            {
                "status": "launched",
                "custom_domain": "example.com",
                "canonical_base_url": "https://example.com/",
                "indexing_approved": True,
                "umbrella_name_screened": True,
                "product_name_screened": True,
                "approved_by": "reviewer",
                "approved_on": "2026-07-21",
            }
        )
        self.data["social_preview"] = {
            "draft_path": "site/assets/images/social-preview.svg",
            "public_url": "https://example.com/social-preview.png",
            "platform_ready_raster": True,
        }
        (self.root / "site/CNAME").write_text("example.com\n", encoding="utf-8")
        (self.root / "site/robots.txt").write_text("User-agent: *\nAllow: /\n", encoding="utf-8")
        errors = launch.validate_state(self.data, self.root)
        self.assertIn("index.html: launched page must not contain noindex", errors)


if __name__ == "__main__":
    unittest.main()
