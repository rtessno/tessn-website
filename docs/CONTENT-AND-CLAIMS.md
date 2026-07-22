# Content and Claims Governance

## Purpose

Protect credibility by ensuring public statements remain aligned with product evidence and business status.

## Approved core language

- Current is a support investigation platform for complex technical escalations.
- Current makes the investigation a first-class work object.
- Current structures evidence, timelines, findings, hypotheses, decisions, and handoffs.
- Current is designed to complement ticketing, observability, collaboration, and documentation systems.
- Current emphasizes deterministic analysis and inspectable evidence before optional AI explanation.
- Current is being prepared for design-partner and pilot evaluation.

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

## Prohibited or discouraged language

- Fully autonomous diagnosis
- Guaranteed root cause
- Replace your support stack
- Single pane of glass
- Revolutionary
- Next-generation
- All-in-one
- AI-powered as the primary headline

## Legal-status rule

Use **Tessn** as a brand. Do not use **Tessn Solutions LLC** or another entity designation until formation is complete and the exact legal name is confirmed.

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
