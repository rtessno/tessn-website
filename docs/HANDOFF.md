# Tessn Website Handoff

## Handoff date

July 22, 2026

## Repository

`rtessno/tessn-website`

## Current state

The GitHub Pages preview is live and verified:

`https://rtessno.github.io/tessn-website/`

Issue #2 is closed after **15/15** automated deployment checks passed. The repository contains revision-bound Current product claims, the Current product-visual evidence gate, controlled pilot-intake foundation, fail-closed launch metadata controls, public trust/deployment boundaries, and static-quality validation.

Milestone merges:

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

Use the repository `main` ref as the website source of truth. Product claim manifests intentionally pin authoritative upstream product commits.

## Verified Pages deployment

Public preview:

```text
https://rtessno.github.io/tessn-website/
```

Automated verification passed 15/15 checks for Home, Current, Pilot, About, Trust, Privacy, Terms, CSS, JavaScript, required SVG assets, `robots.txt`, pilot and trust boundaries, and nested custom 404 behavior.

The preview remains `noindex,nofollow`; successful deployment does not imply launch approval.

## Current product source review

Issue #20 and PR #21 refreshed the Current page from exact authoritative source evidence.

Pinned source:

```text
Repository: rtessno/support-copilot
Commit: 4643c749f021c3ebf67075964f8fd5804e62c7e1
Reviewed: July 22, 2026
```

Reviewed source paths:

- `README.md`
- `cli-site/README.md`
- `cli-site/src/pages/index.astro`
- `docs-site/README.md`

Added:

- `docs/product-claims/current.json`
- `docs/CURRENT-SOURCE-REVIEW.md`
- `scripts/validate_product_claims.py`
- `tests/test_validate_product_claims.py`
- CI claim-validation step

The Current page now distinguishes:

- authenticated web investigation workspace
- Current CLI
- Current Desktop as a development preview
- Docker Compose
- Kubernetes with Helm
- private-beta and design-partner availability
- operator and configuration responsibility
- no-public-download state

Current Desktop must remain described as requiring a separately running Current Server and not bundling the backend, database, Redis, workers, or analyzers.

Future Current claim changes require a new exact upstream SHA, source-path review, manifest update, visible limitation review, and full validation. Do not infer public capabilities from roadmaps, tests, pre-releases, or branch names alone.

## Static quality and claim validation

CI currently runs:

- Python helper compilation
- all unit tests
- route, asset, navigation, preview, pilot, trust, and no-download validation
- static language, landmark, skip-link, heading, image-alt, external-request, and asset-budget validation
- exact-source Current product claim validation
- Current screenshot evidence validation
- launch-state validation

The Current claim gate rejects claim drift such as public downloads, general availability, an unbounded Desktop status, missing limitations, missing source evidence, or incomplete visible page boundaries.

## Active deployed quality review

Issue #16 is active and unblocked.

Remaining browser-dependent work:

- iPhone, tablet, compact desktop, wide desktop, and 200% zoom review
- expanded Current-page layout review
- keyboard-only navigation and screen-reader spot checks
- contrast and reduced-motion review
- browser page-weight and performance measurements
- caching, console, and network-request inspection
- browser-level broken-link and layout review
- Trust, Privacy, and Terms reconciliation against deployed behavior
- appropriate legal review before commercial launch

## Product visual evidence

Issue #3 remains open for actual captures.

- Current-side tracker: `rtessno/support-copilot` issue #1873
- synthetic data is the default public capture mode
- every public image requires an `approved_public` manifest and matching SHA-256
- no accepted public Current screenshot set has been integrated

Next step: execute issue #1873, capture at least three implemented Current surfaces with synthetic data, review them, and integrate only manifests that pass `scripts/validate_product_visuals.py`.

## Cross-repository website audit

Private tracker: `rtessno/software-portfolio#9`.

Findings:

- `support-copilot` is authoritative for Current product claims.
- `portfolio-web` contains strong product, documentation, media, release, deployment, SBOM/provenance, rollback, and incident-response governance patterns.
- `brand-assets` contains candidate visual packs but human sign-off remains pending.
- Ouli and PhrasePilot have viable public narratives but should not dilute the Current conversion path without a deliberate portfolio decision.
- I Love Me and Travel Buddy are later Labs candidates after publication and visual-evidence review.
- Oulifit governance patterns may be reused internally; its storefront positioning should remain separate by default.
- private pricing, buyer strategy, revenue hypotheses, risk registers, and internal operating details must not be copied into the public website.

