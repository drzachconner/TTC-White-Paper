# Phase 3: Credibility & Claims - Research

**Researched:** 2026-03-05
**Domain:** Evidence auditing for a chiropractic white paper -- claim-citation alignment, evidence tiering, PEAR/RNG treatment
**Confidence:** HIGH

## Summary

Phase 3 requires a systematic audit of every factual and clinical claim in the TTC white paper to ensure each claim is backed by evidence proportional to its assertive strength. The paper contains approximately 40-50 distinct factual/clinical claims spread across 12 Parts plus appendices, ranging from well-established anatomical facts (HIGH evidence) through emerging mechanobiological hypotheses (MEDIUM evidence) to speculative consciousness-related claims (LOW evidence). The most significant credibility risk is not that the paper makes false claims, but that it frequently presents emerging or speculative findings with the same assertive confidence as established facts -- creating an "evidence flatness" where readers cannot distinguish what is well-proven from what is exploratory.

The PEAR/RNG content in Part IX represents the single highest credibility risk. The Princeton Engineering Anomalies Research lab closed in 2007 after failing to produce replicable results; the Radin & Nelson (1989) meta-analysis has been substantially criticized; and the Bosch, Steinkamp & Boller (2006) meta-analysis in Psychological Bulletin concluded that selective reporting could explain the observed effects. Including this material without substantial caveats would undermine the paper's credibility with evidence-minded readers. The paper also contains several other claims that require hedging or tiering, particularly around fascial memory, liquid-crystalline conduction, piezoelectric signaling, and the "20% prefrontal cortex" claim attributed to Haavik.

**Primary recommendation:** Create a three-tier evidence classification system (Established / Emerging / Exploratory) and apply it to every factual claim in the paper, then rewrite language so claim strength matches evidence tier. Treat the PEAR/RNG content with explicit "exploratory" framing and substantial caveats, or move to an appendix with appropriate disclaimers.

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|-----------------|
| CRED-01 | Every factual/clinical claim reviewed for evidence strength match | The Complete Claim Audit (Section: Architecture Patterns) provides the claim-by-claim inventory with evidence tier assignments for every factual claim in the paper |
| CRED-02 | Intent section (PEAR/RNG) treatment decided and implemented (keep/reframe/appendix) | The PEAR/RNG Evidence Landscape (Section: Common Pitfalls, Pitfall 1) and the detailed analysis in the Claim Audit provide full context for the author's decision. Research recommends keeping in-text with heavy "exploratory" framing |
| CRED-03 | Evidence Map section honestly distinguishes established vs emerging vs speculative | The Three-Tier Evidence Classification System (Section: Architecture Patterns, Pattern 1) provides the framework and language templates for tiering |
| CRED-04 | No overclaiming -- citation strength matches claim strength | The Common Pitfalls section catalogs the specific overclaiming patterns found in this paper with concrete rewrite guidance |
</phase_requirements>

## Standard Stack

This is an editorial project, not a software project. The "stack" is the set of tools and frameworks used for the credibility audit.

### Core

| Tool/Framework | Purpose | Why Standard |
|----------------|---------|--------------|
| Three-Tier Evidence Classification | Categorize every claim as Established / Emerging / Exploratory | Standard approach in evidence-based health sciences writing; maps directly to evidence pyramid levels |
| Claim-Citation Matrix | Spreadsheet-style mapping of every claim to its supporting citation with evidence tier | Standard editorial audit technique for academic and professional health sciences documents |
| Hedging Language Templates | Standardized phrases for each evidence tier | Prevents inconsistent language that confuses readers about evidence strength |

### Supporting

| Tool | Purpose | When to Use |
|------|---------|-------------|
| Evidence Pyramid Reference | Map citation types to evidence levels | When assessing whether a citation (RCT, case series, textbook, theoretical paper) matches the claim it supports |
| PEAR/RNG Literature Summary | Pre-researched evidence landscape for intent section | When making the author's decision on PEAR/RNG treatment |

## Architecture Patterns

### Pattern 1: Three-Tier Evidence Classification System

**What:** Every factual claim in the paper is assigned one of three tiers based on the strength of its supporting evidence. The paper's language is then calibrated to match.

**Tier Definitions:**

