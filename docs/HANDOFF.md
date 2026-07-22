# Tessn Website Handoff

## Handoff date

July 22, 2026

## Repository

`rtessno/tessn-website`

## Current state

The repository contains the website foundation, deployment verification, Current product-visual evidence gate, controlled pilot-intake foundation, fail-closed launch metadata controls, public trust/deployment boundaries, and a pre-deployment static-quality gate.

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
PR #14  — fail-closed launch metadata guardrails
PR #15  — trust and deployment boundaries
PR #17  — fan-out milestone handoff reconciliation
```

Use the repository `main` ref as the source of truth rather than copying a commit SHA into this document.

The repository contains:

- responsive Tessn and Current presentation pages
- Pilot, About, Trust, Privacy, and Terms pages
- dependency-free HTML, CSS, JavaScript, SVG, and Python verification helpers
- pre-deployment route, accessibility, static-quality, visual-evidence, and launch-state validation
- post-deployment HTTP verification
- preview noindex and crawler-blocking controls
- product-visual evidence governance and manifest validation
- controlled pilot-intake architecture and privacy boundaries
- machine-readable preview and launch state
- draft social-preview artwork for design review
- trust and deployment content that distinguishes demonstrated behavior, product direction, pilot commitments, and non-claims
- project context, architecture, decisions, roadmap, backlog, and continuation instructions

## Verified Pages blocker

The latest `main` deployment remains blocked before artifact upload:

```text
Run: 29891467285
Job: deploy
Failure step: Configure Pages
Artifact upload: skipped
Deployment: skipped
```

Required manual action:

1. Open repository **Settings**.
2. Select **Pages** under Code and automation.
3. Set **Build and deployment → Source** to **GitHub Actions**.
4. Rerun `Deploy GitHub Pages`, or push a new commit to `main`.
5. Confirm the automated issue #2 report changes from FAIL to PASS.

Expected URL, not yet verified:

```text
https://rtessno.github.io/tessn-website/
```

After successful deployment, issue #2 automatically verifies Home, Current, Pilot, About, Trust, Privacy, Terms, CSS, JavaScript, SVG assets, preview crawler controls, pilot safety copy, trust boundaries, and nested 404 behavior.

## Static quality milestone

The current continuation branch adds:

- `scripts/validate_quality.py`
- `tests/test_validate_quality.py`
- CI enforcement in `.github/workflows/validate-site.yml`

The gate checks:

- `lang` and non-empty page titles
- exactly one main and one footer landmark
- valid skip-link targets
- exactly one h1 and no skipped heading levels
- image alt attributes
- unexpected external asset hosts and protocol-relative references
- HTML, CSS, JavaScript, and SVG file-size budgets

These checks complete the repository-automatable portion of issue #16. Real browser, assistive-technology, performance, caching, console, and network review still require a working deployed URL.

## Product visual evidence

Issue #3 remains open for actual captures.

- Current-side tracker: `rtessno/support-copilot` issue #1873
- synthetic data is the default public capture mode
- every public image requires an `approved_public` manifest and matching SHA-256
- no accepted public Current screenshot set has been integrated

Next step: execute issue #1873, capture at least three implemented Current surfaces with synthetic data, review them, and integrate only manifests that pass `scripts/validate_product_visuals.py`.

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

- `docs/launch/launch-state.json` remains `preview`
- no custom domain or `CNAME`
- no canonical URL or sitemap
- no live Open Graph URL or social image URL
- no structured data or analytics
- no indexing or legal-entity approval
- draft social-preview SVG exists for design review only

Remaining: complete name screening, acquire the domain, activate Pages, configure DNS and HTTPS, generate a platform-ready raster, transition to `launch_candidate` while retaining noindex, add final metadata, complete launch review, then explicitly transition to `launched`.

## Deployed quality review

Issue #16 now separates completed static automation from browser-dependent work.

Completed repository-side checks:

- document language and title
- main/footer landmarks
- skip links
- heading order
- image alternative text
- unexpected external asset hosts
- static asset budgets

Remaining after issue #2 passes:

- iPhone, tablet, compact desktop, wide desktop, and 200% zoom review
- keyboard-only navigation and screen-reader spot checks
- contrast and reduced-motion review
- deployed broken-link, page-weight, image-size, caching, console, and third-party-request checks
- Trust, Privacy, and Terms review against actual deployed behavior
- appropriate legal review before commercial launch

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
11. Trust content must not convert roadmap direction or internal tests into public assurance claims.

## Organized issue queue

### Tessn website

- #2 — P0 Pages deployment — **blocked only on Settings → Pages → GitHub Actions**
- #16 — P1 deployed responsive/accessibility/performance review — **static automation advanced; browser review blocked on issue #2**
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
python3 scripts/validate_quality.py
python3 scripts/validate_product_visuals.py
python3 scripts/validate_launch_state.py
```

Open `http://localhost:8000`.

## Immediate next tasks

1. Perform the manual Pages source change and close issue #2 after deployed verification passes.
2. Execute the browser-dependent remainder of issue #16 against the working deployed URL.
3. Execute `support-copilot` issue #1873 and integrate approved screenshots through issue #3.
4. Create and secure the pilot-interest mailbox, then activate issue #4.
5. Complete name screening and domain selection through issue #5.
6. Keep downloads disabled until `current-release` governance is complete.

## Acceptance criteria for the next pass

- Pages deployment and post-deployment verification are green.
- Every route, including Trust, loads through the deployed project path.
- Issue #16 records responsive, accessibility, performance, and integrity results.
- At least three reviewed and manifested Current screenshots are present.
- One tested dedicated pilot-interest action exists with accurate privacy language.
- Naming, domain, and launch-state decisions are documented accurately.
- No claim exceeds the demonstrable Current release or exact deployment scope.
