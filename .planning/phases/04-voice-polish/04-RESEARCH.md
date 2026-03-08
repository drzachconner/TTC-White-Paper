# Phase 4: Voice & Polish - Research

**Researched:** 2026-03-08
**Domain:** Editorial voice harmonization, AI-tell elimination, terminology standardization, prose tightening for a chiropractic white paper
**Confidence:** HIGH

## Summary

Phase 4 is an editorial voice pass over a 1,074-line chiropractic white paper that has been through three prior editorial passes (citations, structure, credibility). The paper is in good structural and evidentiary shape, but the accumulated editing has introduced some patterns that need attention: (1) AI-sounding phrases from the editorial process, (2) terminology variants that should be standardized, (3) repetitive stock phrases used as rhetorical refrains beyond their useful frequency, (4) credibility-pass insertions ("In the TTC model") that sometimes read as bureaucratic rather than natural, and (5) occasional throat-clearing transitions that could be tightened.

The author's authentic voice -- visible in renditions 06 and 07 (the earliest drafts) -- is distinctive: direct, declarative, philosophically bold but clinically grounded. Sentences like "We said 'tone,' but we adjusted 'bones'" and "Subluxation is a tone problem first, a bone problem second" show a clinical-poetic register that is the paper's signature. The voice pass must preserve and amplify this register, not flatten it toward generic academic prose. The goal is a paper that sounds authored -- like a clinician-thinker who has spent decades developing a model -- not like a committee document or an AI-generated summary.

The key challenge is surgical precision: this paper has been refined over 8 renditions and 3 GSD phases. The voice pass must not undo credibility hedging, citation accuracy, or structural improvements from Phases 1-3. Every edit must be voice-only -- changing how things are said, not what is said.

**Primary recommendation:** Execute a three-pass voice audit: (1) AI-tell scan and elimination, (2) terminology standardization with a canonical terms table, (3) prose tightening focused on repetitive refrains and filler transitions. Present all changes as a before/after diff for author review before committing.

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|-----------------|
| VOIC-01 | Register harmonized -- clinical-scientific primary, philosophical as intentional seasoning | Voice Register Analysis (Architecture Patterns section) provides the author's authentic voice fingerprint from renditions 06-07 and specific passages where register is uneven in the current draft |
| VOIC-02 | AI-sounding phrasing eliminated throughout | Comprehensive AI-Tell Inventory (Architecture Patterns section) catalogs every instance found in the current paper with recommended replacements |
| VOIC-03 | Consistent terminology (pick one term where variants exist) | Canonical Terms Table (Architecture Patterns section) maps every variant to a single standardized form with one location for each variant's definition |
| VOIC-04 | Prose tightened -- filler removed, transitions sharpened | Repetitive Refrains Inventory and Filler Transitions list (Common Pitfalls section) identify the specific phrases appearing beyond useful frequency and the throat-clearing patterns to cut |
</phase_requirements>

## Standard Stack

This is an editorial project, not a software project. The "stack" is the set of editorial techniques and reference materials used for the voice pass.

### Core

| Tool/Framework | Purpose | Why Standard |
|----------------|---------|--------------|
| AI-Tell Word List | Comprehensive checklist of words/phrases that signal AI authorship | Community-validated lists from Wikipedia, AI Phrase Finder, and editorial professionals identify specific lexical markers |
| Canonical Terms Table | Single-source-of-truth mapping for every TTC term variant | Standard editorial practice for technical documents with domain-specific vocabulary |
| Before/After Diff Log | Track every change with original and replacement text | Required for author review -- voice is subjective and the author must approve changes |
| Vital Aspects Checklist | Cross-reference after edits to ensure no key TTC concepts were lost | Project convention established in renditions/08_vital_aspects.md |

### Supporting

| Tool | Purpose | When to Use |
|------|---------|-------------|
| Renditions 06 and 07 | Author's authentic voice reference | When deciding whether a passage sounds "authored" vs. "edited" |
| grep/search | Verify AI-tell elimination and terminology standardization | After each edit pass to confirm zero remaining instances |

## Architecture Patterns

