# Tessn Website Handoff

## Handoff date

July 21, 2026

## Repository

`rtessno/tessn-website`

## Current state

The website foundation and deployment-readiness controls are merged to `main`.

Key merges:

```text
PR #1  — foundation
PR #7  — static deployment validation and route/accessibility fixes
PR #8  — post-deployment HTTP verification and issue reporting
```

Current `main` commit after PR #8:

```text
8b5a324c77417a41834f44404903874d7a17d53b
```

The repository contains:

- a responsive Tessn homepage
- a full Current product page
- a design-partner and pilot overview
- founder and operating-principles page
- draft privacy and terms pages
- dependency-free HTML, CSS, JavaScript, SVG, and Python verification helpers
- accessible mobile navigation and visible keyboard focus
- GitHub Pages deployment workflow
- pre-deployment static validation workflow
- post-deployment HTTP verification workflow
- preview noindex controls
- security and contribution policies
- project context, architecture, claims governance, release integration, decisions, roadmap, backlog, and continuation instructions

## Completed deployment-readiness controls

The repository now verifies:

- all seven HTML pages and required assets
- internal routes and references
- primary-navigation accessibility labels
- preview `noindex` and `robots.txt` controls
- the prohibition on public installer links
- nested project Pages 404 behavior
- deployed route, asset, content-type, preview-directive, and 404 responses after a successful Pages deployment

Post-deployment results are written to one marker-based comment on issue #2 while that issue remains open.

## Verified Pages blocker

The `Deploy GitHub Pages` run below was triggered from `main` after PR #8:

```text
Run: 29889297595
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

## Important guardrails

1. `tessn-website` is public and must contain no secrets, customer evidence, private Current source, or installers.
2. `current-release` remains private and is the separate release-governance boundary.
3. No public installer may be linked yet.
4. Tessn must not be presented as an LLC until formation is complete.
5. Current remains a provisional product name pending final clearance.
6. Public claims must remain within `docs/CONTENT-AND-CLAIMS.md`.
7. Preview indexing controls remain enabled.

## Organized issue queue

### Tessn website

- #2 — P0: Activate and verify GitHub Pages deployment — **blocked only on Settings → Pages → GitHub Actions**
- #3 — P1: Add sanitized Current product screenshots
- #4 — P1: Establish pilot contact and privacy-reviewed intake
- #5 — P1: Complete naming, domain, and launch metadata

### Current release repository

- `rtessno/current-release` #1 — Establish Current release governance before public downloads

## Local preview and validation

```bash
git clone https://github.com/rtessno/tessn-website.git
cd tessn-website
python3 -m http.server 8000 --directory site
python3 scripts/validate_site.py
```

Open `http://localhost:8000`.

## Immediate next tasks

1. Perform the manual Pages source change and confirm issue #2 passes.
2. Verify mobile and desktop rendering at the deployed URL, then close issue #2.
3. Continue issue #3 only with evidence from an exact Current revision and synthetic or irreversibly sanitized data.
4. Choose the pilot contact method through issue #4 before collecting visitor information.
5. Continue naming and custom-domain work through issue #5.
6. Keep downloads disabled until the `current-release` governance issue is complete.

## Acceptance criteria for the next pass

- Pages deployment and post-deployment verification are green.
- Every route loads through the deployed project path.
- The deployed URL is documented as verified.
- At least three reviewed and sanitized Current screenshots are present.
- A real contact path exists with appropriate privacy language.
- No claim exceeds the demonstrable Current release.
- Documentation reflects the new state after every milestone.