| Tier | Label | Evidence Level | Language Pattern |
|------|-------|----------------|-----------------|
| 1 | **Established** | Systematic reviews, multiple RCTs, standard anatomy textbooks, widely replicated findings | State as fact: "X does Y" / "Research demonstrates" / "Evidence shows" |
| 2 | **Emerging** | Single RCTs, well-designed observational studies, peer-reviewed mechanistic research with limited clinical validation, single-lab findings awaiting replication | Hedge appropriately: "Research suggests" / "Evidence indicates" / "Studies have found" / "Preliminary evidence supports" |
| 3 | **Exploratory** | Theoretical frameworks, single studies with small samples, contested meta-analyses, speculative extrapolations from adjacent fields, conference materials | Signal clearly: "One line of inquiry..." / "Exploratory research has examined..." / "While not yet established..." / "This remains a working hypothesis" |

**When to use:** Apply to every factual sentence in the paper during the claim audit.

### Pattern 2: The Complete Claim Audit

**What:** A section-by-section inventory of every factual/clinical claim, its supporting citation, the evidence tier, and whether the current language matches the tier.

**The audit below catalogs claims that need attention. Claims already properly calibrated are not listed.**

---

#### Executive Summary

| Claim | Current Citation | Evidence Tier | Current Language Match? | Issue |
|-------|-----------------|---------------|------------------------|-------|
| "Meningeal system...is a contractile, sensorimotor, information-bearing continuum" | Multiple (Fede 2018, Breig 1978, Schleip 2003) | EMERGING | PARTIAL | "Contractile" is supported (Fede, Schleip); "sensorimotor" is supported (mechanoreceptors in dura); "information-bearing continuum" is a theoretical synthesis, not a direct finding |
| "Fibroblast-to-myofibroblast conversion mediated by TGF-beta1 signaling" | Tomasek 2002, Wipff 2007 | ESTABLISHED (for fascia generally) / EMERGING (for meninges specifically) | YES for mechanism, NO for meningeal application | The TGF-beta1/myofibroblast pathway is well-established in wound healing literature; its specific role in meningeal contracture is an extrapolation |
| "The system waits to experience range of motion into the area of restricted tension without a stress response before it will release" | No direct citation | EXPLORATORY | NO -- stated as fact | This is a clinical model/hypothesis, not a demonstrated finding. Needs "In the TTC model..." framing |

#### Part III: The NeuroSpinal System

| Claim | Current Citation | Evidence Tier | Current Language Match? | Issue |
|-------|-----------------|---------------|------------------------|-------|
| Myodural bridge "forming an active and passive tension-monitoring system" | Liu 2017, Scali 2011, Zheng 2014 | EMERGING | PARTIAL | Anatomical existence is established; "tension-monitoring system" function is interpretive. Liu 2017 is a review, not original functional data |
| "NeuroSpinal System extends its influence beyond the spinal canal through direct fascial continuities" | Liu 2017 | EMERGING | NO -- stated as established fact | Anatomical connection is demonstrated; "extends its influence" implies functional significance not yet proven |
| Meningeo-fascial continuum "behaves as a tensegrity lattice" | No direct citation | EXPLORATORY | NO -- stated as fact | Tensegrity applied to the meningeal system is a conceptual model, not an empirically verified structural description |
| "α-SMA-positive myofibroblasts within the meninges, providing intrinsic contractile force" | Fede 2018, Langevin 2016 | EMERGING | PARTIAL | Fede 2018 is about fascia, not specifically meninges. Langevin 2016 is about fascia as a sensory organ. Neither directly demonstrates alpha-SMA in meninges. This is an extrapolation from fascial research to meningeal tissue |
| Piezoelectric signal transduction in dura/fascia | Becker & Selden 1985 | EXPLORATORY | NO -- stated as mechanism | Becker & Selden is a popular science book, not peer-reviewed research. Piezoelectric properties of collagen are real but the specific signaling claims go beyond established evidence |
| Liquid-crystalline conduction exceeds speed of synaptic transmission | Ho & Knight 1998 | EXPLORATORY | NO -- "demonstrates" language | Ho & Knight is a theoretical/speculative paper proposing a mechanism for acupuncture meridians. The "liquid crystalline water layers" acting as "proton-conductive pathways" is an unverified hypothesis. The claim that this "can exceed the speed of synaptic transmission" is speculative |
| "fascia and meningeal tissues may retain 'mechanical memories'" | Fede 2018 | EMERGING (for fascia) / EXPLORATORY (for meninges) | PARTIAL -- "emerging research suggests" is appropriate hedging | The Fede/Tozzi paper (actually published as editorial in 2013/2014, not 2018 as cited) explicitly asks the question rather than answering it. "May retain" is acceptable hedging but the source is weaker than implied |

