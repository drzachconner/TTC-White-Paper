#!/usr/bin/env python3
"""
md2latex.py — Convert TTC White Paper markdown to LaTeX.
One-time conversion tool; optimized for this specific document.
"""

import re
import sys

INPUT_FILE = "/Users/zachconnermba/Code/TTC-White-Paper/renditions/09_2026-03-16_STRUCTURAL_VISUAL_REDESIGN.md"
OUTPUT_FILE = "/Users/zachconnermba/Code/TTC-White-Paper/renditions/ttc-paper.tex"

GRAPHICS_PATH = "graphics/"

# Map of image filenames (from markdown alt text / path patterns) to actual files
IMAGE_MAP = {
    "concept-map": ("01-concept-map-a-split-v2.png",
                    r"Bone-First vs.\ Tension-First: Two Paradigms of Subluxation"),
    "clinical-flowchart": ("03-clinical-flowchart-a-parallel-v2.png",
                           r"Traditional Chiropractic vs.\ TTC Clinical Pathway"),
    "meningeal-anatomy": ("05-meningeal-anatomy-a-four-panel-v2.png",
                          "Meningeal Anatomy: The NeuroSpinal System"),
    "technique-table": ("06-technique-table-a-four-column.png",
                        "Technique Comparison: Osseous, OsseoTonal, Tonal, Tonal Energetics"),
    "timeline": ("07-timeline-a-horizontal.png",
                 "Historical Timeline: From Bone-on-Nerve to Tone-First"),
    "summary-infographic": ("08-summary-infographic-c-paradigm-shift.png",
                            "TTC Paradigm Shift: Summary"),
    "five-ds-cascade": ("09-five-ds-cascade-c-threat-to-release.png",
                        "The 5 D's Cascade: From Threat Perception to Release"),
    "not-about": ("11-not-about-a-two-column.png",
                  "TTC IS\\ldots\\ A Paradigm Shift"),
    "guitar": ("12-guitar-a-instrument.png",
               "The Self-Tuning Guitar: A Metaphor for TTC"),
    "contact-params": ("15-contact-params-a-silhouette.png",
                       "TTC Contact Parameters: Location, Vector, Amount, Intent"),
    "dd-palmer": ("18-dd-palmer-a-typographic.png",
                  r"D.D.\ Palmer: ``Life is an expression of tone''"),
    "upstream": ("19-upstream-a-cascade.png",
                 "Upstream Insight: Aberrant NeuroSpinal Tension Precedes the 5 D's"),
}

