# Structural Reorder Specification — Rendition 09 → 10

**Source file:** `renditions/09_2026-03-16_STRUCTURAL_VISUAL_REDESIGN.md`
**Target file:** `renditions/10_2026-03-16_STRUCTURAL_REORDER.md` (new file to be created by executor)
**Spec author:** structural-reorder-agent
**Date:** 2026-03-16

---

## Purpose

This document specifies the exact reordering of sections from rendition 09, the rationale for each move, and the transition text to be inserted or modified at each relocated boundary. No content is deleted. All 18 vital aspects are preserved. The executor must produce rendition 10 by copying and pasting sections in the order specified below, then inserting or adjusting the transition text flagged in each step.

---

## Overview: Structural Logic of the New Order

The current structure tells the story in historical/explanatory order (foundation → anatomy → pathophysiology → protocol → history → evidence). The new structure tells it in **audience-psychology order**:

1. Hook the reader with the clinical problem (the philosophy–practice gap)
2. Ground them in shared principle
3. Show the anatomy of the solution
4. Prove it with evidence
5. Explain the mechanism
6. Demonstrate the clinical method
7. Validate with historical lineage
8. Cover expectations/ethics
9. Provide reference material (glossary, epilogue, refs, appendices)

History has been moved *after* the clinical protocol because for a seminar-practitioner audience, history functions as validation ("others have been building toward this") — not as foundation. The reader should understand and believe TTC before they learn where it came from. Evidence moves immediately after anatomy so that the anatomical claims are supported before the mechanism is introduced.

---

## New Section Order and Part Renumbering

| New # | New Heading | Old Section | Old Lines |
|---|---|---|---|
| — | Title block + Palmer epigraph | Title/Subtitle/epigraph | 1–9 |
| — | Executive Summary | Executive Summary | 11–21 |
| — | First Principles | First Principles | 23–35 |
| Part I | From Principle to Clinical Method | Part I | 37–80 |
| Part II | The NeuroSpinal System (C-SMFU) | Part II | 82–141 |
| Part III | Evidence Map and Research Invitations | Part VII | 554–587 |
| Part IV | Pathophysiology of NeuroSpinal Subluxation | Part III | 143–304 |
| Part V | TTC Analysis and Adjustment Protocol | Part IV | 306–364 |
| Part VI | From Bone-on-Nerve to Tone-First: Historical Evolution | Part V | 366–432 |
| Part VII | Historical Lineage and Positioning | Part VI | 434–552 |
| Part VIII | Clinical Expectations and Ethics | Part VIII | 589–611 |
| Part IX | TTC Glossary | Part IX | 613–650 |
| Part X | Epilogue: The Self-Tuning Guitar | Part X | 652–660 |
| — | References | References | 662–734 |
| — | Appendix A | Appendix A + subsections | 736–1011 |
| — | Appendix B | Appendix B | 1013–1025 |

---

## Detailed Section-by-Section Instructions

---

### BLOCK 1: Title Block + Epigraph
**Source lines:** 1–9
**Action:** Copy verbatim. No changes.

```
# The NeuroSpinal System as the Primary Tone-Setter
## Model and Clinical Application of Talsky Tonal Chiropractic

---

> *"Life is an expression of tone; the cause of disease is any variation in tone."*
> — D.D. Palmer, *The Chiropractor's Adjuster*, 1910

---
```

**Transition into Executive Summary:** None needed (existing `---` divider serves as separator).

---

### BLOCK 2: Executive Summary
**Source lines:** 11–21
**Action:** Copy verbatim. No changes.

**Note for separate Executive Summary rewrite agent:** This section is flagged for a standalone rewrite pass (< 300 words, self-contained). That rewrite happens after the structural reorder is complete. Rendition 10 carries the current Executive Summary text unchanged.

**Transition out:** Existing `---` divider (line 21). Retain.

---

### BLOCK 3: First Principles
**Source lines:** 23–35
**Action:** Copy verbatim. No changes.

**Internal cross-reference updates required:** Line 33 contains two references:

1. `"...see Section 5.4 for the full account of these contributions..."` — After reordering, Section 5.4 becomes **Part VI, Section 6.4**:
   - **Old:** `(see Section 5.4 for the full account of these contributions)`
   - **New:** `(see Part VI, Section 6.4 for the full account of these contributions)`

