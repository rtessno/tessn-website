# Ordered Next Tasks

## Completed — Foundation

- PR #1 merged to `main`.
- Static website, deployment workflow, governance documents, roadmap, backlog, and handoff are present.
- Follow-on work is organized as GitHub issues.

## Task 1 — Activate and verify Pages

Tracking: issue #2 and PR #7

Completed on PR #7:

- Verified the repository is public and contains only public presentation source and governance documentation.
- Confirmed the deploy workflow uploads only `site/`.
- Added automated validation for required routes, internal references, assets, preview indexing controls, navigation labels, and prohibited installer links.
- Fixed nested 404 behavior for the `/tessn-website/` project Pages path.
- Added missing navigation accessibility metadata to Privacy and Terms.
- Passed the pull-request validation workflow.

Remaining:

- Settings → Pages → Source: GitHub Actions.
- Merge PR #7 and observe the `main` validation and deployment workflows.
- Verify `https://rtessno.github.io/tessn-website/` over HTTP.
- Test `/`, `/current/`, `/pilot/`, `/about/`, `/privacy/`, `/terms/`, assets, mobile navigation, and nested 404 behavior.
- Update README and HANDOFF with the verified deployment result.
- Close issue #2 only after the deployed checks pass.

## Task 2 — Add real product evidence

Tracking: issue #3

- Produce a synthetic Current demonstration case.
- Capture at least three polished screenshots.
- Sanitize and review.
- Add alt text and captions.
- Confirm visuals support rather than overstate claims.

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
