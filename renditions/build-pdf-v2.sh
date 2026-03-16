#!/bin/sh
# =============================================================================
# TTC White Paper — PDF Build Script v2
# Produces a production-quality PDF with embedded graphics and enhanced styling.
#
# Usage: bash renditions/build-pdf-v2.sh
# Output: renditions/TTC-White-Paper-v2.pdf
# =============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

SOURCE_MD="$REPO_DIR/renditions/09_2026-03-16_STRUCTURAL_VISUAL_REDESIGN.md"
CSS="$REPO_DIR/renditions/ttc-paper-v2.css"
OUTPUT_PDF="$REPO_DIR/renditions/TTC-White-Paper-v2.pdf"
GRAPHICS_DIR="$REPO_DIR/visual-production/output"
WORK_DIR="$(mktemp -d)"

# Cleanup on exit
cleanup() { rm -rf "$WORK_DIR"; }
trap cleanup EXIT

echo "=== TTC White Paper PDF Builder v2 ==="
echo "Working directory: $WORK_DIR"
echo ""

# ── Verify dependencies ────────────────────────────────────────────────────
echo "Checking dependencies..."

if ! command -v pandoc >/dev/null 2>&1; then
  echo "ERROR: pandoc not found. Install with: brew install pandoc"
  exit 1
fi
echo "  pandoc: $(pandoc --version | head -1)"

if command -v weasyprint >/dev/null 2>&1; then
  RENDERER="weasyprint"
  echo "  renderer: weasyprint ($(weasyprint --version 2>&1 | head -1))"
elif command -v wkhtmltopdf >/dev/null 2>&1; then
  RENDERER="wkhtmltopdf"
  echo "  renderer: wkhtmltopdf"
else
  echo "ERROR: Neither weasyprint nor wkhtmltopdf found."
  exit 1
fi

echo ""

# ── Use Python for all heavy lifting (graphics injection + PDF build) ──────
echo "Running build pipeline..."

python3 - "$SOURCE_MD" "$WORK_DIR" "$CSS" "$OUTPUT_PDF" "$GRAPHICS_DIR" "$RENDERER" <<'PYEOF'
import sys
import os
import subprocess
import shutil

source_path  = sys.argv[1]
work_dir     = sys.argv[2]
css_path     = sys.argv[3]
output_pdf   = sys.argv[4]
graphics_dir = sys.argv[5]
renderer     = sys.argv[6]

work_md   = os.path.join(work_dir, "paper-with-graphics.md")
work_html = os.path.join(work_dir, "paper.html")

# ── Graphic selection (key -> source path) ────────────────────────────────
GRAPHIC_SELECTIONS = {
    "18-dd-palmer-quote":   "18-dd-palmer-quote/18-dd-palmer-a-typographic.png",
    "01-concept-map":       "01-concept-map/01-concept-map-a-split-v2.png",
    "10-said-tone":         "10-said-tone-adjusted-bones/10-said-tone-b-bridge.png",
    "05-meningeal-anatomy": "05-meningeal-anatomy/05-meningeal-anatomy-a-four-panel-v2.png",
    "17-layers":            "17-layers-of-compensation/17-layers-a-concentric.png",
    "09-five-ds-cascade":   "09-five-ds-cascade/09-five-ds-cascade-c-threat-to-release.png",
    "04-mechanotransduction":"04-mechanotransduction/04-mechanotransduction-a-horizontal.png",
    "14-safety-signal":     "14-safety-signal-trap/14-safety-signal-a-circular.png",
    "19-upstream-insight":  "19-upstream-insight/19-upstream-b-reveal.png",
    "15-contact-params":    "15-contact-parameters/15-contact-params-a-silhouette.png",
    "03-clinical-flowchart":"03-clinical-flowchart/03-clinical-flowchart-a-parallel-v2.png",
    "16-force-noise":       "16-force-noise/16-force-noise-a-waveform.png",
    "07-timeline":          "07-timeline/07-timeline-a-horizontal.png",
    "13-anesthesia":        "13-anesthesia-finding/13-anesthesia-a-split.png",
    "06-technique-table":   "06-technique-table/06-technique-table-a-four-column.png",
    "11-not-about":         "11-not-about/11-not-about-a-two-column.png",
    "02-outcome-variance":  "02-outcome-variance/02-outcome-variance-a-stacked-bar-v2.png",
    "08-summary-infographic":"08-summary-infographic/08-summary-infographic-c-paradigm-shift.png",
    "12-guitar":            "12-guitar-metaphor/12-guitar-a-instrument.png",
}