2. `"...detailed throughout Parts V and VI."` — After reordering, old Parts V and VI become new Parts VI and VII:
   - **Old:** `detailed throughout Parts V and VI`
   - **New:** `detailed throughout Parts VI and VII`

**Transition out:** Existing `---` divider (line 35). Retain.

---

### BLOCK 4: Part I — From Principle to Clinical Method
**Source lines:** 37–80
**Action:** Copy verbatim. Update heading to reflect it is still Part I (unchanged numbering).

**Heading stays:** `## Part I. From Principle to Clinical Method`

**Internal cross-reference update required:** Line 50 contains:
> "The full pathophysiology of this mechanism, including why it persists and how it is resolved, is described in Part III."

After reordering, the pathophysiology is now **Part IV**. Update:
- **Old text:** `(The full pathophysiology of this mechanism, including why it persists and how it is resolved, is described in Part III.)`
- **New text:** `(The full pathophysiology of this mechanism, including why it persists and how it is resolved, is described in Part IV.)`

**Transition out:** Existing `---` divider (line 80). Retain.

---

### BLOCK 5: Part II — The NeuroSpinal System (C-SMFU)
**Source lines:** 82–141
**Action:** Copy verbatim. Heading remains Part II (unchanged numbering).

**Heading stays:** `## Part II. The NeuroSpinal System (Cranio-Spinal Meningeal Functional Unit)`

**Internal cross-reference update required:** Line 115 contains:
> "(see Section 5.2 for the full historical account)"

After reordering, Section 5.2 (The Shift from Compression to Tension-Based Interference) will now be at **Part VI, Section 6.2**. Update:
- **Old text:** `(see Section 5.2 for the full historical account)`
- **New text:** `(see Part VI, Section 6.2 for the full historical account)`

**Internal cross-reference update required:** Line 137 contains:
> "(see Part III for the full mechanism)"

After reordering, Part III becomes Part IV. Update:
- **Old text:** `(see Part III for the full mechanism)`
- **New text:** `(see Part IV for the full mechanism)`

**Transition out of Part II:** Replace existing `---` divider with the following transition paragraph + divider, which bridges the anatomy section to the evidence map that now follows immediately:

---

> **TRANSITION TEXT — insert between Part II and Part III (Evidence Map):**
>
> The anatomy described above is not speculative. A growing body of peer-reviewed research supports the meningeal system's contractile capacity, the myodural bridge's clinical significance, and the neurophysiological effects of tonal chiropractic inputs. The following evidence map surveys this foundation and identifies the research questions TTC is positioned to answer.

Then insert the `---` divider.

---

### BLOCK 6: Part III — Evidence Map and Research Invitations
**Source lines:** 554–587
**Action:** Copy content verbatim. **Renumber heading** from Part VII to Part III.

- **Old heading:** `## Part VII. Evidence Map And Research Invitations`
- **New heading:** `## Part III. Evidence Map and Research Invitations`

**No internal cross-references to update within this section** (it references Haavik, Lelic, and general literature — no section numbers).

**Transition out of Part III:** Replace existing `---` divider with the following transition paragraph + divider, which bridges the evidence map to the pathophysiology section:

---

> **TRANSITION TEXT — insert between Part III (Evidence Map) and Part IV (Pathophysiology):**
>
> The anatomical and neurophysiological evidence establishes that the meningeal system is active, contractile, and clinically significant. The mechanism by which it initiates subluxation — and why that pattern persists — is the subject of Part IV. To the authors' knowledge, this is the first mechanobiological account within chiropractic of why meningeal contraction begins, how it is sustained at the cellular level, and what conditions allow it to release.

Then insert the `---` divider.

---

### BLOCK 7: Part IV — Pathophysiology of NeuroSpinal Subluxation
**Source lines:** 143–304
**Action:** Copy content verbatim. **Renumber heading** from Part III to Part IV.

- **Old heading:** `## Part III. Pathophysiology of NeuroSpinal Subluxation`
- **New heading:** `## Part IV. Pathophysiology of NeuroSpinal Subluxation`