#### Part IV: Historical Evolution

| Claim | Current Citation | Evidence Tier | Current Language Match? | Issue |
|-------|-----------------|---------------|------------------------|-------|
| "Modern neuroscience increasingly challenges the long-held assumption that vertebral misalignment routinely causes neural interference through direct mechanical compression" | None directly | ESTABLISHED (the challenge exists) | YES | Fair characterization of the field's evolution |
| Haavik "demonstrated that interference more often stems from tension, distortion, and altered afferent input -- not direct compression" | Haavik & Murphy 2007 | EMERGING | PARTIAL | The 2007 study showed SEP changes after cervical manipulation in 12 subjects. "Demonstrated" is too strong for n=12 with 20-minute effects. Better: "provided evidence suggesting" |
| Allostatic load framework applied to NeuroSpinal System | No citation for the specific application | EMERGING (allostatic load concept) / EXPLORATORY (application to NeuroSpinal System) | PARTIAL | McEwen's allostatic load concept is well-established (HIGH). Applying it specifically to the meningeal system as the site of accumulation is the paper's own theoretical contribution -- should be framed as such |

#### Part V: Historical Lineage

| Claim | Current Citation | Evidence Tier | Current Language Match? | Issue |
|-------|-----------------|---------------|------------------------|-------|
| Toftness "consistently won pre- and post-x-ray competitions for the reduction in scoliosis" | Talsky & Nadler 2025 (seminar materials) | LOW -- unsourced/anecdotal | NO -- stated as historical fact | This claim relies on seminar materials, not published evidence. Either provide a verifiable source or hedge: "According to accounts within the technique community..." |
| Van Rumpt "discovered in 1923 that a very specific light force thrust was successful in accomplishing osseous correction" | No citation | LOW -- historical claim without primary source | NO -- stated as fact | Historical claims about technique founders should note the source or use "is credited with" language |
| Haavik's "nearly 20% on average in prefrontal cortex processing" | Lelic et al. 2016 (implied) | EMERGING | PARTIAL | The Lelic 2016 study used brain source localization (not direct measurement), with a small sample size. "Nearly 20% on average" is cited by chiropractic organizations but the methodology and sample size warrant hedging |

#### Part VI: Pathophysiology

| Claim | Current Citation | Evidence Tier | Current Language Match? | Issue |
|-------|-----------------|---------------|------------------------|-------|
| "Subluxation begins upstream of joint fixation" | No direct citation -- this IS the paper's thesis | MODEL/THESIS | PARTIAL | This is the paper's core argument, not a research finding. Currently stated as fact. Should be framed as the model's proposition |
| Fibroblast-to-myofibroblast via TGF-beta1 in meningeal tissues | Tomasek 2002, Wipff 2007 | ESTABLISHED (general mechanism) / EMERGING (meningeal application) | NO | The mechanism is well-established in connective tissue generally (Tomasek, Wipff). Its specific occurrence in meningeal tissue is an extrapolation that should be acknowledged |
| "CSF hydrodynamics...pulse, swirl, and return dynamics" | Brinker 2014, Alperin 2000 | ESTABLISHED (CSF dynamics generally) / EMERGING (specific claims about TTC-relevant effects) | YES | The citations support that CSF dynamics exist and are measurable; the specific connection to tone regulation is the paper's synthesis |
| "Flexibility phenomenon seen under anesthesia" parallel | McHugh 1998 | ESTABLISHED | YES | Well-cited demonstration that ROM limitations are often neural, not structural |
| Layers of compensatory tension architecture | No direct citation | EXPLORATORY/MODEL | NO -- stated as factual mechanism | This is the paper's clinical model, not a research finding. Needs "In the TTC model..." framing |

#### Part IX: Evidence Map and Research Invitations

