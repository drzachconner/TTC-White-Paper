# TTC White Paper — Project Instructions

## Project Overview

Editorial production of *"The Primary Tone-Setter: Model and Clinical Application of Talsky Tonal Chiropractic"* by Dr. Zach Conner. This is a white paper refinement project — we take an 85KB master paper through sequential editorial passes to produce a publishable, credible document for chiropractic professionals.

## Tech Stack

- **Claude Code (Opus 4.6)** — All editorial passes
- **Perplexity Pro** — Citation verification (Phase 1, complete)
- **GPT-5.2** — Adversarial review (Phase 5, manual)
- **Markdown** — Primary format
- **PDF export** — Final deliverable (pandoc or similar)

## Architecture

This is a writing project, not software. The "architecture" is the editorial pipeline:

```
Master Paper (rendition 01) → Citation Fix → Structure Pass → Credibility Pass → Voice Pass → Adversarial → Final
```

All edits happen in-place on the master paper file. Each phase produces a committed version.

## Directory Structure

```
TTC-White-Paper/
├── CLAUDE.md                    # This file
├── CATALOG.md                   # Complete rendition catalog
├── PLAN.md                      # Original production plan (pre-GSD)
├── GEMINI-INTAKE.md             # Pre-built file for Gemini audit
├── AI-WRITING-RESEARCH-REPORT.md # AI tools research
├── .planning/                   # GSD state
│   ├── PROJECT.md               # Project context
│   ├── REQUIREMENTS.md          # 23 requirements, 6 phases
│   ├── ROADMAP.md               # Phase structure
│   ├── STATE.md                 # Current progress
│   └── config.json              # GSD config
├── renditions/                  # All paper versions (8 files)
│   ├── 01_2026-02-03_MASTER_PAPER_COMPLETE.md  ← WORKING FILE
│   ├── 02–07 (older renditions for cross-reference)
│   └── 08_vital_aspects.md      ← Checklist of key principles
├── editorial/                   # Feedback & review process
│   ├── 2025-11-01_detailed_feedback.md
│   ├── 2025-11-01_suggested_refinements.md
│   ├── 2025-11-02_Haavik_Research_Collaboration_Proposal.md
│   └── 2026-02-26_perplexity_citation_audit.md
└── supporting/                  # PDFs & reference materials (15 files)
```

## Development Conventions

- **Working file**: Always edit `renditions/01_2026-02-03_MASTER_PAPER_COMPLETE.md`
- **Never delete content without checking**: Cross-reference vital aspects checklist before removing anything
- **Voice preservation**: The philosophical-clinical blend IS the paper's identity. Refine, don't flatten.
- **Citation format**: APA-style with DOIs where available
- **Commit after every phase**: Each editorial pass = one committed version

## Environment Variables

None — this is a writing project with no API integrations.

## Workflow

1. `git pull --rebase` before any changes
2. Read the master paper + relevant editorial/rendition files
3. Make editorial changes to master paper
4. Commit with descriptive conventional commit message
5. `git push`
6. Use `/gsd:progress` to check status between phases
7. Use `/gsd:resume-work` when starting a new session

## Known Issues

- **Epstein/Senzon citations**: Now resolved to specific publications, but these authors have limited indexed work. The 1996 JVSR article predates DOI assignment.
- **Ward (1980)**: Verified but rare — only available through used book market. Physical copy confirmation by author is ideal.
- **Intent section (PEAR/RNG)**: Treatment undecided — will be resolved in Phase 3 (Credibility).
- **Redundancy**: Multiple concepts appear 3-4 times across sections. Phase 2 will consolidate.

## Security

No secrets, credentials, or sensitive data in this project.

## Subagent Orchestration

| Phase | Recommended Approach |
|-------|---------------------|
| Phase 2 (Structure) | Main agent — needs full paper context |
| Phase 3 (Credibility) | Main agent — needs full paper + citation context |
| Phase 4 (Voice) | Main agent — needs full paper context |
| Phase 5 (Adversarial) | Manual (user pastes GPT output) |
| Phase 6 (Final) | Main agent + pdf-tools skill for PDF export |

No team parallelism needed — phases are strictly sequential and each operates on the full document.

## GSD + Teams Strategy

**GSD phases**: 6 sequential editorial passes
**Teams**: Not needed — each phase modifies the same single document
**Parallelism**: None — each pass builds on the previous one's stability

## MCP Connections

None required for this project.

## Completed Work

- **Phase 1: Citations** — Complete (2026-02-26)
  - All 29 references verified with Perplexity Pro
  - 8 incorrect citations fixed
  - 3 vague citations (Epstein, Senzon, Ward) resolved to specific publications
  - DOIs added to all journal articles
  - All in-text citations updated to match

Current: Phase 2 of 6 — 0% complete
