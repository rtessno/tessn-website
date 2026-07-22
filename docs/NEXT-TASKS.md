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
- Issue #22 — Current documentation-navigation audit; remain link-free until the revision-aware public-safety gate passes

Verified preview:

`https://rtessno.github.io/tessn-website/`

The repository remains public, preview-only, noindex, and free of public downloads.

## Current product claim state

Public Current capability language is pinned to:

`rtessno/support-copilot@4643c749f021c3ebf67075964f8fd5804e62c7e1`

The page distinguishes Web, CLI, Desktop development-preview, Docker Compose, and Kubernetes/Helm surfaces. Later claim changes require an exact source refresh through `docs/product-claims/current.json` and `scripts/validate_product_claims.py`.

## Current documentation decision

`docs/CURRENT-DOCUMENTATION-NAVIGATION.md` records the fail-closed outcome of issue #22.

Tessn currently publishes no Current Docs, CLI install, release, private-repository, or raw OpenAPI link because the upstream Pages artifact:

- is not stamped with an exact externally verifiable Current revision
- merges Docs and CLI distribution-oriented navigation into one Pages artifact
- includes installation, customer-distribution, environment-variable, operator-security, OpenAPI, GitHub, and edit-on-GitHub surfaces
- has not passed Tessn's external-host allowlist, release-state, and rollback gates

Reconsider only after the exact public artifact, routes, navigation, release consistency, safety review, and rollback behavior are verified together.

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

- Confirm the post-PR #21 deployment contains the strengthened Current-route boundaries.
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
- Run the synthetic demonstration case locally.
- Capture at least three polished screenshots from implemented product surfaces.
- Complete and approve one manifest per image.
- Integrate the images with factual alt text and captions.
- Review the visual layout on mobile and desktop.
- Update issue #3 and HANDOFF after integration.

This task requires a locally rendered Current instance and cannot be completed through repository-only GitHub actions.

## Task 3 — Activate the pilot contact path

Tracking: issue #4

- Create the dedicated business mailbox.
- Configure multi-factor authentication and recovery.
- Select a retention process that can be followed consistently.
- Test sending and receiving.
- Approve the address for publication in this public repository.
- Replace the pending state with one working `mailto:` action.
- Re-review the privacy notice and test mobile and desktop behavior.
- Close issue #4.

## Task 4 — Complete naming, domain, and launch metadata

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

## Task 5 — Release repository readiness

Tracking: `rtessno/current-release` issue #1

Current blocker:

- `current-release` is empty and has no root Git commit.
- Create the initial README commit on `main`; the connected contents interface cannot create the first commit in an empty repository.

After bootstrap:

- Build the release-governance foundation through a feature branch and pull request.
- Define supported platforms without guessing.
- Define release states, immutable artifact records, signing, notarization, checksums, malware scanning, SBOMs, licensing, support, access, withdrawal, upgrade, and rollback.
- Add fail-closed validation and tests.
- Keep direct downloads disabled until an exact artifact passes every gate.

## Task 6 — Decide website responsibilities and portfolio breadth

Tracking: `rtessno/software-portfolio#9` and `#10`

- Confirm Tessn as the umbrella, product directory, pilot entry, and umbrella trust/legal site.
- Confirm `support-copilot/website` as the eventual authoritative detailed Current marketing and evaluation site after deployment approval.
- Keep Current Docs and CLI sites authoritative for technical learning after public-safety verification.
- Retain `portfolio-web` as a governance and migration source rather than a competing production website.
- Keep Current as the primary conversion path for the present preview.
- Revalidate Ouli and PhrasePilot against current exact revisions before public pages.
- Treat I Love Me and Travel Buddy as later Labs candidates.
- Reuse Oulifit governance patterns internally without importing unrelated storefront positioning.