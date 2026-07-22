# Tessn Website Handoff

## Handoff date

July 21, 2026

## Repository

`rtessno/tessn-website`

## Current state

The initial website foundation was merged into `main` through pull request #1. Deployment-readiness hardening is active in draft pull request #7 on branch `agent/pages-activation-verification`.

Foundation merge commit:

```text
f3dac73e2a367b0e6774175dd656c4305520acd1
```

The repository contains:

- a responsive Tessn homepage
- a full Current product page
- a design-partner and pilot overview
- founder and operating-principles page
- draft privacy and terms pages
- dependency-free HTML, CSS, JavaScript, and SVG assets
- accessible mobile navigation and visible keyboard focus
- GitHub Pages deployment workflow
- static-site validation workflow and dependency-free validator
- preview noindex controls
- security and contribution policies
- project context, architecture, claims governance, release integration, decisions, roadmap, backlog, and continuation instructions

## Deployment-readiness milestone

PR #7 adds and has successfully run a validation gate that checks:

- all seven HTML pages and required assets
- internal routes and references
- primary-navigation accessibility labels
- preview `noindex` and `robots.txt` controls
- the prohibition on public installer links
- the nested project Pages 404 base path

The deployment workflow still uploads only `site/`.

## Important findings

1. `tessn-website` is currently **public**. Its tracked content is presentation source and governance documentation intended to contain no secrets, customer evidence, private product code, or installers.
2. GitHub Pages on GitHub Free requires a public repository; private-repository Pages requires an eligible paid plan. The public state is being retained for the current Pages preview unless the hosting plan changes.
3. `current-release` is private and must remain the separate release-governance boundary.
4. No public installer should be linked yet.
5. Tessn must not be presented as an LLC until formation is complete.
6. Current remains a provisional product name pending final clearance.

## Deployment state

Expected project Pages URL:

```text
https://rtessno.github.io/tessn-website/
```

Completed:

- deployment workflow reviewed
- artifact scope confirmed as `site/` only
- route and asset validation added and green on PR #7
- 404 project-path defect repaired
- Privacy and Terms navigation labeling repaired

Remaining manual/external verification:

1. Open Settings → Pages.
2. Confirm **GitHub Actions** is selected as the source.
3. Merge PR #7 to trigger validation and deployment from `main`.
4. Observe `Deploy GitHub Pages` complete successfully.
5. Validate `/`, `/current/`, `/pilot/`, `/about/`, `/privacy/`, `/terms/`, assets, mobile navigation, and a nested 404 over HTTP.
6. Record the verified deployment result here and in README, then close issue #2.

## Organized issue queue

### Tessn website

- #2 — P0: Activate and verify GitHub Pages deployment — **in progress through PR #7**
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

1. Complete issue #2 by confirming the Pages source, merging PR #7, and verifying the deployed site.
2. Inspect mobile and desktop rendering at the deployed project URL.
3. Begin issue #3 only with synthetic or irreversibly sanitized Current visuals.
4. Choose the pilot contact method through issue #4 before collecting any visitor information.
5. Continue naming and custom-domain work through issue #5.
6. Keep downloads disabled until the `current-release` governance issue is complete.

## Acceptance criteria for the next pass

- Pages deployment is green.
- Every route loads through the deployed project path.
- Repository visibility remains intentional.
- The deployed URL is documented as verified.
- A real contact path exists with appropriate privacy language.
- At least three sanitized product screenshots are present.
- No claim exceeds the demonstrable Current release.
- Documentation reflects the new state after every milestone.
