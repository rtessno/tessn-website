# Tessn Website

Public-facing website repository for **Tessn**, the umbrella brand behind Current and future software products.

## Status

The GitHub Pages preview is live and verified:

```text
https://rtessno.github.io/tessn-website/
```

Automated post-deployment verification passes **15/15 checks**, including every public route, required CSS/JavaScript/SVG asset, preview crawler controls, pilot safety language, Trust boundaries, and nested 404 behavior. Issue #2 is closed as completed.

The preview remains `noindex,nofollow` and is not launch-approved. Naming, domain, pilot contact, screenshots, legal review, and release gates remain open.

Deployment and quality controls include:

- dependency-free route, asset, accessibility-metadata, preview-indexing, 404-path, pilot-safety, trust-boundary, and no-download validation
- static quality checks for document landmarks, skip-link targets, heading order, image alternative text, external asset hosts, and asset budgets
- revision-bound Current product claim validation
- post-deployment HTTP verification for every public route and required asset
- marker-based deployment reporting
- Current product screenshot evidence validation
- controlled pilot-intake architecture without direct website collection
- fail-closed preview and launch metadata validation

## Primary product

**Current** is a private-beta support investigation platform for complex technical escalations. It helps teams turn fragmented tickets, logs, files, commands, notes, screenshots, and documentation into structured, reproducible, and auditable investigations.

The Current page now distinguishes:

- authenticated web workspace
- implemented Current CLI
- Current Desktop development preview
- Docker Compose deployment path
- Kubernetes/Helm deployment path
- maturity, availability, operator responsibility, and no-download limitations

Public capability language is pinned to an exact `rtessno/support-copilot` revision through `docs/product-claims/current.json`. See `docs/CURRENT-SOURCE-REVIEW.md`.

## Trust and deployment boundaries

The Trust page distinguishes:

- demonstrated behavior of the static website
- Current product principles and direction
- deployment- and pilot-specific commitments that require written scope
- security, compliance, availability, outcome, legal-entity, integration, and installer claims that are not made

It explicitly states that it is not a security assessment, compliance statement, service-level agreement, data-processing agreement, pilot agreement, or software warranty. See `site/trust/index.html` and `docs/CONTENT-AND-CLAIMS.md`.

## Pilot interest

The initial pilot-interest architecture is a dedicated business email address, but no address is published until the mailbox, multi-factor authentication, account recovery, retention practice, privacy language, and sending/receiving tests are complete.

The website does not collect information directly. Initial outreach must not include customer evidence, logs, captures, credentials, internal URLs, proprietary source, regulated information, contracts, or pricing. See `docs/PILOT-INTAKE.md`.

## Launch controls

`docs/launch/launch-state.json` records whether the site is a preview, launch candidate, or launched. The current state is `preview`.

While the state is preview, validation rejects:

- custom-domain `CNAME`
- canonical URLs
- sitemap publication
- live Open Graph URL metadata
- structured data
- analytics approval
- search indexing
- legal-entity approval

A draft social-preview SVG is included for design review only. Live social tags require a platform-ready raster and an absolute HTTPS URL on the approved final domain. See `docs/LAUNCH-CONTROLS.md`.

## Local preview

```bash
python3 -m http.server 8000 --directory site
```

Then open `http://localhost:8000`.

## Validation

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/validate_site.py
python3 scripts/validate_quality.py
python3 scripts/validate_product_claims.py
python3 scripts/validate_product_visuals.py
python3 scripts/validate_launch_state.py
```

The validators check required routes and assets, internal references, preview indexing controls, primary-navigation labels, pilot-intake safety copy, trust-page boundaries, the prohibition on publishing installer links, document landmarks, skip-link targets, heading order, image alternative text, unexpected external asset hosts, asset budgets, exact-source Current product claims, evidence manifests for public Current screenshots, and the preview/launch metadata state.

Every image under `site/assets/images/current/` must have an approved same-stem JSON manifest with an exact Current source commit, fixture identity, viewport, sanitization review, supported claims, reviewer, alt text, caption, and matching SHA-256. See `docs/PRODUCT-VISUAL-EVIDENCE.md`.

`.github/workflows/verify-pages.yml` checks the deployed routes, assets, `robots.txt`, preview directives, trust boundaries, pilot safety copy, and nested 404 behavior after each successful deployment.

## Repository map

- `site/` — deployable public website
- `site/trust/` — trust, deployment, and public-claim boundaries
- `scripts/validate_site.py` — dependency-free pre-deployment, intake-safety, and trust validation
- `scripts/validate_quality.py` — static accessibility, asset-budget, and external-request validation
- `scripts/validate_product_claims.py` — exact-source Current capability, maturity, availability, and limitation validation
- `scripts/validate_product_visuals.py` — Current screenshot evidence validation
- `scripts/validate_launch_state.py` — preview and launch metadata validation
- `scripts/verify_deployed_site.py` — deployed HTTP verification
- `scripts/upsert_issue_comment.py` — marker-based verification reporting
- `.github/workflows/deploy-pages.yml` — GitHub Pages deployment
- `.github/workflows/validate-site.yml` — pull-request and `main` validation gate
- `.github/workflows/verify-pages.yml` — post-deployment verification gate
- `docs/PROJECT-CONTEXT.md` — durable business and product context
- `docs/CONTENT-AND-CLAIMS.md` — public language and trust-claim governance
- `docs/CURRENT-SOURCE-REVIEW.md` — exact Current source review and promotion boundaries
- `docs/product-claims/current.json` — machine-readable Current public claim state
- `docs/PRODUCT-VISUAL-EVIDENCE.md` — public product screenshot acceptance gate
- `docs/product-visuals/MANIFEST-TEMPLATE.json` — screenshot evidence manifest template
- `docs/PILOT-INTAKE.md` — pilot-interest activation, qualification, and data boundaries
- `docs/LAUNCH-CONTROLS.md` — naming, domain, metadata, indexing, and rollback gates
- `docs/launch/launch-state.json` — machine-readable preview and launch state
- `docs/ROADMAP.md` — ordered implementation roadmap
- `docs/HANDOFF.md` — current-state handoff
- `docs/NEW-CHAT-START.md` — exact starting point for the next ChatGPT project

## Important naming note

Tessn is currently an umbrella brand. Do not represent the business as `Tessn Solutions LLC` until the legal entity has actually been formed.

## Downloads

The website intentionally does not expose public installers yet. Release packaging and the separate `rtessno/current-release` repository are covered in `docs/RELEASE-INTEGRATION.md`.

## License

All rights reserved unless an explicit license is added later. Website source and content are not offered under an open-source license by default.
