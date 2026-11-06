# Roadmap

Scope and priorities come from the [PRD](docs/PRD.md) and [ADR-0002](docs/adr/0002-escopo-do-mvp-somente-gravacoes-oficiais.md) (MVP: official recordings only, through fingerprinting, on an open catalog).

## MVP: fingerprint identification

### Foundation

- [x] Product requirements and architecture decisions (PRD, ADRs 0001–0003)
- [x] Docker Compose environment: web, API, worker, PostgreSQL
- [x] Health check and CI
- [ ] ADR: job queue between API and worker
- [ ] ADR: source of the open reference catalog
- [ ] Database schema and migrations: compositions, recordings, fingerprints (ADR-0001)

### Fingerprinting engine

- [ ] Load audio and resample to a fixed rate and mono
- [ ] Spectrogram generation
- [ ] Peak extraction (constellation map)
- [ ] Hash generation from peak pairs
- [ ] Store fingerprints with an index on the hash
- [ ] Matching: hash lookup plus time-offset alignment
- [ ] Confidence score and per-mode threshold

### Catalog

- [ ] Ingestion script: register tracks with metadata, source and license
- [ ] Ingest a first set of openly licensed tracks

### API and worker

- [ ] Upload endpoint: receive audio and enqueue a job
- [ ] Worker: consume jobs, run fingerprinting and matching, store the result
- [ ] Result delivery to the client (WebSocket or polling)

### Web app

- [ ] Microphone capture (MediaRecorder API)
- [ ] Recording screen
- [ ] Result screen: title, artist, album, year, confidence, identification type, links
- [ ] Low-confidence screen: most likely candidates ("Is it one of these?")

### Quality

- [ ] Accuracy test: catalog tracks with added noise, cut into short excerpts
- [ ] Measure accuracy against the PRD target for official recordings
- [ ] Response-time measurement

## After the MVP

- Live performances and covers
- Query by humming
- Identification from lyrics excerpts
- Instrumental and fingerstyle recordings
- Sample detection

Long-term ideas (music analysis, sheet music and tablature) are described in the PRD vision.
