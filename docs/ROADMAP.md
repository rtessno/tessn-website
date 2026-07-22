# Tessn Website Roadmap

## Milestone 0 — Foundation

Status: **Complete and merged to `main` through PR #1**

Delivered:

- Static multi-page website scaffold
- Responsive visual system
- Homepage and Current product page
- Pilot, About, Privacy, and Terms pages
- GitHub Pages workflow
- Preview indexing controls
- Security and contribution guidance
- Durable project context and continuation handoff
- Organized issue queue for the next workstreams

## Milestone 1 — Repository and deployment activation

Status: **Blocked on one manual repository setting — tracked by issue #2**

Completed:

1. Confirmed the repository is public and contains only presentation-site source and governance documentation suitable for public visibility.
2. Added a dependency-free validator for required routes, internal links, assets, navigation labels, preview indexing controls, and the no-download gate.
3. Added pull-request and `main` validation through `.github/workflows/validate-site.yml`.
4. Fixed the nested project Pages 404 base path.
5. Added missing accessible primary-navigation labels on Privacy and Terms.
6. Confirmed the deployment workflow uploads only `site/`.
7. Added post-deployment HTTP verification and marker-based reporting to issue #2 through PR #8.
8. Triggered and reran `Deploy GitHub Pages` from `main`; both attempts failed before artifact upload.

Verified blocker:

- latest rerun `29889952423` failed in the **Configure Pages** step
- artifact upload and deployment were skipped
- repository **Settings → Pages → Source** must be set to **GitHub Actions**

Remaining:

1. Change the Pages source setting to **GitHub Actions**.
2. Rerun `Deploy GitHub Pages`, or push a new commit to `main`.
3. Observe the automated issue #2 report pass.
4. Validate mobile and desktop rendering at `https://rtessno.github.io/tessn-website/`.
5. Record the verified deployment result in README and HANDOFF, then close issue #2.

## Milestone 2 — Real product visuals

Status: **Evidence gate complete; capture and integration pending — tracked by issue #3**

Completed website-side foundation through PR #10:

1. Confirmed the Current repository has an active synthetic demonstration data policy and seed corpus.
2. Confirmed no accepted public screenshot set or authoritative visual baseline was identified at the observed Current `main` revision.
3. Defined the public screenshot acceptance and rejection rules in `docs/PRODUCT-VISUAL-EVIDENCE.md`.
4. Added a required sidecar manifest template for source revision, fixture, viewport, supported claims, review, sanitization, and image digest.
5. Added `scripts/validate_product_visuals.py` and connected it to the pull-request validation workflow.
6. Added unit tests for approved, draft, digest-mismatch, incomplete-sanitization, and non-public fixture cases.
7. Opened `rtessno/support-copilot` issue #1873 as the exact-revision synthetic capture handoff.

Remaining:

1. Freeze an exact Current candidate SHA through `support-copilot` issue #1873.
2. Run Current with a synthetic demonstration case.
3. Capture polished screenshots of:
   - case overview
   - evidence workspace
   - deterministic findings or timeline
   - optional engineering handoff
   - optional Publisher/Gateway knowledge outcome
4. Complete one approved manifest per image.
5. Integrate at least three approved images with descriptive alternative text and factual captions.
6. Review mobile and desktop presentation.
7. Update claims governance, handoff, roadmap, and issue #3 after integration.

## Milestone 3 — Pilot conversion path

Status: **Intake foundation complete; dedicated address activation pending — tracked by issue #4**

Completed through PR #13:

1. Selected a dedicated business email as the initial pilot-interest channel architecture.
2. Rejected public GitHub issues, profiles, embedded forms, scheduling tools, and evidence uploads as the initial intake path.
3. Defined minimum first-contact fields and qualification questions in `docs/PILOT-INTAKE.md`.
4. Defined limited-access handling and a retention baseline without promising an unenforceable numeric period.
5. Added explicit prohibitions on customer evidence, logs, captures, credentials, internal URLs, proprietary source, regulated information, contracts, and pricing.
6. Removed the founder GitHub profile as the pilot-interest action.
7. Updated the pilot and privacy pages while keeping direct collection disabled.
8. Added static validation for the contact-pending state and sensitive-evidence warning.

Remaining:

1. Create and secure the dedicated business mailbox.
2. Configure multi-factor authentication and account recovery.
3. Select a retention process that can be followed consistently.
4. Test sending and receiving.
5. Publish the approved address and replace the pending state with one working `mailto:` action.
6. Re-review the privacy notice and test the path on mobile and desktop.
7. Close issue #4 only after the public action works.

## Milestone 4 — Brand, domain, and launch metadata

Status: **Fail-closed launch foundation complete; naming and domain decisions pending — tracked by issue #5**

Completed website-side foundation:

1. Added `docs/launch/launch-state.json` as the machine-readable preview, launch-candidate, and launched state.
2. Added `docs/LAUNCH-CONTROLS.md` with naming, domain, HTTPS, metadata, indexing, structured-data, analytics, rollback, and approval gates.
3. Added `scripts/validate_launch_state.py` and unit tests.
4. Enforced launch-state validation in `.github/workflows/validate-site.yml`.
5. Added draft 1200×630 social-preview SVG artwork for design review.
6. Kept live social tags, canonical URLs, sitemap, CNAME, structured data, analytics, and indexing disabled.
7. Preserved the provisional Tessn and Current naming status and the no-LLC rule.

Remaining:

1. Complete umbrella-brand and product-name screening.
2. Select and acquire the public domain.
3. Activate and verify GitHub Pages.
4. Configure DNS, Pages custom domain, and HTTPS.
5. Generate and review a platform-ready social preview raster.
6. Transition the manifest to `launch_candidate` while keeping indexing disabled.
7. Add canonical, Open Graph, social, sitemap, and accurate structured metadata.
8. Complete content, privacy, terms, accessibility, and launch review.
9. Transition to `launched` and remove noindex only through an explicit reviewed change.

## Milestone 5 — Launch-quality content

1. Validate every public capability claim against the target Current release.
2. Add a concise security and deployment page.
3. Add product architecture and edition information only when commercially settled.
4. Complete accessibility review.
5. Complete performance and broken-link checks.
6. Obtain appropriate legal review for privacy and terms.

## Milestone 6 — Controlled downloads

Cross-repository work begins with `rtessno/current-release` issue #1.

1. Harden `current-release` repository governance.
2. Produce signed and scanned preview installers.
3. Publish checksums, release notes, licensing, and platform requirements.
4. Add access-controlled or public download behavior according to release strategy.
5. Document upgrade, rollback, support, and issue reporting.

## Milestone 7 — Evidence-backed commercialization

1. Run design-partner discovery.
2. Establish operational baselines.
3. Execute a controlled pilot.
4. Publish only verified outcomes.
5. Add a case study or testimonial only with written permission.
