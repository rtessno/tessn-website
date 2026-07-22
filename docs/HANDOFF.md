# Tessn Website Handoff

## Handoff date

July 22, 2026

## Repository

`rtessno/tessn-website`

## Current state

The GitHub Pages preview is live:

`https://rtessno.github.io/tessn-website/`

The repository contains:

- revision-bound Current product claims
- product-visual evidence governance
- controlled pilot-intake boundaries
- fail-closed launch metadata
- Trust, Privacy, and Terms pages
- static accessibility and asset-quality validation
- post-deployment HTTP verification
- a documented fail-closed Current documentation-navigation decision

The preview remains `noindex,nofollow`, contains no public download, and is not launch-approved.

## Completed milestones

```text
PR #1   — foundation
PR #7   — static deployment validation and route/accessibility fixes
PR #8   — post-deployment HTTP verification and issue reporting
PR #9   — Pages activation blocker documentation
PR #10  — Current product visual evidence gate
PR #11  — product visual milestone handoff and roadmap closeout
PR #12  — stable HANDOFF state
PR #13  — controlled pilot intake readiness
PR #14  — fail-closed launch metadata guardrails
PR #15  — trust and deployment boundaries
PR #17  — fan-out milestone handoff reconciliation
PR #18  — static accessibility and asset-quality gate
PR #19  — verified Pages deployment reconciliation
PR #21  — revision-bound Current product surfaces and claim validation
```

Use `main` as the website source of truth. Product claim manifests intentionally pin exact authoritative product revisions.

## Current product source review

Issue #20 and PR #21 refreshed the Current page from:

```text
Repository: rtessno/support-copilot
Commit: 4643c749f021c3ebf67075964f8fd5804e62c7e1
Reviewed: July 22, 2026
```

Reviewed paths:

- `README.md`
- `cli-site/README.md`
- `cli-site/src/pages/index.astro`
- `docs-site/README.md`

The Current page distinguishes:

- authenticated web investigation workspace
- Current CLI
- Current Desktop as a development preview
- Docker Compose
- Kubernetes with Helm
- private-beta and design-partner availability
- operator and configuration responsibility
- no-public-download state

Current Desktop must remain described as requiring a separately running Current Server and not bundling the backend, database, Redis, workers, or analyzers.

Future Current claim changes require a new exact upstream SHA, reviewed source paths, manifest update, visible limitations, review date, and passing CI.

## Current documentation-navigation decision

Tracking: issue #22.

Decision: **do not add a Current Docs, CLI install, release, private GitHub repository, or raw OpenAPI link to Tessn at this stage.**

The review found:

- the upstream Pages workflow builds Docs and CLI from `main`
- the public artifact is not stamped with an exact externally verifiable Current source or release identity
- Docs navigation includes installation, customer-distribution, environment-variable, operator-security, OpenAPI, GitHub, and edit-on-GitHub surfaces
- CLI install and release navigation is merged into the same Pages artifact
- private or permission-dependent repository navigation is not a reliable public resource
- the connected environment could not independently resolve and verify the candidate public URL

The full decision and reconsideration gate are in `docs/CURRENT-DOCUMENTATION-NAVIGATION.md`.

`support-copilot/docs-site` remains authoritative for technical documentation. `support-copilot/cli-site` remains authoritative for CLI learning. Tessn owns only whether and how a verified public action is presented.

A later link requires exact deployed identity, route/search verification, public-safe navigation, consistency with `current-release`, explicit allowlisting, maturity/support boundaries, and rollback behavior.

## Validation state

Pull-request CI runs:

- Python helper compilation
- unit tests
- route, asset, navigation, preview, pilot, trust, and no-download validation
- static language, landmark, skip-link, heading, image-alt, external-request, and asset-budget validation
- exact-source Current product claim validation
- Current screenshot evidence validation
- launch-state validation

The post-deployment verifier requires the refreshed Current maturity, Web, CLI, Desktop development-preview, separate-server, Docker Compose, Kubernetes/Helm, and no-download text.

Issue #16 must confirm the deployment marker has refreshed against those stronger checks before closing the new-copy verification item.

## Active deployed quality review

Issue #16 remains active.

Repository-side automation is complete. Browser-dependent work remains:

- iPhone, tablet, compact desktop, wide desktop, and 200% zoom review
- expanded Current-page layout and card stacking
- keyboard-only navigation and screen-reader spot checks
- contrast and reduced-motion review
- browser page-weight and performance measurements
- caching, console, and network-request inspection
- browser-level broken-link review
- Trust, Privacy, and Terms reconciliation against deployed behavior
- appropriate legal review before commercial launch

