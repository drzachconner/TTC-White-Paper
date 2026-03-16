#!/usr/bin/env python3
"""
md2typst.py — Convert TTC White Paper markdown to Typst.
Produces a professional white paper layout.
"""

import re
import sys

INPUT_FILE = "/Users/zachconnermba/Code/TTC-White-Paper/renditions/09_2026-03-16_STRUCTURAL_VISUAL_REDESIGN.md"
OUTPUT_FILE = "/Users/zachconnermba/Code/TTC-White-Paper/renditions/ttc-paper.typ"

# Graphics placement map: (section_keyword, filename, caption)
GRAPHICS = [
    ("Executive Summary", "08-summary-infographic-c-paradigm-shift.jpg", "The TTC Paradigm Shift"),
    ("Part I. From Principle", "01-concept-map-a-split-v2.jpg", "Bone-First vs. Tension-First: Two Paradigms"),
    ("The Clinical Distinction", "11-not-about-a-two-column.jpg", "TTC: A Paradigm Shift"),
    ("Clinical Observations", "03-clinical-flowchart-a-parallel-v2.jpg", "Traditional vs. TTC Clinical Pathway"),
    ("Part II. The NeuroSpinal System", "05-meningeal-anatomy-a-four-panel-v2.jpg", "The NeuroSpinal System: Meningeal Anatomy"),
    ("Part IV. Pathophysiology", "09-five-ds-cascade-c-threat-to-release.jpg", "The 5 D's Cascade"),
    ("Why Precision Matters", "19-upstream-a-cascade.jpg", "Upstream: Aberrant NeuroSpinal Tension"),
    ("Part V. TTC Analysis", "15-contact-params-a-silhouette.jpg", "TTC Contact Parameters"),
    ("Part VI. From Bone-on-Nerve", "07-timeline-a-horizontal.jpg", "Historical Timeline"),
    ("Part VII. Historical Lineage", "06-technique-table-a-four-column.jpg", "Technique Comparison"),
    ("Part X. Epilogue", "12-guitar-a-instrument.jpg", "The Self-Tuning Guitar"),
]


def escape_typst(text):
    """Escape special Typst characters."""
    # @ # $ are special in Typst
    text = text.replace('\\', '\\\\')
    text = text.replace('#', '\\#')
    text = text.replace('$', '\\$')
    text = text.replace('@', '\\@')
    text = text.replace('<', '\\<')
    text = text.replace('>', '\\>')
    return text


def process_inline(text):
    """Convert inline markdown to Typst markup."""
    # Bold+italic ***text***
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'_*\1*_', text)
    # Bold **text**
    text = re.sub(r'\*\*(.+?)\*\*', r'*\1*', text)
    # Italic *text* (careful not to match already processed)
    text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'_\1_', text)
    # Inline code `text`
    text = re.sub(r'`([^`]+)`', r'`\1`', text)
    return text


def escape_and_process(text):
    """Escape then apply inline formatting."""
    text = escape_typst(text)
    text = process_inline(text)
    return text


