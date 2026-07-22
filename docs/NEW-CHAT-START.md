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
@GitHub start next tasks. Read README.md, docs/PROJECT-CONTEXT.md, docs/HANDOFF.md, docs/ROADMAP.md, docs/WEBSITE-BACKLOG.md, docs/CONTENT-AND-CLAIMS.md, and docs/DECISIONS.md first. Inspect the current repository and open pull requests. Continue from the highest-priority incomplete tasks, beginning with review/merge readiness and GitHub Pages deployment verification. Keep documentation and HANDOFF.md current after every completed milestone. Do not publish downloads, claim LLC status, or add unverified product claims.
```

## Expected first-pass behavior

The new project should:

1. Inspect the open foundation pull request and changed files.
2. Verify the site structure and deployment workflow.
3. Identify anything blocking merge.
4. Merge only when the foundation is coherent.
5. Verify or guide the manual Pages source setting.
6. Update the roadmap, backlog, decisions, and handoff as work progresses.

## Context boundaries

The website project may reference Current's public positioning, but should not copy private source, secrets, customer data, or internal evidence into this repository.