# Copy graphics to work dir
print("Copying graphics to work directory...")
for key, rel_path in GRAPHIC_SELECTIONS.items():
    src = os.path.join(graphics_dir, rel_path)
    dst = os.path.join(work_dir, key + ".png")
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"  OK: {key}")
    else:
        print(f"  WARN: missing {src}")
print()

# ── Build graphic insertion blocks ────────────────────────────────────────
def img_block(key, caption=None):
    """Return markdown lines for a figure block."""
    img_path = os.path.join(work_dir, key + ".png")
    lines = ["\n"]
    if caption:
        lines.append(f'![{caption}]({img_path})\n')
        lines.append(f'\n_{caption}_\n')
    else:
        lines.append(f'![]({img_path})\n')
    lines.append("\n")
    return lines

# ── Read source markdown ──────────────────────────────────────────────────
with open(source_path, 'r') as f:
    lines = f.readlines()

output_lines = []
i = 0
n = len(lines)

# Insertion state
inserted = {k: False for k in [
    'epigraph', 'concept_map', 'said_tone', 'meningeal',
    'layers', 'five_ds', 'mechanotransduction', 'safety_signal',
    'upstream', 'contact_params', 'flowchart', 'force_noise',
    'timeline', 'anesthesia', 'technique_table', 'not_about',
    'outcome_variance', 'summary_infographic', 'guitar'
]}

print("Inserting graphics into markdown...")