LATEX_PREAMBLE = r"""\documentclass[11pt,letterpaper]{article}

% ─── Font & Encoding ────────────────────────────────────────────────────────
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{newpxtext,newpxmath}   % Palatino-style serif
\usepackage[scaled=0.90]{helvet}   % Helvetica sans-serif for headings

% ─── Page Layout ─────────────────────────────────────────────────────────────
\usepackage[
  letterpaper,
  top=1in, bottom=1in,
  left=1.25in, right=1.25in
]{geometry}

% ─── Micro-typography ────────────────────────────────────────────────────────
\usepackage{microtype}

% ─── Colors ──────────────────────────────────────────────────────────────────
\usepackage[dvipsnames,svgnames,x11names]{xcolor}
\definecolor{primaryblue}{HTML}{2E6DA4}
\definecolor{darktext}{HTML}{1a1a2e}
\definecolor{accentteal}{HTML}{3A8E8C}
\definecolor{lightbluebg}{HTML}{EDF3FA}
\definecolor{clinicalborder}{HTML}{7EA88C}
\definecolor{clinicalbg}{HTML}{F4F7F4}

% ─── Headers & Footers ───────────────────────────────────────────────────────
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0.4pt}
\fancyhead[LE]{\small\sffamily\color{primaryblue}\leftmark}
\fancyhead[RO]{\small\sffamily\color{primaryblue}TTC White Paper}
\fancyfoot[C]{\small\thepage}
\fancypagestyle{plain}{%
  \fancyhf{}%
  \fancyfoot[C]{\small\thepage}%
  \renewcommand{\headrulewidth}{0pt}%
}

% ─── Section Styling ─────────────────────────────────────────────────────────
\usepackage{titlesec}
% H1 (section): large sans-serif blue
\titleformat{\section}
  {\sffamily\bfseries\LARGE\color{primaryblue}}
  {}
  {0em}
  {}
  [\vspace{0.2ex}{\color{primaryblue}\hrule height 1.5pt}\vspace{0.5ex}]

% H2 (subsection): medium sans-serif with blue accent line
\titleformat{\subsection}
  {\sffamily\bfseries\large\color{primaryblue}}
  {}
  {0em}
  {}
  [\vspace{0.15ex}{\color{primaryblue!60}\hrule height 0.8pt}\vspace{0.3ex}]

% H3 (subsubsection): smaller sans-serif
\titleformat{\subsubsection}
  {\sffamily\bfseries\normalsize\color{darktext}}
  {}
  {0em}
  {}

% H4 (paragraph): italic serif, run-in
\titleformat{\paragraph}[runin]
  {\itshape\bfseries\normalsize\color{darktext}}
  {}
  {0em}
  {}[.\ ]

\titlespacing*{\section}{0pt}{2ex plus 1ex minus .2ex}{1ex plus .2ex}
\titlespacing*{\subsection}{0pt}{1.5ex plus 0.8ex minus .2ex}{0.7ex plus .2ex}
\titlespacing*{\subsubsection}{0pt}{1.2ex plus 0.5ex minus .2ex}{0.5ex plus .2ex}

% ─── Line Spacing ────────────────────────────────────────────────────────────
\usepackage{setspace}
\setstretch{1.4}
\setlength{\parskip}{0.4ex plus 0.2ex minus 0.1ex}
\setlength{\parindent}{0pt}

% ─── Ragged Right ────────────────────────────────────────────────────────────
\usepackage{ragged2e}
\RaggedRight

% ─── Graphics ────────────────────────────────────────────────────────────────
\usepackage{graphicx}
\graphicspath{{graphics/}}
\usepackage{float}
\usepackage{placeins}
\usepackage[font=small,labelfont=bf,skip=4pt]{caption}

% ─── Tables ──────────────────────────────────────────────────────────────────
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{longtable}
\usepackage{array}
\usepackage{colortbl}

% ─── Lists ───────────────────────────────────────────────────────────────────
\usepackage{enumitem}
\setlist[itemize]{noitemsep, topsep=3pt, leftmargin=1.5em}
\setlist[enumerate]{noitemsep, topsep=3pt, leftmargin=1.5em}

% ─── tcolorbox ───────────────────────────────────────────────────────────────
\usepackage[most]{tcolorbox}

% Pull quote box
\tcbuselibrary{skins,breakable}
\newtcolorbox{pullquotebox}{
  enhanced,
  breakable,
  before skip=1.2em,
  after skip=1.2em,
  left=12pt,
  right=8pt,
  top=6pt,
  bottom=6pt,
  arc=2pt,
  boxrule=0pt,
  frame hidden,
  borderline west={4pt}{0pt}{primaryblue},
  colback=lightbluebg,
  fontupper=\itshape\large,
}

% Clinical vignette box
\newtcolorbox{vignetteinner}{
  enhanced,
  breakable,
  before skip=1em,
  after skip=1em,
  left=10pt,
  right=8pt,
  top=6pt,
  bottom=6pt,
  arc=2pt,
  boxrule=0pt,
  frame hidden,
  borderline west={4pt}{0pt}{clinicalborder},
  colback=clinicalbg,
  fontupper=\itshape\small,
}

% Evidence snapshot box (lighter styling)
\newtcolorbox{evidencebox}{
  enhanced,
  breakable,
  before skip=0.8em,
  after skip=0.8em,
  left=8pt,
  right=6pt,
  top=4pt,
  bottom=4pt,
  arc=2pt,
  boxrule=0.5pt,
  colframe=primaryblue!40,
  colback=lightbluebg!60,
  fontupper=\small,
}

% Part break styling
\newcommand{\partbreak}[2]{%
  \clearpage%
  \vspace*{1.5cm}%
  {\sffamily\bfseries\fontsize{20}{24}\selectfont\color{primaryblue}#1}\par%
  \vspace{0.5em}%
  {\itshape\large #2}\par%
  \vspace{1cm}%
}

% ─── Hyperref ────────────────────────────────────────────────────────────────
\usepackage[
  colorlinks=true,
  linkcolor=primaryblue,
  urlcolor=accentteal,
  citecolor=accentteal,
  bookmarks=true,
  bookmarksopen=false,
  pdftitle={The NeuroSpinal System as the Primary Tone-Setter},
  pdfauthor={Dr. Zach Conner},
]{hyperref}

% ─── Footnotes ───────────────────────────────────────────────────────────────
\usepackage[hang,flushmargin]{footmisc}

% ─── Misc ────────────────────────────────────────────────────────────────────
\usepackage{soul}      % for \hl if needed
\usepackage{csquotes}

\color{darktext}

% ─── Document Begin ──────────────────────────────────────────────────────────
\begin{document}

% Title Page
\begin{titlepage}
\vspace*{2cm}
{\sffamily\bfseries\fontsize{28}{34}\selectfont\color{primaryblue}
The NeuroSpinal System as\\[0.3ex]the Primary Tone-Setter\par}
\vspace{0.8em}
{\sffamily\bfseries\fontsize{16}{20}\selectfont\color{accentteal}
Model and Clinical Application of Talsky Tonal Chiropractic\par}
\vspace{1.5em}
{\large\itshape Dr. Zach Conner, D.C.\par}
\vspace{0.5em}
{\normalsize Talsky Tonal Chiropractic\par}
\vfill
\begin{center}
\includegraphics[width=0.65\textwidth]{18-dd-palmer-a-typographic.png}
\end{center}
\vfill
{\small\color{primaryblue!70}
\textit{``Life is an expression of tone; the cause of disease is any variation in tone.''}\\
\hspace*{2em}--- D.D.\ Palmer, \textit{The Chiropractor's Adjuster}, 1910\par}
\vspace{1cm}
\end{titlepage}

% Table of Contents
\clearpage
\setstretch{1.2}
\tableofcontents
\setstretch{1.4}
\clearpage

"""