| Claim | Current Citation | Evidence Tier | Current Language Match? | Issue |
|-------|-----------------|---------------|------------------------|-------|
| PEAR/RNG "intention-linked deviations from chance...odds against chance of 50,000 to 1" | Radin & Nelson 1989 | CONTESTED/LOW | NO -- presented as suggestive evidence without adequate caveat | See detailed PEAR/RNG analysis below. The "50,000 to 1" statistic is from a contested meta-analysis whose methodology has been substantially criticized |
| "focused intent may influence physical systems at small but measurable levels" | Radin & Nelson 1989 (implied) | CONTESTED/LOW | PARTIAL -- "may" provides some hedging | The hedging is insufficient given the state of the evidence. This claim requires substantial caveats about failed replications and methodological criticism |
| Haavik "nearly 20% on average in prefrontal cortex processing" (repeated) | Lelic et al. 2016 (implied) | EMERGING | NO -- stated as demonstrated fact | See notes in Part V above |

#### Part XI: Glossary

| Claim | Current Citation | Evidence Tier | Current Language Match? | Issue |
|-------|-----------------|---------------|------------------------|-------|
| "Tone is the mechanism through which Universal Intelligence manifests and maintains the physical universe" | No citation -- philosophical axiom | PHILOSOPHICAL AXIOM | N/A -- acceptable as defined philosophical position | This is a definitional statement within the chiropractic vitalistic tradition, not a factual claim requiring evidence. Acceptable as-is within a paper for this audience |

### Anti-Patterns to Avoid

- **Evidence Flatness:** Treating all citations as equally authoritative. A textbook anatomy reference (Standring 2020) and a speculative popular science book (Oschman 2000) should not receive the same assertive language.
- **Citation-as-Shield:** Attaching a citation to a claim does not make the claim proportional. The strength of the claim must match the strength of the citation, not merely its existence.
- **Extrapolation Without Acknowledgment:** Using findings from fascia research to make claims about meninges without noting the extrapolation. Several claims in this paper cite fascial research (Fede 2018, Langevin 2016, Schleip 2003) but apply findings to meningeal tissue without acknowledging this is an inference.
- **Model-as-Fact:** The paper's core thesis (NeuroSpinal System as primary tone-setter, subluxation as secondary to meningeal tension) is a theoretical model, not a proven mechanism. When stated as fact, it becomes an overclaim. When stated as the paper's model/proposition, it becomes a legitimate contribution.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Evidence tiering | Ad-hoc language decisions | Three-tier system with standardized hedging phrases | Consistency; prevents drift back to flat assertive language during editing |
| PEAR/RNG treatment | Subjective judgment about how controversial the content is | Published meta-analyses and critic responses as basis for framing | Author needs to see the actual evidence landscape, not just an editor's opinion |
| Claim-citation alignment | Reading through and making intuitive adjustments | Systematic claim matrix with every factual sentence cataloged | Without a matrix, claims get missed; the paper is 85KB with claims on nearly every page |

**Key insight:** The biggest risk in credibility editing is not removing content -- it is failing to distinguish between evidence tiers. A paper can include speculative content and remain credible IF the language signals clearly that the content is speculative. The problem is not what the paper says but how confidently it says it.

## Common Pitfalls

### Pitfall 1: The PEAR/RNG Credibility Trap
**What goes wrong:** Including PEAR/RNG research without adequate context makes the entire paper vulnerable to dismissal by skeptical readers. A single paragraph about consciousness-affecting-random-number-generators can overshadow 30 pages of solid mechanobiological argument.
**Why it happens:** The author genuinely values the concept of congruent intent and sees PEAR as supporting evidence. The white paper format feels safer for this content than a journal article would.
**How to avoid:** Three options for the author's decision:
  - **Option A (Recommended): Keep in text with heavy exploratory framing.** Rewrite the PEAR paragraph to explicitly acknowledge: (1) PEAR lab closed in 2007 after 28 years without producing replicable results; (2) the Bosch et al. (2006) meta-analysis in Psychological Bulletin found a statistically significant but extremely small effect size that was "strongly and inversely related to sample size" and showed "extreme heterogeneity" -- patterns consistent with publication bias; (3) the Radin & Nelson (1989) "50,000 to 1" odds have been substantially criticized for methodological issues including potential selective reporting; (4) this line of research "remains deeply contested in the scientific community." Frame as: "Some exploratory research has examined whether focused intent can influence physical systems, though this work remains contested and has not produced reliably replicable results."
  - **Option B: Move to appendix.** Relocate all PEAR/RNG content to an appendix titled "Exploratory: Intent and Information" with full disclaimers. This physically separates the speculative content from the core argument.
  - **Option C: Remove entirely.** Delete the PEAR/RNG references and let the "congruent intent" concept stand on its established neurophysiological basis (practitioner attentional state, therapeutic alliance, contextual factors) without invoking consciousness-affects-matter research.
