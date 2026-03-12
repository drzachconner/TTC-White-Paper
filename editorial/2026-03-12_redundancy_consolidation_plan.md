# Redundancy Consolidation Pass — Editorial Plan

**Date:** 2026-03-12
**File to edit:** `renditions/01_2026-02-03_MASTER_PAPER_COMPLETE.md`
**Purpose:** Eliminate repetition that has accumulated across 6 editorial phases + recent Epstein credit additions. The paper restates its core concepts 3-5x each before reaching the sections where they earn their authority. State things once with precision, then build on them.

## IMPORTANT RULES
- **Do NOT delete content without checking `renditions/08_2025-11-02_vital_aspects.md`** — all 18 vital aspects must remain present
- **Preserve the author's philosophical-clinical voice** — tighten, don't flatten
- **When cutting, ensure the BEST version of each concept survives** — the one with the most precision, the right context, and the strongest phrasing
- **Glossary restatements are acceptable** — glossaries exist for standalone reference
- **Visual model (ASCII diagram) restatements are acceptable** — diagrams need to be self-contained
- **Tables are acceptable** as navigation aids even if they restate prose
- **Commit after each tier** with a descriptive conventional commit message

## TIER 1 — Cut immediately (verbatim duplications, zero information loss)

### 1a. Line ~151 (Part III, Structural Composition closing sentence)
**Problem:** Verbatim copy of line ~75 (Part II, Clinical Problem). Same subsystem list: "breath, gait, vestibular integration and gaze stabilization, sensorimotor coordination, autonomic regulation, and load management."
**Action:** Delete line 151's sentence entirely. The concept already lives at line 75 with better framing.

### 1b. Lines ~224-226 (Section 4.3, Allostatic Load)
**Problem:** The passage from "when incoming stress exceeds the body's adaptive capacity" through "intelligent attempt by the body to stabilize itself and limit overwhelm" is a near-exact copy of lines 77-82 (Part II, The Clinical Problem). Section 4.3 even acknowledges this by referencing "the dual distortions of misinformation and missing information described in Part II."
**Action:** Reduce Section 4.3 to a 2-3 sentence bridge that names the allostatic load concept and forward-references Part VI. Do NOT re-explain the mechanism — Part II already did it. Keep only what's unique to 4.3: the label "allostatic load" applied to the NeuroSpinal System, and the sentence about the system no longer recognizing safety.

### 1c. Line ~634 (Part IX, Evidence Map opening sentence)
**Problem:** Re-introduces Breig, Ward, and Haavik as if the reader hasn't met them. By Part IX, each has been introduced 2-4 times.
**Action:** Cut this sentence. Open Part IX directly with the forward-looking research agenda.

## TIER 2 — Compress heavily (restates without advancing)

### 2a. Line ~39 (First Principles, closing paragraph)
**Problem:** "NeuroSpinal Subluxation is fundamentally a state of altered NeuroSpinal tone... represent the body's compensatory adaptation to this upstream tonal dysregulation" restates the Executive Summary thesis from 4 lines earlier.
**Action:** Cut or reduce to a single transitional sentence. The thesis is already stated at lines 13-15.

### 2b. Lines ~181-182 (Part III, Fountainhead of Tone)
**Problem:** TGF-β1/myofibroblast mechanism stated for the 3rd time, before Part VI (where it earns its authority) has even been reached.
**Action:** Replace the mechanism detail with: "When stress overloads the system, the meninges contract protectively (see Part VI for the full mechanism)." Keep the five-D cascade introduction that follows — that IS new content here.

### 2c. Lines ~184-186 (Part III, three-bullet summary)
**Problem:** Three bullets ("Vertebral misalignments are secondary compensations..." / "The musculoskeletal system organizes itself around a central imbalance" / "Bones move and hold their positions as a result of core dural and fascial tension, not the other way around") restate the thesis after the preceding prose already said it better.
**Action:** The third bullet ("Bones move... not the other way around") is a strong epigram worth keeping. Cut the first two bullets. Fold the third into the preceding prose or keep it as a standalone statement.

### 2d. Line ~188 (Part III, closing sentence)
**Problem:** "This facilitates a learning experience for the nervous system, allowing it to begin resolving subluxation on its own" — same concept appears in the Epilogue (line ~738) with better context.
**Action:** Cut this sentence. The Epilogue is the better home for "learning experience."

### 2e. Line ~290 (Section 5.1, Epstein biography entry)
**Problem:** Near-verbatim of Section 4.4 (line ~244). "First professional articulation within chiropractic of the initiatory neurophysiological step..." appears in both locations with identical phrasing.
**Action:** Reduce the Section 5.1 Epstein entry to 2-3 sentences: name, date, brief credit, and "(see Section 4.4 for full treatment of Epstein's contributions)." Section 4.4 is the authoritative home.

### 2f. Lines ~336-338 (Section 5.3, Talsky's Tonal Lineage)
**Problem:** 4th restatement of Epstein's synthesis contribution — same technique list, same "first integrated tonal clinical framework" claim as Section 4.4.
**Action:** Compress to: "Epstein's synthesis of pre-existing indicators into a unified tonal framework (see Section 4.4), along with frameworks from Breig, Ward, Speransky, and Korr, was the foundation Talsky built on during his five years of study." The Korr reference is the only new content — keep it.

### 2g. Lines ~350-351 (Section 5.4, opening paragraph)
**Problem:** 5th full Epstein credit inventory (SMFU, Class A/B, synthesis, wave dynamics). All previously covered in detail at Section 4.4.
**Action:** Reduce to 2-3 sentences: acknowledge the debt ("Without Epstein's foundational insight, TTC would not be possible"), then pivot quickly to the distinction. Drop the full re-enumeration of SMFU/Class A/B/synthesis/waves — Section 4.4 has it.