LATEX_POSTAMBLE = r"""
\end{document}
"""


def escape_latex(text):
    """Escape special LaTeX characters in body text."""
    # Order matters — backslash must come first
    replacements = [
        ('\\', r'\textbackslash{}'),
        ('&', r'\&'),
        ('%', r'\%'),
        ('#', r'\#'),
        ('_', r'\_'),
        ('^', r'\^{}'),
        ('~', r'\textasciitilde{}'),
        ('{', r'\{'),
        ('}', r'\}'),
        ('$', r'\$'),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def process_inline(text):
    """Convert inline markdown to LaTeX (bold, italic, code)."""
    # Bold+italic ***text***
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'\\textbf{\\textit{\1}}', text)
    # Bold **text**
    text = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', text)
    # Italic *text* (not at word start to avoid confusion)
    text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'\\textit{\1}', text)
    # Inline code `text`
    text = re.sub(r'`([^`]+)`', r'\\texttt{\1}', text)
    return text


def escape_and_process(text):
    """Escape LaTeX chars then apply inline markdown."""
    text = escape_latex(text)
    text = process_inline(text)
    return text


def figure_for_key(key):
    """Return LaTeX figure block for a graphic key."""
    if key not in IMAGE_MAP:
        return ''
    fname, caption = IMAGE_MAP[key]
    return (
        f'\n\\begin{{figure}}[htbp]\n'
        f'\\centering\n'
        f'\\includegraphics[width=0.85\\textwidth]{{{fname}}}\n'
        f'\\caption{{{caption}}}\n'
        f'\\end{{figure}}\n'
        f'\\FloatBarrier\n'
    )


def detect_image_key(alt_text, path):
    """Try to match an image to our IMAGE_MAP."""
    combined = (alt_text + ' ' + path).lower()
    for key in IMAGE_MAP:
        if key in combined:
            return key
        # Also check filename fragments
        fname_key = key.replace('-', '')
        if fname_key in combined.replace('-', '').replace('_', ''):
            return key
    # Try path-based matching
    for key in IMAGE_MAP:
        if IMAGE_MAP[key][0].split('.')[0].replace('-', '') in combined.replace('-', '').replace('_', ''):
            return key
    return None


def is_vignette_start(line):
    """Detect clinical observation blockquote headers."""
    return bool(re.match(r'^>\s*\*\*Clinical Observation', line))


def is_evidence_snapshot(line):
    """Detect evidence snapshot blockquote headers."""
    return bool(re.match(r'^>\s*\*\*Evidence Snapshot', line))


