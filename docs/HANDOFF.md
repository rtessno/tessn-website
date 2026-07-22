# Tessn Website Handoff

## Handoff date

July 21, 2026

## Repository

`rtessno/tessn-website`

## Current state

The website foundation, deployment-readiness controls, verified Pages-blocker documentation, Current product visual evidence gate, and controlled pilot-intake foundation are implemented in repository history.

Milestone merges before this pass:

```text
PR #1   — foundation
PR #7   — static deployment validation and route/accessibility fixes
PR #8   — post-deployment HTTP verification and issue reporting
PR #9   — verified Pages activation blocker documentation
PR #10  — Current product visual evidence gate
PR #11  — product visual milestone handoff and roadmap closeout
PR #12  — stable HANDOFF state
```

Use the repository `main` ref as the source of truth rather than copying a commit SHA into this document; updating the handoff itself changes that SHA.

The repository contains:

- a responsive Tessn homepage
- a full Current product page
- a design-partner and pilot overview
- founder and operating-principles page
- draft privacy and terms pages
- dependency-free HTML, CSS, JavaScript, SVG, and Python verification helpers
- accessible mobile navigation and visible keyboard focus
- GitHub Pages deployment workflow
- pre-deployment static and product-visual validation workflow
- post-deployment HTTP verification workflow
- preview noindex controls
- security and contribution policies
- product visual evidence governance and manifest template
- controlled pilot-intake architecture and qualification rules
- project context, architecture, claims governance, release integration, decisions, roadmap, backlog, and continuation instructions

## Completed deployment-readiness controls

The repository verifies:

- all HTML pages and required assets
- internal routes and references
- primary-navigation accessibility labels
- preview `noindex` and `robots.txt` controls
- the prohibition on public installer links
- nested project Pages 404 behavior
- the pilot contact-pending state and sensitive-evidence warning
- deployed route, asset, content-type, preview-directive, and 404 responses after a successful Pages deployment

Post-deployment results are written to one marker-based comment on issue #2 while that issue remains open.

## Verified Pages blocker

The deployment was rerun during the continuation pass:

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

Verified source context:

- Current repository: `rtessno/support-copilot`
- observed Current `main`: `4643c749f021c3ebf67075964f8fd5804e62c7e1`
- active synthetic demonstration policy and seed corpus are present
- the Current visual capture protocol states that no screenshot or visual baseline is accepted by that document
- no accepted public screenshot set was identified
- Current-side execution is tracked by `rtessno/support-copilot` issue #1873

The gate includes:

- `docs/PRODUCT-VISUAL-EVIDENCE.md`
- `docs/product-visuals/MANIFEST-TEMPLATE.json`
- `scripts/validate_product_visuals.py`
- unit tests covering approved, draft, digest-mismatch, incomplete-sanitization, and non-public fixture cases
- required source revision, fixture, viewport, claims, sanitization, reviewer, approval, alt-text, caption, and SHA-256 metadata
- enforcement in `.github/workflows/validate-site.yml`

No product screenshot has been published. The next visual step requires running an exact Current revision with synthetic data, capturing at least three product surfaces, completing one approved manifest per image, and integrating only images that pass the gate.

## Pilot intake milestone

Issue #4 has advanced through a controlled website-side foundation without publishing an invented address or collecting visitor information.

Decisions and controls:

- a dedicated business email is the selected initial contact architecture
- the founder GitHub profile is no longer used as the pilot intake path
- public GitHub issues, embedded forms, scheduling tools, and evidence uploads are not the initial channel
- `docs/PILOT-INTAKE.md` defines activation, qualification, access, retention, and future-provider gates
- the pilot page states which high-level information is appropriate for first contact
- the pilot and privacy pages prohibit customer evidence, logs, captures, credentials, internal URLs, proprietary source, regulated information, contracts, and pricing
- the website continues to collect no information directly
- static validation enforces the contact-pending state and sensitive-evidence warning

Remaining issue #4 blocker:

1. Create the dedicated business mailbox.
2. Configure multi-factor authentication and recovery.
3. Select a retention process that can be followed consistently.
4. Test sending and receiving.
5. Approve the address for publication.
6. Replace the pending state with one working `mailto:` action.
7. Re-review privacy copy and test mobile and desktop behavior.

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

## Organized issue queue

### Tessn website

- #2 — P0: Activate and verify GitHub Pages deployment — **blocked only on Settings → Pages → GitHub Actions**
- #3 — P1: Add sanitized Current product screenshots — **capture tracked by support-copilot #1873**
- #4 — P1: Establish pilot contact and privacy-reviewed intake — **foundation complete; mailbox activation pending**
- #5 — P1: Complete naming, domain, and launch metadata

### Current product

- `rtessno/support-copilot` #1873 — capture approved synthetic Current product visuals for the website

### Current release repository

- `rtessno/current-release` #1 — establish Current release governance before public downloads

## Local preview and validation

```bash
git clone https://github.com/rtessno/tessn-website.git
cd tessn-website
python3 -m http.server 8000 --directory site
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/validate_site.py
python3 scripts/validate_product_visuals.py
```

Open `http://localhost:8000`.

## Immediate next tasks

1. Perform the manual Pages source change and confirm issue #2 passes.
2. Verify mobile and desktop rendering at the deployed URL, then close issue #2.
3. Execute `support-copilot` issue #1873 and integrate at least three approved Current screenshots through issue #3.
4. Create and secure the dedicated pilot-interest mailbox, then activate issue #4's public action.
5. Continue naming and custom-domain work through issue #5.
6. Keep downloads disabled until the `current-release` governance issue is complete.

## Acceptance criteria for the next pass

- Pages deployment and post-deployment verification are green.
- Every route loads through the deployed project path.
- The deployed URL is documented as verified.
- At least three reviewed and manifested Current screenshots are present.
- One tested dedicated pilot-interest action exists with accurate privacy language.
- No claim exceeds the demonstrable Current release.
- Documentation reflects the new state after every milestone.