TYPST_PREAMBLE = r"""// ═══════════════════════════════════════════════════════════════════════
// TTC White Paper — Professional Typst Template
// ═══════════════════════════════════════════════════════════════════════

#set document(
  title: "The NeuroSpinal System as the Primary Tone-Setter",
  author: "Dr. Zach Conner, D.C.",
)

// ─── Color Palette ─────────────────────────────────────────────────────
#let primary = rgb("#2E6DA4")
#let primary-light = rgb("#EDF3FA")
#let accent = rgb("#3A8E8C")
#let dark = rgb("#1a1a2e")
#let clinical-green = rgb("#7EA88C")
#let clinical-bg = rgb("#F4F7F4")
#let warm-gray = rgb("#F8F7F5")

// ─── Page Setup ────────────────────────────────────────────────────────
#set page(
  paper: "us-letter",
  margin: (top: 0.9in, bottom: 0.9in, left: 1.1in, right: 1.1in),
  header: context {
    if counter(page).get().first() > 2 {
      set text(size: 8.5pt, font: "Avenir Next", fill: primary.lighten(20%))
      grid(
        columns: (1fr, 1fr),
        align: (left, right),
        smallcaps[The Primary Tone-Setter],
        [TTC White Paper],
      )
      v(2pt)
      line(length: 100%, stroke: 0.4pt + primary.lighten(50%))
    }
  },
  footer: context {
    if counter(page).get().first() > 1 {
      set text(size: 9pt, fill: dark.lighten(40%))
      align(center)[#counter(page).display()]
    }
  },
)

// ─── Typography ────────────────────────────────────────────────────────
#set text(
  font: "Charter",
  size: 10.5pt,
  fill: dark,
  lang: "en",
)

#set par(
  justify: true,
  leading: 0.72em,
  first-line-indent: 0pt,
  spacing: 0.85em,
)

// ─── Heading Styles ────────────────────────────────────────────────────
#show heading.where(level: 1): it => {
  v(1.2em)
  block(width: 100%)[
    #set text(font: "Avenir Next", size: 18pt, fill: primary, weight: "bold")
    #it.body
    #v(3pt)
    #line(length: 100%, stroke: 1.5pt + primary)
  ]
  v(0.6em)
}

#show heading.where(level: 2): it => {
  v(0.9em)
  block(width: 100%)[
    #set text(font: "Avenir Next", size: 13pt, fill: primary, weight: "semibold")
    #it.body
    #v(2pt)
    #line(length: 100%, stroke: 0.7pt + primary.lighten(40%))
  ]
  v(0.4em)
}

#show heading.where(level: 3): it => {
  v(0.7em)
  block[
    #set text(font: "Avenir Next", size: 11pt, fill: dark, weight: "semibold")
    #it.body
  ]
  v(0.3em)
}

#show heading.where(level: 4): it => {
  v(0.5em)
  block[
    #set text(font: "Charter", size: 10.5pt, fill: dark, weight: "bold", style: "italic")
    #it.body
  ]
  v(0.2em)
}

// ─── Component Functions ───────────────────────────────────────────────

// Pull quote
#let pullquote(body) = {
  v(0.6em)
  block(
    width: 100%,
    inset: (left: 16pt, right: 12pt, top: 10pt, bottom: 10pt),
    fill: primary-light,
    stroke: (left: 4pt + primary, rest: none),
    radius: (right: 3pt),
  )[
    #set text(style: "italic", size: 10.5pt, fill: dark.lighten(15%))
    #set par(leading: 0.65em)
    #body
  ]
  v(0.6em)
}

// Chapter/Part break
#let partbreak(title, orientation) = {
  v(1.2em)
  line(length: 100%, stroke: 1.5pt + primary)
  v(0.5em)
  block[
    #set text(font: "Avenir Next", size: 17pt, fill: primary, weight: "bold")
    #title
  ]
  if orientation != none and orientation != "" {
    v(0.2em)
    block[
      #set text(style: "italic", size: 9.5pt, fill: dark.lighten(30%))
      #orientation
    ]
  }
  v(0.2em)
  line(length: 100%, stroke: 0.5pt + primary.lighten(40%))
  v(0.8em)
}

// Clinical vignette box
#let vignette(title, body) = {
  v(0.5em)
  block(
    width: 100%,
    inset: (left: 14pt, right: 10pt, top: 10pt, bottom: 10pt),
    fill: clinical-bg,
    stroke: (left: 4pt + clinical-green, rest: none),
    radius: (right: 3pt),
  )[
    #set text(size: 9.5pt)
    *#title*
    #v(4pt)
    #set text(style: "italic")
    #body
  ]
  v(0.5em)
}

// Evidence box
#let evidencebox(title, body) = {
  v(0.4em)
  block(
    width: 100%,
    inset: 10pt,
    fill: primary-light.lighten(30%),
    stroke: 0.5pt + primary.lighten(40%),
    radius: 3pt,
  )[
    #set text(size: 9.5pt)
    *#title*
    #v(3pt)
    #body
  ]
  v(0.4em)
}

// Figure with caption
#let fig(path, caption-text) = {
  v(0.5em)
  figure(
    image(path, width: 65%),
    caption: text(size: 9pt)[#caption-text],
  )
  v(0.5em)
}

// ═══════════════════════════════════════════════════════════════════════
// TITLE PAGE
// ═══════════════════════════════════════════════════════════════════════
#page(header: none, footer: none, margin: (top: 1.5in, bottom: 1in, left: 1.1in, right: 1.1in))[
  #set text(fill: dark)

  #v(0.5in)
  #text(font: "Avenir Next", size: 32pt, fill: primary, weight: "bold")[
    The NeuroSpinal System as \
    the Primary Tone-Setter
  ]

  #v(0.3em)
  #text(font: "Avenir Next", size: 15pt, fill: accent, weight: "medium")[
    Model and Clinical Application of \
    Talsky Tonal Chiropractic
  ]

  #v(1.5em)
  #line(length: 40%, stroke: 1pt + primary.lighten(40%))
  #v(0.8em)

  #text(font: "Charter", size: 12pt, style: "italic")[Dr. Zach Conner, D.C.] \
  #v(0.2em)
  #text(font: "Charter", size: 10.5pt, fill: dark.lighten(30%))[Talsky Tonal Chiropractic]

  #v(1fr)

  #align(center)[
    #image("graphics/18-dd-palmer-a-typographic.jpg", width: 55%)
  ]

  #v(1fr)

  #block(
    inset: (left: 12pt),
    stroke: (left: 2pt + primary.lighten(30%)),
  )[
    #set text(size: 9.5pt, fill: primary.darken(10%))
    #emph["Life is an expression of tone; the cause of disease is any variation in tone."] \
    #h(1em) --- D.D. Palmer, #emph[The Chiropractor's Adjuster], 1910
  ]
]

// ═══════════════════════════════════════════════════════════════════════
// TABLE OF CONTENTS
// ═══════════════════════════════════════════════════════════════════════
#page(header: none)[
  #v(0.5in)
  #text(font: "Avenir Next", size: 20pt, fill: primary, weight: "bold")[Contents]
  #v(0.3em)
  #line(length: 100%, stroke: 1pt + primary)
  #v(0.8em)

  #set text(size: 10pt)
  #show outline.entry.where(level: 1): it => {
    v(0.4em)
    set text(font: "Avenir Next", weight: "semibold", fill: primary)
    it
  }
  #show outline.entry.where(level: 2): it => {
    set text(fill: dark.lighten(10%))
    it
  }
  #outline(
    title: none,
    indent: 1.5em,
    depth: 2,
  )
]

// ═══════════════════════════════════════════════════════════════════════
// DOCUMENT BODY BEGINS
// ═══════════════════════════════════════════════════════════════════════

"""


