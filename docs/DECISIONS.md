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

## 2026-07-21 — Retain public repository visibility for the GitHub Pages preview

**Decision:** Keep `rtessno/tessn-website` public during the current GitHub Pages preview phase.

**Reason:** GitHub Pages is available from public repositories on GitHub Free, while private-repository Pages requires an eligible paid plan. The repository is intentionally limited to public presentation source and governance documentation and must not contain private Current source, customer evidence, credentials, installers, or other sensitive material. Revisit repository visibility if the hosting plan or deployment architecture changes.

## 2026-07-21 — Gate Pages deployment with dependency-free validation

**Decision:** Validate the static site on pull requests and pushes to `main` using `scripts/validate_site.py` and `.github/workflows/validate-site.yml`.

**Reason:** The site has no build system, but deployment still requires repeatable checks for required routes, broken internal references, accessibility metadata, preview indexing controls, and accidental installer links. A standard-library validator preserves the dependency-free architecture.
