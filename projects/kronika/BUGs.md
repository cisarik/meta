# Kronika — Bug and Residual Log

```text
Artifact relationship: project-owned Cooperator note
Authority: none — this file is a memory aid, not task authority, not a
  roadmap, not an ADR, not a specification
Consumer: the COOPERATOR and future Orchestrators of Kronika runs
Discoverability: Meta-local at projects/kronika/BUGs.md
Retention/cleanup: Cooperator-owned; cleanup requires explicit COOPERATOR
  authority
Author: ORCHESTRATOR session of the youtube-download-failure whole, at the
  COOPERATOR's request, 2026-11-14
Visibility: public-safe — no secrets, credentials, private URLs, titles,
  channels, filenames or host identifiers
```

## 2026-11-14 — YouTube download residual: DOWNLOAD_HTTP_403 (not a Kronika defect)

- **Logical whole:** `youtube-download-failure` (Meta
  `01/11-youtube-download-failure/`); accepted candidate
  `aa95034ad32432ff1c137a1a1d761d87d6852b89`, deployed to the NUC the same day.
- **Observed (COOPERATOR live attempt, one only, no retry):** the previously
  failing video passes inspection (metadata readable) and fails at the
  download stage with the sanitized code `DOWNLOAD_HTTP_403`. Metadata and
  publication are not cataloged.
- **Classification:** residual / known limitation, NOT a Kronika code defect.
  The download path is unchanged since the period when the download worked;
  the accepted inspection projection and the new download diagnostics are
  working as designed. The evidence pattern (webpage/inspection OK, media
  request 403) points to a YouTube-side access change — typically
  anti-bot/PO-token or IP-level restriction on the media URL. The exact cause
  (PO token vs. IP) is NOT established and is not claimed.
- **Disposition:** the specific video remains unacquirable inside the
  existing cookie-free acquisition contract. Fixing 403 (PO token, cookies,
  authenticated media) would be a new acquisition mechanism — a new logical
  whole with explicit COOPERATOR decisions, not a repair of this whole.
- **Quota note:** one failed-request slot was consumed. Do not retry without
  a new bounded decision; a retry creates a new claim and consumes another
  slot without new evidence.
- **Product behavior:** the administrator dialog now shows the truthful
  `download / DOWNLOAD_HTTP_403`; the companion still shows `Download failed`
  (correct status surface). No URL, title, channel or filename is recorded.
