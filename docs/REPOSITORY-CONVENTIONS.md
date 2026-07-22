# Repository Conventions

## Branches

Use focused branch names:

- `feature/<capability>`
- `content/<page-or-message>`
- `fix/<defect>`
- `docs/<topic>`

## Commits

Prefer conventional, scoped messages:

- `feat: add Current product gallery`
- `fix: repair nested Pages links`
- `docs: update pilot handoff`
- `chore: configure custom domain`

## Pull requests

Every pull request should include:

- user-visible outcome
- pages and assets changed
- local preview or validation performed
- screenshots for visual changes when available
- claims or legal text added
- remaining placeholders and follow-up work

## File ownership

- `site/` is public deployable content.
- `docs/` is project operations and handoff context.
- `.github/workflows/` is deployment automation.

## Safety boundaries

Do not commit:

- customer data
- proprietary logs
- private repository content copied wholesale
- API keys or tokens
- legal entity claims not yet true
- unsupported performance claims
- unsigned public installer assets

## Definition of done

A website change is done when:

- it works through a local HTTP server
- nested links and asset paths resolve
- mobile navigation works
- keyboard focus remains visible
- content follows `docs/CONTENT-AND-CLAIMS.md`
- documentation and backlog are updated when the operating state changes