### 2h. Line ~370 (Section 5.4, closing sentence)
**Problem:** "Where Epstein opened the door... TTC walks through it with the science of why it contracts, the clinical method of how to engage..." restates Section 4.4's conclusion.
**Action:** Keep the metaphor, cut the content restatement. Change to: "Where Epstein opened the door, TTC walks through it — with the science, the clinical method, and the real-time verification described throughout this paper."

### 2i. Line ~376 (Part VI, opening paragraph)
**Problem:** 4th occurrence of "previous models identified *that*; TTC explains *why/how/what*" framing. By Part VI this has been read 3 times.
**Action:** Compress to one sentence: "Previous tonal models identified the clinical phenomenon; this section presents the underlying biology." Then go straight into the pathophysiology. Part VI should feel like a payoff, not another preview.

### 2j. Line ~220 (Section 4.2, closing sentence)
**Problem:** "Neural interference stems from aberrant NeuroSpinal tension, not primary compression, redirecting the focus of chiropractic from bones to tone" restates the core thesis for the 5th time.
**Action:** Cut or convert to a forward-pointing transition into Section 4.3.

### 2k. Line ~671 (Part X, opening)
**Problem:** Near-verbatim of line 354: "delivering precise corrective information through touch to a system whose inherent drive is to self-correct."
**Action:** Rephrase to avoid the verbatim repetition, or cut the setup and open Part X with its distinctive content (the clinical trajectory and practitioner integration).

### 2l. Line ~382 (Part VI, parenthetical)
**Problem:** "(what Breig termed Adverse Mechanical Tension)" — 6th in-text Breig AMT attribution. Reader knows by now.
**Action:** Cut the parenthetical. The terminology note in Section 4.4 and the glossary entry handle this. Just use "aberrant NeuroSpinal tension" without the Breig attribution here.

## TIER 3 — Consolidate across sections

### 3a. Part I: Sections 1.1 and 1.3
**Problem:** Both make the same argument (philosophy/technique gap). Section 1.3 ("We said tone, but we adjusted bones") says it better than 1.1.
**Action:** Fold 1.3's strongest content into 1.1. Eliminate the redundant section. Result: 1.1 (the gap), 1.2 (the logic), 1.4 (the bridge).

### 3b. Part VII: Sections 7.2 and 7.3
**Problem:** Pressure testing explained 3 times within 10 lines of each other.
**Action:** Consolidate into one clear explanation. State the mechanism once, then move on.

### 3c. Lines ~159 and ~202 (Breig's AMT)
**Problem:** Introduced "as if new" at both locations with nearly identical wording.
**Action:** Part III (line 159) should use a condensed reference: "As Breig (1978) demonstrated, aberrant tension in this system can disturb neural function without vertebral displacement." Part IV Section 4.2 (line 202) is the right home for the full historical introduction — keep it there.

### 3d. Lines ~254 and ~360 (Tonal Line of Drive definition)
**Problem:** Identical definition verbatim, only 100 lines apart (Section 4.4 and Section 5.4).
**Action:** Define fully at line 254 (Section 4.4). At line 360 (Section 5.4), reference it: "the Tonal Line of Drive (described in Section 4.4)" rather than re-defining.

### 3e. Lines ~354 and ~628 ("physical inputs to physical")
**Problem:** Near-verbatim phrase in both Section 5.4 and Part VIII.
**Action:** Vary the language in one location. Part VIII is the natural "cheat sheet" home; Section 5.4 can express the concept differently.

## TIER 4 — Structural questions (discuss with author if uncertain)

### 4a. First Principles → Part I → Part II
The argument "chiropractic professes tone but practices structure; TTC bridges the gap" restarts 3 times before any new material arrives. Consider whether the paper needs all three entry ramps or if one strong statement suffices.

### 4b. Part VIII ("What TTC Is and Is Not")
Re-covers Section 5.4 and Part II in bullet form. Consider whether it earns standalone status or should be absorbed. The technique category definitions (Osseous / Tonal / OsseoTonal / Tonal Energetics) ARE unique and should be preserved wherever they land.

### 4c. Epstein in 4 locations
Sections 4.4, 5.1, 5.3, and 5.4 all cover Epstein's contributions. Section 4.4 is the authoritative home. The other three should acknowledge and cross-reference, not re-argue.

## TIER 5 — Phrase frequency (do last, after structural cuts)

| Phrase | Current | Target | How |
|--------|---------|--------|-----|
| "best window in" | 13 | 6-8 | Cut in passages where it appears 2+ times in quick succession |
| "self-correct/self-correction" | 10+ | 5-6 | Vary with "resume its own corrective process," "begin resolving," etc. |
| "congruent intent" | 10 | 6-8 | TTC term — some repetition is appropriate, but 10 is excessive |
| "why/how/what" triad | 5 | 2-3 | Keep in Section 4.4 close and Part VI opening only |
| TGF-β1/myofibroblast (before Part VI) | 5 | 1-2 | Exec Summary + Part III evidence section only; Part VI is the payoff |
| "re-initiate its own process" | 4 | 2 | First Principles + Epilogue |
| "physical inputs to physical" | 4 | 2 | Section 5.4 + Part VIII |

## VERIFICATION AFTER EACH TIER

After completing each tier:
1. Grep for the specific phrases that were targeted to confirm reduction
2. Cross-reference `renditions/08_2025-11-02_vital_aspects.md` to confirm all 18 vital aspects are still present
3. Read the surrounding context of each cut to ensure flow isn't broken
4. Commit with descriptive message