def convert_table(rows):
    """Convert a list of markdown table rows to LaTeX booktabs table."""
    if len(rows) < 2:
        return ''

    # Parse cells
    def parse_row(row):
        row = row.strip().strip('|')
        cells = [c.strip() for c in row.split('|')]
        return cells

    header = parse_row(rows[0])
    # rows[1] is separator
    data_rows = [parse_row(r) for r in rows[2:]]

    ncols = len(header)
    # Column spec: first col left, rest left-aligned, use X for wide tables
    col_spec = 'l' + 'l' * (ncols - 1)

    lines = []
    lines.append('')
    lines.append('\\begin{center}')
    lines.append(f'\\begin{{tabular}}{{{col_spec}}}')
    lines.append('\\toprule')

    # Header row
    header_cells = ' & '.join(
        f'\\textbf{{\\textsf{{\\color{{white}}{escape_and_process(h)}}}}}'
        for h in header
    )
    lines.append(f'\\rowcolor{{primaryblue}}')
    lines.append(f'{header_cells} \\\\')
    lines.append('\\midrule')

    for i, row in enumerate(data_rows):
        if not any(c.strip() for c in row):
            continue
        if i % 2 == 0:
            lines.append('\\rowcolor{lightbluebg!40}')
        cells = ' & '.join(escape_and_process(c) for c in row)
        lines.append(f'{cells} \\\\')

    lines.append('\\bottomrule')
    lines.append('\\end{tabular}')
    lines.append('\\end{center}')
    lines.append('')
    return '\n'.join(lines)