**No internal cross-references to update within this section** (the section is self-contained and uses only relative language like "Part III" for internal sub-sections, which become subheadings under Part IV).

**Transition out of Part IV:** Replace existing `---` divider with the following transition paragraph + divider:

---

> **TRANSITION TEXT — insert between Part IV (Pathophysiology) and Part V (Protocol):**
>
> The mechanism is now in view: threat perception initiates meningeal contraction, myofibroblast conversion deepens and sustains it, and the NeuroSpinal System holds its defensive posture until it receives precisely the informational input that signals safety. Part V describes exactly how TTC delivers that input.

Then insert the `---` divider.

---

### BLOCK 8: Part V — TTC Analysis and Adjustment Protocol
**Source lines:** 306–364
**Action:** Copy content verbatim. **Renumber heading** from Part IV to Part V.

- **Old heading:** `## Part IV. TTC Analysis and Adjustment Protocol`
- **New heading:** `## Part V. TTC Analysis and Adjustment Protocol`

**Internal sub-section numbering:** Sub-sections 4.1, 4.2, 4.3 should be renumbered to 5.1, 5.2, 5.3 to match the new Part number.

- `### 4.1 Global Tonal Indicators` → `### 5.1 Global Tonal Indicators`
- `### 4.2 Tonal Analysis and the Best Window In` → `### 5.2 Tonal Analysis and the Best Window In`
- `### 4.3 Contact Parameters (Location, Vector, Amount, Intent)` → `### 5.3 Contact Parameters (Location, Vector, Amount, Intent)`

**Transition out of Part V:** Replace existing `---` divider with the following transition paragraph + divider:

---

> **TRANSITION TEXT — insert between Part V (Protocol) and Part VI (Historical Evolution):**
>
> The model is now complete: mechanism, evidence, and method. TTC did not emerge from a vacuum. It is the next iteration in a long evolution of chiropractic thought — from compression-first to tension-aware to tone-first. Understanding that lineage explains why TTC's contributions are distinct, and why they are necessary.

Then insert the `---` divider.

---

### BLOCK 9: Part VI — From Bone-on-Nerve to Tone-First: Historical Evolution
**Source lines:** 366–432
**Action:** Copy content verbatim. **Renumber heading** from Part V to Part VI.

- **Old heading:** `## Part V. From Bone-on-Nerve to Tone-First: Historical Evolution`
- **New heading:** `## Part VI. From Bone-on-Nerve to Tone-First: Historical Evolution`

**Internal sub-section renumbering:** Sub-sections 5.x become 6.x:
- `### 5.1 The Traditional Subluxation Model...` → `### 6.1 The Traditional Subluxation Model...`
- `### 5.2 The Shift from Compression to Tension-Based Interference` → `### 6.2 The Shift from Compression to Tension-Based Interference`
- `### 5.3 Allostatic Load...` → `### 6.3 Allostatic Load...`
- `### 5.4 Facilitated Subluxation and Meningeal Models (Epstein)` → `### 6.4 Facilitated Subluxation and Meningeal Models (Epstein)`
- `### 5.5 From Segmental to Systems Thinking` → `### 6.5 From Segmental to Systems Thinking`

**Internal cross-references to update within this section:**

- Line 396 (old 5.3): `"...described in Part I — ...is described in Part III."` → Update "Part III" to "Part IV": `"...is described in Part IV."`
- Line 402 (old 5.4): `"(see Section 5.4 for the full historical account)"` — This is a self-reference within the former Part V to Section 5.4. After renumbering, old 5.4 → **new 6.4**. Any internal reference to "Section 5.4" inside this section becomes "Section 6.4."
- Line 416 (old 5.4): `"Part III presents the full mechanobiological model..."` → Update to `"Part IV presents the full mechanobiological model..."`
- Line 422 (old 5.4): `"Part III details the full pathophysiology..."` — Update to `"Part IV details the full pathophysiology..."`
- Line 426 (old 5.4): `"(For acknowledgment of Network Spinal's foundational contributions and TTC's distinct methodological approach, see Section 6.4.)"` → After renumbering, old Section 6.4 is now **Section 7.4**. Update to: `"(For acknowledgment of Network Spinal's foundational contributions and TTC's distinct methodological approach, see Section 7.4.)"`
- Line 378 (old 5.2): The table and surrounding text refer to "Part III" as the destination for the pathophysiology cascade. Each of these → "Part IV."

