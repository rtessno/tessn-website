# Tessn Website Handoff

## Handoff date

July 21, 2026

## Repository

`rtessno/tessn-website`

## Work completed

The initial website foundation has been created on branch:

```text
feature/website-foundation
```

It includes:

- a responsive Tessn homepage
- a full Current product page
- a design-partner/pilot overview
- founder and operating-principles page
- draft privacy and terms pages
- custom CSS visual system
- accessible mobile navigation
- conceptual SVG product workflow visual
- GitHub Pages deployment workflow
- preview noindex controls
- security and contribution policies
- project context, architecture, claim governance, release integration, decisions, roadmap, backlog, and continuation instructions

## Important findings

1. `tessn-website` was reported by GitHub as **public**, even though the founder believed it was private.
2. `current-release` was reported as private and empty.
3. No public installer should be linked yet.
4. Tessn should not be presented as an LLC until formation is complete.
5. Current remains a provisional product name pending final clearance.

## Deployment state

The workflow exists but GitHub Pages may still require repository configuration:

1. Merge the foundation pull request to `main`.
2. Open Settings → Pages.
3. Select **GitHub Actions** as the source.
4. Trigger or observe `Deploy GitHub Pages`.
5. Validate the generated site URL.

## Local preview

```bash
git clone https://github.com/rtessno/tessn-website.git
cd tessn-website
git checkout feature/website-foundation
python3 -m http.server 8000 --directory site
```

Open `http://localhost:8000`.

## Immediate next tasks

1. Review and merge the pull request.
2. Enable and verify Pages deployment.
3. Inspect mobile and desktop rendering.
4. Choose the pilot contact method.
5. Create synthetic, sanitized Current screenshots.
6. Replace conceptual visuals with real product evidence.
7. Continue naming and custom-domain work.

## Acceptance criteria for the next pass

- Pages deployment is green.
- Every route loads through the deployed project path.
- Repository visibility is intentional.
- A real contact path exists with appropriate privacy language.
- At least three sanitized product screenshots are present.
- No claim exceeds the demonstrable Current release.
- Documentation reflects the new state.
