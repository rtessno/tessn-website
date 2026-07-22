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
8. Triggered `Deploy GitHub Pages` from `main` and captured the exact failure state.

Verified blocker:

- workflow run `29889297595` failed in the **Configure Pages** step
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

Remaining:

1. Freeze an exact Current candidate SHA.
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

Status: **Queued — tracked by issue #4**

1. Select a public contact channel.
2. Decide whether intake uses email, scheduling, or a privacy-reviewed form provider.
3. Define pilot qualification questions.
4. Draft pilot overview, commercial boundaries, and success measures.
5. Update the privacy notice before collecting information.
6. Replace the temporary GitHub-profile action.

## Milestone 4 — Brand and domain

Status: **Queued — tracked by issue #5**

1. Complete product-name and parent-name screening.
2. Decide the public umbrella name.
3. Purchase the selected domain.
4. Configure DNS and GitHub Pages custom-domain settings.
5. Enforce HTTPS.
6. Add canonical URLs, social cards, sitemap, and structured metadata.
7. Remove noindex only after launch review.

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