**Transition out of Part VI:** Replace existing `---` divider with the following:

---

> **TRANSITION TEXT — insert between Part VI (Historical Evolution) and Part VII (Historical Lineage):**
>
> The conceptual evolution from compression to tension to tone establishes *what* changed and *why*. Part VII traces the practitioners who drove that evolution — the specific individuals and techniques whose contributions form TTC's direct lineage.

Then insert the `---` divider.

---

### BLOCK 10: Part VII — Historical Lineage and Positioning
**Source lines:** 434–552
**Action:** Copy content verbatim. **Renumber heading** from Part VI to Part VII.

- **Old heading:** `## Part VI. Historical Lineage and Positioning`
- **New heading:** `## Part VII. Historical Lineage and Positioning`

**Internal sub-section renumbering:** Sub-sections 6.x become 7.x:
- `### 6.1 Tonal Pioneers` → `### 7.1 Tonal Pioneers`
- `### 6.2 The Emergence of OsseoTonal Models` → `### 7.2 The Emergence of OsseoTonal Models`
- `### 6.3 The Evolution from Torque Release Technique to Talsky Tonal Chiropractic` → `### 7.3 The Evolution from Torque Release Technique to Talsky Tonal Chiropractic`
- `### 6.4 TTC and Network Spinal: Shared Foundations, Distinct Approaches` → `### 7.4 TTC and Network Spinal: Shared Foundations, Distinct Approaches`
- `### 6.5 The Technique Landscape` → `### 7.5 The Technique Landscape`

**Internal cross-references to update within this section:**

- Line 460 (old 6.1, Epstein entry): `"(See Section 5.4 for full treatment of Epstein's contributions; Section 6.4 for TTC's relationship to this work.)"` → Update to: `"(See Part VI, Section 6.4 for full treatment of Epstein's contributions; Section 7.4 for TTC's relationship to this work.)"`
- Line 508 (old 6.3): `"...Epstein's synthesis of pre-existing indicators... (see Section 5.4)..."` → Update to `"(see Part VI, Section 6.4)"`
- Line 521 (old 6.4): `"(see Section 5.4 for the full account of these contributions)"` → Update to `"(see Part VI, Section 6.4 for the full account of these contributions)"`
- Line 528 (old 6.4): `"(see Part III for the full model)"` → Update to `"(see Part IV for the full model)"`
- Line 464 (old 6.1, Haavik entry): `"applying these findings to TTC specifically remains a research priority (see Part VII)"` → After reordering, Part VII is now Historical Lineage; the Evidence Map is now Part III. Update to: `"applying these findings to TTC specifically remains a research priority (see Part III)"`

**Transition out of Part VII:** Replace existing `---` divider with the following:

---

> **TRANSITION TEXT — insert between Part VII (Historical Lineage) and Part VIII (Clinical Expectations):**
>
> With the model, the mechanism, the method, and the lineage established, the practitioner faces a practical question: what should patients expect, and what ethical commitments govern TTC practice?

Then insert the `---` divider.

---

### BLOCK 11: Part VIII — Clinical Expectations and Ethics
**Source lines:** 589–611
**Action:** Copy content verbatim. Heading renumbering stays at Part VIII (old Part VIII → new Part VIII; numbering coincidentally unchanged in this position).

**Heading stays:** `## Part VIII. Clinical Expectations and Ethics`

**Transition out of Part VIII:** Existing `---` divider (line 611). Retain.

---

### BLOCK 12: Part IX — TTC Glossary
**Source lines:** 613–650
**Action:** Copy verbatim. Heading numbering stays at Part IX (unchanged).

**Heading stays:** `## Part IX. TTC Glossary`

**Internal cross-reference updates within the Glossary:**

- Line 619 (Aberrant NeuroSpinal Tension entry): `"(see Section 5.4 for full terminology note)"` → Update to `"(see Part VI, Section 6.4 for full terminology note)"`

**Transition out of Part IX:** Existing `---` divider (line 650). Retain.

---

