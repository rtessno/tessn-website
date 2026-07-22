# Tessn Website Handoff

## Handoff date

July 21, 2026

## Repository

`rtessno/tessn-website`

## Current state

The initial website foundation was merged into `main` through pull request #1.

Merge commit:

```text
f3dac73e2a367b0e6774175dd656c4305520acd1
```

The repository now contains:

- a responsive Tessn homepage
- a full Current product page
- a design-partner and pilot overview
- founder and operating-principles page
- draft privacy and terms pages
- dependency-free HTML, CSS, JavaScript, and SVG assets
- accessible mobile navigation and visible keyboard focus
- GitHub Pages deployment workflow
- preview noindex controls
- security and contribution policies
- project context, architecture, claims governance, release integration, decisions, roadmap, backlog, and continuation instructions

## Important findings

1. `tessn-website` was reported by GitHub as **public**, even though the founder believed it was private. Verify visibility manually and intentionally.
2. `current-release` was reported as private and empty except for its initial README.
3. No public installer should be linked yet.
4. Tessn should not be presented as an LLC until formation is complete.
5. Current remains a provisional product name pending final clearance.
6. A local clone-based validation could not be run during bootstrap because the execution environment could not resolve GitHub. The site has no dependencies or build step, but deployed route validation remains required.

## Deployment state

The Pages workflow is present on `main` and uploads only `site/`.

No workflow status was attached to the merge commit through the available connector. The likely next action is the repository-level Pages setting:

1. Open Settings → Pages.
2. Select **GitHub Actions** as the source.
3. Trigger or observe `Deploy GitHub Pages`.
4. Validate the generated site URL.
5. Record the URL in this handoff and README.

## Organized issue queue

### Tessn website

- #2 — P0: Activate and verify GitHub Pages deployment
- #3 — P1: Add sanitized Current product screenshots
- #4 — P1: Establish pilot contact and privacy-reviewed intake
- #5 — P1: Complete naming, domain, and launch metadata

### Current release repository

- `rtessno/current-release` #1 — Establish Current release governance before public downloads

## Local preview

```bash
git clone https://github.com/rtessno/tessn-website.git
cd tessn-website
python3 -m http.server 8000 --directory site
```

Open `http://localhost:8000`.

## Immediate next tasks

1. Complete issue #2 and verify Pages deployment.
2. Inspect mobile and desktop rendering at the deployed project URL.
3. Confirm repository visibility is intentional.
4. Choose the pilot contact method through issue #4.
5. Create synthetic, sanitized Current screenshots through issue #3.
6. Continue naming and custom-domain work through issue #5.
7. Keep downloads disabled until the `current-release` governance issue is complete.

## Acceptance criteria for the next pass

- Pages deployment is green.
- Every route loads through the deployed project path.
- Repository visibility is intentional.
- The deployed URL is documented.
- A real contact path exists with appropriate privacy language.
- At least three sanitized product screenshots are present.
- No claim exceeds the demonstrable Current release.
- Documentation reflects the new state after each milestone.
