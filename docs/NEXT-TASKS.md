# Ordered Next Tasks

## Completed — Foundation and deployment readiness

- PR #1 merged the static website foundation to `main`.
- PR #7 added static validation, repaired nested 404 behavior, and fixed navigation accessibility metadata.
- PR #8 added post-deployment HTTP verification and marker-based reporting to issue #2.
- PR #9 synchronized documentation with the verified Pages activation blocker.
- The repository is public, contains only presentation source and governance documentation, and keeps downloads disabled.

## Task 1 — Activate and verify Pages

Tracking: issue #2

Completed:

- Confirmed the deploy workflow uploads only `site/`.
- Validated required routes, internal references, assets, preview indexing controls, navigation labels, and prohibited installer links.
- Triggered deployment from `main`.
- Captured run `29889297595` and confirmed failure at **Configure Pages** before artifact upload.
- Added automatic deployed-site verification that updates issue #2 after every Pages deployment while the issue is open.

Manual blocker:

- Settings → Pages → Source: **GitHub Actions**.

After the setting changes:

- Rerun `Deploy GitHub Pages`, or push a commit to `main`.
- Confirm the issue #2 report passes for `https://rtessno.github.io/tessn-website/`.
- Inspect `/`, `/current/`, `/pilot/`, `/about/`, `/privacy/`, `/terms/`, assets, mobile navigation, and nested 404 behavior.
- Update README and HANDOFF with the verified result.
- Close issue #2.

## Task 2 — Add real product evidence

Tracking: issue #3

Completed website-side foundation:

- Verified the Current repository has an active synthetic demonstration data policy and seed corpus.
- Verified no accepted public screenshot set or authoritative visual baseline was identified at the observed Current `main` revision.
- Defined the screenshot acceptance and rejection process in `docs/PRODUCT-VISUAL-EVIDENCE.md`.
- Added a mandatory JSON manifest template.
- Added automated validation for source commit, fixture, viewport, public approval, sanitization, alt text, caption, supported claims, and final image digest.

Remaining capture and integration work:

- Freeze the exact Current candidate SHA that will be rendered.
- Run the synthetic demonstration case.
- Capture at least three polished screenshots from implemented product surfaces.
- Complete and approve one manifest per image.
- Integrate the images with factual alt text and captions.
- Review the visual layout on mobile and desktop.
- Update issue #3 and HANDOFF after integration.

## Task 3 — Establish contact path

Tracking: issue #4

- Choose a dedicated business email or approved form/scheduling provider.
- Document data collection and retention.
- Update privacy notice.
- Replace temporary GitHub-profile CTA.
- Explicitly prohibit sensitive evidence in initial intake.

## Task 4 — Domain and launch controls

Tracking: issue #5

- Complete name screening.
- Select domain.
- Configure DNS and Pages custom domain.
- Remove or revise the project-path `<base>` in `site/404.html` when the custom domain is activated.
- Add canonical and social metadata.
- Add final sitemap.
- Remove noindex only after launch review.

## Task 5 — Release repository readiness

Tracking: `rtessno/current-release` issue #1

- Add release governance and documentation.
- Define supported platforms.
- Define signing, checksums, SBOM, licensing, support, and access model.
- Keep direct downloads disabled until the gate is satisfied.
