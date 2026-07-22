# Starting the Dedicated Tessn Website ChatGPT Project

## Project setup

Create a new ChatGPT project dedicated to the Tessn website and connect the GitHub repository:

```text
rtessno/tessn-website
```

Keep the Current product-development project separate. This repository should remain focused on presentation, content, pilot conversion, domain configuration, and download integration.

## First message

Use this exact message in the new project:

```text
@GitHub start next tasks. Read README.md, docs/PROJECT-CONTEXT.md, docs/HANDOFF.md, docs/ROADMAP.md, docs/WEBSITE-BACKLOG.md, docs/NEXT-TASKS.md, docs/CONTENT-AND-CLAIMS.md, and docs/DECISIONS.md first. Inspect main and the open issues. Continue from issue #2, Activate and verify GitHub Pages deployment, then proceed through the highest-priority incomplete tasks. Keep documentation and HANDOFF.md current after every completed milestone. Do not publish downloads, claim LLC status, or add unverified product claims.
```

## Expected first-pass behavior

The new project should:

1. Confirm the foundation from PR #1 is present on `main`.
2. Inspect issue #2 and the Pages deployment workflow.
3. Verify or guide the manual Pages source setting.
4. Validate the deployed routes, assets, mobile navigation, and artifact scope.
5. Record the deployed URL and close issue #2 only when acceptance criteria are met.
6. Continue with issues #3, #4, and #5 in priority order.
7. Update the roadmap, backlog, decisions, and handoff as work progresses.

## Existing organized work

- Website issue #2 — Pages deployment verification
- Website issue #3 — sanitized Current product screenshots
- Website issue #4 — pilot contact and privacy-reviewed intake
- Website issue #5 — naming, domain, and launch metadata
- `current-release` issue #1 — release governance before public downloads

## Context boundaries

The website project may reference Current's public positioning, but should not copy private source, secrets, customer data, or internal evidence into this repository.
