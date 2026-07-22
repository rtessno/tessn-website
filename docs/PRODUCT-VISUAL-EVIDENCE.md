# Current Product Visual Evidence Gate

## Purpose

Issue #3 requires real product visuals, but the public website must not publish screenshots merely because an image exists. Every public Current screenshot must be traceable to an exact implemented revision, use synthetic or deliberately reviewed sanitized data, and pass an explicit publication review.

This document governs images placed under:

```text
site/assets/images/current/
```

## Current evidence status

As of July 21, 2026:

- Current source repository: `rtessno/support-copilot`
- observed `main` revision: `4643c749f021c3ebf67075964f8fd5804e62c7e1`
- active synthetic-data policy: `docs/commercialization/synthetic-demo-data-policy.md`
- synthetic corpus root: `docs/commercialization/synthetic-demo/`
- visual capture protocol: `docs/f10/product-visual/F10_PV_1B_EVIDENCE_CAPTURE_PROTOCOL.md`
- accepted public screenshot set: **none identified**

The observed source revision is a reference point, not an approved screenshot candidate. A capture must record the exact revision actually rendered.

## Publication rule

A screenshot may be committed to the public website only when all conditions below are satisfied:

1. The image was captured from an exact Current commit SHA.
2. The demonstrated workflow is implemented at that SHA.
3. The data is synthetic by default, or sanitized through a deliberate review.
4. The screenshot contains no customer, employee, credential, internal URL, proprietary log, contract, or pricing information.
5. The image has descriptive alternative text and a concise factual caption.
6. Every website claim supported by the image is listed in its manifest.
7. A reviewer explicitly sets the manifest status to `approved_public`.
8. The image bytes match the manifest SHA-256 digest.
9. `python3 scripts/validate_product_visuals.py` passes.
10. The website layout and copy are reviewed after integration.

No screenshot may be inferred to be approved from a roadmap, test fixture, conceptual mockup, or unexecuted capture plan.

## Required capture set

Issue #3 remains satisfied only after at least three reviewed images are integrated. The preferred first set is:

1. **Case overview** — customer-safe synthetic case context, ownership, impact, and investigation status.
2. **Evidence workspace** — synthetic logs or files with inspectable analysis and source references.
3. **Findings or timeline** — deterministic findings, explicit evidence linkage, or a traceable event sequence.

Later candidates may include an engineering handoff and Publisher/Gateway knowledge outcome when those exact surfaces can be demonstrated and reviewed.

## File convention

Use a stable descriptive stem:

```text
current__<surface>__<viewport>__<source-sha-12>.png
current__<surface>__<viewport>__<source-sha-12>.json
```

Example:

```text
current__case-overview__1440x1000__abc123def456.png
current__case-overview__1440x1000__abc123def456.json
```

The sidecar JSON is mandatory and must use the fields shown in `docs/product-visuals/MANIFEST-TEMPLATE.json`.

## Review workflow

1. Freeze the Current candidate SHA.
2. Select or create a synthetic fixture.
3. Capture the required surface at a defined viewport.
4. Review the raw image for prohibited information.
5. Crop only to improve presentation; do not alter product state or conceal defects.
6. Create the sidecar manifest and calculate the final image SHA-256.
7. Confirm the image supports only implemented, approved public language.
8. Set `status` to `approved_public` only after review.
9. Add the image and manifest in one pull request.
10. Run static-site and product-visual validation.
11. Integrate with factual alt text and captions.
12. Update issue #3, `docs/HANDOFF.md`, the roadmap, and backlog.

## Rejection conditions

Reject or block a candidate when:

- the source revision is unknown or abbreviated only
- the state cannot be reproduced
- the visual is a design mock presented as implemented product
- the data origin is unclear
- sanitization review is incomplete
- a capability or outcome is not demonstrable at the recorded SHA
- the image is visually broken, misleading, illegible, or dependent on unexplained context
- the manifest hash does not match
- the reviewer or review date is missing

## Relationship to claims governance

A screenshot is evidence for a bounded visual state, not proof of business outcomes, performance improvements, security certifications, production scale, general availability, or customer adoption. `docs/CONTENT-AND-CLAIMS.md` remains authoritative for public wording.
