# Current Source Review

## Purpose

Record the exact authoritative Current revision used for public website capability language.

## Reviewed source

- Repository: `rtessno/support-copilot`
- Commit: `4643c749f021c3ebf67075964f8fd5804e62c7e1`
- Review date: July 22, 2026
- Website tracker: issue #20
- Cross-repository audit: `rtessno/software-portfolio#9`

Reviewed paths:

1. `README.md`
2. `cli-site/README.md`
3. `cli-site/src/pages/index.astro`
4. `docs-site/README.md`

Machine-readable claim state: `docs/product-claims/current.json`.

Validation: `python3 scripts/validate_product_claims.py`.

## Promoted public capability categories

### Web workspace

The website may state that Current includes an authenticated web investigation console backed by FastAPI, PostgreSQL, workers, and deterministic analyzers. The web surface is described for visual investigation, collaboration, administration, and review.

### Current CLI

The website may state that the CLI can create and manage investigations, add evidence, inspect deterministic findings, support ticket-linked workflows, export records, and provide machine-readable output. It connects to a reachable Current Server.

### Current Desktop

The website must label Current Desktop as a **development preview**. It reuses the frontend and connects to a separately running Current Server. It does not bundle the backend, database, Redis, workers, or analyzers.

### Deployment models

The website may state that Current includes Docker Compose and Kubernetes/Helm packaging paths. These are deployment and operator foundations, not public hosting, certification, production approval, or a service-level commitment.

### CLI trust boundaries

The website may describe scoped tokens, OS keychain storage, TLS verification, proxy/custom-CA controls, and actor-attributed operations only as capabilities of the reviewed CLI surface. Exact deployment behavior remains configuration-specific.

## Excluded from promotion

The review does not authorize:

- installer, bundle, package, release, or source-download links
- general-availability claims
- signed, notarized, scanned, or supported installer claims
- certification, compliance, uptime, service-level, or measured-outcome claims
- automatic diagnosis or guaranteed root-cause claims
- public air-gapped distribution approval
- private engineering URLs or instructions presented as public user documentation
- named integration claims outside the reviewed and demonstrated scope
- screenshots without the separate approved visual-evidence manifest

## Freshness rule

A branch name or latest README is not a durable source reference. When Current capabilities or public wording change:

1. select the exact new Current commit
2. re-read every allowlisted source path
3. update the product-claims manifest
4. update visible website language and limitations together
5. update the review date
6. run all claim, visual, launch, site, and quality validation
7. document the change in HANDOFF and the tracking issue

Do not silently broaden claims because a feature appears in a roadmap, test, pull request, pre-release, or private demonstration.