### Pattern 1: The Author's Authentic Voice Fingerprint

**What:** Dr. Conner's writing has a distinctive register visible in the earliest drafts (renditions 06-07, written before AI editing). This fingerprint defines the target voice for Phase 4.

**Voice characteristics (from renditions 06-07):**
- **Declarative and direct:** "Subluxation is a tone problem first, a bone problem second." Not hedged to death.
- **Clinical-poetic fusion:** "a symphony led by intelligence via tensioned membranes and pressurized fluids" -- scientific metaphor that earns its abstraction
- **Confrontational thesis framing:** "We said 'tone,' but we adjusted 'bones.' We said 'intelligence,' but we delivered force." -- rhetorical parallelism with bite
- **Second-person clinical address:** "If you practice osseous techniques: Use global tonal indicators to inform your segmental analysis." -- practitioner-to-practitioner
- **Short punchy sentences mixed with longer explanatory ones:** "That's the essence of Talsky Tonal Chiropractic." followed by a detailed explanation
- **Philosophical axioms stated as axioms, not defended:** "Tone is the language of intelligence." -- no throat-clearing
- **Dashes used for parenthetical emphasis:** Heavy use of em-dashes for asides and qualifications, which gives urgency

**What the voice is NOT:**
- Academic passive voice ("It has been demonstrated that...")
- AI-smoothed blandness ("It's important to note that...")
- Committee language ("Furthermore, it should be acknowledged...")
- Generic wellness copy ("This holistic approach empowers...")

### Pattern 2: Comprehensive AI-Tell Inventory

**What:** Every AI-sounding word or phrase found in the current paper (rendition 01), with line numbers and recommended action.

**Confirmed AI-tell words found in the paper:**

| Word/Phrase | Line(s) | Context | Action |
|-------------|---------|---------|--------|
| "crucial" | 223 | "made a crucial contribution" | Replace with "significant" or "key" or restructure sentence |
| "comprehensive" | 315 | "comprehensive tonal analysis system" | Replace with "complete" or "unified" or "integrated" |
| "In essence" | 297 | "In essence, any osseous technique..." | Delete -- just start the sentence with "Any osseous technique..." |
| "fundamentally" | 13, 33, 83 | Three uses -- one in title-level question (keep), two in body (review) | Keep the Executive Summary question ("fundamentally about altered nervous system tone") -- it's intentional rhetorical emphasis. Evaluate the other two for necessity. |
| "paradigm shift" / "paradigm" | 115, 263, 736 | Section header "The Paradigm Shift" and Breig description | The section header use is intentional and fits the paper's thesis. The Breig line ("shifted the paradigm") is borderline -- could be "reframed the model" |
| "robust" | 991, 1012 | Appendix A anatomical descriptions | Technical anatomical usage -- NOT an AI tell in this context. Keep. |
| "landscape" | 612 | Part IX research section | "the broader research landscape" -- mild AI tell. Replace with "the broader body of research" or just "broader research" |

**Phrases to search and eliminate (NOT yet found but must verify at edit time):**

