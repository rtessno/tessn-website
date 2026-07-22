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

Primary tracking issue: #2. Latest rerun `29889952423` failed at **Configure Pages** before artifact upload because the Pages publishing source is not activated.

## P1 — Presentation quality

- [x] Define the Current screenshot evidence and publication gate.
- [x] Add a mandatory screenshot sidecar manifest template.
- [x] Add automated validation for source revision, fixture mode, sanitization, review status, claims, and image digest.
- [x] Open `rtessno/support-copilot` issue #1873 for the exact-revision synthetic capture handoff.
- [x] Create draft 1200×630 social-sharing artwork for design review.
- [ ] Freeze an exact Current candidate SHA for capture.
- [ ] Capture and approve at least three synthetic Current screenshots.
- [ ] Integrate approved screenshots with factual alt text and captions.
- [ ] Create an investigation before/after visual.
- [ ] Add a product navigation or screenshot gallery.
- [ ] Convert the social artwork to a reviewed platform-ready raster.
- [ ] Add concise deployment and trust content.
- [ ] Verify typography and spacing on iPhone, tablet, and desktop.
- [ ] Test keyboard-only navigation and screen-reader landmarks.

Primary tracking issue: #3. No accepted public screenshot set was identified at the observed Current revision, so no product images have been published.

## P1 — Commercial readiness

- [x] Select a dedicated business email as the initial pilot-interest channel architecture.
- [x] Define design-partner qualification questions.
- [x] Define initial intake data boundaries and handling baseline.
- [x] Update the pilot and privacy pages before collecting information.
- [x] Remove the temporary GitHub-profile CTA.
- [x] Explicitly prohibit sensitive evidence and credentials in first contact.
- [x] Add a fail-closed preview and launch-state manifest.
- [x] Document naming, domain, metadata, indexing, structured-data, analytics, and rollback gates.
- [x] Add automated launch-state validation and unit tests.
- [ ] Create and secure the dedicated business mailbox.
- [ ] Select and operationalize a retention process.
- [ ] Publish and test the dedicated address.
- [ ] Draft pilot agreement requirements.
- [ ] Define pricing hypothesis without publishing it prematurely.
- [ ] Complete umbrella-brand and product-name screening.
- [ ] Select and acquire the custom domain.
- [ ] Configure DNS, Pages custom domain, and HTTPS.
- [ ] Transition the launch manifest to `launch_candidate` while keeping indexing disabled.
- [ ] Add final canonical, Open Graph, social, sitemap, and accurate structured metadata.
- [ ] Complete launch review and explicitly approve indexing.

Primary tracking issues: #4 and #5. Issue #4 remains open until one tested public contact action exists. Issue #5 remains open until naming, domain, metadata, HTTPS, and launch approval are complete.

## P2 — Release integration

- [ ] Add README and release policy to `current-release`.
- [ ] Define supported platforms.
- [ ] Define signing and notarization.
- [ ] Define checksum and SBOM generation.
- [ ] Define public versus approved-preview access.
- [ ] Add release-status component to website.

Primary tracking issue: `rtessno/current-release` #1.

## P2 — Discoverability

- [x] Add fail-closed validation that prohibits premature canonical URLs, CNAME, sitemap, structured data, analytics, and indexing.
- [ ] Remove preview noindex controls after approval.
- [ ] Add canonical URL using the verified final domain.
- [ ] Add sitemap with the final domain.
- [ ] Add live Open Graph and social metadata with a platform-ready raster.
- [ ] Add structured organization and software metadata after naming and legal review.
- [ ] Add privacy-reviewed analytics only if a concrete decision requires it.
