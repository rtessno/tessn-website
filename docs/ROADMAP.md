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
2. Added dependency-free route, asset, accessibility, preview, pilot-safety, trust-boundary, no-download, and static-quality validation.
3. Added pull-request and `main` validation through `.github/workflows/validate-site.yml`.
4. Fixed the nested project Pages 404 base path.
5. Confirmed the deployment workflow uploads only `site/`.
6. Added post-deployment HTTP verification and marker-based reporting to issue #2.
7. Triggered and reran `Deploy GitHub Pages` from `main`; attempts continue to fail before artifact upload.

Verified blocker:

- latest run `29891467285` failed in the **Configure Pages** step
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

Completed website-side foundation:

1. Confirmed the Current repository has an active synthetic demonstration data policy and seed corpus.
2. Confirmed no accepted public screenshot set or authoritative visual baseline was identified at the observed Current `main` revision.
3. Defined public screenshot acceptance and rejection rules.
4. Added required sidecar manifests and automated validation.
5. Added unit tests for positive and negative evidence states.
6. Opened `rtessno/support-copilot` issue #1873 as the exact-revision synthetic capture handoff.

Remaining:

1. Freeze an exact Current candidate SHA through `support-copilot` issue #1873.
2. Run Current with a synthetic demonstration case.
3. Capture at least three implemented product surfaces.
4. Complete one approved manifest per image.
5. Integrate approved images with factual alternative text and captions.
6. Review mobile and desktop presentation.
7. Update claims governance, handoff, roadmap, and issue #3 after integration.

## Milestone 3 — Pilot conversion path

Status: **Intake foundation complete; dedicated address activation pending — tracked by issue #4**

Completed through PR #13:

1. Selected a dedicated business email as the initial pilot-interest channel architecture.
2. Rejected public GitHub issues, profiles, embedded forms, scheduling tools, and evidence uploads as the initial intake path.
3. Defined minimum first-contact fields and qualification questions.
4. Defined limited-access handling and a retention baseline.
5. Added explicit sensitive-evidence prohibitions.
6. Removed the founder GitHub profile as the intake action.
7. Updated the pilot and privacy pages while keeping direct collection disabled.
8. Added static validation for the pending state and safety warning.

Remaining:

1. Create and secure the dedicated business mailbox.
2. Configure multi-factor authentication and account recovery.
3. Select an enforceable retention process.
4. Test sending and receiving.
5. Publish the approved address and replace the pending state with one working `mailto:` action.
6. Re-review the privacy notice and test mobile and desktop behavior.
7. Close issue #4 only after the public action works.

## Milestone 4 — Brand, domain, and launch metadata

Status: **Fail-closed launch foundation complete; naming and domain decisions pending — tracked by issue #5**

Completed through PR #14:

1. Added a machine-readable preview, launch-candidate, and launched state.
2. Documented naming, domain, HTTPS, metadata, indexing, structured-data, analytics, approval, and rollback gates.
3. Added automated launch-state validation and unit tests.
4. Added draft 1200×630 social-preview artwork for design review.
5. Kept live social tags, canonical URLs, sitemap, CNAME, structured data, analytics, and indexing disabled.
6. Preserved provisional naming and the no-LLC rule.

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

## Milestone 5 — Launch-quality trust and static quality

Status: **Website-side foundation complete; deployed browser review remains blocked on Pages**

Completed website-side foundation:

1. Added `site/trust/index.html`.
2. Distinguished demonstrated website behavior, Current product principles, pilot-specific commitments, and claims that remain unverified.
3. Documented that the preview has no application accounts, payment flow, embedded intake form, first-party analytics, customer-evidence upload, or public installer.
4. Added explicit non-claims for certification, compliance, general availability, uptime, customer counts, measured outcomes, guaranteed diagnosis, named integrations, legal entity, and installer assurance.
5. Added static and deployed-route checks for the Trust page and required boundary language.
6. Added `scripts/validate_quality.py` and unit tests for document language, main/footer landmarks, skip-link targets, heading order, image alternative text, unexpected external asset hosts, and asset budgets.
7. Enforced the static-quality gate in `.github/workflows/validate-site.yml`.

Remaining browser-dependent work through issue #16:

1. Review typography and spacing on iPhone, tablet, compact desktop, wide desktop, and at 200% zoom.
2. Complete keyboard-only and screen-reader review.
3. Review contrast and reduced-motion behavior.
4. Complete deployed performance, caching, console, third-party request, and broken-link checks.
5. Obtain appropriate legal review for Privacy and Terms.
6. Add deployment-specific controls only when demonstrated for the exact pilot configuration.
7. Add product architecture or edition information only when commercially settled and evidence-backed.

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
