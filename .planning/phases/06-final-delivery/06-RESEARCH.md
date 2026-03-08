# Phase 6: Final Delivery - Research

**Researched:** 2026-03-08
**Domain:** Vital aspects verification, markdown finalization, PDF export
**Confidence:** HIGH

## Summary

Phase 6 is the final phase of a 6-phase editorial production pipeline. The paper has been through citation verification, structural consolidation, credibility hardening, voice polishing, and adversarial review. This phase verifies no key TTC principles were lost, commits the final markdown, and produces a PDF for seminar distribution.

The master paper is 1,078 lines (~105KB) of standard markdown with bold/italic emphasis, blockquotes, tables (29 table rows), code-style diagrams (1 ASCII diagram block), horizontal rules, bulleted lists, nested headers (H1-H3), and a footnote. It contains no images, no embedded HTML, and no LaTeX math. This straightforward markdown translates cleanly to both HTML and PDF.

**Primary recommendation:** Use pandoc (v3.7.0.2, already installed) to convert markdown to HTML5 with custom CSS styling, then install `weasyprint` via brew to convert the styled HTML to PDF. This two-step pipeline gives full control over typography and layout without requiring a LaTeX installation.

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|-----------------|
| DELV-01 | Final polished markdown committed to repo | The current master paper at `renditions/01_2026-02-03_MASTER_PAPER_COMPLETE.md` has been through 5 phases of edits. Verification step: confirm no markdown formatting errors, orphaned references are cosmetic only, and the document is clean. Commit as the final version. |
| DELV-02 | PDF exported and ready for distribution | Pandoc 3.7.0.2 is installed. No LaTeX engine exists on the system. Two viable PDF paths: (1) `brew install weasyprint` then pandoc → HTML → weasyprint → PDF, or (2) `brew install typst` then pandoc → typst → PDF. Weasyprint recommended for superior CSS typography control. |
| DELV-03 | Vital aspects checklist verified — all key TTC principles survive edits | The checklist at `renditions/08_2025-11-02_vital_aspects.md` contains 18 distinct verifiable concepts (see Vital Aspects Verification Protocol below). Each must be confirmed present in the final draft. |
</phase_requirements>

## Standard Stack

### Core
| Tool | Version | Purpose | Why Standard |
|------|---------|---------|--------------|
| pandoc | 3.7.0.2 | Markdown → HTML5 conversion | Already installed; gold standard for document conversion |
| weasyprint | 68.1 | HTML → PDF conversion | Available via `brew install weasyprint`; CSS-based PDF rendering with excellent typography; uses pango (already installed) and cairo (already installed) |

### Supporting
| Tool | Version | Purpose | When to Use |
|------|---------|---------|-------------|
| Custom CSS | N/A | PDF styling (fonts, margins, page breaks) | Required for professional seminar-quality PDF |
| pandoc metadata | N/A | Title, author, date YAML front matter | Add to markdown for proper PDF title page |

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| weasyprint | typst (`brew install typst`) | Typst is newer, faster, but less CSS control; pandoc typst output is less mature than HTML output |
| weasyprint | basictex (`brew install --cask basictex`) | Full LaTeX engine; ~400MB install; overkill for this document; LaTeX debugging is painful |
| pandoc+weasyprint | reportlab (Python) | Programmatic PDF creation; requires writing Python layout code; unnecessary when pandoc handles conversion |
| weasyprint | Chrome headless (`--print-to-pdf`) | Requires Chrome; less precise page control; not reproducible |

**Installation:**
```bash
brew install weasyprint
```

## Architecture Patterns

### Recommended Pipeline
```
renditions/01_...MASTER_PAPER_COMPLETE.md
  ↓ (pandoc: markdown → HTML5 with CSS)
  /tmp/ttc-paper.html
  ↓ (weasyprint: HTML → PDF)
  renditions/TTC-White-Paper-Final.pdf
```

### Pattern 1: Pandoc with Custom CSS
**What:** Use pandoc to convert markdown to standalone HTML5, embedding a custom CSS stylesheet that controls typography, margins, and page breaks.
**When to use:** When you need professional PDF output from markdown without LaTeX.
**Command:**
```bash
pandoc renditions/01_2026-02-03_MASTER_PAPER_COMPLETE.md \
  -f markdown \
  -t html5 \
  --standalone \
  --css=renditions/ttc-paper.css \
  --metadata title="The NeuroSpinal System as the Primary Tone-Setter" \
  --metadata author="Dr. Zach Conner" \
  -o /tmp/ttc-paper.html
```

