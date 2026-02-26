# Phase 2: Structure & Redundancy - Context

**Gathered:** 2026-02-26
**Status:** Ready for planning

<domain>
## Phase Boundary

Consolidate overlapping content, recover lost material from earlier renditions, and incorporate unresolved Nov 2025 editorial feedback — so the paper reads as a coherent, non-repetitive argument where each concept has one definitive home. No new content creation; this is structural surgery on existing material.

</domain>

<decisions>
## Implementation Decisions

### Redundancy Strategy
- Claude decides per-instance whether duplicate appearances get a brief callback ("As described in Part II...") or are cut entirely — no blanket rule
- Length is not a goal to reduce — only cut when content is genuinely redundant and doesn't add value in that location
- The cascade sequence (dyskinesia, dysafferentation, etc.) currently lives in both Part III and Part IV — Claude must read both, analyze the flow, and recommend which Part should own the full treatment
- Executive Summary approach: **Researcher to investigate** — what are best practices for Executive Summaries in professional/clinical white papers of this type?

### Content Recovery
- Systematic diff of all renditions (02–07) against the Feb 2026 master to surface anything that was lost
- Present findings for author approval before adding anything back — list what was found with recommendations
- When recovered content conflicts with the master (same idea expressed differently), Claude picks whichever version is better-written regardless of source rendition
- No specific content flagged by author as known-missing — let the diff surface what's there

### Section Architecture
- Part order is correct as-is: I (Philosophical Foundation) → II (NeuroSpinal Model) → III (Subluxation Mechanism) → IV (Clinical Application)
- Executive Summary opening: **Researcher to investigate** — should it lead with clinical mechanism or philosophical foundation, based on white paper best practices?
- Claude should do a full overlap audit across all Parts (not just the cascade sequence) and present findings
- No specific misplaced sections identified by author — Claude identifies during structural analysis

### Editorial Feedback Handling
- Read both Nov 2025 feedback documents (detailed_feedback.md + suggested_refinements.md)
- Identify what remains unaddressed in the current master
- Present recommendations: what to incorporate vs. skip — author approves before changes
- Haavik Research Collaboration Proposal is a separate initiative — do NOT let it influence this paper
- Cross-reference the Perplexity citation audit (2026-02-26) after structural changes to verify citations still make sense in new locations

### Claude's Discretion
- Choosing brief-callback vs. full-cut for each redundancy instance
- Picking the better-written version when content conflicts between renditions
- Identifying misplaced content across Parts
- Implementation details of structural reorganization

</decisions>

<specifics>
## Specific Ideas

- The vital aspects checklist (renditions/08_vital_aspects.md) must be checked against any structural changes — no key TTC principles should be lost
- Two research questions for the phase researcher:
  1. White paper Executive Summary best practices (standalone synopsis vs. preview-only vs. hybrid)
  2. Optimal Executive Summary opening for clinical/professional white papers (mechanism-first vs. philosophy-first)

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope

</deferred>

---

*Phase: 02-structure-redundancy*
*Context gathered: 2026-02-26*
