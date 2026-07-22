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

Status: **Complete — issue #2 closed**

Verified preview:

`https://rtessno.github.io/tessn-website/`

Completed:

1. Confirmed the repository is public and contains only presentation-site source and governance documentation suitable for public visibility.
2. Added dependency-free route, asset, accessibility, preview, pilot-safety, trust-boundary, no-download, and static-quality validation.
3. Added pull-request and `main` validation through `.github/workflows/validate-site.yml`.
4. Fixed the nested project Pages 404 base path.
5. Confirmed the deployment workflow uploads only `site/`.
6. Added post-deployment HTTP verification and marker-based reporting.
7. Activated GitHub Pages with GitHub Actions as the publishing source.
8. Verified 15/15 deployed routes, assets, preview controls, and boundary checks.
9. Closed issue #2 as completed.

The deployed preview remains `noindex,nofollow` and is not launch-approved.

## Milestone 1A — Current product surfaces and claim provenance

Status: **Complete through PR #21 and issue #20**

Completed:

1. Audited cross-repository website material through `rtessno/software-portfolio#9`.
2. Selected exact authoritative Current revision `4643c749f021c3ebf67075964f8fd5804e62c7e1`.
3. Reviewed `README.md`, `cli-site/README.md`, `cli-site/src/pages/index.astro`, and `docs-site/README.md`.
4. Added `docs/product-claims/current.json` with maturity, availability, surfaces, deployment models, trust boundaries, limitations, and prohibited claims.
5. Added `scripts/validate_product_claims.py` and positive/negative unit tests.
6. Enforced claim validation in `.github/workflows/validate-site.yml`.
7. Refreshed the Current page with explicit Web, CLI, Desktop development-preview, Docker Compose, and Kubernetes/Helm sections.
8. Added `docs/CURRENT-SOURCE-REVIEW.md` and expanded content-governance rules.
9. Preserved private-beta, no-download, no-certification, no-outcome-guarantee, and configuration-specific trust boundaries.

Continuation rule:

- Later Current claims require a new exact source commit, source-path review, manifest update, visible limitation review, and CI validation.
- Product visuals remain separately governed through issue #3 and `support-copilot#1873`.

## Milestone 1B — Current documentation navigation

Status: **Audit complete; link-free decision recorded through issue #22**

Completed:

1. Reviewed the upstream Docs and CLI Pages workflow and source configuration.
2. Confirmed the Pages workflow builds Docs and CLI from `main` but does not publish an exact externally verifiable source or release identity.
3. Confirmed the documentation navigation contains installation, customer-distribution, environment-variable, operator-security, OpenAPI, GitHub, and edit-on-GitHub surfaces.
4. Confirmed the CLI product site is merged into the same Pages artifact and includes install and release navigation.
5. Added `docs/CURRENT-DOCUMENTATION-NAVIGATION.md`.
6. Expanded `docs/CONTENT-AND-CLAIMS.md` with the external documentation gate.
7. Chose to keep Tessn link-free rather than presenting a permission-dependent or distribution-oriented technical surface as a neutral public resource.

Reconsideration requires:

- stable public HTTPS deployment
- exact deployed source or release identity
- route and search verification
- public-safe navigation independent of private repository access
- consistency with the `current-release` state
- visible maturity, availability, support, and release boundaries
- explicit allowlisting, deployed verification, and rollback behavior

Tessn must not fork detailed Current operator documentation. `support-copilot/docs-site` and `support-copilot/cli-site` remain authoritative.

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
7. Activated and verified the GitHub Pages project preview.

Remaining:

1. Complete umbrella-brand and product-name screening.
2. Select and acquire the public domain.
3. Configure DNS, Pages custom domain, and HTTPS.
4. Generate and review a platform-ready social preview raster.
5. Transition the manifest to `launch_candidate` while keeping indexing disabled.
6. Add canonical, Open Graph, social, sitemap, and accurate structured metadata.
7. Complete content, privacy, terms, accessibility, and launch review.
8. Transition to `launched` and remove noindex only through an explicit reviewed change.

## Milestone 5 — Launch-quality trust and static quality

Status: **Static foundation complete; deployed browser review active through issue #16**

Completed website-side foundation:

1. Added `site/trust/index.html`.
2. Distinguished demonstrated website behavior, Current product principles, pilot-specific commitments, and claims that remain unverified.
3. Documented that the preview has no application accounts, payment flow, embedded intake form, first-party analytics, customer-evidence upload, or public installer.
4. Added explicit non-claims for certification, compliance, general availability, uptime, customer counts, measured outcomes, guaranteed diagnosis, named integrations, legal entity, and installer assurance.
5. Added static and deployed-route checks for the Trust page and required boundary language.
6. Added `scripts/validate_quality.py` and unit tests for document language, main/footer landmarks, skip-link targets, heading order, image alternative text, unexpected external asset hosts, and asset budgets.
7. Enforced the static-quality gate in `.github/workflows/validate-site.yml`.
8. Verified all deployed routes and required assets over HTTP.
9. Added exact-source product-claim validation for maturity, availability, surfaces, deployments, limitations, and prohibited claims.

Active browser-dependent work through issue #16:

1. Confirm the strengthened post-PR #21 Current-route checks against the deployed preview.
2. Review typography and spacing on iPhone, tablet, compact desktop, wide desktop, and at 200% zoom.
3. Complete keyboard-only and screen-reader review.
4. Review contrast and reduced-motion behavior.
5. Complete deployed performance, caching, console, third-party request, and browser broken-link checks.
6. Obtain appropriate legal review for Privacy and Terms.
7. Add deployment-specific controls only when demonstrated for the exact pilot configuration.
8. Add product architecture or edition information only when commercially settled and evidence-backed.

## Milestone 6 — Controlled downloads

Status: **Blocked on one-time empty-repository bootstrap in `rtessno/current-release` issue #1**

1. Create the initial README commit on `current-release/main`.
2. Build release governance through a feature branch and pull request.
3. Define supported platforms and fail-closed release states.
4. Define immutable artifact records, signing, notarization, malware scanning, checksums, SBOMs, licensing, access, support, upgrade, rollback, withdrawal, and reporting.
5. Add validation and tests.
6. Produce an exact reviewed preview artifact only after the governance foundation passes.
7. Add website release status or access behavior only after explicit approval.

## Milestone 7 — Evidence-backed commercialization

1. Run design-partner discovery.
2. Establish operational baselines.
3. Execute a controlled pilot.
4. Publish only verified outcomes.
5. Add a case study or testimonial only with written permission.