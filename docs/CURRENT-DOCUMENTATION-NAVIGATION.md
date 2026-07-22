# Current Documentation Navigation Decision

## Decision

The Tessn preview remains **link-free** for Current technical documentation and CLI installation/release navigation.

This is a deliberate fail-closed decision, not an assertion that the upstream documentation does not exist.

Tracking: issue #22.

## Sources reviewed

Authoritative repository: `rtessno/support-copilot`.

Reviewed source paths:

- `.github/workflows/docs-site.yml`
- `docs-site/README.md`
- `docs-site/astro.config.mjs`
- `cli-site/README.md`
- `cli-site/src/pages/index.astro`

Review date: July 22, 2026.

## Findings

### Deployment identity is not externally verifiable

The upstream workflow builds the documentation site and CLI site from the checked-out `main` branch and deploys a merged Pages artifact. The deployed artifact does not currently publish an exact Current source commit or release-manifest identity that Tessn can verify before linking.

A branch-triggered deployment is not sufficient evidence of which exact product revision a visitor is reading after later repository changes.

### The documentation surface is broader than a public evaluation link

The documentation navigation includes:

- installation guidance
- image-bundle customer installation
- configuration and environment-variable reference
- operator runbooks and deployment topologies
- authentication, OAuth, device-flow, and secret-rotation material
- a generated REST API reference
- GitHub repository and edit-on-GitHub links

Those surfaces may be appropriate for approved operators or technical evaluators, but they must not be treated as a neutral public product resource while Current remains private beta and the Tessn site prohibits public downloads.

### Docs and CLI are deployed together

The upstream Pages workflow merges the CLI product site into the documentation artifact under `/support-copilot/cli/`. The CLI site includes install and release navigation. A link to the root documentation site therefore creates a connected path to distribution-oriented content that has not passed the separate `current-release` gate.

### Repository visibility and route safety remain configuration-dependent

The docs configuration links to the Current GitHub repository and edit paths. Tessn must not present private or permission-dependent repository navigation as a reliable public resource.

## Public-site outcome

The Tessn Current page will continue to describe product surfaces at a conservative overview level without adding:

- a Current Docs link
- a Current CLI install link
- a release link
- a private GitHub repository link
- raw OpenAPI navigation
- curated technical snapshots that would create a second documentation source of truth

The website should state no more than that technical documentation and CLI surfaces exist in the authoritative Current repository and remain under publication review.

## Reconsideration gate

A later PR may add one documentation action only when all of the following are true:

1. The public HTTPS destination resolves consistently.
2. The deployed artifact exposes an exact source or release commit identity.
3. Home, quickstart, operator, search, and CLI routes are verified under the final base path.
4. Public navigation does not require access to a private repository.
5. Installation and release routes are consistent with the `current-release` state.
6. Sensitive configuration, credentials, internal-only procedures, fixtures, roadmaps, and private commercial material are excluded or deliberately approved.
7. Maturity, availability, support, and release state remain visible.
8. The external host is explicitly allowlisted and covered by deployed verification.
9. Privacy, Trust, Terms, claims governance, roadmap, backlog, and handoff are reviewed together.
10. A rollback path exists if the external documentation becomes stale, unavailable, or unsafe.

## Ownership

- `support-copilot/docs-site` owns authoritative Current technical documentation.
- `support-copilot/cli-site` owns Current CLI learning and command navigation.
- `tessn-website` owns only the decision to link, the public framing around that link, and the external-navigation safety gate.

Tessn must not fork or manually maintain detailed Current operator documentation.