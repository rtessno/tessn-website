# Ordered Next Tasks

## Completed — Foundation and deployment readiness

- PR #1 merged the static website foundation to `main`.
- PR #7 added static validation, repaired nested 404 behavior, and fixed navigation accessibility metadata.
- PR #8 added post-deployment HTTP verification and marker-based reporting to issue #2.
- PR #9 synchronized documentation with the verified Pages activation blocker.
- PR #10 established the Current product visual evidence gate.
- PR #13 established controlled pilot-intake readiness.
- The repository is public, contains only presentation source and governance documentation, and keeps downloads disabled.

## Task 1 — Activate and verify Pages

Tracking: issue #2

Completed:

- Confirmed the deploy workflow uploads only `site/`.
- Validated required routes, internal references, assets, preview indexing controls, navigation labels, and prohibited installer links.
- Triggered and reran deployment from `main`.
- Captured latest rerun `29889952423` and confirmed failure at **Configure Pages** before artifact upload.
- Added automatic deployed-site verification that updates issue #2 after every Pages deployment while the issue is open.

Manual blocker:

- Settings → Pages → Source: **GitHub Actions**.

After the setting changes:

- Rerun `Deploy GitHub Pages`, or push a commit to `main`.
- Confirm the issue #2 report passes for `https://rtessno.github.io/tessn-website/`.
- Inspect `/`, `/current/`, `/pilot/`, `/about/`, `/privacy/`, `/terms/`, assets, mobile navigation, and nested 404 behavior.
- Update README and HANDOFF with the verified result.
- Close issue #2.

## Task 2 — Add real product evidence

Tracking: issue #3 and `rtessno/support-copilot` issue #1873

Completed website-side foundation:

- Verified the Current repository has an active synthetic demonstration data policy and seed corpus.
- Verified no accepted public screenshot set or authoritative visual baseline was identified at the observed Current `main` revision.
- Defined the screenshot acceptance and rejection process in `docs/PRODUCT-VISUAL-EVIDENCE.md`.
- Added a mandatory JSON manifest template.
- Added automated validation for source commit, fixture, viewport, public approval, sanitization, alt text, caption, supported claims, and final image digest.
- Opened the Current-side capture handoff as `support-copilot` issue #1873.

Remaining capture and integration work:

- Freeze the exact Current candidate SHA that will be rendered.
- Run the synthetic demonstration case.
- Capture at least three polished screenshots from implemented product surfaces.
- Complete and approve one manifest per image.
- Integrate the images with factual alt text and captions.
- Review the visual layout on mobile and desktop.
- Update issue #3 and HANDOFF after integration.

## Task 3 — Activate the pilot contact path

Tracking: issue #4

Completed foundation through PR #13:

- Selected a dedicated business email as the initial channel architecture.
- Defined minimum first-contact information and qualification questions.
- Defined limited-access handling and a retention baseline.
- Updated the pilot and privacy pages before collection.
- Removed the founder GitHub profile as the intake path.
- Added explicit prohibitions on customer evidence, logs, captures, credentials, internal URLs, proprietary source, regulated information, contracts, and pricing.
- Added automated checks for the pending state and safety warning.

Remaining activation work:

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

- Added `docs/launch/launch-state.json`.
- Added `docs/LAUNCH-CONTROLS.md`.
- Added automated preview and launch-state validation with unit tests.
- Added draft 1200×630 social-preview artwork.
- Preserved noindex, crawler blocking, and the absence of canonical URLs, CNAME, sitemap, structured data, analytics, and live social tags.

Remaining decision and activation work:

- Complete umbrella-brand and product-name screening.
- Select and acquire the domain.
- Activate and verify GitHub Pages.
- Configure DNS, Pages custom domain, and HTTPS.
- Generate and review a platform-ready social preview raster.
- Transition the manifest to `launch_candidate` with indexing still disabled.
- Add canonical, Open Graph, social, sitemap, and accurate structured metadata.
- Complete content, privacy, terms, accessibility, and launch review.
- Transition to `launched` and remove noindex only through an explicit reviewed change.

## Task 5 — Release repository readiness

Tracking: `rtessno/current-release` issue #1

- Add release governance and documentation.
- Define supported platforms.
- Define signing, checksums, SBOM, licensing, support, and access model.
- Keep direct downloads disabled until the gate is satisfied.