**Warning signs:** Any language that uses PEAR findings to support TTC's mechanism of action rather than simply acknowledging them as an area of interest.

**PEAR/RNG Evidence Summary for Author Decision:**

| Source | Finding | Limitation |
|--------|---------|------------|
| Radin & Nelson (1989) | Meta-analysis of 597 RNG studies; reported "odds against chance of 50,000 to 1" | Methodology criticized by Boller (2006) and Schub (2006); no direct statistical significance quoted in the paper itself; results "acutely sensitive to the method used to combine the data" |
| Bosch, Steinkamp & Boller (2006) -- *Psychological Bulletin*, 132(4), 497-523 | Meta-analysis of 380 RNG studies; found "significant but very small overall effect size" | Effect sizes "strongly and inversely related to sample size" and "extremely heterogeneous"; Monte Carlo simulation showed patterns "could in principle be a result of publication bias"; authors concluded psychokinesis is "not proven" |
| PEAR Lab (1979-2007) | 28 years of research at Princeton; observed effects "between one and about 0.1%" | Lab closed 2007; results not reliably replicable; two German organizations failed to reproduce; PEAR itself failed to reproduce some results; criticized for poor controls, possible data selection, optional stopping; Princeton administration considered it an embarrassment |

**PROJECT.md already notes:** "Add Bosch et al. (2006) to PEAR -- Pairs original with independent APA meta-analysis; shows balance" as a pending decision. This research confirms that adding Bosch is essential if PEAR content remains.

### Pitfall 2: The Fascial-to-Meningeal Extrapolation Gap
**What goes wrong:** The paper cites research on fascia (Fede 2018, Langevin 2016, Schleip 2003) but applies findings to meningeal tissue as if they are equivalent. Fascia and meninges share some structural characteristics but are distinct tissue types with different embryological origins, cellular composition, and functional roles.
**Why it happens:** The TTC model requires the meninges to possess contractile and sensory properties similar to fascia. The fascial research is more extensive and better documented, making it a natural (but imprecise) source.
**How to avoid:** Add explicit bridging language: "While direct investigation of meningeal myofibroblast activity is limited, research in fascia -- which shares structural and compositional similarities with meningeal tissue -- has demonstrated..." This preserves the argument while honestly noting the extrapolation.
**Warning signs:** Any sentence citing Fede, Langevin, or Schleip that directly attributes their fascial findings to meningeal tissue without noting the inference.

### Pitfall 3: The Haavik "20%" Overclaim
**What goes wrong:** The paper states Haavik's research showed "nearly 20% on average in prefrontal cortex processing" as if this is a robust, replicated finding. The actual study (Lelic et al. 2016) used brain source localization (an indirect measurement method) with a small sample size.
**Why it happens:** This statistic is widely repeated in chiropractic marketing materials and has become accepted within the profession without attention to the study's limitations.
**How to avoid:** Reframe: "A brain source localization study (Lelic et al., 2016) found changes in prefrontal cortex processing following spinal manipulation, though the authors note that further research with larger samples is needed to confirm these preliminary findings."
**Warning signs:** Using the "20%" figure without citing the specific study or noting sample size limitations.

### Pitfall 4: Model-as-Fact Confusion
**What goes wrong:** The paper's core thesis -- that the NeuroSpinal System is the "primary tone-setter" and that subluxation is secondary to meningeal tension -- is presented throughout as established fact rather than as the paper's proposed model.
**Why it happens:** The author deeply believes this model and has extensive clinical experience supporting it. It feels true because it works clinically.
**How to avoid:** At key assertion points, use framing language: "In the TTC model..." / "This paper proposes that..." / "The TTC framework holds that..." This does not weaken the argument -- it actually strengthens credibility by showing the author understands the difference between a well-supported model and a proven mechanism.
**Warning signs:** Sentences that begin with declarative statements about meningeal primacy without acknowledging this is the paper's thesis rather than established science. Example: "Subluxation begins upstream of joint fixation" should become "In the TTC model, subluxation begins upstream of joint fixation" or "This paper argues that subluxation begins upstream of joint fixation."

