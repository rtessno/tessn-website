# Tessn Website

Public-facing website repository for **Tessn**, the umbrella brand behind Current and future software products.

## Status

Initial presentation-site foundation. The repository contains a dependency-free static website, GitHub Pages deployment workflow, project documentation, and a continuation handoff for a dedicated ChatGPT project.

## Primary product

**Current** is a support investigation platform for complex technical escalations. It helps teams turn fragmented tickets, logs, files, commands, notes, screenshots, and documentation into structured, reproducible, and auditable investigations.

## Local preview

```bash
python3 -m http.server 8000 --directory site
```

Then open `http://localhost:8000`.

## Repository map

- `site/` — deployable public website
- `.github/workflows/deploy-pages.yml` — GitHub Pages deployment
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
