# Roadmap: TTC White Paper Editorial Production

## Overview

Six sequential editorial passes transform the master draft into a polished, credible white paper. Each phase is a complete pass over the document with a specific editorial lens. Phase 1 (Citations) is complete. The remaining five phases move from structural surgery through credibility hardening, voice refinement, adversarial stress-testing, and final delivery. The document improves with each pass, and later passes depend on earlier ones being stable.

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [x] **Phase 1: Citations** - Verify all references, add DOIs, resolve vague citations
- [ ] **Phase 2: Structure & Redundancy** - Consolidate overlapping content, recover lost material, apply unincorporated feedback
- [ ] **Phase 3: Credibility & Claims** - Audit every claim for evidence strength, decide intent section treatment
- [ ] **Phase 4: Voice & Polish** - Harmonize register, eliminate AI phrasing, tighten prose
- [ ] **Phase 5: Adversarial Review** - External LLM critique and response
- [ ] **Phase 6: Final Delivery** - Vital aspects verification, markdown commit, PDF export

## Phase Details

### Phase 1: Citations
**Goal**: Every reference in the paper is verifiable, correctly attributed, and properly formatted
**Depends on**: Nothing (first phase)
**Requirements**: CITE-01, CITE-02, CITE-03, CITE-04
**Success Criteria** (what must be TRUE):
  1. Every in-text citation has a matching entry in the References section
  2. All journal article references include correct author, year, volume, page, and DOI
  3. Vague "Epstein," "Senzon," and "Ward" citations resolve to specific named publications
**Plans**: Complete

Plans:
- [x] 01-01: Citation verification and DOI resolution

### Phase 2: Structure & Redundancy
**Goal**: The paper reads as a coherent, non-repetitive argument where each concept has one definitive home
**Depends on**: Phase 1
**Requirements**: STRC-01, STRC-02, STRC-03, STRC-04, STRC-05, STRC-06
**Success Criteria** (what must be TRUE):
  1. A reader encounters each major concept (misinformation/missing information framework, "we do not seek to apply force" principle, cascade sequence) in one primary location rather than scattered across sections
  2. The Executive Summary opens with the clinical mechanism and a reader can identify the paper's core thesis within the first paragraph
  3. Content from earlier renditions that was lost in the Feb 2026 master has been evaluated and valuable material recovered
  4. All actionable items from the Nov 2025 editorial feedback are either incorporated or explicitly documented as rejected with rationale
  5. Parts III and IV have distinct, non-overlapping scopes for the cascade sequence material
**Plans**: 2 plans

Plans:
- [ ] 02-01-PLAN.md — Full structural audit: redundancy map, content recovery diff, editorial feedback gap analysis, author approval checkpoint
- [ ] 02-02-PLAN.md — Execute all approved edits: Executive Summary restructure, redundancy consolidation, content recovery, editorial feedback incorporation, post-edit verification

### Phase 3: Credibility & Claims
**Goal**: Every claim in the paper is backed by evidence proportional to the strength of the assertion
**Depends on**: Phase 2
**Requirements**: CRED-01, CRED-02, CRED-03, CRED-04
**Success Criteria** (what must be TRUE):
  1. A skeptical colleague reading any factual claim can trace it to a cited source of appropriate strength (RCT for causal claims, case series for clinical observations, etc.)
  2. The intent section (PEAR/RNG) has been deliberately treated — kept with proper caveats, reframed as exploratory, or moved to an appendix — with the decision documented
  3. The Evidence Map section uses explicit language distinguishing established findings from emerging research from speculative connections
  4. No sentence makes a stronger claim than its supporting citation can bear
**Plans**: TBD

Plans:
- [ ] 03-01: TBD

### Phase 4: Voice & Polish
**Goal**: The paper sounds like Dr. Conner wrote it — clinical-scientific backbone with philosophical depth as intentional seasoning, not AI-generated flatness
**Depends on**: Phase 3
**Requirements**: VOIC-01, VOIC-02, VOIC-03, VOIC-04
**Success Criteria** (what must be TRUE):
  1. Reading any passage aloud, the register is consistently clinical-scientific with philosophical flourishes that feel authored rather than algorithmic
  2. A search for common AI tells (e.g., "it's important to note," "delve," "tapestry," "multifaceted") returns zero results
  3. Each technical term (subluxation vs. vertebral subluxation complex, AMT vs. Adverse Mechanical Tension, etc.) uses one consistent form throughout, with variants defined once and then standardized
  4. Every paragraph earns its word count — no filler sentences, no throat-clearing transitions
**Plans**: TBD

Plans:
- [ ] 04-01: TBD

### Phase 5: Adversarial Review
**Goal**: The paper has been stress-tested by an external model and all valid criticisms have been addressed
**Depends on**: Phase 4
**Requirements**: ADVR-01, ADVR-02
**Success Criteria** (what must be TRUE):
  1. A GPT-5.2 adversarial critique has been received covering logical coherence, evidentiary gaps, and rhetorical weaknesses
  2. Every critique point has been addressed — either fixed in the text or rebutted with documented rationale for keeping the original
**Plans**: TBD

Plans:
- [ ] 05-01: TBD

### Phase 6: Final Delivery
**Goal**: The paper is complete, verified against the vital aspects checklist, and ready for distribution in both markdown and PDF formats
**Depends on**: Phase 5
**Requirements**: DELV-01, DELV-02, DELV-03
**Success Criteria** (what must be TRUE):
  1. Every item on the vital aspects checklist (renditions/08_2025-11-02_vital_aspects.md) is present in the final draft — no key TTC principles were lost during editing
  2. The final markdown is committed to the repo as a clean, well-formatted document
  3. A PDF export exists and is ready for seminar distribution and digital sharing
**Plans**: TBD

Plans:
- [ ] 06-01: TBD

## Progress

**Execution Order:**
Phases execute in numeric order: 1 (done) -> 2 -> 3 -> 4 -> 5 -> 6

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Citations | 1/1 | Complete | 2026-02-26 |
| 2. Structure & Redundancy | 0/? | Not started | - |
| 3. Credibility & Claims | 0/? | Not started | - |
| 4. Voice & Polish | 0/? | Not started | - |
| 5. Adversarial Review | 0/? | Not started | - |
| 6. Final Delivery | 0/? | Not started | - |
