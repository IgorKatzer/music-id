# Music ID (working title)

A music identification app that aims to recognize a song by its **composition** rather than by a specific recording, so it can eventually work on live performances, covers and hummed melodies, not only on official studio audio.

> **Status: early stage.** The current goal is the MVP: identifying official recordings through audio fingerprinting. The product name is provisional.

## Who it is for

People who hear a song and want to know what it is: on the radio, at a show, at a bar with a cover band, or when all they remember is the melody. The MVP covers the first case (official recordings); the others are the direction of the project.

## Why

Existing tools answer "which recording is this?". They depend on similarity to a known recording and tend to fail when the same song is played live, covered, or simply hummed. This project aims to answer "which song is this?".

## Built with

| Layer | Technology |
|-------|------------|
| Front end | React, TypeScript, Vite |
| Back end | Python, FastAPI, as a modular monolith run as two processes (API and worker) |
| Audio | numpy, scipy, librosa; own fingerprinting implementation (landmark-based, in the style of Wang, 2003) |
| Database | PostgreSQL |
| Environment | Docker Compose |
| Tests and CI | pytest, Vitest, GitHub Actions |

The reasoning behind each choice is recorded in [`docs/adr/0003-stack-do-mvp.md`](docs/adr/0003-stack-do-mvp.md).

## How to run

Requirements: Docker with Docker Compose. On Windows, use WSL2.

```bash
git clone https://github.com/<your-user>/<this-repo>.git
cd <this-repo>
docker compose up --build
```

Then open:

- http://localhost:5173: the web app. It shows whether the API and the database are reachable.
- http://localhost:8000/docs: the API documentation (FastAPI / OpenAPI).

To override the local database credentials, copy `.env.example` to `.env` and edit it.

### Running the tests

```bash
# back end
cd backend
pip install -r requirements-dev.txt
python -m pytest

# front end
cd apps/web
npm install
npm test
```

## What works today

- Docker Compose environment with the web app, API, worker and PostgreSQL.
- Health check from the web app to the API and from the API to the database.
- CI running the back-end and front-end tests on every push and pull request.

Audio capture and fingerprinting are next. See the [roadmap](ROADMAP.md).

## Repository layout

```
apps/web/        Front end: audio capture and result screen
backend/         API and worker (modules: api, worker, fingerprint, matching, catalog)
data/catalog/    Reference catalog metadata (public-domain / openly licensed music only)
data/samples/    Test audio recorded by the author
docs/PRD.md      Product requirements (pt-BR version in docs/PRD.pt-BR.md)
docs/adr/        Architecture Decision Records (in Portuguese)
ROADMAP.md       Planned work
```

## Data rules

- The reference catalog contains only public-domain or openly licensed music.
- Test audio is recorded by the author. No third-party personal data is stored or processed.
- No secrets are committed. Local settings go in `.env`, which is git-ignored.

## License

[MIT](LICENSE) © 2026 Igor Katzer