### BLOCK 13: Part X — Epilogue: The Self-Tuning Guitar
**Source lines:** 652–660
**Action:** Copy verbatim. Heading stays Part X (unchanged).

**Heading stays:** `## Part X. Epilogue: The Self-Tuning Guitar`

**Transition out of Part X:** Existing `---` divider (line 660). Retain.

---

### BLOCK 14: References
**Source lines:** 662–734
**Action:** Copy verbatim. No changes.

**Heading stays:** `## References`

**Transition out:** Existing `---` divider (line 734). Retain.

---

### BLOCK 15: Appendix A (full, including all subsections)
**Source lines:** 736–1011
**Action:** Copy verbatim. No changes. Includes:
- Main Appendix A heading and footnote (lines 736–759)
- Sections 1–8 (Primary attachment areas, lines 762–847)
- "Additional Clinically Significant Areas of Indirect Dural Involvement" subheading (line 849)
- Sections 9–22 (lines 853–972)
- "Summary: Clinical Integration" (lines 974–987)
- "Additional References for Appendix A" (lines 989–1011)

**Heading stays:** `## Appendix A: Dural Attachment Sites and Harmonic Resonance in TTC`

**Transition out:** Existing `---` divider (line 1011). Retain.

---

### BLOCK 16: Appendix B
**Source lines:** 1013–1025
**Action:** Copy content. One cross-reference update required.

**Heading stays:** `## Appendix B: Exploratory — Intent and Information`

**Internal cross-reference update required:** Line 1019 contains:
> "The neurophysiological basis for congruent intent described in Part VII..."

After reordering, the Evidence Map (including the intent/information discussion) is now **Part III**. Update:
- **Old:** `described in Part VII`
- **New:** `described in Part III`

---

## Complete Cross-Reference Update Master List

This is the exhaustive list of all in-text section references that must be updated. Execute all of these when constructing rendition 10. References not in this list are either self-contained or use non-numbered language and require no update.

