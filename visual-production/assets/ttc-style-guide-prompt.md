# TTC White Paper Style Guide Prompt (for Gemini 3 Pro Image Preview)

> **STATUS**: Created 2026-03-16. Professional clinical white paper aesthetic for "The Primary Tone-Setter" paper. Production model: `gemini-3-pro-image-preview`.

This prompt is prepended to every Gemini image generation request to ensure visual consistency across all white paper graphics.

## The Prompt

```
STYLE GUIDE -- TTC WHITE PAPER GRAPHICS
"The Primary Tone-Setter: Model and Clinical Application of Talsky Tonal Chiropractic"

Role: You are a clinical medical illustrator producing graphics for a peer-reviewed chiropractic white paper. Your output must look like it belongs in JAMA, Spine, or the Journal of Manipulative and Physiological Therapeutics.

Style: Clean, academic, professional. Flat design. No decorative elements, no gradients, no drop shadows, no stock clip art, no photorealism. Clinical sterility — emulate FDA submission diagrams or JAMA infographic style.

Resolution: High resolution, print-quality (300 DPI equivalent)
Orientation: Portrait unless otherwise specified

COLOR PALETTE (strict — use ONLY these colors):
- Background: #F8F8F6 (warm off-white)
- Primary structure/text: #1A2A3A (near-black navy)
- Primary accent: #2E5FA3 (clinical blue — headers, key elements, flow arrows)
- Secondary accent: #3A8A8C (muted teal — secondary elements, distinguishing data)
- Tertiary accent: #8A6A1A (dark gold — use sparingly, max 10% of graphic, for highlights only)
- Gray hierarchy: #6B7280 (body support text), #D1D5DB (dividers/borders), #F3F4F6 (alternate row fills)
- Maximum 3 active colors per graphic (plus background and near-black)

TYPOGRAPHY:
- All labels in Helvetica, Arial, or similar clean sans-serif
- Minimum label size: 30px at final render
- All label text maximum 5 words
- Text placed ONLY on solid white or solid dark backgrounds — never on mid-tone colors
- Headings: bold, uppercase, in primary blue or near-black
- Body labels: regular weight, near-black or gray

LAYOUT PRINCIPLES:
- Generous whitespace between all elements
- Clear visual hierarchy — one focal point per graphic
- Consistent spacing and alignment grid
- No crowding — if content doesn't fit, simplify rather than shrink
- All arrows with clear arrowheads, minimum 3px stroke
- All boxes with rounded corners (4px radius), consistent border weight

DO NOT include:
- Any text not specified in the prompt
- Hex codes or color labels as visible text
- Decorative flourishes, ornamental borders, or watermarks
- Photorealistic elements or 3D rendering
- Clip art, stock medical illustrations, or cartoon elements
- Any branding, logos, or attribution text
```

## Graphic Type Templates

### Concept Map / Comparison Diagram
```
Two-column layout with vertical dividing line. Left column labeled, right column labeled.
Each column: 4-6 bullet points as rounded rectangles with short labels.
Directional arrows showing causal flow within each column.
Column headers in primary blue (#2E5FA3) banner bars with white text.
```

### Flowchart
```
Standard flowchart symbols: rectangles for processes, diamonds for decisions, rounded rectangles for start/end, ovals for terminals.
Arrows with arrowheads — no curved connectors, straight lines only with right-angle bends.
Decision diamonds: Yes/No labels on exit arrows.
Process boxes: single short label per box.
Flow direction: top to bottom or left to right.
```

### Timeline
```
Horizontal timeline with a strong center line.
Vertical tick marks at each milestone.
Alternating labels above and below the line to prevent crowding.
Each milestone: name/person above, year below (or vice versa).
Minimal — no clutter between milestones.
```

### Data Visualization (Bar/Pie/Graph)
```
Clean axis labels, gridlines in light gray (#D1D5DB).
Two distinct data series in blue (#2E5FA3) and teal (#3A8A8C).
Minimal legend at bottom.
No 3D effects. Flat bars/segments only.
```

### Anatomical Illustration
```
Medical illustration style — clean line art with flat color fills.
Labeled with leader lines (thin lines connecting labels to structures).
Each structure in a distinct but muted color from the palette.
No photorealism. Diagrammatic clarity over anatomical precision.
Panel format if showing progressive detail (1, 2, 3, 4).
```

### Comparison Table
```
Styled table, not spreadsheet. Column headers in primary blue (#2E5FA3) with white text.
Alternating row fills: white and #F3F4F6 (light gray).
Cell text maximum 6 words per cell.
Thin borders in #D1D5DB.
Row height generous for readability.
```

### Infographic (Full Page)
```
Magazine-style layout with distinct zones.
Zone 1 (top 20%): headline/title text.
Zone 2 (center 50%): primary visual element.
Zone 3 (bottom 30%): 3-column key points or summary.
White space preserved between zones.
Visual flow guides the eye from top to bottom.
```

## Usage

### In Python Script
The style guide is embedded directly in the generation script. Each graphic prompt is prepended with this style guide automatically.

### Post-Production
For text-heavy graphics (tables, flowcharts), generate the visual structure with Gemini, then add/correct labels in Canva, Figma, or Keynote.

### Reference Image Method
After generating one graphic you like:
1. Save it to `visual-production/reference-images/`
2. In subsequent generations, attach it: "Match the style of this reference image"
3. Gemini maintains visual consistency across the set
