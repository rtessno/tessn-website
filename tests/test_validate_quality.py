from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = REPO_ROOT / "scripts" / "validate_quality.py"
SPEC = importlib.util.spec_from_file_location("validate_quality", MODULE_PATH)
assert SPEC and SPEC.loader
quality = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(quality)


class StaticQualityTests(unittest.TestCase):
    def write_page(self, body: str) -> Path:
        temp = tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8")
        temp.write(body)
        temp.close()
        return Path(temp.name)

    def tearDown(self) -> None:
        for path in getattr(self, "paths", []):
            path.unlink(missing_ok=True)

    def keep(self, path: Path) -> Path:
        self.paths = getattr(self, "paths", []) + [path]
        return path

    def test_accepts_accessible_minimal_page(self) -> None:
        page = self.keep(self.write_page(
            '<!doctype html><html lang="en"><head><title>Page</title></head>'
            '<body><a class="skip-link" href="#main">Skip</a><main id="main">'
            '<h1>Title</h1><img src="x.svg" alt=""></main><footer>Footer</footer></body></html>'
        ))
        original = quality.SITE_ROOT
        quality.SITE_ROOT = page.parent
        try:
            self.assertEqual(quality.validate_page(page), [])
        finally:
            quality.SITE_ROOT = original

    def test_rejects_missing_skip_target(self) -> None:
        page = self.keep(self.write_page(
            '<html lang="en"><head><title>Page</title></head><body>'
            '<a class="skip-link" href="#missing">Skip</a><main id="main">'
            '<h1>Title</h1></main><footer>Footer</footer></body></html>'
        ))
        original = quality.SITE_ROOT
        quality.SITE_ROOT = page.parent
        try:
            errors = quality.validate_page(page)
        finally:
            quality.SITE_ROOT = original
        self.assertTrue(any("skip link target" in error for error in errors))

    def test_rejects_heading_jump(self) -> None:
        page = self.keep(self.write_page(
            '<html lang="en"><head><title>Page</title></head><body>'
            '<a class="skip-link" href="#main">Skip</a><main id="main">'
            '<h1>Title</h1><h3>Jump</h3></main><footer>Footer</footer></body></html>'
        ))
        original = quality.SITE_ROOT
        quality.SITE_ROOT = page.parent
        try:
            errors = quality.validate_page(page)
        finally:
            quality.SITE_ROOT = original
        self.assertTrue(any("heading level jumps" in error for error in errors))

    def test_rejects_missing_image_alt(self) -> None:
        page = self.keep(self.write_page(
            '<html lang="en"><head><title>Page</title></head><body>'
            '<a class="skip-link" href="#main">Skip</a><main id="main">'
            '<h1>Title</h1><img src="x.svg"></main><footer>Footer</footer></body></html>'
        ))
        original = quality.SITE_ROOT
        quality.SITE_ROOT = page.parent
        try:
            errors = quality.validate_page(page)
        finally:
            quality.SITE_ROOT = original
        self.assertTrue(any("missing alt" in error for error in errors))

    def test_rejects_external_asset_host(self) -> None:
        page = self.keep(self.write_page(
            '<html lang="en"><head><title>Page</title>'
            '<script src="https://example.com/a.js"></script></head><body>'
            '<a class="skip-link" href="#main">Skip</a><main id="main">'
            '<h1>Title</h1></main><footer>Footer</footer></body></html>'
        ))
        original = quality.SITE_ROOT
        quality.SITE_ROOT = page.parent
        try:
            errors = quality.validate_page(page)
        finally:
            quality.SITE_ROOT = original
        self.assertTrue(any("unexpected external" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