| Location (old line #) | Old reference | New reference | Notes |
|---|---|---|---|
| First Principles, line 33 | `Section 5.4` | `Part VI, Section 6.4` | Two occurrences in same line |
| Part I (line 50) | `Part III` | `Part IV` | Pathophysiology forward-ref |
| Part II (line 115) | `Section 5.2` | `Part VI, Section 6.2` | Historical account of Breig |
| Part II (line 137) | `Part III` | `Part IV` | Full mechanism forward-ref |
| Part VI intro (line 370) | `Part III` | `Part IV` | Cascade reference |
| Part VI, Sec 6.3 / new 6.3 (line 396) | `Part III` | `Part IV` | Allostatic load back-ref |
| Part VI, Sec 6.4 / new 6.4 (line 416) | `Part III` | `Part IV` | Mechanobiological model |
| Part VI, Sec 6.4 / new 6.4 (line 422) | `Part III` | `Part IV` | Pathophysiology back-ref |
| Part VI, Sec 6.4 / new 6.4 (line 426) | `Section 6.4` | `Section 7.4` | Network Spinal forward-ref |
| Part VII, Sec 7.1 / old 6.1 (line 460) | `Section 5.4` and `Section 6.4` | `Part VI, Section 6.4` and `Section 7.4` | Epstein entry |
| Part VII, Sec 7.3 / old 6.3 (line 508) | `Section 5.4` | `Part VI, Section 6.4` | Talsky lineage |
| Part VII, Sec 7.4 / old 6.4 (line 521) | `Section 5.4` | `Part VI, Section 6.4` | Network Spinal acknowledgment |
| Part VII, Sec 7.4 / old 6.4 (line 528) | `Part III` | `Part IV` | Full model reference |
| Glossary (line 619) | `Section 5.4` | `Part VI, Section 6.4` | Aberrant NeuroSpinal Tension entry |
| First Principles (line 33) | `Parts V and VI` | `Parts VI and VII` | TTC's distinct contributions are now in Parts VI and VII |
| Part VII/7.1 — Haavik entry (line 464) | `see Part VII` | `see Part III` | "research priority" forward-ref; Part VII is now Historical Lineage; Evidence Map is now Part III |
| Appendix B (line 1019) | `described in Part VII` | `described in Part III` | Intent/information neurophysiology is in the Evidence Map, now Part III |

---

## Content Consolidation Flags

The following instances of potential overlap between sections were identified. **No content is deleted in rendition 10** — consolidation decisions are flagged here for a later pass.

### Flag 1: Part I and Part IV overlap — "least amount / best window in"
Part I (old lines 62–66) and Part V / old Part IV (old lines 308–363) both describe the TTC protocol principles: least amount of the most effective input, finding the best window in, tonal pressure testing, leg balancing. This is intentional repetition serving different purposes (Part I = conceptual orientation, Part V = clinical detail), but it reads as redundant in the new order where they are only two sections apart. **Recommendation for a later pass:** Trim Part I's protocol detail to conceptual language only; reserve clinical specifics for Part V exclusively.

### Flag 2: Part III (Evidence Map) and Part II both cite Haavik + Dorrier
Part II (old line 115) and the new Part III Evidence Map (old Part VII, line 566) both cite Haavik's research and the 20% prefrontal cortex finding, with overlapping language. In the new order, these sections are adjacent. **Recommendation for a later pass:** In Part II, reduce Haavik to one-sentence mention with forward reference to Part III. Remove the Haavik 20% statistic from Part II entirely — it appears in full in Part III.

### Flag 3: Part VI, Section 6.4 (old 5.4) and Part VII, Section 7.4 (old 6.4) — Epstein and Network Spinal
Section 6.4 (historical Epstein) and Section 7.4 (TTC vs. Network Spinal positioning) are now adjacent. Both describe Epstein's contributions and TTC's debt to that work. The sections serve distinct functions (6.4 = historical account, 7.4 = positioning statement) and should remain separate. However, the opening of Section 7.4 ("Without Epstein's foundational insight...") should check that it does not re-explain what was just said in 6.4. **Recommendation for a later pass:** The first paragraph of Section 7.4 can be condensed to a single transitional sentence since the full treatment is now immediately preceding.

### Flag 4: "From Bone-on-Nerve to Tone-First" framing in Part I vs. Part VI heading
Part I already contains the sentence "We said 'tone,' but we adjusted 'bones.'" (old line 39), which is the same conceptual territory as Part VI's title "From Bone-on-Nerve to Tone-First." With Part VI now coming after protocol, readers will have seen this framing twice. This is acceptable for emphasis; flag only if voice editing reveals it feels repetitive.

---

## Vital Aspects Preservation Verification

The 18 vital aspects (from `renditions/08_2025-11-02_vital_aspects.md`) are distributed across the paper as follows in the new structure. The reorder does not delete any section, so all 18 remain present. The executor should verify after assembly:

| Vital Aspect | Appears In (new location) |
|---|---|
| NeuroSpinal System as Primary Tone-Setter | Part II, Part IV |
| Aberrant NeuroSpinal tension persists after stressor | Part IV |
| Myofibroblast mechanism (TGF-β1) | Part IV |
| Class A and Class B both involve meningeal contracture | Part IV, Part VI/6.4 |
| Tonal Line of Drive (vector of release) | Part V, Part VII/7.4 |
| Mandatory leg balancing / pressure testing verification | Part V |
| Least amount of the most effective input | Part I, Part V |
| Best window in | Part I, Part IV, Part V |
| Congruent intent (physical-only) | Part I, Part V |
| TTC as model first, technique second | Executive Summary, Part VII/7.4 |
| 5 D's cascade | Part IV |
| Epstein's foundational contributions | Part VI/6.4, Part VII/7.1 |
| TTC extends Epstein to ALL subluxation | Part VI/6.4, Part VII/7.4 |
| Breig / Ward / Haavik lineage | Part VI/6.2, Part VII/7.1 |
| C-SMFU extends SMFU to include cranial pole | Part II, Glossary |
| Harmonic Resonance | Appendix A |
| Piezoelectric signal transduction | Part II |
| Safety signal mechanism | Part IV |

---

## Appendix: Transition Text Summary (All New Transitions)

For ease of execution, all new transition text is collected here:

**Transition A — End of Part II → Start of Part III (Evidence Map):**
> The anatomy described above is not speculative. A growing body of peer-reviewed research supports the meningeal system's contractile capacity, the myodural bridge's clinical significance, and the neurophysiological effects of tonal chiropractic inputs. The following evidence map surveys this foundation and identifies the research questions TTC is positioned to answer.

**Transition B — End of Part III (Evidence Map) → Start of Part IV (Pathophysiology):**
> The anatomical and neurophysiological evidence establishes that the meningeal system is active, contractile, and clinically significant. The mechanism by which it initiates subluxation — and why that pattern persists — is the subject of Part IV. To the authors' knowledge, this is the first mechanobiological account within chiropractic of why meningeal contraction begins, how it is sustained at the cellular level, and what conditions allow it to release.

**Transition C — End of Part IV (Pathophysiology) → Start of Part V (Protocol):**
> The mechanism is now in view: threat perception initiates meningeal contraction, myofibroblast conversion deepens and sustains it, and the NeuroSpinal System holds its defensive posture until it receives precisely the informational input that signals safety. Part V describes exactly how TTC delivers that input.

**Transition D — End of Part V (Protocol) → Start of Part VI (Historical Evolution):**
> The model is now complete: mechanism, evidence, and method. TTC did not emerge from a vacuum. It is the next iteration in a long evolution of chiropractic thought — from compression-first to tension-aware to tone-first. Understanding that lineage explains why TTC's contributions are distinct, and why they are necessary.

**Transition E — End of Part VI (Historical Evolution) → Start of Part VII (Historical Lineage):**
> The conceptual evolution from compression to tension to tone establishes *what* changed and *why*. Part VII traces the practitioners who drove that evolution — the specific individuals and techniques whose contributions form TTC's direct lineage.

**Transition F — End of Part VII (Historical Lineage) → Start of Part VIII (Clinical Expectations):**
> With the model, the mechanism, the method, and the lineage established, the practitioner faces a practical question: what should patients expect, and what ethical commitments govern TTC practice?

---

## Execution Checklist for Rendition 10 Builder

- [ ] Copy Title block + epigraph (lines 1–9)
- [ ] Copy Executive Summary (lines 11–21) — note: flagged for future rewrite, not changed here
- [ ] Copy First Principles (lines 23–35); update cross-ref on line 33 (2 occurrences)
- [ ] Copy Part I (lines 37–80); update cross-ref on line 50
- [ ] Copy Part II (lines 82–141); update cross-refs on lines 115 and 137; insert Transition A after section
- [ ] Copy Part VII content (lines 554–587); rename heading to Part III; insert Transition B after section
- [ ] Copy Part III content (lines 143–304); rename heading to Part IV; insert Transition C after section
- [ ] Copy Part IV content (lines 306–364); rename heading to Part V; renumber sub-sections 4.x → 5.x; insert Transition D after section
- [ ] Copy Part V content (lines 366–432); rename heading to Part VI; renumber sub-sections 5.x → 6.x; update all internal cross-refs; insert Transition E after section
- [ ] Copy Part VI content (lines 434–552); rename heading to Part VII; renumber sub-sections 6.x → 7.x; update all internal cross-refs; insert Transition F after section
- [ ] Copy Part VIII (lines 589–611) — no changes
- [ ] Copy Part IX (lines 613–650); update Glossary cross-ref (line 619)
- [ ] Copy Part X (lines 652–660) — no changes
- [ ] Copy References (lines 662–734) — no changes
- [ ] Copy Appendix A (lines 736–1011) — no changes
- [ ] Copy Appendix B (lines 1013–1025); update cross-ref on line 1019 (`Part VII` → `Part III`)
- [ ] Run global search for "Part III" — verify all remaining instances refer to the Evidence Map (new Part III), not the Pathophysiology (now Part IV)
- [ ] Run global search for "Part IV" — verify all remaining instances refer to Pathophysiology (new Part IV)
- [ ] Run global search for "Section 5." — verify all remaining instances have been updated to "Section 6." or "Section 7." as appropriate
- [ ] Run global search for "Section 6.4" — verify all instances now correctly refer to the Network Spinal section (new 7.4) or the historical Epstein section (new 6.4) as intended by context
- [ ] Verify 18 vital aspects all present using the table above
- [ ] Verify Palmer epigraph is at top
- [ ] Verify Appendix A and B are at the end
