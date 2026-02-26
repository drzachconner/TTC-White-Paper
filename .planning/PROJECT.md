# TTC White Paper — Editorial Production

## What This Is

A publishable white paper titled *"The Primary Tone-Setter: Model and Clinical Application of Talsky Tonal Chiropractic"* by Dr. Zach Conner. The paper presents a tonal chiropractic model where vertebral subluxation is secondary to primary meningeal tension (Adverse Mechanical Tension), and the NeuroSpinal System is the body's primary tone setter. Target audience is practicing chiropractors, students, and technique-minded clinicians. Not a journal submission — a professional white paper for seminar distribution and digital sharing.

## Core Value

The finished paper must be credible enough that a skeptical but fair chiropractic colleague would take it seriously, while preserving the author's distinctive philosophical-clinical voice that IS the paper's identity.

## Requirements

### Validated

- ✓ All renditions cataloged and organized — `CATALOG.md`
- ✓ All citations verified with DOIs — Phase 1 complete (2026-02-26)
- ✓ Epstein, Senzon, Ward references resolved to specific publications
- ✓ Master paper selected as starting point — `renditions/01_2026-02-03_MASTER_PAPER_COMPLETE.md`

### Active

- [ ] Consolidate redundancy (Executive Summary vs Parts I, II, IV overlap)
- [ ] Recover valuable content lost from earlier renditions
- [ ] Incorporate unresolved Nov 2025 editorial feedback
- [ ] Review all factual/clinical claims for evidence strength
- [ ] Decide intent section (PEAR/RNG) treatment — keep, reframe, or appendix
- [ ] Harmonize register — clinical-scientific primary, philosophical as seasoning
- [ ] Eliminate AI-sounding phrasing
- [ ] Consistent terminology throughout
- [ ] Adversarial review by external LLM (GPT-5.2)
- [ ] Address adversarial feedback
- [ ] Final polish and consistency pass
- [ ] Export to PDF
- [ ] Final markdown committed to repo

### Out of Scope

- Journal submission formatting (structured abstract, word limits, IMRAD) — this is a white paper
- New original research or data collection
- Rewriting from scratch — we refine, not replace
- Graphic design / layout — content only; design happens separately

## Context

The paper has been through 8+ renditions over ~2 years (April 2025 – February 2026). All renditions are cataloged in `CATALOG.md` and available in `renditions/` and `supporting/`. The Nov 2025 editorial review produced detailed feedback (`editorial/2025-11-01_detailed_feedback.md` and `editorial/2025-11-01_suggested_refinements.md`) — some was incorporated into the Feb 2026 master, some was not. A "vital aspects" checklist (`renditions/08_2025-11-02_vital_aspects.md`) lists key TTC principles that must survive all edits.

Key editorial concerns from prior feedback:
- Redundancy between sections (same concepts repeated 3-4 times)
- "Misinformation / missing information" framework appears in multiple places
- Cascade sequence (dyskinesia, dysafferentation, etc.) duplicated across Parts III and IV
- Some passages lost from older renditions that had value
- Voice occasionally drifts toward AI-sounding flatness

The Gemini pre-editorial audit (originally planned as Phase 0) has been folded into the first editorial pass — Claude will do the cross-rendition comparison directly from the repo files.

## Constraints

- **Voice**: Preserve the author's distinctive philosophical-clinical register. Refine, don't flatten.
- **References**: Epstein, Senzon, Talsky references are authoritative for this audience — keep them.
- **Format**: White paper (no word count limits, no structured abstract required)
- **Tooling**: Claude Code (Opus 4.6) for all editorial passes; author handles GPT adversarial review manually
- **Deliverables**: Final polished markdown + PDF export

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| White paper, not journal | No word limits, keeps philosophical voice, fits seminar audience | ✓ Good |
| Keep Epstein/Senzon/Talsky refs | Authoritative for chiropractic audience; now properly cited | ✓ Good |
| Fold Gemini audit into Pass 1 | Claude can do cross-rendition comparison directly from repo | — Pending |
| Intent section (PEAR/RNG) | Decide during credibility pass — lower risk in white paper format | — Pending |
| Add Bosch et al. (2006) to PEAR | Pairs original with independent APA meta-analysis; shows balance | — Pending |

---
*Last updated: 2026-02-26 after GSD initialization*
