# TTC White Paper — Production Plan

**Date:** February 25, 2026
**Target:** Publishable white paper (not journal submission)
**Audience:** Chiropractic profession — practitioners, students, technique-minded clinicians

---

## Strategic Decisions (Locked In)

- **Format:** White paper (no word count limits, no structured abstract required)
- **Epstein, Senzon, Talsky references:** KEEP — they are authoritative for this audience. Fix them from vague date ranges to specific, citable publications with titles, journals/publishers, and years.
- **Intent section (PEAR/RNG):** TBD — decide during editorial passes whether to keep as-is, reframe, or move to appendix. Lower risk in white paper format than journal submission.
- **Voice:** Preserve the author's distinctive register. The philosophical-clinical blend IS the paper's identity for this audience. Refine, don't flatten.

---

## The Plan

### Phase 0: Gemini Pre-Editorial Audit (One-Shot)
**Who:** Gemini 3.1 Pro (you, manually)
**Input:** `GEMINI-INTAKE.md` (already in repo)
**Time:** ~20 minutes

Prompt Gemini with the intake file and ask for:
1. Content that exists in older renditions but was **lost** in the current master (rendition 01)
2. Which Nov 2025 editorial feedback items were **not yet incorporated** into the Feb 2026 master
3. Section-by-section consistency check across all 8 versions — contradictions, drift, or weakened passages

Paste Gemini's output back here. This becomes input for Phase 2.

---

### Phase 1: Citation Audit & Repair ✅ COMPLETE (2026-02-26)
**Who:** You + Perplexity Pro
**Input:** References section of rendition 01

**Completed:**
- [x] Perplexity audit of all 29 citations (results in `editorial/2026-02-26_perplexity_citation_audit.md`)
- [x] Fixed wrong first author: Ahn → Senoğlu (2013 dural sac paper)
- [x] Fixed wrong year/pages: Alperin 2005 → 2000, vol 217(3):877-885
- [x] Fixed wrong author/year: Hinz 2012 → Wipff et al. 2007 (TGF-β1 paper)
- [x] Fixed wrong year/pages: McHugh 2012 → 1998, vol 8(4):215-222
- [x] Fixed bogus citation: Langevin & Huijing 2012 → Langevin et al. 2016 (real JBMT paper)
- [x] Fixed wrong pages: Fede et al. pages 1-12 → 38-43; added full author list
- [x] Fixed wrong pages: Liu et al. 605-611 → 602-611
- [x] Fixed wrong publisher: Palmer 1910 → Palmer School of Chiropractic, Davenport IA
- [x] Added DOIs to all verifiable journal articles
- [x] Added full author lists, subtitles, cities to books
- [x] Flagged Ward (1980) as unverifiable in bibliographic databases
- [x] Updated all in-text citations to match corrected references
- [x] Talsky & Nadler (2025) clarified as seminar materials

**Still open (Epstein/Senzon — requires separate research):**
- [ ] Replace `Epstein, D. (1994–2000s)` with specific publications
- [ ] Replace `Epstein, D., & Senzon, S. (selected writings...)` with exact publications
- [ ] Replace `Senzon, S. A. (2011–2024)` with specific papers

---

### Phase 2: Editorial Pass 1 — Structure & Redundancy
**Who:** Claude Opus 4.6 (me)
**Input:** Master paper + editorial feedback + Gemini audit output + fixed citations
**Time:** 1 session

Work:
- Consolidate redundancy between Executive Summary, Parts I, II, and IV
- "Misinformation / missing information" framework → one primary location, brief cross-references elsewhere
- "We do not seek to apply force to what is stuck" → one definitive placement
- Cascade sequence (dyskinesia, dysafferentation, etc.) → consolidate Parts III and IV
- Check Gemini's "lost content" report — restore anything valuable that dropped out of earlier drafts
- Apply any unincorporated Nov 2025 editorial feedback
- Produce: revised master with change log

---

### Phase 3: Editorial Pass 2 — Credibility & Claims
**Who:** Claude Opus 4.6 (me)
**Input:** Output of Phase 2
**Time:** 1 session

Work:
- Review every factual/clinical claim — flag any that need stronger support
- Decide intent section treatment (keep / reframe / appendix) based on white paper context
- Ensure evidence claims match the strength of their citations (no overclaiming)
- Tighten the "Evidence Map" section — make it honest about what's established vs. emerging vs. speculative
- Produce: revised draft with credibility notes

---

### Phase 4: Editorial Pass 3 — Voice, Register & Line Edit
**Who:** Claude Opus 4.6 (me)
**Input:** Output of Phase 3
**Time:** 1 session

Work:
- Harmonize register — clinical-scientific as primary, philosophical as intentional seasoning
- Executive Summary: lead with clinical mechanism, then philosophical frame
- Eliminate any remaining AI-sounding phrasing
- Tighten prose — remove filler, sharpen transitions
- Ensure consistent terminology throughout (pick one term and stick with it where variants exist)
- Produce: polished draft

---

### Phase 5: Adversarial Review (Optional)
**Who:** GPT-5.2 (you, manually)
**Time:** ~30 minutes

Send the polished draft to ChatGPT with:
> "You are a skeptical but fair chiropractic colleague reviewing this white paper before it's distributed at a professional seminar. Identify: logical gaps, unsupported claims, sections that would lose a practicing chiropractor's trust, and anything that reads as AI-generated. Be critical and specific."

Paste the critique back here. I'll make targeted revisions.

---

### Phase 6: Final Polish & Delivery
**Who:** Claude Opus 4.6 (me) + you
**Time:** 1 session

- Address any adversarial review feedback
- Final consistency pass
- You: read aloud, verify clinical accuracy matches your practice
- Commit final version to repo
- Export to PDF/Word if needed

---

## Tools & Cost

| Tool | Role | Cost |
|---|---|---|
| Claude Code (Opus 4.6) | All editorial passes | Already have |
| Perplexity Pro | Citation verification | $20/month |
| Gemini 3.1 Pro | One-shot pre-editorial audit | Free tier or $19.99/month |
| ChatGPT Plus | Adversarial review (optional) | $20/month |
| **Total** | | **~$20–60** |

---

## File Roles

| File | Role in Plan |
|---|---|
| `renditions/01_2026-02-03_MASTER_PAPER_COMPLETE.md` | Starting point — the document to refine |
| `editorial/2025-11-01_detailed_feedback.md` | Unresolved feedback to check against |
| `editorial/2025-11-01_suggested_refinements.md` | Specific edits to verify incorporation |
| `renditions/08_2025-11-02_vital_aspects.md` | Checklist — all key principles must survive |
| `GEMINI-INTAKE.md` | Pre-built file for Gemini audit |
| `PLAN.md` | **This file** |