## Product visual evidence

Issue #3 and `rtessno/support-copilot#1873` remain open.

- synthetic data is the default public capture mode
- at least three implemented Current surfaces are required
- each image requires an `approved_public` manifest and matching SHA-256
- no accepted public Current screenshot set has been integrated

This task requires a locally rendered Current instance. Repository-only GitHub actions cannot generate genuine product screenshots.

## Pilot intake

Issue #4 has a completed website-side foundation.

Remaining external work:

- create the dedicated mailbox
- configure MFA and recovery
- select an enforceable retention process
- test sending and receiving
- approve the address for publication
- add one working `mailto:` action
- re-review privacy copy and rendered behavior

No address may be invented.

## Naming, domain, and launch metadata

Issue #5 remains open.

Current state:

- `docs/launch/launch-state.json` is `preview`
- no custom domain or `CNAME`
- no canonical URL or sitemap
- no live Open Graph URL or social image URL
- no structured data or analytics
- no indexing or legal-entity approval
- draft social-preview SVG only

Remaining external decisions and activation:

- umbrella and product-name screening
- domain selection and purchase
- DNS, Pages custom domain, and HTTPS
- platform-ready social raster
- `launch_candidate` transition while retaining noindex
- final metadata and launch review
- explicit `launched` transition before indexing

## Release governance

`rtessno/current-release` issue #1 is the no-download authority.

The repository is private but completely empty and has no initial Git commit. The connected contents interface cannot create the root commit in an empty repository.

One-time maintainer action:

1. Create a minimal `README.md` commit on `current-release/main`.
2. Keep the repository private and artifact-free.

After bootstrap, implement through a feature branch and pull request:

- release policy and fail-closed machine-readable state
- supported-platform matrix without guessing
- immutable artifact records
- signing and notarization
- SHA-256, malware scanning, and SBOM controls
- licensing and access decisions
- support and vulnerability-reporting boundaries
- installation, upgrade, rollback, withdrawal, and release-note templates
- validation, tests, and CI

Tessn must continue showing `No public download` until an exact artifact passes every release gate.

## Cross-repository website responsibility

Private trackers: `rtessno/software-portfolio#9` and `#10`.

Recommended model:

- `tessn-website` — umbrella narrative, concise product directory, pilot entry, umbrella trust/legal
- `support-copilot/website` — eventual authoritative detailed Current marketing and evaluation site after deployment approval
- `support-copilot/docs-site` and `cli-site` — authoritative technical learning surfaces after public-safety verification
- `portfolio-web` — governance and migration source, not a competing production website

Keep detailed Current content in Tessn only as the deployed fallback until the dedicated Current website is hosted and verified.

## Guardrails

1. `tessn-website` is public and must contain no secrets, customer evidence, private Current source, or installers.
2. No public installer may be linked.
3. Tessn must not be presented as an LLC until formation is complete.
4. Current remains a provisional product name pending clearance.
5. Claims must remain within `docs/CONTENT-AND-CLAIMS.md` and the Current claim manifest.
6. Preview indexing controls remain enabled.
7. Product visuals require exact source, approved manifests, synthetic or reviewed data, and matching hashes.
8. Initial pilot intake must not become an evidence-transfer channel.
9. Domain, metadata, analytics, structured-data, and indexing changes must match the launch manifest.
10. Documentation links require exact deployed identity, public-safety review, allowlisting, release consistency, and rollback.
11. Internal tests, packaging paths, or roadmaps are not public assurance.
12. Maturity, availability, limitations, and release state remain visible beside capabilities.

## Open queue

### Tessn website

- #16 — deployed responsive, accessibility, performance, and legal review
- #3 — Current screenshots; capture tracked by `support-copilot#1873`
- #4 — pilot mailbox activation
- #5 — naming, domain, metadata, and launch
- #22 — documentation-navigation audit; close after the decision PR merges

### Cross-repository

- `software-portfolio#9` — cross-repository content promotion
- `software-portfolio#10` — website responsibility model
- `support-copilot#1873` — approved synthetic Current visuals
- `current-release#1` — initial repository bootstrap and release governance

## Immediate continuation order

1. Merge the documentation-navigation decision and close issue #22.
2. Confirm the strengthened post-PR #21 deployment marker and continue issue #16.
3. Perform local Current synthetic screenshot capture through `support-copilot#1873`.
4. Create and secure the pilot mailbox.
5. Complete naming and domain decisions.
6. Create the initial `current-release` README commit, then implement release governance.
7. Approve the three-site responsibility model before expanding portfolio breadth.