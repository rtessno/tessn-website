# Tessn Website

Public-facing website repository for **Tessn**, the umbrella brand behind Current and future software products.

## Status

GitHub Pages preview activation is in progress. The repository contains a dependency-free static website, Pages deployment and validation workflows, project documentation, and a continuation handoff.

Static route, asset, accessibility-metadata, preview-indexing, 404-path, and no-download checks were added and passed on pull request #7. The remaining deployment gate is to confirm **Settings → Pages → Source: GitHub Actions**, observe the `main` deployment, and verify the public preview over HTTP.

Expected project Pages URL:

```text
https://rtessno.github.io/tessn-website/
```

The preview remains `noindex,nofollow` and must not be treated as a launch-ready public site until the deployed URL is verified and the remaining launch gates are complete.

## Primary product

**Current** is a support investigation platform for complex technical escalations. It helps teams turn fragmented tickets, logs, files, commands, notes, screenshots, and documentation into structured, reproducible, and auditable investigations.

## Local preview

```bash
python3 -m http.server 8000 --directory site
```

Then open `http://localhost:8000`.

## Validation

```bash
python3 scripts/validate_site.py
```

The validator checks required routes and assets, internal references, preview indexing controls, primary-navigation labels, and the prohibition on publishing installer links.

## Repository map

- `site/` — deployable public website
- `scripts/validate_site.py` — dependency-free deployment-readiness validation
- `.github/workflows/deploy-pages.yml` — GitHub Pages deployment
- `.github/workflows/validate-site.yml` — pull-request and `main` validation gate
- `docs/PROJECT-CONTEXT.md` — durable business and product context
- `docs/ROADMAP.md` — ordered implementation roadmap
- `docs/HANDOFF.md` — current-state handoff
- `docs/NEW-CHAT-START.md` — exact starting point for the next ChatGPT project

## Important naming note

Tessn is currently an umbrella brand. Do not represent the business as `Tessn Solutions LLC` until the legal entity has actually been formed.

## Downloads

The website intentionally does not expose public installers yet. Release packaging and the separate `rtessno/current-release` repository are covered in `docs/RELEASE-INTEGRATION.md`.

## License

All rights reserved unless an explicit license is added later. Website source and content are not offered under an open-source license by default.
