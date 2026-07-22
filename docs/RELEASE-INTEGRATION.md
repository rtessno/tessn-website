# Current Release Integration

## Repositories

- Private product development: existing Current/support-copilot repository
- Website: `rtessno/tessn-website`
- Distribution staging: `rtessno/current-release`

## Current state

The website must not link to an installer yet. `current-release` was observed as private and empty during the website bootstrap.

A private release repository cannot provide unauthenticated public downloads. When public distribution is approved, the release repository or another download host must be accessible to intended users.

## Release-readiness gate

Do not expose a download button until all applicable items exist:

- versioned installer assets
- supported operating-system and architecture list
- installation and removal instructions
- license or evaluation terms
- release notes
- SHA-256 checksums
- code-signing and notarization plan
- malware scanning
- software bill of materials where applicable
- support and issue-reporting path
- upgrade and rollback expectations
- privacy and telemetry disclosure

## Recommended first public release structure

```text
Current Preview v0.1.0
├── current-macos-arm64.dmg
├── current-windows-x64.exe
├── SHA256SUMS.txt
├── RELEASE-NOTES.md
└── SBOM.spdx.json
```

Asset names should remain stable if the website will use a `releases/latest/download/...` URL.

## Website states

### Current state

Display: **Private preview — downloads available only through an approved pilot process.**

### Controlled preview

Display a request-access action rather than a direct installer.

### Public preview

Link to the latest signed release and show platform, version, checksum, terms, and minimum requirements.

## Separation rule

Never copy private source code, internal roadmaps, customer data, secrets, or proprietary fixtures into the public distribution repository.