def convert_markdown_to_typst(md_text):
    """Main conversion function."""
    lines = md_text.split('\n')
    output = []
    i = 0

    # State
    in_list = False
    list_type = None  # 'bullet' or 'numbered'
    in_blockquote = False
    in_vignette = False
    in_evidence = False
    in_pullquote = False
    in_code_block = False
    table_rows = []
    collecting_table = False
    vignette_header = ""
    vignette_lines = []
    evidence_header = ""
    evidence_lines = []
    pullquote_lines = []
    emitted_partbreaks = set()

    # Skip document title and subtitle
    title_skipped = False
    subtitle_skipped = False

    # Track sections for graphic insertion
    pending_graphic = None
    paragraphs_since_section = 0

    def flush_list():
        nonlocal in_list, list_type
        if in_list:
            output.append('')
            in_list = False
            list_type = None

    def flush_table():
        nonlocal table_rows, collecting_table
        if table_rows and len(table_rows) >= 2:
            output.append(convert_table(table_rows))
        table_rows = []
        collecting_table = False

    def flush_vignette():
        nonlocal in_vignette, vignette_lines, vignette_header
        if in_vignette and vignette_lines:
            body_text = '\n'.join(vignette_lines)
            output.append(f'#vignette[{escape_and_process(vignette_header)}][{escape_and_process(body_text)}]')
        in_vignette = False
        vignette_lines = []
        vignette_header = ""

    def flush_evidence():
        nonlocal in_evidence, evidence_lines, evidence_header
        if in_evidence and evidence_lines:
            body_text = '\n'.join(evidence_lines)
            output.append(f'#evidencebox[{escape_and_process(evidence_header)}][{escape_and_process(body_text)}]')
        in_evidence = False
        evidence_lines = []
        evidence_header = ""

    def flush_pullquote():
        nonlocal in_pullquote, pullquote_lines
        if in_pullquote and pullquote_lines:
            text = ' '.join(l.strip() for l in pullquote_lines if l.strip())
            # Remove surrounding **
            text = re.sub(r'^\*\*(.+)\*\*$', r'\1', text.strip())
            # Remove surrounding "
            text = text.strip('"').strip('"').strip('"')
            output.append(f'#pullquote["{escape_typst(text)}"]')
        in_pullquote = False
        pullquote_lines = []

    def check_graphic_insert(section_text):
        """Check if a graphic should be inserted for this section."""
        nonlocal pending_graphic
        for keyword, filename, caption in GRAPHICS:
            if keyword in section_text:
                # Insert immediately after the heading
                output.append(f'#fig("graphics/{filename}", [{escape_typst(caption)}])')
                return

    def convert_table(rows):
        """Convert markdown table rows to Typst table."""
        if len(rows) < 2:
            return ''

        def parse_row(row):
            row = row.strip().strip('|')
            return [c.strip() for c in row.split('|')]

        header = parse_row(rows[0])
        data_rows = [parse_row(r) for r in rows[2:]]  # skip separator
        ncols = len(header)

        lines = []
        lines.append(f'#v(0.4em)')
        lines.append(f'#figure(')
        lines.append(f'  table(')
        lines.append(f'    columns: {ncols},')
        lines.append(f'    align: left,')
        lines.append(f'    stroke: 0.5pt + primary.lighten(60%),')
        lines.append(f'    fill: (_, row) => if row == 0 {{ primary }} else if calc.odd(row) {{ primary-light.lighten(40%) }} else {{ white }},')
        # Header
        for h in header:
            h_escaped = escape_and_process(h)
            lines.append(f'    table.cell[#text(fill: white, weight: "bold", font: "Avenir Next", size: 9pt)[{h_escaped}]],')
        # Data rows
        for row in data_rows:
            if not any(c.strip() for c in row):
                continue
            for cell in row:
                cell_escaped = escape_and_process(cell)
                lines.append(f'    [{cell_escaped}],')
        lines.append(f'  ),')
        lines.append(f'  kind: table,')
        lines.append(f')')
        lines.append(f'#v(0.4em)')
        return '\n'.join(lines)

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # ── Code blocks ─────────────────────────────────────────
        if stripped.startswith('```'):
            if in_code_block:
                output.append('```')
                in_code_block = False
            else:
                flush_list()
                flush_table()
                lang = stripped[3:].strip()
                output.append(f'```{lang}' if lang else '```')
                in_code_block = True
            i += 1
            continue

        if in_code_block:
            output.append(line)
            i += 1
            continue

        # ── Tables ──────────────────────────────────────────────
        if stripped.startswith('|') and '|' in stripped[1:]:
            flush_list()
            table_rows.append(stripped)
            collecting_table = True
            i += 1
            continue
        elif collecting_table:
            flush_table()

        # ── Horizontal rules ────────────────────────────────────
        if stripped in ('---', '***', '___') or re.match(r'^-{3,}$', stripped):
            flush_list()
            flush_vignette()
            flush_evidence()
            flush_pullquote()
            # Don't emit anything — we handle section breaks via headings
            i += 1
            continue

        # ── Images ──────────────────────────────────────────────
        img_match = re.match(r'^!\[([^\]]*)\]\(([^)]+)\)', stripped)
        if img_match:
            flush_list()
            alt = img_match.group(1)
            path = img_match.group(2)
            # Try to find in our graphics map
            found = False
            for keyword, filename, caption in GRAPHICS:
                if filename.split('.')[0].replace('-', '') in path.replace('-', '').replace('_', ''):
                    output.append(f'#fig("graphics/{filename}", [{escape_typst(caption)}])')
                    found = True
                    break
            if not found:
                output.append(f'// Image: {alt} ({path})')
            i += 1
            continue

        # ── Headings ────────────────────────────────────────────
        h_match = re.match(r'^(#{1,4})\s+(.+)$', stripped)
        if h_match:
            flush_list()
            flush_vignette()
            flush_evidence()
            flush_pullquote()
            level = len(h_match.group(1))
            title_text = h_match.group(2).strip()

            # Skip document title and subtitle
            if level == 1 and not title_skipped:
                title_skipped = True
                i += 1
                continue
            if level == 2 and not subtitle_skipped and 'Model and Clinical Application' in title_text:
                subtitle_skipped = True
                i += 1
                continue

            # Detect Part breaks at H3
            part_match = re.match(r'^Part\s+(I{1,3}V?|V?I{0,3}|[IVX]+)\.\s+(.+)$', title_text)
            if level == 3 and part_match:
                part_label = part_match.group(1)
                part_title = part_match.group(2)

                # Look ahead for orientation text
                orientation = ''
                j = i + 1
                while j < len(lines) and not lines[j].strip():
                    j += 1
                if j < len(lines):
                    italic_match = re.match(r'^\*(.+)\*$', lines[j].strip())
                    if italic_match:
                        orientation = italic_match.group(1)
                        i = j + 1
                    else:
                        i += 1
                else:
                    i += 1

                orientation_escaped = escape_typst(orientation) if orientation else ''
                output.append(f'#partbreak[Part {part_label}. {escape_typst(part_title)}][{orientation_escaped}]')
                emitted_partbreaks.add(part_label)

                # Check for graphic insertion
                check_graphic_insert(f'Part {part_label}. {part_title}')
                continue

            # H2 Part headings — skip if partbreak already emitted
            if level == 2:
                part_match2 = re.match(r'^Part\s+(I{1,3}V?|V?I{0,3}|[IVX]+)\.\s+(.+)$', title_text)
                if part_match2 and part_match2.group(1) in emitted_partbreaks:
                    i += 1
                    continue

            # Emit heading
            title_escaped = escape_and_process(title_text)
            if level == 1 or (level == 2 and re.match(r'^Part\s+', title_text)):
                output.append(f'\n= {title_escaped}\n')
                check_graphic_insert(title_text)
            elif level == 2:
                output.append(f'\n= {title_escaped}\n')
                check_graphic_insert(title_text)
            elif level == 3:
                # Skip decorative "First Principles" H3 (it's a chapter break, not a real section)
                if title_text == 'First Principles':
                    # Look ahead for orientation text and skip it too
                    j = i + 1
                    while j < len(lines) and not lines[j].strip():
                        j += 1
                    if j < len(lines):
                        italic_match = re.match(r'^\*(.+)\*$', lines[j].strip())
                        if italic_match:
                            i = j + 1
                            continue
                    i += 1
                    continue
                output.append(f'\n== {title_escaped}\n')
                check_graphic_insert(title_text)
            elif level == 4:
                output.append(f'\n=== {title_escaped}\n')

            i += 1
            continue

        # ── Blockquotes ─────────────────────────────────────────
        if stripped.startswith('>'):
            flush_list()
            content = re.sub(r'^>\s?', '', stripped)

            # Clinical vignette detection
            if re.match(r'\*\*Clinical Observation', content):
                flush_pullquote()
                flush_evidence()
                in_vignette = True
                vignette_header = re.sub(r'\*\*(.+?)\*\*', r'\1', content)
                vignette_lines = []
                i += 1
                continue

            if in_vignette:
                if not stripped or stripped == '>':
                    vignette_lines.append('')
                else:
                    inner = re.sub(r'^>\s?', '', stripped)
                    inner = re.sub(r'^\*(.+)\*$', r'\1', inner.strip())
                    vignette_lines.append(inner)
                i += 1
                continue

            # Evidence snapshot
            if re.match(r'\*\*Evidence Snapshot', content):
                flush_pullquote()
                in_evidence = True
                evidence_header = re.sub(r'\*\*(.+?)\*\*', r'\1', content)
                evidence_lines = []
                i += 1
                continue

            if in_evidence:
                if stripped == '>' or not stripped:
                    pass
                else:
                    inner = re.sub(r'^>\s?', '', stripped)
                    evidence_lines.append(inner)
                i += 1
                continue

            # Pull quote
            if not in_pullquote:
                flush_evidence()
                in_pullquote = True
                pullquote_lines = [content]
            else:
                pullquote_lines.append(content)
            i += 1
            continue

        # Flush blockquote states on non-blockquote line
        if in_vignette:
            flush_vignette()
        if in_evidence:
            flush_evidence()
        if in_pullquote:
            flush_pullquote()

        # ── Bullet lists ────────────────────────────────────────
        bullet_match = re.match(r'^[-*•]\s+(.+)$', stripped)
        if bullet_match:
            if not in_list or list_type != 'bullet':
                flush_list()
                in_list = True
                list_type = 'bullet'
            item_text = escape_and_process(bullet_match.group(1))
            output.append(f'- {item_text}')
            i += 1
            continue

        # Numbered lists
        num_match = re.match(r'^(\d+)\.\s+(.+)$', stripped)
        if num_match and not re.match(r'^\d{4}', stripped):
            if not in_list or list_type != 'numbered':
                flush_list()
                in_list = True
                list_type = 'numbered'
            item_text = escape_and_process(num_match.group(2))
            output.append(f'+ {item_text}')
            i += 1
            continue

        # Sub-bullets
        sub_bullet = re.match(r'^\s{2,}[-*]\s+(.+)$', line)
        if sub_bullet:
            item_text = escape_and_process(sub_bullet.group(1))
            output.append(f'  - {item_text}')
            i += 1
            continue

        # Empty line
        if not stripped:
            flush_list()
            output.append('')
            i += 1
            continue

        # ── Footnote definitions ────────────────────────────────
        footnote_match = re.match(r'^\[\^([^\]]+)\]:\s*(.+)$', stripped)
        if footnote_match:
            fn_text = escape_and_process(footnote_match.group(2))
            # Skip footnote defs for now
            i += 1
            continue

        # Remove inline footnote refs
        stripped = re.sub(r'\[\^[^\]]+\]', '', stripped)

        # ── Regular paragraph ───────────────────────────────────
        flush_list()
        text = escape_and_process(stripped)
        output.append(text)
        output.append('')
        i += 1

    # Flush remaining
    flush_list()
    flush_vignette()
    flush_evidence()
    flush_pullquote()
    if collecting_table:
        flush_table()

    return '\n'.join(output)


