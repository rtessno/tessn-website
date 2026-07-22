# Tessn Website Handoff

## Handoff date

July 21, 2026

## Repository

`rtessno/tessn-website`

## Current state

The repository contains the website foundation, deployment verification, Current product-visual evidence gate, controlled pilot-intake foundation, and fail-closed launch metadata controls.

Milestone merges before this branch:

```text
PR #1   — foundation
PR #7   — static deployment validation and route/accessibility fixes
PR #8   — post-deployment HTTP verification and issue reporting
PR #9   — verified Pages activation blocker documentation
PR #10  — Current product visual evidence gate
PR #11  — product visual milestone handoff and roadmap closeout
PR #12  — stable HANDOFF state
PR #13  — controlled pilot intake readiness
```

Use the repository `main` ref as the source of truth rather than copying a commit SHA into this document; updating the handoff itself changes that SHA.

The repository contains:

- responsive Tessn and Current presentation pages
- pilot, About, Privacy, and Terms pages
- dependency-free HTML, CSS, JavaScript, SVG, and Python verification helpers
- accessible mobile navigation and visible keyboard focus
- pre-deployment validation and post-deployment HTTP verification
- preview noindex and crawler-blocking controls
- product-visual evidence governance and manifest validation
- controlled pilot-intake architecture and privacy boundaries
- machine-readable preview and launch state
- draft social-preview artwork for design review
- project context, architecture, decisions, roadmap, backlog, and continuation instructions

## Verified Pages blocker

The deployment rerun remains blocked before artifact upload:

```text
Run: 29889952423
Job: deploy
Failure step: Configure Pages
Artifact upload: skipped
Deployment: skipped
```

The workflow and site are not the blocker. GitHub Pages has not been activated as the repository publishing source.

### Required manual action

1. Open repository **Settings**.
2. Select **Pages** under Code and automation.
3. Under Build and deployment, set **Source** to **GitHub Actions**.
4. Rerun `Deploy GitHub Pages`, or push a new commit to `main`.
5. Confirm the automated issue #2 report changes from FAIL to PASS.

Expected URL, not yet verified:

```text
https://rtessno.github.io/tessn-website/
```

## Product visual evidence milestone

Issue #3 has a completed website-side evidence gate without publishing unreviewed images.

- Current repository: `rtessno/support-copilot`
- observed Current `main`: `4643c749f021c3ebf67075964f8fd5804e62c7e1`
- Current-side execution tracker: `rtessno/support-copilot` issue #1873
- synthetic data is the default public capture mode
- every public image requires an `approved_public` manifest and matching SHA-256
- no accepted public screenshot set has been integrated

The next visual step is to execute issue #1873, capture at least three implemented Current surfaces with synthetic data, review them, and integrate only manifests that pass `scripts/validate_product_visuals.py`.

## Pilot intake milestone

Issue #4 has a completed website-side intake foundation without publishing an invented address or collecting visitor information.

- dedicated business email selected as the initial architecture
- founder GitHub profile removed as the intake path
- public GitHub issues, forms, scheduling tools, and evidence uploads rejected for initial intake
- `docs/PILOT-INTAKE.md` defines activation, qualification, access, retention, and provider gates
- pilot and privacy pages prohibit sensitive evidence and credentials
- static validation enforces the pending state and warning

Remaining blocker: create and secure the mailbox, configure MFA and recovery, choose an enforceable retention process, test it, approve the address for publication, add one working `mailto:` action, and re-review privacy copy.

## Launch metadata milestone

Issue #5 has a fail-closed website-side launch foundation.

Added controls:

- `docs/launch/launch-state.json` records `preview`, `launch_candidate`, or `launched`
- `docs/LAUNCH-CONTROLS.md` defines naming, domain, HTTPS, canonical, social, sitemap, structured-data, analytics, indexing, approval, and rollback gates
- `scripts/validate_launch_state.py` rejects premature launch behavior
- unit tests cover preview acceptance, premature canonical URL, CNAME, indexing, incomplete launch candidate, and launched noindex states
- `.github/workflows/validate-site.yml` runs the launch validator
- `site/assets/images/social-preview.svg` is draft artwork only

The current manifest remains `preview`. Therefore:

- no custom domain or `CNAME`
- no canonical URL
- no sitemap publication
- no live Open Graph URL or social image URL
- no structured data
- no analytics
- no indexing approval
- no legal-entity approval

Remaining issue #5 work:

1. Complete umbrella-brand and product-name screening.
2. Select and acquire the domain.
3. Activate and verify GitHub Pages.
4. Configure DNS, custom-domain Pages settings, and HTTPS.
5. Generate and review a platform-ready social preview raster.
6. Transition to `launch_candidate` while retaining noindex.
7. Add canonical, social, sitemap, and accurate structured metadata.
8. Complete content, privacy, terms, accessibility, and launch review.
9. Transition to `launched` and enable indexing only through an explicit reviewed change.

## Important guardrails

1. `tessn-website` is public and must contain no secrets, customer evidence, private Current source, or installers.
2. `current-release` remains private and is the separate release-governance boundary.
3. No public installer may be linked yet.
4. Tessn must not be presented as an LLC until formation is complete.
5. Current remains a provisional product name pending final clearance.
6. Public claims must remain within `docs/CONTENT-AND-CLAIMS.md`.
7. Preview indexing controls remain enabled.
8. Product visuals require an `approved_public` manifest and exact source commit.
9. Initial pilot intake must not become an evidence-transfer channel.
10. Canonical, domain, structured-data, analytics, and indexing changes must match the launch manifest.

## Organized issue queue

### Tessn website

- #2 — P0 Pages deployment — **blocked only on Settings → Pages → GitHub Actions**
- #3 — P1 Current screenshots — **capture tracked by support-copilot #1873**
- #4 — P1 pilot contact — **foundation complete; mailbox activation pending**
- #5 — P1 naming/domain/metadata — **fail-closed foundation complete; decisions and activation pending**

### Cross-repository

- `rtessno/support-copilot` #1873 — approved synthetic Current product visuals
- `rtessno/current-release` #1 — release governance before public downloads

## Local preview and validation

```bash
git clone https://github.com/rtessno/tessn-website.git
cd tessn-website
python3 -m http.server 8000 --directory site
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/validate_site.py
python3 scripts/validate_product_visuals.py
python3 scripts/validate_launch_state.py
```

Open `http://localhost:8000`.

## Immediate next tasks

1. Perform the manual Pages source change and close issue #2 after deployed verification passes.
2. Execute `support-copilot` issue #1873 and integrate approved screenshots through issue #3.
3. Create and secure the pilot-interest mailbox, then activate issue #4.
4. Complete name screening and domain selection through issue #5.
5. Add concise deployment and trust content without claiming certifications or unsupported controls.
6. Keep downloads disabled until `current-release` governance is complete.

## Acceptance criteria for the next pass

- Pages deployment and post-deployment verification are green.
- Every route loads through the deployed project path.
- At least three reviewed and manifested Current screenshots are present.
- One tested dedicated pilot-interest action exists with accurate privacy language.
- Naming, domain, and launch-state decisions are documented accurately.
- No claim exceeds the demonstrable Current release.
