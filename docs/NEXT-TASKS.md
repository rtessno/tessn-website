# Ordered Next Tasks

## Completed foundations

- PR #1 — static website foundation
- PR #7 — route, 404, and accessibility validation
- PR #8 — post-deployment HTTP verification and issue reporting
- PR #9 — verified Pages blocker documentation
- PR #10 — Current product visual evidence gate
- PR #13 — controlled pilot-intake readiness
- PR #14 — fail-closed launch metadata guardrails

The repository remains public, preview-only, noindex, and free of public downloads.

## Task 1 — Activate and verify Pages

Tracking: issue #2

Completed:

- Confirmed the deploy workflow uploads only `site/`.
- Added static and deployed validation for routes, assets, accessibility metadata, preview controls, pilot safety, trust boundaries, and prohibited installer links.
- Triggered and reran deployment from `main`.
- Captured latest rerun `29889952423` and confirmed failure at **Configure Pages** before artifact upload.
- Added automatic deployed-site verification that updates issue #2 while the issue is open.

Manual blocker:

- Settings → Pages → Source: **GitHub Actions**.

After the setting changes:

- Rerun `Deploy GitHub Pages`, or push a commit to `main`.
- Confirm the issue #2 report passes for `https://rtessno.github.io/tessn-website/`.
- Inspect all routes, assets, mobile navigation, trust content, pilot safety copy, and nested 404 behavior.
- Update README and HANDOFF with the verified result.
- Close issue #2.

## Task 2 — Add real product evidence

Tracking: issue #3 and `rtessno/support-copilot` issue #1873

- Freeze the exact Current candidate SHA that will be rendered.
- Run the synthetic demonstration case.
- Capture at least three polished screenshots from implemented product surfaces.
- Complete and approve one manifest per image.
- Integrate the images with factual alt text and captions.
- Review the visual layout on mobile and desktop.
- Update issue #3 and HANDOFF after integration.

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
- no premature canonical, CNAME, sitemap, structured data, analytics, live social tags, or indexing

Remaining:

- Complete umbrella-brand and product-name screening.
- Select and acquire the domain.
- Activate and verify GitHub Pages.
- Configure DNS, Pages custom domain, and HTTPS.
- Generate and review a platform-ready social preview raster.
- Transition to `launch_candidate` with indexing still disabled.
- Add canonical, Open Graph, social, sitemap, and accurate structured metadata.
- Complete content, privacy, terms, accessibility, and launch review.
- Transition to `launched` and remove noindex only through an explicit reviewed change.

## Task 5 — Complete deployed quality review

The Trust page and claim boundaries are implemented. Remaining launch-quality work:

- Inspect typography and spacing on iPhone, tablet, and desktop.
- Test keyboard-only navigation and screen-reader landmarks.
- Run deployed performance and broken-link checks.
- Obtain appropriate legal review for Privacy and Terms.
- Add deployment-specific controls only when demonstrated for the exact pilot configuration.
- Add product architecture and edition information only when commercially settled and evidence-backed.

## Task 6 — Release repository readiness

Tracking: `rtessno/current-release` issue #1

- Add release governance and documentation.
- Define supported platforms.
- Define signing, checksums, SBOM, licensing, support, and access model.
- Keep direct downloads disabled until the gate is satisfied.