def convert_markdown_to_latex(md_text):
    """Main conversion function."""
    lines = md_text.split('\n')
    output = []
    i = 0

    # State tracking
    in_itemize = False
    in_enumerate = False
    in_blockquote = False
    in_vignette = False
    in_evidence = False
    in_pullquote = False
    in_code_block = False
    table_rows = []
    collecting_table = False
    vignette_lines = []
    evidence_lines = []
    pullquote_lines = []

    def flush_list():
        nonlocal in_itemize, in_enumerate
        if in_itemize:
            output.append('\\end{itemize}')
            in_itemize = False
        if in_enumerate:
            output.append('\\end{enumerate}')
            in_enumerate = False

    def flush_table():
        nonlocal table_rows, collecting_table
        if table_rows:
            output.append(convert_table(table_rows))
            table_rows = []
        collecting_table = False

    def flush_vignette():
        nonlocal in_vignette, vignette_lines
        if in_vignette and vignette_lines:
            # First line is the header
            header = vignette_lines[0]
            body = vignette_lines[1:]
            output.append('\\begin{vignetteinner}')
            output.append(f'{{\\normalfont\\bfseries {escape_and_process(header)}}}\\\\[4pt]')
            for bl in body:
                if bl.strip():
                    output.append(escape_and_process(bl) + '\\\\[2pt]')
            output.append('\\end{vignetteinner}')
        in_vignette = False
        vignette_lines = []

    def flush_evidence():
        nonlocal in_evidence, evidence_lines
        if in_evidence and evidence_lines:
            header = evidence_lines[0]
            body = evidence_lines[1:]
            output.append('\\begin{evidencebox}')
            output.append(f'{{\\normalfont\\bfseries {escape_and_process(header)}}}\\\\[3pt]')
            for bl in body:
                if bl.strip():
                    output.append(escape_and_process(bl) + '\\par')
            output.append('\\end{evidencebox}')
        in_evidence = False
        evidence_lines = []

    def flush_pullquote():
        nonlocal in_pullquote, pullquote_lines
        if in_pullquote and pullquote_lines:
            text = ' '.join(l.strip() for l in pullquote_lines if l.strip())
            # Remove surrounding ** if present
            text = re.sub(r'^\*\*(.+)\*\*$', r'\1', text.strip())
            output.append('\\begin{pullquotebox}')
            output.append(escape_and_process(text))
            output.append('\\end{pullquotebox}')
        in_pullquote = False
        pullquote_lines = []

    # Track if we already emitted the title page section (skip H1 and H2 title)
    title_skipped = False
    subtitle_skipped = False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # ── Code blocks ─────────────────────────────────────────────────────
        if stripped.startswith('```'):
            if in_code_block:
                output.append('\\end{verbatim}')
                in_code_block = False
            else:
                flush_list()
                flush_table()
                # For the ASCII diagram in Part IV, use a small verbatim
                output.append('\\begin{verbatim}')
                in_code_block = True
            i += 1
            continue

        if in_code_block:
            output.append(line)
            i += 1
            continue

        # ── Tables ──────────────────────────────────────────────────────────
        if stripped.startswith('|') and '|' in stripped[1:]:
            flush_list()
            table_rows.append(stripped)
            collecting_table = True
            i += 1
            continue
        elif collecting_table:
            flush_table()

        # ── Horizontal rules ─────────────────────────────────────────────────
        if stripped in ('---', '***', '___') or re.match(r'^-{3,}$', stripped):
            flush_list()
            flush_vignette()
            flush_evidence()
            flush_pullquote()
            output.append('')
            i += 1
            continue

        # ── Images ───────────────────────────────────────────────────────────
        img_match = re.match(r'^!\[([^\]]*)\]\(([^)]+)\)', stripped)
        if img_match:
            flush_list()
            alt = img_match.group(1)
            path = img_match.group(2)
            key = detect_image_key(alt, path)
            if key:
                output.append(figure_for_key(key))
            else:
                output.append(f'% [Image not found: {alt}]')
            i += 1
            continue

        # ── Headings ─────────────────────────────────────────────────────────
        h_match = re.match(r'^(#{1,4})\s+(.+)$', stripped)
        if h_match:
            flush_list()
            flush_vignette()
            flush_evidence()
            flush_pullquote()
            level = len(h_match.group(1))
            title_text = h_match.group(2).strip()

            # Skip the document title (H1) and subtitle (H2 "Model and Clinical...")
            if level == 1 and not title_skipped:
                title_skipped = True
                i += 1
                continue
            if level == 2 and not subtitle_skipped and 'Model and Clinical Application' in title_text:
                subtitle_skipped = True
                i += 1
                continue

            # Detect "Part X. Title" pattern at H3 or H2 for part breaks
            part_match = re.match(r'^Part\s+(I{1,3}V?|V?I{0,3}|[IVX]+)\.\s+(.+)$', title_text)
            if level == 3 and part_match:
                # Look ahead for the italic orientation text
                orientation = ''
                if i + 1 < len(lines):
                    next_stripped = lines[i + 1].strip()
                    # Often next line is blank, then the italic line
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
                else:
                    i += 1

                part_label = part_match.group(1)
                part_title = part_match.group(2)
                orientation_escaped = escape_and_process(orientation) if orientation else ''
                output.append(f'\n\\partbreak{{Part {part_label}. {escape_and_process(part_title)}}}{{{orientation_escaped}}}')
                continue

            # Section heading mapping
            escaped_title = escape_and_process(title_text)
            # Add section mark for fancy header
            if level == 1:
                output.append(f'\n\\section{{{escaped_title}}}')
                output.append(f'\\markboth{{{escaped_title}}}{{{escaped_title}}}')
            elif level == 2:
                # Check if it's a Part heading at H2 level
                part_match2 = re.match(r'^Part\s+(I{1,3}V?|V?I{0,3}|[IVX]+)\.\s+(.+)$', title_text)
                if part_match2:
                    part_label = part_match2.group(1)
                    part_title = part_match2.group(2)
                    output.append(f'\n\\section{{Part {part_label}. {escape_and_process(part_title)}}}')
                    output.append(f'\\markboth{{Part {part_label}. {escape_and_process(part_title)}}}{{Part {part_label}}}')
                else:
                    output.append(f'\n\\section{{{escaped_title}}}')
                    output.append(f'\\markboth{{{escaped_title}}}{{{escaped_title}}}')
            elif level == 3:
                output.append(f'\n\\subsection{{{escaped_title}}}')
            elif level == 4:
                output.append(f'\n\\subsubsection{{{escaped_title}}}')
            i += 1
            continue

        # ── Blockquotes ──────────────────────────────────────────────────────
        if stripped.startswith('>'):
            flush_list()
            content = re.sub(r'^>\s?', '', stripped)

            # Clinical vignette detection
            if re.match(r'\*\*Clinical Observation', content):
                flush_pullquote()
                flush_evidence()
                in_vignette = True
                # Extract header text
                header = re.sub(r'\*\*(.+?)\*\*', r'\1', content)
                vignette_lines = [header]
                i += 1
                continue

            if in_vignette:
                if not stripped or stripped == '>':
                    # blank blockquote line = paragraph break within vignette
                    vignette_lines.append('')
                else:
                    inner = re.sub(r'^>\s?', '', stripped)
                    # italic lines: *text* -> just text (it will be italic via vignetteinner)
                    inner = re.sub(r'^\*(.+)\*$', r'\1', inner.strip())
                    vignette_lines.append(inner)
                i += 1
                continue

            # Evidence snapshot detection
            if re.match(r'\*\*Evidence Snapshot', content):
                flush_pullquote()
                in_evidence = True
                header = re.sub(r'\*\*(.+?)\*\*', r'\1', content)
                evidence_lines = [header]
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

            # Pull quote: bold text inside blockquote
            # Start a pull quote
            if not in_pullquote:
                flush_evidence()
                in_pullquote = True
                pullquote_lines = [content]
            else:
                pullquote_lines.append(content)
            i += 1
            continue

        # If we were in a blockquote-type block and hit a non-blockquote line
        if in_vignette:
            flush_vignette()
        if in_evidence:
            flush_evidence()
        if in_pullquote:
            flush_pullquote()

        # ── Bullet lists ─────────────────────────────────────────────────────
        bullet_match = re.match(r'^[-*•]\s+(.+)$', stripped)
        if bullet_match:
            if not in_itemize:
                flush_list()
                output.append('\\begin{itemize}')
                in_itemize = True
            item_text = escape_and_process(bullet_match.group(1))
            output.append(f'\\item {item_text}')
            i += 1
            continue

        # Numbered lists
        num_match = re.match(r'^(\d+)\.\s+(.+)$', stripped)
        if num_match and not re.match(r'^\d{4}', stripped):  # avoid matching years
            if not in_enumerate:
                flush_list()
                output.append('\\begin{enumerate}')
                in_enumerate = True
            item_text = escape_and_process(num_match.group(2))
            output.append(f'\\item {item_text}')
            i += 1
            continue

        # Sub-bullets (indented)
        sub_bullet = re.match(r'^\s{2,}[-*]\s+(.+)$', line)
        if sub_bullet:
            if not in_itemize:
                output.append('\\begin{itemize}')
                in_itemize = True
            item_text = escape_and_process(sub_bullet.group(1))
            output.append(f'\\item {item_text}')
            i += 1
            continue

        # Bullet with special chars (•, ·)
        bullet2 = re.match(r'^[•·]\s+(.+)$', stripped)
        if bullet2:
            if not in_itemize:
                flush_list()
                output.append('\\begin{itemize}')
                in_itemize = True
            item_text = escape_and_process(bullet2.group(1))
            output.append(f'\\item {item_text}')
            i += 1
            continue

        # End lists on blank or non-list line
        if not stripped:
            flush_list()
            output.append('')
            i += 1
            continue

        # ── Footnote definitions ──────────────────────────────────────────────
        footnote_match = re.match(r'^\[\^([^\]]+)\]:\s*(.+)$', stripped)
        if footnote_match:
            # Convert to LaTeX \footnote — but we'll just put it as a margin note
            fn_text = escape_and_process(footnote_match.group(2))
            output.append(f'\\footnotetext{{{fn_text}}}')
            i += 1
            continue

        # Remove inline footnote refs
        stripped = re.sub(r'\[\^[^\]]+\]', '', stripped)

        # ── Regular paragraph text ────────────────────────────────────────────
        flush_list()
        text = escape_and_process(stripped)
        output.append(text + '\n')
        i += 1

    # Flush any remaining open blocks
    flush_list()
    flush_vignette()
    flush_evidence()
    flush_pullquote()
    if collecting_table:
        flush_table()

    return '\n'.join(output)