Near-term responsibility model: keep `tessn-website` as the live dependency-free public site and selectively port validated governance concepts rather than maintaining two public website sources of truth.

## Pilot intake

Issue #4 has a completed website-side foundation.

- dedicated business email selected as the initial architecture
- founder GitHub profile removed as the intake path
- public GitHub issues, forms, scheduling tools, and evidence uploads rejected for initial intake
- pilot and privacy pages prohibit sensitive evidence and credentials
- website still collects no information directly
- static validation enforces the pending state and warning

Remaining blocker: create and secure the mailbox, configure MFA and recovery, select an enforceable retention process, test it, approve the address for publication, add one working `mailto:` action, and re-review privacy copy.

## Launch metadata

Issue #5 has a fail-closed website-side foundation.

- GitHub Pages project preview is verified
- `docs/launch/launch-state.json` remains `preview`
- no custom domain or `CNAME`
- no canonical URL or sitemap
- no live Open Graph URL or social image URL
- no structured data or analytics
- no indexing or legal-entity approval
- draft social-preview SVG exists for design review only

Remaining: complete name screening, acquire the domain, configure DNS and HTTPS, generate a platform-ready raster, transition to `launch_candidate` while retaining noindex, add final metadata, complete launch review, then explicitly transition to `launched`.

## Important guardrails

1. `tessn-website` is public and must contain no secrets, customer evidence, private Current source, or installers.
2. `current-release` remains private and is the separate release-governance boundary.
3. No public installer may be linked yet.
4. Tessn must not be presented as an LLC until formation is complete.
5. Current remains a provisional product name pending final clearance.
6. Public claims must remain within `docs/CONTENT-AND-CLAIMS.md` and the Current claim manifest.
7. Preview indexing controls remain enabled.
8. Product visuals require an `approved_public` manifest and exact source commit.
9. Initial pilot intake must not become an evidence-transfer channel.
10. Canonical, domain, structured-data, analytics, and indexing changes must match the launch manifest.
11. Trust content must not convert roadmap direction, tests, packaging, or internal controls into public assurance claims.
12. Product maturity, availability, limitations, and release state must remain visible beside capability claims.
13. Public documentation URLs require separate deployed verification and validator approval.

## Organized issue queue

### Tessn website

- #16 — P1 deployed responsive/accessibility/performance review — **active and unblocked**
- #3 — P1 Current screenshots — **capture tracked by support-copilot #1873**
- #4 — P1 pilot contact — **foundation complete; mailbox activation pending**
- #5 — P1 naming/domain/metadata — **fail-closed foundation complete; decisions and activation pending**
- #20 — P1 Current product surfaces — **completed through PR #21**
- #2 — P0 Pages deployment — **closed; 15/15 checks passed**

### Cross-repository

- `rtessno/software-portfolio` #9 — cross-repository content promotion and website responsibility model
- `rtessno/support-copilot` #1873 — approved synthetic Current product visuals
- `rtessno/current-release` #1 — release governance before public downloads

## Local preview and validation

```bash
git clone https://github.com/rtessno/tessn-website.git
cd tessn-website
python3 -m http.server 8000 --directory site
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/validate_site.py
python3 scripts/validate_quality.py
python3 scripts/validate_product_claims.py
python3 scripts/validate_product_visuals.py
python3 scripts/validate_launch_state.py
```

Open `http://localhost:8000`.

## Immediate next tasks

1. Execute issue #16 against the verified deployed URL, including the expanded Current page.
2. Execute `support-copilot` issue #1873 and integrate approved screenshots through issue #3.
3. Verify the public Current documentation deployment before adding navigation to it.
4. Create and secure the pilot-interest mailbox, then activate issue #4.
5. Complete name screening and domain selection through issue #5.
6. Keep downloads disabled until `current-release` governance is complete.
7. Decide portfolio breadth through `software-portfolio#9` only after Current remains a clear primary conversion path.

## Acceptance criteria for the next pass

- Issue #16 records responsive, accessibility, performance, and integrity results for the refreshed page.
- At least three reviewed and manifested Current screenshots are present.
- Any documentation link is verified, public-safe, and explicitly allowlisted.
- One tested dedicated pilot-interest action exists with accurate privacy language.
- Naming, domain, and launch-state decisions are documented accurately.
- No claim exceeds the exact reviewed Current release or deployment scope.