while i < n:
    line = lines[i]
    s = line.strip()

    # 18. DD Palmer epigraph — after the closing --- that follows the epigraph block
    if not inserted['epigraph']:
        if s.startswith('> *"Life is an expression of tone'):
            # Emit this line and look for the end of the epigraph --- block
            output_lines.append(line)
            i += 1
            while i < n:
                output_lines.append(lines[i])
                if lines[i].strip() == '---':
                    i += 1
                    break
                i += 1
            output_lines += img_block('18-dd-palmer-quote',
                'D.D. Palmer: "Life is an expression of tone" (1910)')
            inserted['epigraph'] = True
            continue

    # 10. Said tone adjusted bones — after the Part I pull quote
    if not inserted['said_tone']:
        if ('We said' in s and 'tone' in s and 'bones' in s and s.startswith('> **"')):
            output_lines.append(line)
            i += 1
            output_lines += img_block('10-said-tone',
                '"We Said Tone, Adjusted Bones" — the gap between chiropractic philosophy and practice')
            inserted['said_tone'] = True
            continue

    # 01. Concept map — after "Bone-First Model Struggles to Explain" heading
    if not inserted['concept_map']:
        if 'Bone-First Model Struggles to Explain' in s:
            output_lines.append(line)
            i += 1
            output_lines += img_block('01-concept-map',
                'Figure 1. Bone-first vs. tension-first — what each model can and cannot explain')
            inserted['concept_map'] = True
            continue

    # 05. Meningeal anatomy — after "Structural Composition" heading
    if not inserted['meningeal']:
        if s == '### Structural Composition':
            output_lines.append(line)
            i += 1
            output_lines += img_block('05-meningeal-anatomy',
                'Figure 2. The NeuroSpinal System — structural anatomy and clinically significant dural attachments')
            inserted['meningeal'] = True
            continue

    # 17. Layers of compensation — after "Why Precision Matters" heading
    if not inserted['layers']:
        if 'Why Precision Matters' in s and s.startswith('####'):
            output_lines.append(line)
            i += 1
            output_lines += img_block('17-layers',
                'Figure 3. Layered architecture of compensatory tension around the primary NeuroSpinal restriction')
            inserted['layers'] = True
            continue

    # 09. Five D's cascade — after "The Cascade of Dysfunction" heading
    if not inserted['five_ds']:
        if 'Cascade of Dysfunction' in s and s.startswith('####'):
            output_lines.append(line)
            i += 1
            output_lines += img_block('09-five-ds-cascade',
                'Figure 4. The 5 D\'s cascade — from aberrant NeuroSpinal tone to degeneration')
            inserted['five_ds'] = True
            continue

    # 04. Mechanotransduction — after the Mechanobiology paragraph (end of block)
    if not inserted['mechanotransduction']:
        if s.startswith('**Mechanobiology:**') and 'TGF' in line:
            output_lines.append(line)
            i += 1
            # consume the whole paragraph
            while i < n and lines[i].strip() != '':
                output_lines.append(lines[i])
                i += 1
            output_lines += img_block('04-mechanotransduction',
                'Figure 5. Mechanotransduction pathway — from sustained load to myofibroblast conversion')
            inserted['mechanotransduction'] = True
            continue

    # 14. Safety signal trap — after "Why the Contracture Persists" heading
    if not inserted['safety_signal']:
        if 'Why the Contracture Persists' in s and s.startswith('####'):
            output_lines.append(line)
            i += 1
            output_lines += img_block('14-safety-signal',
                'Figure 6. The safety-signal trap — movement restriction prevents the signal needed for release')
            inserted['safety_signal'] = True
            continue

    # 19. Upstream insight — after "The Sequence: From Threat to Release" heading
    if not inserted['upstream']:
        if 'The Sequence: From Threat to Release' in s:
            output_lines.append(line)
            i += 1
            output_lines += img_block('19-upstream-insight',
                'Figure 7. The upstream insight — aberrant NeuroSpinal tone precedes the 5 D\'s cascade')
            inserted['upstream'] = True
            continue

    # 15. Contact parameters — after "5.3 Contact Parameters" heading
    if not inserted['contact_params']:
        if '5.3 Contact Parameters' in s and s.startswith('###'):
            output_lines.append(line)
            i += 1
            output_lines += img_block('15-contact-params',
                'Figure 8. TTC contact parameters: location, vector, amount, and intent')
            inserted['contact_params'] = True
            continue

    # 03. Clinical flowchart — after "5.2 Tonal Analysis" heading
    if not inserted['flowchart']:
        if '5.2 Tonal Analysis' in s and s.startswith('###'):
            output_lines.append(line)
            i += 1
            output_lines += img_block('03-clinical-flowchart',
                'Figure 9. Traditional vs. tension-first clinical decision pathway')
            inserted['flowchart'] = True
            continue

    # 16. Force noise — after "Why Force Isn't the Language of Change" heading
    if not inserted['force_noise']:
        if "Why Force Isn" in s and 'Language of Change' in s:
            output_lines.append(line)
            i += 1
            output_lines += img_block('16-force-noise',
                'Figure 10. Force vs. information — in a signal-regulated system, more force equals more noise')
            inserted['force_noise'] = True
            continue

    # 07. Timeline — at the start of Part VI body
    if not inserted['timeline']:
        if s == '## Part VI. From Bone-on-Nerve to Tone-First: Historical Evolution':
            output_lines.append(line)
            i += 1
            output_lines += img_block('07-timeline',
                'Figure 11. Historical evolution — from D.D. Palmer\'s tone principle to Talsky Tonal Chiropractic')
            inserted['timeline'] = True
            continue

    # 13. Anesthesia finding — after "The mechanism parallels the flexibility phenomenon"
    if not inserted['anesthesia']:
        if 'mechanism parallels the flexibility phenomenon' in s:
            output_lines.append(line)
            i += 1
            output_lines += img_block('13-anesthesia',
                'Figure 12. Ward\'s anesthesia finding — range of motion doubles under anesthesia, revealing neural not structural limitation')
            inserted['anesthesia'] = True
            continue

    # 06. Technique table — after "7.5 The Technique Landscape" heading
    if not inserted['technique_table']:
        if '7.5 The Technique Landscape' in s and s.startswith('###'):
            output_lines.append(line)
            i += 1
            output_lines += img_block('06-technique-table',
                'Figure 13. The chiropractic technique landscape — osseous, OsseoTonal, tonal, and tonal energetics')
            inserted['technique_table'] = True
            continue

    # 11. Not about / paradigm shift — after "The Clinical Distinction" heading
    if not inserted['not_about']:
        if s == '### The Clinical Distinction':
            output_lines.append(line)
            i += 1
            output_lines += img_block('11-not-about',
                'Figure 14. The paradigm shift — from finding fixations to finding receptivity')
            inserted['not_about'] = True
            continue

    # 02. Outcome variance — after Clinical Observation 3 full block ends (---)
    if not inserted['outcome_variance']:
        if s.startswith('> **Clinical Observation 3'):
            # emit observation 3 and everything until ---
            output_lines.append(line)
            i += 1
            while i < n:
                output_lines.append(lines[i])
                if lines[i].strip() == '---':
                    i += 1
                    break
                i += 1
            output_lines += img_block('02-outcome-variance',
                'Figure 15. Clinical outcome variance — why identical presentations produce different results')
            inserted['outcome_variance'] = True
            continue

    # 08. Summary infographic — just BEFORE "Part X. Epilogue" heading
    if not inserted['summary_infographic']:
        if s == '## Part X. Epilogue: The Self-Tuning Guitar':
            output_lines += img_block('08-summary-infographic',
                'Figure 16. TTC paradigm shift summary — the full model at a glance')
            inserted['summary_infographic'] = True
            # fall through to emit the heading too

    # 12. Guitar metaphor — after the "self-tuning guitar" paragraph
    if not inserted['guitar']:
        if 'self-tuning guitar' in s.lower() and 'advanced AI' in line:
            output_lines.append(line)
            i += 1
            # consume the rest of the paragraph
            while i < n and lines[i].strip() != '' and not lines[i].strip().startswith('>'):
                output_lines.append(lines[i])
                i += 1
            output_lines += img_block('12-guitar',
                'Figure 17. The self-tuning guitar — the NeuroSpinal System\'s inherent intelligence')
            inserted['guitar'] = True
            continue

    output_lines.append(line)
    i += 1

