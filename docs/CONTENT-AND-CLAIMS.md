# Content and Claims Governance

## Purpose

Protect credibility by ensuring public statements remain aligned with product evidence and business status.

## Approved core language

- Current is a support investigation platform for complex technical escalations.
- Current makes the investigation a first-class work object.
- Current structures evidence, timelines, findings, hypotheses, decisions, and handoffs.
- Current is designed to complement ticketing, observability, collaboration, and documentation systems.
- Current emphasizes deterministic analysis and inspectable evidence before optional AI explanation.
- Current is a self-hostable multi-service product in private beta and design-partner evaluation.
- Current is being prepared for controlled pilot evaluation rather than general availability.

## Revision-bound Current claims

Public Current capability language is governed by `docs/product-claims/current.json` and `python3 scripts/validate_product_claims.py`.

The manifest must record:

- the authoritative repository
- a full exact source commit SHA
- review date and reviewer
- maturity and availability
- public-download state
- reviewed source paths
- implemented and development-preview product surfaces
- deployment models
- trust boundaries
- known limitations
- prohibited claims

For the reviewed revision, the website may describe:

- an authenticated web investigation workspace
- Current CLI investigation, evidence-intake, findings, export, and machine-readable workflows
- Current Desktop only as a development preview that requires a separately running Current Server
- Docker Compose and Kubernetes/Helm packaging as implemented self-hosted paths
- scoped CLI tokens, OS keychain storage, and operator-managed TLS, proxy, and custom-CA controls

A later product change does not automatically update the website. Refresh the exact commit, source paths, manifest, visible copy, limitations, and review date together.

## Approved trust-boundary language

The website may accurately state that:

- the preview is static and does not operate the Current product
- the preview has no application accounts, payment flow, embedded intake form, first-party analytics service, customer-evidence upload, or public installer
- initial pilot interest is separate from evidence transfer
- deployment, storage, external AI use, integrations, access, retention, and support boundaries are configuration-specific and must be documented for an evaluation
- human review remains necessary
- the preview makes no certification, compliance, general-availability, uptime, customer-count, measured-improvement, or guaranteed-diagnosis claim
- Tessn is an umbrella brand and is not presented as a formed LLC
- a documented packaging path is not the same as an approved public release
- a development preview is not a standalone supported product

Negative boundary statements must not be rewritten into implied positive claims. For example, saying that no certification is claimed does not imply that a certification is planned or that the product already meets the certification criteria.

## Language requiring evidence before publication

- Percent or time savings
- Faster resolution claims
- Reduced escalations or support cost
- Security certifications
- Compliance readiness
- Production-scale customer counts
- Named integrations that are not demonstrable
- General availability
- Signed or verified installer availability
- Customer testimonials, logos, or case studies
- Uptime, support-response, recovery-time, or service-level commitments
- Encryption, isolation, retention, backup, or deletion guarantees that are not demonstrated for the exact deployment
- Air-gapped readiness as an approved distribution state
- Standalone desktop packaging or support
- Public documentation availability without deployed URL verification

## Prohibited or discouraged language

- Fully autonomous diagnosis
- Guaranteed root cause
- Replace your support stack
- Single pane of glass
- Revolutionary
- Next-generation
- All-in-one
- AI-powered as the primary headline
- Secure by default without a defined scope
- Enterprise-grade without objective criteria
- Compliant, certified, or audit-ready without current evidence

## Legal-status rule

Use **Tessn** as a brand. Do not use **Tessn Solutions LLC** or another entity designation until formation is complete and the exact legal name is confirmed.

## Trust page rule

`site/trust/index.html` must distinguish four categories:

1. demonstrated behavior of the public website
2. Current product principles or direction
3. pilot-specific commitments that require a written agreement
4. claims that are not made because evidence or review is incomplete

The page must include an explicit statement that it is not a security assessment, compliance statement, service-level agreement, data-processing agreement, pilot agreement, or software warranty.

Do not describe roadmap documents, tests, threat models, internal controls, packaging paths, or operator guides as customer-facing assurance unless the exact release and deployment have been evaluated and the public language has appropriate review.

## Screenshot rule

All public product screenshots must use synthetic data by default or deliberately reviewed sanitized data. Remove:

- customer names
- email addresses
- ticket identifiers
- IP addresses when sensitive
- internal URLs
- credentials and tokens
- proprietary logs
- employee names
- contract or pricing information

Every image under `site/assets/images/current/` must include a same-stem JSON manifest that records the exact Current source commit, fixture mode and identity, viewport, alt text, caption, supported claims, completed sanitization checklist, reviewer, review date, and final image SHA-256.

The manifest status must be `approved_public`, and `python3 scripts/validate_product_visuals.py` must pass. A roadmap, design mock, test fixture, or planned capture is not public product evidence. See `docs/PRODUCT-VISUAL-EVIDENCE.md`.

## Review gate

Every new public claim should answer:

1. Is it implemented?
2. Can it be demonstrated?
3. Is it relevant to the target buyer?
4. Is it phrased without overstating certainty?
5. Does it require legal, security, or privacy review?
6. When supported by a screenshot, is the image tied to an exact revision and approved manifest?
7. Does the statement describe website behavior, product direction, or a deployment-specific commitment clearly enough to avoid category confusion?
8. Is the claim recorded against the exact authoritative product commit?
9. Are maturity, availability, limitations, and release state visible beside the capability?
