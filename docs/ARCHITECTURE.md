# Website Architecture

## Decision

The initial Tessn website uses dependency-free static HTML, CSS, JavaScript, and SVG assets.

## Why

- GitHub Pages can serve the site directly.
- No framework or package-version maintenance is required.
- A new ChatGPT project or local contributor can understand the complete system immediately.
- The site has no server-side requirements at this stage.
- Static delivery minimizes supply-chain and runtime complexity.

## Directory model

```text
site/
├── index.html
├── 404.html
├── .nojekyll
├── assets/
│   ├── css/site.css
│   ├── js/site.js
│   └── images/
├── current/index.html
├── pilot/index.html
├── about/index.html
├── privacy/index.html
└── terms/index.html
```

The GitHub Pages workflow uploads only `site/`. Repository documentation is not part of the deployment artifact.

## Local development

```bash
python3 -m http.server 8000 --directory site
```

Do not open pages directly with `file://` when testing relative navigation. Use a local HTTP server.

## GitHub Pages deployment

The workflow:

1. Runs on pushes to `main` or manual dispatch.
2. Checks out the repository.
3. Configures GitHub Pages.
4. Uploads the `site/` directory as the Pages artifact.
5. Deploys to the `github-pages` environment.

Repository Settings → Pages must use **GitHub Actions** as the source.

## Preview indexing

Every page currently uses `noindex,nofollow`, and `robots.txt` disallows crawling. Remove both controls only after content, contact, legal, domain, and launch readiness have been reviewed.

## Future framework trigger

Do not migrate to Astro, React, or another framework merely for preference. Consider a framework when at least one is true:

- repeated shared components create material maintenance risk
- structured content collections are needed
- documentation volume becomes substantial
- localization is approved
- a real build-time data integration is required

## Backend trigger

GitHub Pages must not be used for customer evidence, authentication, payments, or product runtime. Add a separate service only when a specific approved feature requires it.