def insert_graphics_at_sections(latex_body):
    """Insert graphics at appropriate section markers.

    Uses line-by-line approach to avoid breaking mid-command.
    Each tuple is (keyword_in_section_line, figure_key).
    The figure is inserted on the line AFTER the complete section line.
    """
    # Map of substring to search for in a \section or \subsection line -> figure key
    insertions = [
        ('Executive Summary', 'summary-infographic'),
        ('Part I. From Principle', 'concept-map'),
        ('The Clinical Distinction', 'not-about'),
        ('Clinical Observations', 'clinical-flowchart'),
        ('Part II. The NeuroSpinal System', 'meningeal-anatomy'),
        ('Part IV. Pathophysiology', 'five-ds-cascade'),
        ('Why Precision Matters', 'upstream'),
        ('Part V. TTC Analysis', 'contact-params'),
        ('Part VI. From Bone-on-Nerve', 'timeline'),
        ('Part VII. Historical Lineage', 'technique-table'),
        ('Part X. Epilogue', 'guitar'),
    ]

    lines = latex_body.split('\n')
    result = []
    inserted = set()

    for line in lines:
        result.append(line)
        # Check if this line contains a section/subsection command
        if any(cmd in line for cmd in (r'\section{', r'\subsection{', r'\subsubsection{', r'\partbreak{')):
            for keyword, fig_key in insertions:
                if keyword in line and fig_key not in inserted:
                    fig = figure_for_key(fig_key)
                    if fig:
                        result.append(fig)
                        inserted.add(fig_key)
                    break

    return '\n'.join(result)