These are the highest-priority AI tells from the community-validated lists. The current paper appears clean on most of them, but a final verification pass should confirm zero instances of:
- "it's important to note" / "it is important to note"
- "delve" / "delving"
- "tapestry"
- "multifaceted"
- "noteworthy"
- "it should be noted"
- "it is worth noting"
- "holistic" (except in the Epstein citation title where it's a direct quote)
- "myriad"
- "plethora"
- "embark"
- "leverage" / "leveraging" (non-financial context)
- "harness"
- "cutting-edge"
- "groundbreaking"
- "transformative"
- "innovative"
- "underscores"
- "bolster"
- "pivotal"
- "captivating"

### Pattern 3: Terminology Standardization -- Canonical Terms Table

**What:** Every TTC-specific term that has variants in the paper, mapped to a single canonical form.

| Concept | Variants Found | Canonical Form | Define Once At |
|---------|---------------|----------------|----------------|
| The primary organizing system | "NeuroSpinal System," "Cranio-Spinal Meningeal Functional Unit," "C-SMFU" | **NeuroSpinal System** (primary), with C-SMFU as parenthetical synonym defined once | Part III heading (line 121), Glossary (line 685) |
| The paper's central metaphor | "Primary Tone-Setter," "primary tone setter," "Primary Tone Setter," "primary tone-setter," "primary tone generator" | **Primary Tone-Setter** (capitalized, hyphenated) | Executive Summary (first use), Glossary |
| Aberrant tension condition | "Adverse Mechanical Tension," "AMT" | **Adverse Mechanical Tension (AMT)** at first use, then **AMT** throughout | Part V first mention (line 199), Glossary |
| The TTC approach | "subluxation" (generic), "NeuroSpinal Subluxation," "vertebral subluxation," "vertebral subluxation complex," "VSC" | Keep all -- these are distinct concepts with intentional usage. "subluxation" = general term, "NeuroSpinal Subluxation" = TTC-specific upstream concept, "VSC" = conventional downstream concept. But ensure each use is deliberate. | Glossary entries (lines 687-688) |
| Self-correction process | "re-initiate its own process of self-correction," "re-initiate its own process of self-correcting," "re-initiate its own process of self-adjustment," "re-initiate its own adjustment process," "re-initiate its own process of detensioning and subluxation reduction," "re-initiate its own process of unwinding and self-correcting" | This is a **repetitive refrain problem**, not a terminology problem. See Pattern 4. | N/A |
| Fascial-meningeal connection | "meningeo-fascial continuum," "Meningeo-Fascial Continuum" | **meningeo-fascial continuum** (lowercase unless starting a sentence) | Part III (line 146), Glossary |
| Key phrases | "least amount of the most effective input," "best window in," "intelligent system that wants to correct," "communicating corrective intent through touch" | These are intentional signature phrases -- keep but manage frequency. See Pattern 4. | Multiple locations (intentional refrains) |

### Pattern 4: Repetitive Refrains -- Frequency Analysis

**What:** Key TTC phrases that appear more often than rhetorical emphasis requires, creating a "broken record" effect rather than a leitmotif.

| Phrase | Count | Recommended Max | Action |
|--------|-------|-----------------|--------|
| "re-initiate its own process of [self-correction/self-adjusting/etc.]" | 9 | 3-4 | Define the canonical form once in the glossary and Part I. Use the full form 2-3 times in high-impact locations (Executive Summary, Part I thesis, Epilogue). In other locations, vary: "facilitate the body's self-correction," "allow the system to resume its own corrective process," "cue the system's own adjustment," etc. |
| "intelligent system that wants to correct" | 5+ | 2-3 | Powerful phrase but loses impact through repetition. Use the full form in the Executive Summary and Epilogue (bookending). Elsewhere: "the system's inherent drive to self-correct," "the body's corrective intelligence," etc. |
| "least amount of the most effective input" | 7 | 3-4 | Signature phrase. Keep in the thesis, the protocol section, and the glossary. Elsewhere, vary: "minimal, precise input," "enough to be perceived, not enough to overwhelm," etc. |
| "communicating corrective intent through touch" | 3 | 2 | Keep in the Executive Summary and the glossary definition of Tonal Adjustment. |
| "intelligence of the body" | 6+ | 3-4 | Some of these are in the glossary (keep). In the body text, keep 2-3 and vary others: "the body's organizing intelligence," "the system's intelligence," etc. |
| "congruent intent" | 17 | 8-10 | This is a core technical term, not just a refrain. Many uses are appropriate (protocol descriptions, glossary, definitions). But 17 is high. Review each use: if "intent" alone or "focused intent" would suffice, simplify. |

### Pattern 5: Phase 3 Insertions That Need Voice Smoothing

**What:** Phase 3 (Credibility) added hedging language, model framing ("In the TTC model"), and evidence-tier calibrations. Some of these read naturally; others feel bureaucratic and break voice flow.

**Examples requiring smoothing:**

1. **"In the TTC model" prefix** (appears ~5 times): Some uses are necessary to prevent overclaiming. But "In the TTC model, subluxation begins upstream of joint fixation" (line 353) reads like a disclaimer rather than a thesis statement. Better: "Subluxation, as TTC understands it, begins upstream of joint fixation" -- or just state it directly since the entire paper IS the TTC model.

2. **"provided evidence" vs. "demonstrated"** (Haavik): The hedge was added for credibility. Keep the hedge but make it read naturally: "Haavik's research has shown that chiropractic adjustments produce measurable changes in brain function" is both accurate and natural-sounding.

3. **Pathological-vs-physiological caveats**: Lines like "a mechanism demonstrated in meningeal tissue under pathological conditions" (line 671, glossary AMT entry) are necessary caveats. They read fine in the glossary. In the body text, ensure they don't create speed bumps.

### Anti-Patterns to Avoid

- **Over-flattening:** Do NOT remove all philosophical language. The paper's value is in the philosophical-clinical synthesis. Remove AI tells and filler, but keep authored philosophical flourishes.
- **Hedging everything:** Phase 3 added appropriate hedging. Do NOT add more hedging in Phase 4. The goal is to make existing hedging sound natural, not to add new hedging.
- **Genericizing signature phrases:** "least amount of the most effective input" is NOT an AI tell -- it's a coined TTC phrase. Do not replace it everywhere; manage its frequency.
- **Academic passive conversion:** Do NOT convert the author's direct "we" voice into passive academic voice. "We assess global NeuroSpinal tone" is better than "Global NeuroSpinal tone is assessed."
- **Losing the confrontational edge:** Lines like "We said 'tone,' but we adjusted 'bones'" are the paper's identity. These are NOT candidates for smoothing.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| AI-tell detection | Manual paragraph-by-paragraph reading | grep/search for the specific word list in Pattern 2 | The word list is finite and searchable; human reading misses distributed patterns |
| Terminology consistency check | Manual scanning for term variants | grep for each variant in the Canonical Terms Table | 1,074 lines with 43+ uses of "subluxation" alone -- manual review will miss variants |
| Repetition frequency counting | Estimation | grep -c for each refrain in Pattern 4 | Exact counts drive decisions about which instances to keep vs. vary |
| Voice register assessment | Algorithmic analysis | Human reading with renditions 06-07 as reference | Voice is subjective; the author's earliest drafts are the best reference |

**Key insight:** The mechanical work (AI-tell detection, term counting, repetition frequency) should be done with search tools. The subjective work (register smoothing, refrain variation, philosophical vs. clinical balance) must be done by close reading.

## Common Pitfalls

### Pitfall 1: Destroying Phase 3 Credibility Work
**What goes wrong:** Voice smoothing removes evidence-tier hedging or "In the TTC model" framing that was deliberately added to prevent overclaiming.
**Why it happens:** The voice editor sees hedging as weakness in the prose and removes it.
**How to avoid:** Before changing any hedging language, check whether it was added in Phase 3. If so, preserve the hedge's meaning while improving its voice. "In the TTC model" can become "TTC proposes that" or be deleted if the surrounding context already makes clear this is TTC's framework -- but the overclaim protection must survive.
**Warning signs:** Sentences that now make direct causal claims without citations or model-framing.

### Pitfall 2: Cutting Too Deep on Refrains
**What goes wrong:** Signature TTC phrases are varied so aggressively that the paper loses its identity and reads like a thesaurus exercise.
**Why it happens:** The editor treats every repetition as a problem rather than distinguishing rhetorical emphasis from lazy repetition.
**How to avoid:** Keep the canonical form in 2-4 high-impact locations (Executive Summary, thesis statement, Epilogue, Glossary). Only vary in lower-impact body text locations.
**Warning signs:** The paper no longer has quotable phrases. A reader couldn't tell you the paper's "catchphrase."

### Pitfall 3: Over-Smoothing the Philosophical Register
**What goes wrong:** Lines like "Tone is the language of intelligence" are softened or qualified into blandness.
**Why it happens:** The editor applies clinical-scientific voice standards uniformly, forgetting that the philosophical register is intentional seasoning, not a bug.
**How to avoid:** The target register is clinical-scientific PRIMARY with philosophical FLOURISHES. Do not eliminate philosophical statements; ensure they are earned by surrounding clinical-scientific context.
**Warning signs:** The paper reads like a journal article instead of a white paper with a philosophical backbone.

### Pitfall 4: Missing Register Inconsistencies in the Appendices
**What goes wrong:** The main body is polished but the Appendix A (dural attachments) and Appendix B (PEAR/RNG) retain different registers.
**Why it happens:** Appendix A is almost entirely technical-anatomical. Appendix B was added in Phase 3 with exploratory framing. Both were likely edited with less voice attention.
**How to avoid:** Apply the same voice standards to appendices, but allow the register to be more technical in Appendix A (it's an anatomical reference) and more cautious in Appendix B (it's explicitly exploratory).
**Warning signs:** A reader moving from the main body to an appendix feels a jarring voice shift.

### Pitfall 5: Losing Content While Tightening Prose
**What goes wrong:** Paragraph tightening removes a sentence that contained a unique TTC concept not stated elsewhere.
**Why it happens:** The editor sees a sentence as "filler" when it actually carries unique meaning in a verbose wrapper.
**How to avoid:** Cross-reference the vital aspects checklist (renditions/08_vital_aspects.md) after prose tightening. Run a diff to identify all deletions and verify none remove unique content.
**Warning signs:** A grep for a key TTC concept returns zero results after editing.

## Code Examples

This is an editorial project. "Code examples" are before/after edit examples.

### Example 1: AI-Tell Replacement
```
BEFORE (line 223):
"made a crucial contribution by being the first to formally articulate"

AFTER:
"made a significant contribution: he was the first to formally articulate"
  -- or --
"contributed a key insight: he was the first to formally articulate"
```

### Example 2: Repetitive Refrain Variation
```
KEEP (Executive Summary, high-impact):
"re-initiate its own process of self-correction"

VARY (body text, line 400):
BEFORE: "re-initiate its own process of self-correcting"
AFTER: "resume its own corrective process"

VARY (body text, line 435):
BEFORE: "re-initiate its own process of detensioning and subluxation reduction"
AFTER: "begin releasing held tension and reducing subluxation on its own"
```

### Example 3: Phase 3 Insertion Smoothing
```
BEFORE (line 353):
"In the TTC model, subluxation begins upstream of joint fixation."

AFTER:
"Subluxation begins upstream of joint fixation."
  -- The entire paper IS the TTC model. The section context (Part V)
  makes this clear. No model-framing prefix needed here.

KEEP (line 146):
"In the TTC model, this meningeo-fascial continuum behaves as a tensegrity lattice"
  -- This IS a model claim that needs framing, because tensegrity is
  not universally accepted for this application. Keep the prefix.
```

### Example 4: Filler Transition Tightening
```
BEFORE (line 509):
"With the pathophysiological mechanisms of NeuroSpinal subluxation established,
we now turn to the clinical methodology for engaging the NeuroSpinal System's
own corrective processes."

AFTER:
(Delete entirely. The section heading "Part VII. TTC Analysis and Adjustment
Protocol" already signals the transition. The paragraph that follows opens
with clinical content. The throat-clearing adds nothing.)
```

### Example 5: Terminology Standardization
```
INCONSISTENT:
Line 160: "the primary tone setter" (lowercase, no hyphen)
Line 176: "primary tone generator" (different word!)
Line 696: "Primary Tone-Setter" (capitalized, hyphenated -- CANONICAL)

STANDARDIZE:
All instances -> "Primary Tone-Setter" (capitalized, hyphenated)
EXCEPT: line 176 uses "primary tone generator" which is a deliberate
  variant introducing a different metaphor. Evaluate whether this adds
  value or creates confusion. Recommendation: change to "Primary
  Tone-Setter" for consistency -- the "generator" metaphor is not
  developed elsewhere and creates unnecessary variant.
```

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| Manual reading for AI tells | Searchable word lists from Wikipedia/community research | 2024-2025 | Finite, verifiable lists replace subjective impressions |
| "Remove all repetition" | Distinguish signature refrains from lazy repetition | Always (editorial best practice) | Preserves document identity while eliminating redundancy |
| Uniform register throughout | Intentional register variation (clinical primary, philosophical secondary) | N/A -- specific to this document | The philosophical-clinical blend is the paper's distinctive value |

## Open Questions

1. **How many "In the TTC model" prefixes should survive?**
   - What we know: Phase 3 added ~5 instances to prevent overclaiming. Some are necessary; some are redundant given context.
   - What's unclear: Exactly which ones can be removed without losing overclaim protection.
   - Recommendation: Evaluate each instance. Keep where the claim could be read as universal truth without the prefix. Remove where the surrounding section (Part V, Part VI) already clearly frames content as TTC's model.

2. **Should "congruent intent" count drop from 17 to what number?**
   - What we know: It's a core technical term that appears in glossary (1), definitions (2-3), protocol descriptions (3-4), and general body text (7-8).
   - What's unclear: Whether readers experience the frequency as reinforcement or redundancy.
   - Recommendation: Keep all glossary, definition, and protocol uses. Review body-text uses and consolidate where the term appears in consecutive paragraphs. Target: 10-12 total.

3. **Appendix A register: should it match body text voice?**
   - What we know: Appendix A is a technical anatomical reference with a telegraphic, catalog-style register. This is appropriate for its function.
   - What's unclear: Whether it needs any voice smoothing at all, given its reference-document nature.
   - Recommendation: Light touch only. Fix any AI tells if found, but do not impose narrative voice on what is correctly written as a reference catalog.

4. **The "self-tuning guitar" epilogue: how much editorial latitude?**
   - What we know: The epilogue uses a consumer-friendly metaphor ("advanced AI, sensors, and precision mechanics") that is tonally different from the clinical body.
   - What's unclear: Whether the author wants this kept as-is (it's been present since rendition 06) or refined.
   - Recommendation: Light touch. The register shift is intentional -- epilogues are meant to be accessible. Only fix clear AI tells or filler if present.

