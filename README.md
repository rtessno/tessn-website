# Tessn Website

Public-facing website repository for **Tessn**, the umbrella brand behind Current and future software products.

## Status

The website is deployment-ready, but GitHub Pages is not yet activated in repository settings.

Deployment readiness includes:

- dependency-free static route, asset, accessibility-metadata, preview-indexing, 404-path, pilot-safety, and no-download validation
- post-deployment HTTP verification for every public route and required asset
- marker-based deployment reporting on issue #2
- Current product screenshot evidence validation
- controlled pilot-intake architecture without direct website collection

The latest `main` deployment rerun `29889952423` failed at **Configure Pages** before the artifact-upload step. The remaining activation step is manual because it changes a repository setting not exposed through the connected GitHub tool:

1. Open **Settings → Pages**.
2. Under **Build and deployment**, set **Source** to **GitHub Actions**.
3. Rerun `Deploy GitHub Pages`, or push a new commit to `main`.
4. Confirm the automated report on issue #2 passes.

Expected project Pages URL, not yet verified:

```text
https://rtessno.github.io/tessn-website/
```

The preview remains `noindex,nofollow` and must not be treated as launch-ready until deployment succeeds and the remaining launch gates are complete.

## Primary product

**Current** is a support investigation platform for complex technical escalations. It helps teams turn fragmented tickets, logs, files, commands, notes, screenshots, and documentation into structured, reproducible, and auditable investigations.

## Pilot interest

The initial pilot-interest architecture is a dedicated business email address, but no address is published until the mailbox, multi-factor authentication, account recovery, retention practice, privacy language, and sending/receiving tests are complete.

The website does not collect information directly. Initial outreach must not include customer evidence, logs, captures, credentials, internal URLs, proprietary source, regulated information, contracts, or pricing. See `docs/PILOT-INTAKE.md`.

## Local preview

```bash
python3 -m http.server 8000 --directory site
```

Then open `http://localhost:8000`.

## Validation

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/validate_site.py
python3 scripts/validate_product_visuals.py
```

The validators check required routes and assets, internal references, preview indexing controls, primary-navigation labels, pilot-intake safety copy, the prohibition on publishing installer links, and the evidence manifests for any public Current screenshots.

Every image under `site/assets/images/current/` must have an approved same-stem JSON manifest with an exact Current source commit, fixture identity, viewport, sanitization review, supported claims, reviewer, alt text, caption, and matching SHA-256. See `docs/PRODUCT-VISUAL-EVIDENCE.md`.

After a successful Pages deployment, `.github/workflows/verify-pages.yml` checks the deployed routes, assets, `robots.txt`, preview directives, and nested 404 behavior and updates issue #2 with one current report.

## Repository map

- `site/` — deployable public website
- `scripts/validate_site.py` — dependency-free pre-deployment and intake-safety validation
- `scripts/validate_product_visuals.py` — Current screenshot evidence validation
- `scripts/verify_deployed_site.py` — deployed HTTP verification
- `scripts/upsert_issue_comment.py` — marker-based verification reporting
- `.github/workflows/deploy-pages.yml` — GitHub Pages deployment
- `.github/workflows/validate-site.yml` — pull-request and `main` validation gate
- `.github/workflows/verify-pages.yml` — post-deployment verification gate
- `docs/PROJECT-CONTEXT.md` — durable business and product context
- `docs/PRODUCT-VISUAL-EVIDENCE.md` — public product screenshot acceptance gate
- `docs/product-visuals/MANIFEST-TEMPLATE.json` — screenshot evidence manifest template
- `docs/PILOT-INTAKE.md` — pilot-interest activation, qualification, and data boundaries
- `docs/ROADMAP.md` — ordered implementation roadmap
- `docs/HANDOFF.md` — current-state handoff
- `docs/NEW-CHAT-START.md` — exact starting point for the next ChatGPT project

## Important naming note

Tessn is currently an umbrella brand. Do not represent the business as `Tessn Solutions LLC` until the legal entity has actually been formed.

## Downloads

The website intentionally does not expose public installers yet. Release packaging and the separate `rtessno/current-release` repository are covered in `docs/RELEASE-INTEGRATION.md`.

## License

All rights reserved unless an explicit license is added later. Website source and content are not offered under an open-source license by default.