def post_process(latex_body):
    """Additional post-processing fixes."""
    # Fix double-escaped items that sneak through
    latex_body = latex_body.replace(r'\textbackslash{}textbf{', r'\textbf{')
    latex_body = latex_body.replace(r'\textbackslash{}textit{', r'\textit{')
    latex_body = latex_body.replace(r'\textbackslash{}section{', r'\section{')
    latex_body = latex_body.replace(r'\textbackslash{}subsection{', r'\subsection{')

    # Remove duplicate blank lines (more than 2 consecutive)
    latex_body = re.sub(r'\n{4,}', '\n\n\n', latex_body)

    # Remove decorative ### sub-headings that appear immediately before ## real sections
    # These appear as \subsection{X} + orientation text + \section{X}
    # For "First Principles": remove the subsection and italic text, keep the section
    latex_body = re.sub(
        r'\\subsection\{First Principles\}[\s\S]{0,400}?\\section\{First Principles\}',
        r'\\section{First Principles}',
        latex_body,
        count=1
    )

    # The DD Palmer opening quote is already on the title page — remove the pull quote version
    # that appears before the Executive Summary section
    latex_body = re.sub(
        r'\\begin\{pullquotebox\}[\s\S]{0,200}?(?:Life is an expression|expression of tone)[\s\S]{0,200}?\\end\{pullquotebox\}',
        '',
        latex_body,
        count=1
    )

    # Fix Part break that appears both as partbreak AND as section
    # The document has "### Part X" (decorative) followed by "## Part X" (real section)
    # After processing, we may get both a \partbreak and a \section for the same part
    # Keep the \section and remove the \partbreak that precedes it for the same part

    def remove_duplicate_partbreaks(text):
        # Find all \partbreak occurrences and check if they're immediately followed by \section of same content
        parts = re.split(r'(\\partbreak\{[^}]+\}\{[^}]*\})', text)
        result = []
        skip_next_section = False
        for j, part in enumerate(parts):
            if re.match(r'\\partbreak\{', part):
                # Check what comes after
                after = parts[j + 1] if j + 1 < len(parts) else ''
                # Extract the part title from partbreak
                pb_match = re.match(r'\\partbreak\{(.+?)\}\{', part, re.DOTALL)
                if pb_match:
                    pb_title = pb_match.group(1)
                    # Check if the next section has the same content
                    sec_match = re.search(r'\\section\{' + re.escape(pb_title) + r'\}', after[:500])
                    if sec_match:
                        # Duplicate - keep partbreak, section will stand on its own page
                        # Actually let's keep partbreak and remove the duplicate section title
                        result.append(part)
                        continue
                result.append(part)
            else:
                result.append(part)
        return ''.join(result)

    # Don't try to be clever - just fix known issues
    # The "First Principles" part break should precede the section
    # Fix \markboth calls that have unescaped special chars
    latex_body = re.sub(r'\\markboth\{[^}]*\}\{[^}]*\}', '', latex_body)

    # Remove the second occurrence of the opening DD Palmer quote (it's on title page)
    # The pull quote starting with "Life is" near the top
    # (already handled above with regex)

    return latex_body


def main():
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        md_text = f.read()

    print(f"Read {len(md_text)} chars from {INPUT_FILE}")

    body = convert_markdown_to_latex(md_text)
    body = insert_graphics_at_sections(body)
    body = post_process(body)

    full_doc = LATEX_PREAMBLE + body + LATEX_POSTAMBLE

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(full_doc)

    print(f"Wrote {len(full_doc)} chars to {OUTPUT_FILE}")
    print("Done! Run: cd renditions && tectonic ttc-paper.tex")


if __name__ == '__main__':
    main()