## Sources

### Primary (HIGH confidence)
- **Renditions 06 and 07** -- Author's authentic voice fingerprint (earliest drafts before AI editing)
- **Rendition 01 (current master paper)** -- Direct textual analysis via grep for all patterns documented above
- **Vital aspects checklist** (renditions/08_vital_aspects.md) -- Key TTC concepts that must survive editing
- **Phase 3 Summary** (.planning/phases/03-credibility-claims/03-02-SUMMARY.md) -- Record of what Phase 3 changed and why, essential for avoiding Pitfall 1

### Secondary (MEDIUM confidence)
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) -- Community-maintained list of AI-tell words and patterns, organized by model/era
- [AI Phrase Finder: Full List of Words and Phrases That Identify AI](https://aiphrasefinder.com/words-that-identify-ai/) -- Comprehensive searchable word list from systematic analysis of thousands of AI-generated articles
- [11 Words to Avoid to Not Sound Like AI (AiSDR)](https://aisdr.com/blog/words-to-avoid-so-you-dont-sound-like-ai/) -- Curated editorial list
- [Blake Stockton: Red Flag Words](https://www.blakestockton.com/red-flag-words/) -- Categorized by frequency and severity

### Tertiary (LOW confidence)
- General editorial best practices for white paper voice consistency (multiple sources, well-established but not specific to this domain)

## Metadata

**Confidence breakdown:**
- AI-tell identification: HIGH -- word lists are well-validated by multiple independent sources and verified against the actual paper text via grep
- Terminology standardization: HIGH -- all variants identified by direct grep search of the paper
- Repetitive refrain analysis: HIGH -- exact counts from grep, recommendations based on editorial judgment
- Voice register analysis: HIGH -- based on direct comparison of renditions 06-07 (author's authentic voice) vs. rendition 01 (current state)
- Phase 3 insertion smoothing: MEDIUM -- requires case-by-case judgment about which hedges are load-bearing vs. bureaucratic

**Research date:** 2026-03-08
**Valid until:** N/A -- editorial research is project-specific and does not expire
