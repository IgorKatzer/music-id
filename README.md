# Music ID (working title)

A music identification app that recognizes a song by its **composition** rather than by a specific recording — so it can work on live performances, covers and hummed melodies, not only on official studio audio.

> Status: **early stage**. Product discovery is documented; implementation is starting.
> The product name is provisional.

## Why

Existing tools answer "which recording is this?". They depend on similarity to a known recording and tend to fail when the same song is played live, covered, or simply hummed. This project aims to answer "which song is this?".

## Planned scope

| Stage | Scope |
|-------|-------|
| MVP (in progress) | Identify official recordings only, through audio fingerprinting, on an openly licensed reference catalog; result screen with confidence score and links |
| Next | Live performances and covers; query by humming; lyrics excerpt |
| Long term | Music analysis (chords, instruments) and learning aids (sheet music, tablature) |

Details and open decisions: [`docs/PRD.md`](docs/PRD.md).

## Repository layout

```
apps/web/        Front end (React + TypeScript): audio capture and result screen
backend/         Python + FastAPI modular monolith: API and audio-processing worker
data/catalog/    Reference catalog metadata (public-domain / openly licensed music only)
data/samples/    Test audio recorded by the author
docs/PRD.md      Product requirements (English; pt-BR version in docs/PRD.pt-BR.md)
docs/adr/        Architecture Decision Records (Portuguese)
tests/           Automated tests
```

Stack (ADR-0003): React + TypeScript + Vite on the front end; Python + FastAPI on the back end, as a modular monolith run as two processes (API and worker); PostgreSQL; Docker Compose. Every technical decision is recorded as an ADR in `docs/adr/`.

## Data rules

- The reference catalog contains only public-domain or openly licensed music.
- Test audio is recorded by the author. No third-party personal data is stored or processed.
- No secrets (passwords, API keys) are committed. Use a local `.env` file, which is git-ignored.

## Ownership

Personal project, solely owned by the author. No license is granted: all rights reserved.