def post_process(typst_body):
    """Clean up the output."""
    # Remove excessive blank lines
    typst_body = re.sub(r'\n{4,}', '\n\n\n', typst_body)

    # Remove the DD Palmer pull quote near the top (it's on the title page)
    # The generated text looks like: #pullquote["*"Life is an expression of tone..."*...]
    typst_body = re.sub(
        r'#pullquote\[.*?[Ll]ife is an expression of tone.*?\]\n*',
        '',
        typst_body,
        count=1
    )

    # Remove the decorative "First Principles" H3 heading that appears before the real H1
    # Pattern: == First Principles (with optional orientation text) followed by = First Principles
    typst_body = re.sub(
        r'== First Principles\n.*?\n+= First Principles',
        '= First Principles',
        typst_body,
        count=1,
        flags=re.DOTALL
    )

    # Also catch simpler pattern
    typst_body = re.sub(
        r'== First Principles\n+= First Principles',
        '= First Principles',
        typst_body,
        count=1
    )

    return typst_body


def main():
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        md_text = f.read()

    print(f"Read {len(md_text)} chars from {INPUT_FILE}")

    body = convert_markdown_to_typst(md_text)
    body = post_process(body)

    full_doc = TYPST_PREAMBLE + body

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(full_doc)

    print(f"Wrote {len(full_doc)} chars to {OUTPUT_FILE}")
    print("Done! Run: cd renditions && typst compile ttc-paper.typ")


if __name__ == '__main__':
    main()
