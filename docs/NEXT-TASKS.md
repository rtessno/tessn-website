# Ordered Next Tasks

## Completed foundations

- PR #1 — static website foundation
- PR #7 — route, 404, and accessibility validation
- PR #8 — post-deployment HTTP verification and issue reporting
- PR #9 — verified Pages blocker documentation
- PR #10 — Current product visual evidence gate
- PR #13 — controlled pilot-intake readiness
- PR #14 — fail-closed launch metadata guardrails
- PR #15 — trust and deployment boundaries
- PR #18 — static accessibility and asset-quality gate
- PR #19 — verified Pages deployment reconciliation
- PR #21 — revision-bound Current product surfaces and claim validation
- Issue #2 — GitHub Pages activation and 15/15 deployed verification
- Issue #20 — Current product surface refresh from exact authoritative source

Verified preview:

`https://rtessno.github.io/tessn-website/`

The repository remains public, preview-only, noindex, and free of public downloads.

## Current product claim state

Public Current capability language is pinned to:

`rtessno/support-copilot@4643c749f021c3ebf67075964f8fd5804e62c7e1`

The page now distinguishes Web, CLI, Desktop development-preview, Docker Compose, and Kubernetes/Helm surfaces. Later claim changes require an exact source refresh through `docs/product-claims/current.json` and `scripts/validate_product_claims.py`.

## Task 1 — Complete deployed browser quality review

Tracking: issue #16

Website-side automation completed:

- document language and title checks
- main/footer landmark checks
- skip-link target validation
- one h1 and no skipped heading levels
- image alt-attribute validation
- unexpected external asset-host rejection
- HTML, CSS, JavaScript, and SVG size budgets
- exact-source Current product claim validation
- deployed HTTP verification for all routes and required assets

Remaining:

- Inspect iPhone, tablet, compact desktop, wide desktop, and 200% zoom layouts.
- Re-review the expanded Current page at each viewport.
- Complete keyboard-only and screen-reader spot checks.
- Review contrast and reduced-motion behavior.
- Inspect console output and unexpected third-party network requests.
- Run browser caching, page-weight, and basic performance checks.
- Reconcile Privacy, Trust, and Terms with actual deployed behavior.
- Record browsers, operating systems, viewports, defects, and remediation PRs.

## Task 2 — Add real product evidence

Tracking: issue #3 and `rtessno/support-copilot` issue #1873

- Freeze the exact Current candidate SHA that will be rendered.
- Run the synthetic demonstration case.
- Capture at least three polished screenshots from implemented product surfaces.
- Complete and approve one manifest per image.
- Integrate the images with factual alt text and captions.
- Review the visual layout on mobile and desktop.
- Update issue #3 and HANDOFF after integration.

## Task 3 — Verify public Current documentation navigation

Tracking: issue #20 follow-up or a focused documentation issue

- Verify the deployed Current documentation URL and route stability.
- Confirm its published content is public-safe and aligned with the exact Current source revision.
- Decide whether Tessn should link to the documentation site or publish curated snapshots.
- Allowlist the external host only through an explicit validator change.
- Keep engineering-only and private repository links out of the public website.

## Task 4 — Activate the pilot contact path

Tracking: issue #4

- Create the dedicated business mailbox.
- Configure multi-factor authentication and recovery.
- Select a retention process that can be followed consistently.
- Test sending and receiving.
- Approve the address for publication in this public repository.
- Replace the pending state with one working `mailto:` action.
- Re-review the privacy notice and test mobile and desktop behavior.
- Close issue #4.

## Task 5 — Complete naming, domain, and launch metadata

Tracking: issue #5

Completed fail-closed foundation:

- machine-readable launch state
- naming, domain, metadata, indexing, and rollback controls
- automated launch-state validation and tests
- draft social-preview artwork
- verified GitHub Pages project preview
- no premature canonical, CNAME, sitemap, structured data, analytics, live social tags, or indexing

Remaining:

- Complete umbrella-brand and product-name screening.
- Select and acquire the domain.
- Configure DNS, Pages custom domain, and HTTPS.
- Generate and review a platform-ready social preview raster.
- Transition to `launch_candidate` with indexing still disabled.
- Add canonical, Open Graph, social, sitemap, and accurate structured metadata.
- Complete content, privacy, terms, accessibility, and launch review.
- Transition to `launched` and remove noindex only through an explicit reviewed change.

## Task 6 — Release repository readiness

Tracking: `rtessno/current-release` issue #1

- Add release governance and documentation.
- Define supported platforms.
- Define signing, checksums, SBOM, licensing, support, and access model.
- Keep direct downloads disabled until the gate is satisfied.

## Task 7 — Decide portfolio breadth

Tracking: `rtessno/software-portfolio#9`

- Keep Current as the primary conversion path for the current preview.
- Decide whether a restrained product directory belongs on Tessn.
- Revalidate Ouli and PhrasePilot against current exact revisions before public pages.
- Treat I Love Me and Travel Buddy as later Labs candidates.
- Reuse Oulifit governance patterns internally without importing unrelated storefront positioning.