### Pattern 2: Weasyprint HTML → PDF
**What:** Convert the styled HTML to PDF with proper page sizing, margins, and headers/footers.
**When to use:** After pandoc produces HTML.
**Command:**
```bash
weasyprint /tmp/ttc-paper.html renditions/TTC-White-Paper-Final.pdf
```

### Pattern 3: CSS for Print Media
**What:** CSS `@media print` and `@page` rules control PDF layout: margins, page breaks before major sections, orphan/widow control, font selection.
**Key CSS properties for this paper:**
- `@page { size: letter; margin: 1in; }` — US letter, 1-inch margins
- `h2 { page-break-before: always; }` — Each major section starts on a new page
- `h2:first-of-type { page-break-before: avoid; }` — Executive Summary stays on first page
- `blockquote { font-style: italic; border-left: 3px solid #666; padding-left: 1em; }` — Palmer epigraph styling
- `table { border-collapse: collapse; width: 100%; }` — Clean tables
- `pre { white-space: pre-wrap; font-size: 0.85em; }` — ASCII diagrams fit on page
- `body { font-family: "Georgia", "Times New Roman", serif; font-size: 11pt; line-height: 1.6; }` — Professional serif typography

### Anti-Patterns to Avoid
- **Adding YAML front matter to the working file:** The master paper has been carefully edited across 5 phases. Do NOT modify its content. Pass metadata via pandoc command-line flags instead.
- **Binary PDF in git:** PDF files bloat git history. Commit the PDF but acknowledge it adds ~200-400KB per version. Acceptable for a single final export.
- **Over-styling the CSS:** This is a white paper for chiropractors, not a design piece. Clean, readable typography is the goal. No color themes, no fancy headers, no decorative elements.
- **Modifying the master paper for PDF formatting:** All formatting should happen in the CSS layer, not by changing the markdown content.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Markdown → PDF | Custom Python script with reportlab | pandoc + weasyprint | Pandoc handles all markdown edge cases; reportlab requires manual layout code |
| Page breaks | Manual `\pagebreak` insertions in markdown | CSS `page-break-before` rules | Keep content and presentation separate; don't pollute the editorial markdown |
| Table of contents | Manual TOC section | pandoc `--toc` flag | Pandoc auto-generates TOC from headers |
| Footnote rendering | Manual footnote formatting | pandoc footnote handling | The paper already uses `[^anatomical-detail]` syntax; pandoc renders it correctly |

**Key insight:** The paper is pure markdown with no exotic formatting. Pandoc handles every feature the paper uses (bold, italic, blockquotes, tables, code blocks, footnotes, horizontal rules, nested headers). The only custom work needed is a CSS file for print styling.

## Common Pitfalls

### Pitfall 1: ASCII Diagram Overflow
**What goes wrong:** The ASCII diagram in "Visual Model: AMT and Release Pathways" (lines ~461-504) may overflow the page width in PDF.
**Why it happens:** Code/preformatted blocks use monospace font; the diagram is ~50 characters wide which should fit, but margins matter.
**How to avoid:** Use `pre { white-space: pre-wrap; font-size: 0.85em; }` in CSS. Test the PDF output and adjust font size if the diagram wraps awkwardly.
**Warning signs:** Lines breaking mid-arrow (`→`) or mid-word in the PDF.

### Pitfall 2: Orphaned References Section
**What goes wrong:** The References section (lines 718-786) and Appendix A (lines 790-1065) are long. Page breaks may split individual reference entries across pages.
**Why it happens:** Default pagination doesn't respect reference entry boundaries.
**How to avoid:** CSS `p { orphans: 3; widows: 3; }` helps. For references specifically, each reference is a separate paragraph so this should work naturally. Test and verify.
**Warning signs:** A reference author name on one page, its title on the next.