# Report
total = sum(inserted.values())
print(f"  Inserted {total}/{len(inserted)} graphics")
missing = [k for k, v in inserted.items() if not v]
if missing:
    print(f"  Not found (section marker not matched): {missing}")

# Write work markdown
with open(work_md, 'w') as f:
    f.writelines(output_lines)

print(f"  Work markdown: {work_md}")
print(f"  Lines: {len(output_lines)}")
print()

# ── Convert Markdown → HTML with pandoc ──────────────────────────────────
print("Converting Markdown → HTML with pandoc...")
pandoc_cmd = [
    "pandoc",
    work_md,
    "--from", "markdown",
    "--to", "html5",
    "--standalone",
    "--css", css_path,
    "--toc",
    "--toc-depth=2",
    "--section-divs",
    "--metadata", "title=The NeuroSpinal System as the Primary Tone-Setter",
    "--metadata", "author=Dr. Zach Conner",
    "--metadata", "date=2026",
    "--output", work_html,
]

result = subprocess.run(pandoc_cmd, capture_output=True, text=True)
if result.returncode != 0:
    print("  pandoc stderr:", result.stderr[:2000])
    sys.exit(1)

html_size = os.path.getsize(work_html)
print(f"  HTML written: {work_html}")
print(f"  HTML size: {html_size/1024:.0f} KB")
print()

# ── Convert HTML → PDF ───────────────────────────────────────────────────
print(f"Converting HTML → PDF with {renderer}...")

if renderer == "weasyprint":
    cmd = ["weasyprint", work_html, output_pdf, "--stylesheet", css_path]
elif renderer == "wkhtmltopdf":
    cmd = [
        "wkhtmltopdf",
        "--page-size", "Letter",
        "--margin-top", "1in",
        "--margin-bottom", "1.1in",
        "--margin-left", "1in",
        "--margin-right", "1in",
        "--footer-center", "[page]",
        "--footer-font-size", "9",
        "--enable-local-file-access",
        work_html,
        output_pdf,
    ]

result = subprocess.run(cmd, capture_output=True, text=True)
# weasyprint writes warnings to stderr but still succeeds
if result.returncode != 0:
    print("  STDERR:", result.stderr[:3000])
    sys.exit(1)

if result.stderr:
    # Show first few lines of any warnings
    warn_lines = [l for l in result.stderr.strip().split('\n') if l.strip()][:10]
    for wl in warn_lines:
        print(f"  warn: {wl}")

if os.path.exists(output_pdf):
    size_kb = os.path.getsize(output_pdf) / 1024
    print(f"  PDF written: {output_pdf}")
    print(f"  PDF size: {size_kb:.0f} KB ({size_kb/1024:.1f} MB)")
else:
    print("ERROR: PDF not produced!")
    sys.exit(1)

PYEOF

echo ""

# ── Report ─────────────────────────────────────────────────────────────────
if [ -f "$OUTPUT_PDF" ]; then
  echo "=== Build complete ==="
  echo "Output: $OUTPUT_PDF"

  # Page count via pdfinfo if available
  if command -v pdfinfo >/dev/null 2>&1; then
    PAGES=$(pdfinfo "$OUTPUT_PDF" 2>/dev/null | grep "^Pages:" | awk '{print $2}')
    echo "Pages: $PAGES"
  fi
else
  echo "ERROR: PDF not produced."
  exit 1
fi
