# Website Backlog

## P0 — Required next

- [x] Review and merge the foundation pull request.
- [x] Verify `tessn-website` visibility: the repository is public and contains only public presentation source and governance documentation.
- [x] Add automated validation for required routes, internal links, assets, accessibility metadata, preview indexing controls, and prohibited installer links.
- [x] Repair the custom 404 page for nested GitHub project Pages URLs.
- [x] Confirm the deployment workflow publishes only `site/`.
- [x] Add post-deployment HTTP verification and issue #2 reporting.
- [x] Trigger deployment from `main` and identify the exact blocker.
- [ ] Set Settings → Pages → Source to **GitHub Actions**.
- [ ] Rerun `Deploy GitHub Pages` and confirm it succeeds.
- [ ] Confirm the issue #2 HTTP verification report passes.
- [ ] Inspect the deployed site on iPhone, tablet, and desktop.
- [ ] Record the verified deployed URL in README and HANDOFF.
- [ ] Select pilot contact channel.
- [ ] Replace temporary GitHub-profile CTA.

Primary tracking issue: #2. Run `29889297595` failed at **Configure Pages** before artifact upload because the Pages publishing source is not activated.

## P1 — Presentation quality

- [ ] Add sanitized Current screenshots.
- [ ] Create an investigation before/after visual.
- [ ] Add a product navigation or screenshot gallery.
- [ ] Create social-sharing artwork.
- [ ] Add concise deployment and trust content.
- [ ] Verify typography and spacing on iPhone, tablet, and desktop.
- [ ] Test keyboard-only navigation and screen-reader landmarks.

Primary tracking issue: #3.

## P1 — Commercial readiness

- [ ] Finalize brand naming screen.
- [ ] Select and configure custom domain.
- [ ] Define design-partner qualification.
- [ ] Draft pilot agreement requirements.
- [ ] Define pricing hypothesis without publishing it prematurely.
- [ ] Establish a dedicated business contact.
- [ ] Update privacy handling before collecting pilot information.

Primary tracking issues: #4 and #5.

## P2 — Release integration

- [ ] Add README and release policy to `current-release`.
- [ ] Define supported platforms.
- [ ] Define signing and notarization.
- [ ] Define checksum and SBOM generation.
- [ ] Define public versus approved-preview access.
- [ ] Add release-status component to website.

Primary tracking issue: `rtessno/current-release` #1.

## P2 — Discoverability

- [ ] Remove preview noindex controls after approval.
- [ ] Add canonical URL.
- [ ] Add sitemap with final domain.
- [ ] Add Open Graph and social metadata.
- [ ] Add structured organization and software metadata after legal-name review.
- [ ] Add privacy-reviewed analytics only if a concrete decision requires it.