### Pitfall 3: Vital Aspects False Positive
**What goes wrong:** Concluding a principle is "present" because similar words appear, when the actual concept has been diluted or reframed beyond recognition.
**Why it happens:** Grep-based verification finds keywords but misses semantic meaning.
**How to avoid:** For each vital aspect, verify both (a) the concept is present AND (b) it retains the original strength/framing. Use the exact phrasing from the checklist as the search anchor, then read surrounding context.
**Warning signs:** A principle that exists only in the glossary or a parenthetical rather than as a substantive statement in the body text.

### Pitfall 4: Weasyprint Font Fallback
**What goes wrong:** The specified font (Georgia, Times New Roman) isn't available on the system, and weasyprint falls back to a generic serif that looks poor.
**Why it happens:** macOS includes both Georgia and Times New Roman, so this is unlikely but worth verifying.
**How to avoid:** Test with `fc-list | grep -i georgia` before building. Weasyprint uses system fonts via pango/fontconfig.
**Warning signs:** PDF text looks different from expected; characters rendered in a sans-serif font.

### Pitfall 5: Appendix B Disclaimer Missed in Distribution
**What goes wrong:** The adversarial review added a disclaimer to Appendix B noting it "may be omitted in distribution versions." If seminar distribution should exclude it, this must be handled.
**Why it happens:** The disclaimer was added as guidance text, not as a build-system toggle.
**How to avoid:** Ask the author: should the seminar PDF include Appendix B or not? If not, create the PDF from a copy with Appendix B removed (don't modify the master).
**Warning signs:** Distributing controversial PEAR/RNG content at a seminar without realizing it's optional.

## Vital Aspects Verification Protocol

The checklist at `renditions/08_2025-11-02_vital_aspects.md` contains 18 distinct verifiable concepts. Here is the systematic verification plan:

### Category 1: Foundational Identity (7 items)
| # | Concept | Search Anchor | Where to Verify |
|---|---------|---------------|-----------------|
| 1 | Original intent — progressive reduction of interference | "progressive reduction of physical interference" | First Principles section |
| 2 | Body is intelligent system that wants to correct | "intelligent system that wants to correct" | First Principles, Part I |
| 3 | Not about fixing someone else | "not about us fixing" OR "not about moving bones" | First Principles, Part I |
| 4 | Communicating with the intelligence of the nervous system | "dialog with the intelligence" OR "communicate with" | First Principles, Part I |
| 5 | Engage what is ready, not what is stuck | "engage what is ready" | Part I.2, refrains |
| 6 | Best window in, not biggest fixation | "best window in" | Throughout (canonical refrain) |
| 7 | Most receptivity, not most resistance | "most receptivity" | Part I.2, refrains |

### Category 2: NeuroSpinal System Definition (5 items)
| # | Concept | Search Anchor | Where to Verify |
|---|---------|---------------|-----------------|
| 8 | Not osseous, not articular | "not osseous" OR "non-articular" | Part I, Part II |
| 9 | NeuroSpinal System as working substrate | "NeuroSpinal System" | Throughout (64 instances per Phase 4) |
| 10 | Cranio-Spinal Meningeal Functional Unit equivalence | "Cranio-Spinal Meningeal Functional Unit" | Part III, Glossary |
| 11 | Meningeal layers: pia, arachnoid, dura | "pia mater" AND "arachnoid" AND "dura mater" | Part III |
| 12 | System is active, dynamic, independently motile | "independently motile" | Part III |

### Category 3: Primary Tone-Setter Thesis (3 items)
| # | Concept | Search Anchor | Where to Verify |
|---|---------|---------------|-----------------|
| 13 | Meningeal system as primary tone setter | "Primary Tone-Setter" | Executive Summary, title, throughout |
| 14 | Contracts under stress, expands as stress resolves | "contracts under" OR "expands and relaxes" | Part III, Part VI |
| 15 | Governs global tension patterns | "global tension patterns" OR "adaptability, breath, posture" | Part III, Executive Summary |

### Category 4: TTC Clinical Approach (3 items)
| # | Concept | Search Anchor | Where to Verify |
|---|---------|---------------|-----------------|
| 16 | Input is non-articular, non-osseous, through soft tissue and dural access | "dural access points" OR "soft tissue" | Part II, Part VII |
| 17 | Every contact with intent to influence the whole | "intent to influence the whole" | Part II, Part VII, Part IX |
| 18 | Communicating corrective intent through touch | "corrective intent through touch" | Epilogue, Part I, Part II |

### Verification Method
For each of the 18 items:
1. `grep -n "search anchor" renditions/01_...MASTER_PAPER_COMPLETE.md`
2. Read 3-5 lines of surrounding context
3. Confirm the concept retains its original meaning and strength
4. Mark PRESENT / DILUTED / MISSING
5. Any DILUTED or MISSING = requires author decision before DELV-03 can pass

**Prior verification baseline:** Phases 3, 4, and 5 all confirmed 18/18 vital aspects present. This phase is a final confirmation, not expected to find issues.

## Markdown Cleanup Checklist

Before committing as the final version (DELV-01), verify:

1. **No broken formatting:** All bold/italic markers properly closed
2. **Consistent heading hierarchy:** H1 (title only) → H2 (major sections) → H3 (subsections)
3. **Horizontal rules:** Used consistently as section dividers
4. **Table alignment:** All 29 table rows render correctly
5. **Footnote:** The `[^anatomical-detail]` footnote in Appendix A is properly defined and renders
6. **Blockquote:** Palmer epigraph at top renders correctly
7. **Orphaned references (cosmetic):** 12 pre-existing orphaned reference entries in Appendix A — document these as known and cosmetic, not blocking
8. **No trailing whitespace or inconsistent line endings**
9. **UTF-8 encoding confirmed** (em dashes, curly quotes if any)

## PDF Styling Specifications

For seminar distribution, the PDF should be:
- **Page size:** US Letter (8.5" x 11")
- **Margins:** 1 inch all sides
- **Body font:** Georgia or Times New Roman, 11pt
- **Heading fonts:** Same family, sized proportionally (H1: 20pt, H2: 16pt, H3: 13pt)
- **Line spacing:** 1.5 or 1.6
- **Page numbers:** Bottom center
- **Title page:** Title, subtitle, author, date — derived from H1/H2 headers
- **Section breaks:** Major sections (Parts I-XII, Appendices) start on new pages
- **No headers/footers** other than page numbers (keep it clean)

## Open Questions

1. **Appendix B inclusion in PDF**
   - What we know: Phase 5 added a disclaimer saying Appendix B "may be omitted in distribution versions"
   - What's unclear: Does the author want the seminar PDF to include Appendix B?
   - Recommendation: Ask author. If omitting, create PDF from a filtered copy; never modify the master markdown.

2. **PDF filename and location**
   - What we know: The project convention is `renditions/` directory for all versions
   - What's unclear: Desired filename convention
   - Recommendation: `renditions/TTC-White-Paper-Final-2026-03.pdf` — includes date for versioning

3. **Table of contents in PDF**
   - What we know: Pandoc can auto-generate a TOC via `--toc` flag
   - What's unclear: Whether author wants a TOC for seminar handout
   - Recommendation: Include TOC — the paper is ~30+ pages with 12 major parts plus appendices. A TOC helps navigation.

## Sources

### Primary (HIGH confidence)
- System inspection: `pandoc --version` → 3.7.0.2 confirmed
- System inspection: `brew info weasyprint` → 68.1 available, uses pango (installed) + cairo (installed)
- System inspection: No LaTeX engine installed (pdflatex, xelatex, lualatex all absent)
- System inspection: No typst installed
- File analysis: Master paper is 1,078 lines, ~105KB, standard markdown features only
- File analysis: Vital aspects checklist contains 18 verifiable concepts
- Project history: All prior phases confirmed 18/18 vital aspects present

### Secondary (MEDIUM confidence)
- Pandoc documentation: pandoc supports `--pdf-engine=weasyprint` when weasyprint is installed
- Weasyprint documentation: CSS `@page` and `@media print` rules control PDF layout

## Metadata

**Confidence breakdown:**
- Vital aspects verification: HIGH — systematic protocol defined, prior phases established 18/18 baseline
- Markdown cleanup: HIGH — straightforward formatting check, no exotic features
- PDF export pipeline: HIGH — pandoc installed, weasyprint available via brew, cairo and pango already present
- CSS styling: MEDIUM — specifications defined but exact styling requires iterative testing

**Research date:** 2026-03-08
**Valid until:** 2026-04-08 (stable — no fast-moving dependencies)
