# Decision Log

## 2026-07-21 — Use Tessn as the provisional umbrella brand

**Decision:** Present the public umbrella as Tessn without an LLC suffix.

**Reason:** Company formation and exact legal naming remain unresolved. Product and parent-company branding should remain separable.

## 2026-07-21 — Keep Current as a provisional product name

**Decision:** Continue using Current in the website scaffold while preserving the requirement for final naming and trademark clearance.

**Reason:** Existing product positioning, documentation, and presentation assets use Current. Renaming before a disciplined screen would create churn.

## 2026-07-21 — Use a static, dependency-free website

**Decision:** Implement the first site with HTML, CSS, JavaScript, and SVG rather than Astro or another framework.

**Reason:** The immediate need is a presentation site. Static files reduce build, dependency, security, and handoff complexity while remaining fully compatible with GitHub Pages.

## 2026-07-21 — Separate website and downloads

**Decision:** Deploy website content from `tessn-website` and reserve `current-release` for controlled release assets.

**Reason:** Installer lifecycle, licensing, checksums, signatures, and support expectations should not be coupled to the marketing-site repository.

## 2026-07-21 — Keep preview content out of search indexes

**Decision:** Add page-level noindex directives and disallow crawling in `robots.txt`.

**Reason:** Contact, legal, naming, domain, screenshots, and claims require review before public discovery.