### Pitfall 5: The Oschman/Becker Citation Quality Issue
**What goes wrong:** Becker & Selden (1985) *The Body Electric* and Oschman (2000) *Energy Medicine: The Scientific Basis* are cited alongside peer-reviewed journal articles as if they carry equal evidentiary weight. Both are popular science books, not peer-reviewed research. Oschman's work in particular has received substantial criticism for accepting "kinds of evidence that most scientists would not" (Harriet Hall, MD).
**Why it happens:** These books are widely cited in alternative/complementary medicine communities and contain genuinely interesting hypotheses. But they are not primary research.
**How to avoid:** Either (a) replace these citations with the primary peer-reviewed research they reference, or (b) explicitly note "As synthesized in [popular account]" rather than citing them as if they are primary evidence. The piezoelectric properties of collagen ARE established in peer-reviewed literature -- cite that directly rather than through Becker.
**Warning signs:** Any sentence that uses Becker or Oschman as the sole citation for a factual claim about a biological mechanism.

### Pitfall 6: Unsourced Historical Claims
**What goes wrong:** Several historical claims about technique founders (Van Rumpt's 1923 discovery, Toftness winning x-ray competitions, specific dates of technique development) are stated as fact without primary sources.
**Why it happens:** This is oral tradition within the chiropractic profession, transmitted through seminar culture. The author knows these facts from direct lineage but lacks published verification.
**How to avoid:** For claims sourced from oral tradition, use language like "According to accounts within the technique community..." or "As described in TTC seminar materials (Talsky & Nadler, 2025)..." This is honest and appropriate for a white paper (vs. a journal article which would require stricter sourcing).
**Warning signs:** Historical claims presented as verified fact without any citation at all.

## Evidence Tier Summary by Paper Section

| Paper Section | Dominant Tier | Key Risk Areas |
|---------------|---------------|----------------|
| Executive Summary | EMERGING with some EXPLORATORY | "System waits to experience..." claim; fibroblast-meningeal extrapolation |
| First Principles | PHILOSOPHICAL AXIOM | N/A -- appropriately framed as philosophical position |
| Part I (Application) | PHILOSOPHICAL/MODEL | Low risk -- appropriately framed as perspective |
| Part II (Clinical Method) | MODEL with EMERGING support | "Biology is...a symphony" is metaphor, not claim -- acceptable |
| Part III (NeuroSpinal System) | Mix of ESTABLISHED and EMERGING | Myodural bridge function; alpha-SMA in meninges; piezoelectric/liquid crystalline claims; fascial memory |
| Part IV (Historical) | ESTABLISHED (historical narrative) with EMERGING (Haavik) | Haavik "20%" claim; oversimplified "Haavik demonstrated" language |
| Part V (Lineage) | LOW (historical claims without primary sources) | Toftness competition claim; various founding dates without sources |
| Part VI (Pathophysiology) | EMERGING with EXPLORATORY elements | Model-as-fact throughout; fascial-to-meningeal extrapolation; "layers of compensatory tension" as model |
| Part VII (Protocol) | MODEL/TECHNIQUE DESCRIPTION | Low risk -- describes methodology, not making research claims |
| Part VIII (Positioning) | MODEL | Low risk -- comparative framing |
| Part IX (Evidence Map) | Mix -- but PEAR/RNG is CONTESTED/LOW | PEAR/RNG; repeated Haavik "20%" claim |
| Part X (Ethics) | MODEL | Low risk |
| Part XI (Glossary) | DEFINITIONS | Tone definition includes philosophical axiom -- acceptable for audience |
| Part XII (Epilogue) | METAPHOR | Low risk |

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| PEAR lab research (1979-2007) | Lab closed 2007; no successor producing replicable results | 2007 | PEAR cannot be cited as active/current research; must be contextualized historically |
| Compression model of subluxation | Tension/afferent-based models gaining traction | ~2000s-present | The paper's core thesis IS the current direction; paper is actually ahead of much of the profession |
| Fascia as inert wrapping | Fascia as sensory/contractile organ | ~2007-present (Schleip, Langevin, Stecco) | Strong emerging research supports fascial contractility; meningeal contractility is the less-established extension |

## Open Questions

1. **Fede et al. citation year discrepancy**
   - What we know: The paper cites "Fede et al., 2018" for fascial memory and alpha-SMA claims. The references list shows Fede et al. (2018) in JBMT 22(1):38-43. However, the original "Does fascia hold memories?" editorial appears to have been published in 2013/2014 by Tozzi, not Fede.
   - What's unclear: Whether the 2018 Fede reference is a different paper than the "fascia holds memories" concept, or whether there's a citation confusion. The Fede 2018 paper in the references appears to be correctly cited as a 2018 publication.
   - Recommendation: Verify that the Fede et al. (2018) paper cited in references is indeed the correct source. The "Does fascia hold memories?" editorial is by Tozzi (2014). Fede et al. (2018) may be a different paper that discusses mechanical memory in fascia through a different mechanism. Either way, the claims made in the paper should match what the cited source actually demonstrates.

2. **Meningeal myofibroblast evidence**
   - What we know: Alpha-SMA-positive myofibroblasts are well-documented in fascia. Their presence in meninges is less directly documented, though meningeal fibroblasts are known to exist.
   - What's unclear: Whether there is direct evidence of myofibroblast differentiation in meningeal tissue specifically, or whether this is extrapolated from fascial research.
   - Recommendation: If direct evidence exists, cite it. If not, explicitly acknowledge the extrapolation.

3. **Lelic et al. 2016 -- the actual study behind the "20%" claim**
   - What we know: The paper repeatedly cites "nearly 20% on average in prefrontal cortex processing" but does not directly cite Lelic et al. 2016 in the references.
   - What's unclear: Whether this statistic comes from Lelic 2016 or another Haavik-associated study. The references only list Haavik & Murphy 2007.
   - Recommendation: If citing the "20%" figure, add the specific source (Lelic et al., 2016) to the references and note study limitations.

## Sources

### Primary (HIGH confidence)
- Bosch, H., Steinkamp, F., & Boller, E. (2006). Examining psychokinesis: The interaction of human intention with random number generators--a meta-analysis. *Psychological Bulletin*, 132(4), 497-523. -- Verified via PubMed (PMID: 16822162)
- Evidence hierarchy / levels of evidence framework -- Standard health sciences methodology (multiple university library guides, PMC articles)
- Wikipedia entry on PEAR lab -- Cross-verified with NPR reporting, Nature, Skeptic's Dictionary, multiple independent sources

### Secondary (MEDIUM confidence)
- Haavik & Murphy (2007) study details -- Verified via PubMed (PMID: 17137836); 12-subject study with 20-minute effects
- Lelic et al. (2016) brain source localization study -- Identified via PMC (PMC4800094); small sample, indirect measurement
- Fede et al. (2018) / Tozzi (2014) fascia memory -- Verified publication exists via PubMed (PMID: 24725795) and ScienceDirect
- Myodural bridge research (Scali 2011, Zheng 2014, Liu 2017) -- Anatomical existence well-established; functional significance emerging

### Tertiary (LOW confidence -- flagged for validation)
- Ho & Knight (1998) liquid crystalline collagen hypothesis -- Speculative; related to acupuncture meridian theory which lacks clinical validation
- Oschman (2000) energy medicine claims -- Popular science book; criticized by Harriet Hall, MD for accepting non-standard evidence
- Becker & Selden (1985) bioelectrical claims -- Popular science book, not peer-reviewed primary research
- Historical claims about technique founders (Van Rumpt, Toftness, etc.) -- Oral tradition without primary published sources

## Metadata

**Confidence breakdown:**
- Evidence tiering framework: HIGH -- Standard health sciences methodology, well-established
- Claim-citation alignment audit: HIGH -- Based on direct reading of the paper and verification of each cited source's actual content and evidence level
- PEAR/RNG analysis: HIGH -- Multiple independent sources confirm the contested status of this research, including the definitive Bosch 2006 meta-analysis in Psychological Bulletin
- Fascial-to-meningeal extrapolation identification: MEDIUM -- The gap is clear but the exact state of meningeal myofibroblast research requires deeper literature review than web search can provide
- Historical claim verification: LOW -- Unable to verify oral tradition claims through published sources; flagged for author input

**Research date:** 2026-03-05
**Valid until:** 2026-04-05 (30 days -- this domain is stable; evidence landscape for these topics changes slowly)
