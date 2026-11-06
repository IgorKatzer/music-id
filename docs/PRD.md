# PRD: Music Identification by Composition

- Version: 0.2 (draft for Product Owner review)
- Date: 2026-10-11
- Product Owner: Igor Katzer
- Product name: to be decided ("EchoMind" was only a provisional suggestion)
- Translations: [Português (pt-BR)](PRD.pt-BR.md)

This document consolidates the decisions made during the discovery phase. Anything not yet decided is marked as **Open item** and listed in section 13. None of the target numbers here are final: all of them must be validated through experiments.

## 1. Problem

Current music identification tools depend on similarity to known recordings. As a result, users cannot identify a song when it is performed in a different way, such as in live performances, covers, or when it is only hummed.

## 2. Mission

Enable anyone to identify a song regardless of how it is performed, played back or remembered, and connect that discovery to the services where the song can be listened to or purchased.

## 3. Vision

The product is planned in three layers:

| Layer | What it is | Horizon |
|-------|------------|---------|
| MVP | Music identification | First release |
| Product | Music discovery platform: identify songs from any form of input and take the user to the music | Following releases |
| Vision | Music intelligence platform: analyze arrangements, separate instruments, extract chords and generate sheet music or tablature for learning to play | Long term |

The vision layer is outside the scope of this PRD. It is recorded here because it influences architecture decisions from the start (see ADR-0001).

## 4. Product principles

1. **Composition, not recording.** The system answers "which song is this?", not "which recording is this?". The audio may change; the identity of the song remains.
2. **Sufficiency of evidence.** The system only asserts an identification when it has enough evidence. When it does not, it says so instead of guessing.
3. **Hidden musical complexity.** Users do not need to understand music. Musical key, for example, is ignored during matching.
4. **Inputs are musical evidence.** Audio, a hummed melody and a lyrics excerpt are different forms of evidence about the same work.

## 5. Users

The audience is broad: people who enjoy music. Instead of a narrow persona, the product is defined by the usage situations in section 6.

**Open item:** define an initial persona to guide MVP priorities.

## 6. Use cases

| ID | Situation | Input | Main challenges |
|----|-----------|-------|-----------------|
| UC-001 | A church band plays a song the user does not know | Live audio captured by the phone | Reverberation, different voice, different arrangement, audience singing along, improvisation |
| UC-002 | A song playing on the car radio | Audio captured near the speaker | Noise, compression, announcer, radio jingle or slogan in the middle of the song |
| UC-003 | A childhood anime song the user only remembers the melody of | Humming | Off-key singing, imperfect rhythm, partial memory, no lyrics, different key |
| UC-004 | A song that contains a sample of another work | Audio | Not confusing the sample with the main song |
| UC-005 | The user wakes up with a song stuck in their head and knows nothing about it | Humming or whistling | Incomplete memory, unknown genre |
| UC-006 | A cover band plays in a bar | Live audio captured by the phone | Cover, different singer and arrangement, conversations, applause |

Expected result in every case: the identified composition, with the original work's details. In UC-004, the main result is the song that is playing, with the sample reported separately.

## 7. Product contract: what the system commits to attempting to identify

| # | Input | Condition |
|---|-------|-----------|
| 1 | Official recording | From official or licensed sources |
| 2 | Live performance | Even when the interpretation differs from the original recording |
| 3 | Cover | As long as the original melody is preserved. With improvisation, capturing a passage without improvisation is enough |
| 4 | Humming | At least 10 seconds, with enough melodic information and reasonably in rhythm |
| 5 | Sung excerpt | Even if only the chorus |
| 6 | Lyrics | An excerpt spoken, sung or quoted, even if partial |
| 7 | Instrumental | Fully instrumental music |
| 8 | Fingerstyle | Fingerpicked guitar, as long as the musical structure allows a match |
| 9 | Degraded audio | Radio, noise, conversations, applause, jingles, as long as there is enough musical information |
| 10 | Chords (future) | A sequence played clearly, in the song's order and rhythm. Isolated chords do not count |

Musical key is treated as variable: a change of key must not prevent identification.

Any input outside this table is not accepted. In those cases, and whenever the evidence is insufficient, the system reports that it does not have enough information.

## 8. Result shown to the user

When confidence reaches the minimum threshold for the recognition mode, the screen shows:

- song title;
- original artist or group;
- album and year of the original work (for a cover, these are the original work's details, not the cover's);
- confidence percentage;
- identification type: official audio, live performance, cover, radio, humming, voice, instrumental or fingerstyle, lyrics excerpt;
- links to Spotify, Apple Music and YouTube (the latter only when an official video exists).

When no candidate reaches the threshold, the system does not assert an identification. It reports that it could not identify the song with enough confidence and lists the most likely candidates, asking "Is it one of these?".

Ideas for future versions, outside the MVP: a breakdown of why the song was identified (melody, lyrics, rhythm), using the user's answer to improve the system, links to chord charts and sheet music.

## 9. Functional requirements (draft)

Priorities follow the MVP scope decided in section 11.

| ID | Requirement | Priority |
|----|-------------|-------------------|
| FR-001 | Capture audio from the device microphone | MVP |
| FR-002 | Identify an official recording from the captured audio | MVP |
| FR-003 | Show the result with the fields in section 8 | MVP |
| FR-004 | Show a confidence score and only assert the identification above the mode's threshold | MVP |
| FR-005 | Below the threshold, list the most likely candidates without asserting any of them | MVP |
| FR-006 | Tolerate discontinuous excerpts and interruptions, such as radio jingles | MVP |
| FR-007 | Identify live performances and covers by composition | Post-MVP |
| FR-008 | Identify by humming, with a minimum of 10 seconds | Post-MVP |
| FR-009 | Identify by a lyrics excerpt, spoken, sung or typed | Post-MVP |
| FR-010 | Identify instrumental and fingerstyle music | Post-MVP |
| FR-011 | Distinguish sample, interpolation, cover and remix, reporting the sample separately | Post-MVP |
| FR-012 | Identify by chord sequence | Future |

**Open item:** maximum recording length per query.

## 10. Non-functional requirements and metrics

Provisional targets, proposed as a starting point. They will be adjusted after the first experiments.

| Metric | Provisional target | Applies from |
|--------|--------------------|--------------|
| Accuracy on official recordings | ≥ 98% | MVP |
| Accuracy on noisy recordings | ≥ 95% | MVP |
| Correct answer within the top 5 candidates | ≥ 95% | MVP |
| Response time | < 3 s for 95% of queries | MVP |
| Accuracy on live performances and covers | ≥ 90% | Post-MVP |
| Accuracy on humming | ≥ 85% | Post-MVP |

The overall target stated by the Product Owner is a minimum of 90% accuracy.

Notes:

- A model's score is not automatically a probability. The displayed percentage must be calibrated before it is shown as confidence.
- The minimum threshold is defined per recognition mode, not as a single value for everything.
- Every target is only measurable against a defined test set. **Open item:** build that test set.

## 11. MVP scope

**Decided (ADR-0002):** the first MVP identifies only official recordings, through audio fingerprinting, against a reference catalog of public-domain or openly licensed music.

- In the MVP: FR-001 to FR-006.
- Deferred to later releases: live performances, covers, humming, lyrics, instrumental, fingerstyle and samples (FR-007 to FR-012).

The MVP's goal is to validate the end-to-end architecture (capture, API, processing, database and result screen) with a well-known technique, before building the product's differentiator on top of it.

## 12. Out of scope for this PRD

- Music analysis: instrument separation, chords, BPM, key.
- Sheet music and tablature generation.
- User accounts and search history.
- Display of full lyrics.

## 13. Risks and open items

### Risks

| Risk | Impact | Proposed mitigation |
|------|--------|---------------------|
| Reference catalog: commercial recordings and lyrics are protected by copyright | Without a catalog there is nothing to recognize and no way to measure the targets | Start with public-domain and openly licensed music; study licensing before any commercial use |
| Identifying live performances, covers and humming is an open research problem | Section 10 targets may not be achievable | Treat targets as hypotheses and measure early |
| Similarity is not identity (samples, interpolations) | Wrong attributions | Data model that separates composition from recording (ADR-0001) |
| Users' voice audio is personal data | Legal obligations (Brazil's LGPD) | During development, use only the author's own recordings; define a policy before having users |

### Open items

1. Product name.
2. Initial persona.
3. Maximum recording length per query.
4. Test set for measuring the targets.
5. Source of the reference catalog.
6. Platform for the first client: web or mobile app.
7. Architecture decisions, listed in `docs/adr/README.md`.

## 14. History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-10-11 | First consolidation of the discovery phase |
| 0.2 | 2026-10-12 | MVP scope decided: official recordings only, through fingerprinting (ADR-0002) |
