# Launch and Metadata Controls

## Purpose

This document prevents a preview website from silently becoming a public launch before naming, domain, legal, content, privacy, product-evidence, and deployment gates are complete.

The machine-readable source of truth is `docs/launch/launch-state.json`.

## Current state

The site is in `preview` status.

Preview means:

- every HTML page remains `noindex,nofollow`
- `robots.txt` disallows crawling
- no custom-domain `CNAME` file is present
- no canonical base URL is asserted
- no sitemap is published
- no structured legal-entity metadata is published
- no analytics or lead-tracking scripts are enabled
- social artwork may exist as a draft asset but is not referenced as a live social card
- Tessn is an umbrella brand, not a claimed LLC
- Current remains a provisional product name

## Launch manifest fields

### `status`

Allowed values:

- `preview` — fail-closed development and review state
- `launch_candidate` — domain and metadata are staged but indexing remains disabled
- `launched` — final launch gates are approved and indexing may be enabled

### Naming fields

`umbrella_name_screened` and `product_name_screened` must be true before `launch_candidate` or `launched`.

These fields record completion of a deliberate name-screening process. They do not represent legal advice, trademark registration, or guaranteed availability.

### Domain fields

`custom_domain` is the hostname only, without scheme or path.

`canonical_base_url` must:

- use `https://`
- match the custom domain
- end with `/`
- be verified as resolving over HTTPS before launch

The project Pages URL must not be promoted as a custom domain.

### Indexing

`indexing_approved` may become true only in `launched` status after:

- Pages deployment succeeds
- all public routes pass deployed verification
- naming and domain decisions are complete
- content and claims review is complete
- pilot contact and privacy handling are accurate
- legal pages receive appropriate review
- public product visuals, if present, pass their evidence manifests

### Legal entity

`legal_entity_approved` must remain false until an exact entity exists and the approved public legal name is known.

Do not infer entity status from a domain, mailbox, assumed company name, or future formation plan.

### Social preview

The draft SVG may be used for design review only. A platform-ready raster image must be generated and reviewed before a public `og:image` or `twitter:image` is added.

The public social image URL must be absolute, HTTPS, and match the approved canonical domain.

### Structured data

Organization or software structured data must not be added until:

- naming fields are approved
- legal-entity representation is accurate
- canonical URLs are final
- product availability and edition fields are demonstrable
- no field implies general availability, certifications, customer counts, integrations, or legal status that has not been verified

### Analytics

Analytics remain disabled by default. Enabling analytics requires a concrete decision, documented provider and data flow, privacy notice update, retention details, and consent analysis where applicable.

## Transition to `launch_candidate`

Before setting `status` to `launch_candidate`:

1. Complete umbrella-brand and product-name screening.
2. Select and acquire the domain.
3. Activate GitHub Pages and verify the project site.
4. Configure DNS and HTTPS.
5. Record the custom domain and canonical base URL.
6. Generate a platform-ready social preview raster.
7. Stage canonical, Open Graph, and social metadata.
8. Keep `indexing_approved` false and retain `noindex` and crawler blocking.
9. Run all repository validators and deployed-route checks.

## Transition to `launched`

Before setting `status` to `launched`:

1. Complete content, claims, privacy, terms, accessibility, and broken-link review.
2. Verify the public contact action.
3. Confirm the custom domain resolves over HTTPS.
4. Confirm canonical and social metadata use the final domain.
5. Confirm structured data is accurate or omit it.
6. Explicitly approve indexing.
7. Replace `robots.txt` and page-level noindex controls in one reviewed change.
8. Record approver and approval date.

## Rollback

If the domain, naming decision, legal representation, privacy handling, or product evidence becomes uncertain:

- return the manifest to `preview`
- restore noindex and crawler blocking
- remove canonical, sitemap, CNAME, structured data, and analytics as appropriate
- document the reason in `docs/HANDOFF.md` and the relevant issue

## Prohibited shortcuts

Do not:

- set canonical URLs to an unverified or unowned domain
- add `CNAME` before DNS and Pages ownership are ready
- remove noindex because the site merely looks complete
- publish an organization legal name before formation and confirmation
- publish a social image URL that does not resolve
- claim trademark clearance from a basic web search
- add structured data for features, editions, reviews, ratings, pricing, or availability that are not established
