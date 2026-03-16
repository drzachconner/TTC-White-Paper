#!/usr/bin/env python3
"""Generate TTC White Paper graphics using Gemini 3 Pro Image Preview (Nano Banana 2 Pro).

Usage:
    # Generate all graphics:
    python generate-graphics.py

    # Generate a specific graphic by number (1-8):
    python generate-graphics.py 3

    # Generate a range:
    python generate-graphics.py 1 4

    # Generate a specific variation only:
    python generate-graphics.py --graphic 3 --variation b

Prerequisites:
    export GEMINI_API_KEY=$(op item get 'Google Gemini API' --fields 'credential' --reveal)
"""

import base64
import json
import os
import sys
import time
import urllib.request
import urllib.error

API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError(
        "Set GEMINI_API_KEY before running.\n"
        "  export GEMINI_API_KEY=$(op item get 'Google Gemini API' --fields 'credential' --reveal)"
    )
MODEL = "gemini-3-pro-image-preview"
ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

OUTPUT_BASE = "/Users/zachconnermba/Code/TTC-White-Paper/visual-production/output"
REFERENCE_DIR = "/Users/zachconnermba/Code/TTC-White-Paper/visual-production/reference-images"

# ─── TTC WHITE PAPER STYLE GUIDE ───────────────────────────────────────────────

STYLE_GUIDE = """STYLE GUIDE -- TTC WHITE PAPER GRAPHICS
"The Primary Tone-Setter: Model and Clinical Application of Talsky Tonal Chiropractic"

Role: You are a clinical medical illustrator producing graphics for a peer-reviewed chiropractic white paper. Your output must look like it belongs in JAMA, Spine, or the Journal of Manipulative and Physiological Therapeutics.

Style: Clean, academic, professional. Flat design. No decorative elements, no gradients, no drop shadows, no stock clip art, no photorealism. Clinical sterility — emulate FDA submission diagrams or JAMA infographic style.

Resolution: High resolution, print-quality (300 DPI equivalent)

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

LAYOUT:
- Generous whitespace between all elements
- Clear visual hierarchy — one focal point per graphic
- No crowding — simplify rather than shrink
- All arrows with clear arrowheads, minimum 3px stroke
- All boxes with rounded corners (4px radius)

DO NOT include:
- Any text not specified in the prompt
- Hex codes or color labels as visible text
- Decorative flourishes, ornamental borders, or watermarks
- Photorealistic elements or 3D rendering
- Clip art, stock medical illustrations, or cartoon elements
- Any branding, logos, or attribution text"""

# ─── GRAPHIC DEFINITIONS ───────────────────────────────────────────────────────
# Each graphic has 2-3 variations for the author to choose from.

GRAPHICS = [
    # ═══════════════════════════════════════════════════════════════════════════
    # GRAPHIC 1: Bone-First vs. Tension-First Concept Map
    # ═══════════════════════════════════════════════════════════════════════════
    {
        "id": "01-concept-map",
        "title": "Bone-First vs. Tension-First Concept Map",
        "variations": [
            {
                "suffix": "a-split",
                "prompt": """GRAPHIC TYPE: Two-Column Concept Map (Portrait, full page)

Create a split comparison diagram with a bold vertical dividing line down the center.

LEFT COLUMN — Header banner: "BONE-FIRST PARADIGM" (blue #2E5FA3 banner, white text)
Show this downward cascade with arrows between each box:
1. "Joint Fixation" (top box)
2. "Nerve Compression" (arrow down)
3. "Neurological Deficit" (arrow down)
4. "Symptom / Dysfunction" (arrow down)
5. "Adjust Bone" (bottom box, teal #3A8A8C fill)

RIGHT COLUMN — Header banner: "TENSION-FIRST PARADIGM" (blue #2E5FA3 banner, white text)
Show this downward cascade with arrows between each box:
1. "Stress / Threat" (top box)
2. "Meningeal Contraction" (arrow down)
3. "Aberrant NeuroSpinal Tone" (arrow down)
4. "Compensatory Vertebral Patterns" (arrow down)
5. "Engage NeuroSpinal System" (bottom box, teal #3A8A8C fill)

Between the two columns at the bottom, add a horizontal arrow from RIGHT to LEFT labeled "upstream" to show that the tension-first model addresses the cause that leads to the bone-first model's starting point.

Use rounded rectangles for all boxes. Near-black (#1A2A3A) text. Warm off-white (#F8F8F6) background."""
            },
            {
                "suffix": "b-circular",
                "prompt": """GRAPHIC TYPE: Dual Circular Flow Diagram (Portrait, full page)

Create two circular flow diagrams side by side.

LEFT CIRCLE — Title above: "STRUCTURAL MODEL"
A circular loop with 4 nodes connected by curved arrows going clockwise:
- Top: "Fixation Found"
- Right: "Force Applied"
- Bottom: "Bone Moved"
- Left: "Repeat"
Center of circle: large "?" symbol in gray

RIGHT CIRCLE — Title above: "TTC MODEL"
A circular flow that OPENS into a spiral (not closed loop):
- Top: "Tone Assessed"
- Right: "Receptivity Found"
- Bottom: "Information Delivered"
- Left: spiral outward to "System Self-Corrects"
Center of circle: small icon of radiating waves

Between the two circles at the bottom, a single line of text: "From moving bones to engaging intelligence"

Blue (#2E5FA3) for arrows and headers. Teal (#3A8A8C) for the TTC spiral. Near-black text. Off-white background."""
            },
            {
                "suffix": "c-iceberg",
                "prompt": """GRAPHIC TYPE: Iceberg Diagram (Portrait, full page)

Create a classic iceberg diagram showing what's visible above the waterline vs. what's below.

ABOVE THE WATERLINE (labeled "WHAT WE SEE"):
- "Joint Fixation" (in a box)
- "Postural Shifts" (in a box)
- "Muscle Guarding" (in a box)

THE WATERLINE: A horizontal wavy blue line across the page, labeled "Surface" on the right edge

BELOW THE WATERLINE (labeled "WHAT DRIVES IT"):
- "Aberrant NeuroSpinal Tone" (largest box, teal fill)
- "Meningeal Contraction" (medium box below)
- "Threat Perception" (deepest box)
- Downward arrows connecting each, showing the deeper cause

Left side vertical text: "BONE-FIRST starts here" with arrow pointing to above waterline
Right side vertical text: "TENSION-FIRST starts here" with arrow pointing to below waterline

The iceberg shape should be a simple geometric triangle/trapezoid, not photorealistic. Blue (#2E5FA3) for the water area below the line. Off-white (#F8F8F6) above. Near-black text."""
            }
        ]
    },

    # ═══════════════════════════════════════════════════════════════════════════
    # GRAPHIC 2: Outcome Variance Visualization
    # ═══════════════════════════════════════════════════════════════════════════
    {
        "id": "02-outcome-variance",
        "title": "Outcome Variance Graph",
        "variations": [
            {
                "suffix": "a-stacked-bar",
                "prompt": """GRAPHIC TYPE: Stacked Bar Chart (Landscape, half page)

Create a clean stacked bar chart showing factors contributing to clinical outcomes.

Single horizontal stacked bar spanning the full width, divided into segments:
- Left segment (40%, blue #2E5FA3): labeled "Vertebral Position"
- Middle segment (35%, teal #3A8A8C): labeled "Fascial / Tonal Factors"
- Right segment (25%, dark gold #8A6A1A): labeled "Other Variables"

Above the bar: Title "WHAT EXPLAINS CLINICAL OUTCOMES?"

Below the bar, a callout arrow pointing to the teal segment with text: "Traditional models focus on the blue segment. TTC addresses the tonal factors that drive both."

Use flat color fills, no 3D. Thin gray borders between segments. Off-white background. Near-black text labels."""
            },
            {
                "suffix": "b-pie",
                "prompt": """GRAPHIC TYPE: Pie Chart with Callout (Landscape, half page)

Create a clean pie chart showing the components of clinical outcome variance.

Pie chart with 3 segments:
- 40% segment (blue #2E5FA3): "Vertebral Position"
- 35% segment (teal #3A8A8C): "NeuroSpinal Tone"
- 25% segment (gray #6B7280): "Other Factors"

The teal segment should be slightly "exploded" (pulled out from center by 10px) to draw attention.

A leader line from the teal segment to a callout box that reads: "Where TTC focuses"

Title above: "FACTORS IN CLINICAL OUTCOMES"

Flat design. No 3D. No shadow. Percentage labels inside each segment in white bold text. Off-white background."""
            },
            {
                "suffix": "c-conceptual-scale",
                "prompt": """GRAPHIC TYPE: Balance Scale Diagram (Portrait, half page)

Create a simple balance/seesaw diagram.

A horizontal beam balanced on a triangular fulcrum at center.

LEFT SIDE of beam (tilting down, heavier):
- Stack of 3 small boxes: "NeuroSpinal Tone", "Meningeal State", "Fascial Tension"
- Label below: "TONAL FACTORS"

RIGHT SIDE of beam (tilting up, lighter):
- Single box: "Vertebral Position"
- Label below: "STRUCTURAL FACTORS"

The beam tilts LEFT (tonal side is heavier/more influential).

Title above: "WHAT DRIVES CLINICAL OUTCOMES?"
Subtitle: "Traditional models address the lighter side. TTC addresses the heavier."

Blue (#2E5FA3) for the tonal boxes. Teal (#3A8A8C) for the structural box. Gray fulcrum. Off-white background."""
            }
        ]
    },

    # ═══════════════════════════════════════════════════════════════════════════
    # GRAPHIC 3: Clinical Decision Flowcharts
    # ═══════════════════════════════════════════════════════════════════════════
    {
        "id": "03-clinical-flowchart",
        "title": "Clinical Decision Flowcharts",
        "variations": [
            {
                "suffix": "a-parallel",
                "prompt": """GRAPHIC TYPE: Parallel Flowcharts (Portrait, full page)

Create two parallel vertical flowcharts side by side.

LEFT FLOWCHART — Title: "TRADITIONAL PATHWAY"
All in blue (#2E5FA3) outlines:
1. [Oval] "Patient Presents"
2. [Arrow down]
3. [Rectangle] "Palpate for Fixation"
4. [Arrow down]
5. [Diamond] "Fixation Found?"
6. [Arrow YES down] → [Rectangle] "Apply Force to Segment"
7. [Arrow down] → [Diamond] "Resolved?"
8. [Arrow NO right] → [Rectangle] "Adjust Again or Refer"
8. [Arrow YES down] → [Oval] "Discharge"

RIGHT FLOWCHART — Title: "TTC PATHWAY"
All in teal (#3A8A8C) outlines:
1. [Oval] "Patient Presents"
2. [Arrow down]
3. [Rectangle] "Assess Global Tone"
4. [Arrow down]
5. [Rectangle] "Tonal Pressure Testing"
6. [Arrow down]
7. [Diamond] "Receptivity Found?"
8. [Arrow YES down] → [Rectangle] "Deliver Information"
9. [Arrow down] → [Rectangle] "Allow Integration"
10. [Arrow down] → [Diamond] "System Reorganizing?"
11. [Arrow YES down] → [Oval] "Monitor Tone"

Standard flowchart symbols. Straight arrows with right-angle bends only. Off-white background. Near-black text inside shapes."""
            },
            {
                "suffix": "b-diverging",
                "prompt": """GRAPHIC TYPE: Diverging Pathway Diagram (Portrait, full page)

Create a single flowchart that starts unified then diverges into two paths.

START (top center):
[Oval] "Patient with Subluxation"
[Arrow down]
[Diamond] "Assessment Approach?"

LEFT BRANCH (blue #2E5FA3) — labeled "STRUCTURAL LENS":
[Arrow left-down]
[Rectangle] "Find the Fixation"
[Arrow down]
[Rectangle] "Apply Corrective Force"
[Arrow down]
[Rectangle] "Check: Did Bone Move?"
[Arrow down]
[Oval] "Adjust Again Next Visit"

RIGHT BRANCH (teal #3A8A8C) — labeled "TTC LENS":
[Arrow right-down]
[Rectangle] "Assess NeuroSpinal Tone"
[Arrow down]
[Rectangle] "Find Receptivity"
[Arrow down]
[Rectangle] "Deliver Precise Input"
[Arrow down]
[Oval] "Allow Self-Correction"

At the very bottom, a horizontal bracket connecting both endpoints with text: "Same patient. Different starting question."

Off-white background. Near-black text. Standard flowchart symbols."""
            }
        ]
    },

    # ═══════════════════════════════════════════════════════════════════════════
    # GRAPHIC 4: Mechanotransduction Sequence
    # ═══════════════════════════════════════════════════════════════════════════
    {
        "id": "04-mechanotransduction",
        "title": "Mechanotransduction Sequence",
        "variations": [
            {
                "suffix": "a-horizontal",
                "prompt": """GRAPHIC TYPE: Horizontal Process Sequence (Landscape, half page)

Create a left-to-right horizontal sequence showing the mechanotransduction pathway.

5 steps connected by bold arrows (blue #2E5FA3):

STEP 1: Circle with simple icon (lightning bolt shape)
Label below: "MECHANICAL FORCE"
Sublabel: "Touch / Pressure"

→ (bold arrow)

STEP 2: Circle with simple icon (cell shape)
Label below: "CELLULAR RESPONSE"
Sublabel: "Mechanoreceptor Activation"

→ (bold arrow)

STEP 3: Circle with simple icon (wave pattern)
Label below: "SIGNAL TRANSDUCTION"
Sublabel: "Piezoelectric Conversion"

→ (bold arrow)

STEP 4: Circle with simple icon (branching lines)
Label below: "NEURAL INTEGRATION"
Sublabel: "CNS Processing"

→ (bold arrow)

STEP 5: Circle with simple icon (human figure outline)
Label below: "PHYSIOLOGICAL EFFECT"
Sublabel: "Tone Reorganization"

Title above the sequence: "FROM TOUCH TO TONE: THE MECHANOTRANSDUCTION PATHWAY"

Circles in blue (#2E5FA3) with white icons. Arrows in teal (#3A8A8C). Labels in near-black. Off-white background."""
            },
            {
                "suffix": "b-vertical-cascade",
                "prompt": """GRAPHIC TYPE: Vertical Cascade Diagram (Portrait, half page)

Create a top-to-bottom cascade showing force transmission through tissue layers.

Title: "FORCE TRANSMISSION THROUGH THE NEUROSPINAL SYSTEM"

Layer 1 (top): Wide rectangle labeled "EXTERNAL INPUT"
Sublabel: "Precise touch at meningeal contact point"
[Wavy arrow down — representing force transmission]

Layer 2: Slightly narrower rectangle labeled "DURAL / FASCIAL TISSUE"
Sublabel: "Collagen generates piezoelectric charge"
[Wavy arrow down]

Layer 3: Narrower rectangle labeled "MECHANORECEPTORS"
Sublabel: "Tension → electrical signal"
[Straight arrow down]

Layer 4: Narrower rectangle labeled "CNS INTEGRATION"
Sublabel: "Safety signal updates threat model"
[Straight arrow down]

Layer 5 (bottom): Widest rectangle, emphasized with teal (#3A8A8C) fill
Label: "GLOBAL TONE REORGANIZATION"
Sublabel: "Meningeal release → cascade of adaptation"

Each layer uses increasingly deeper shades from the palette. The narrowing-then-widening shape suggests focused input producing broad effect. Off-white background."""
            },
            {
                "suffix": "c-cellular-zoom",
                "prompt": """GRAPHIC TYPE: Zoom-In Diagram (Portrait, full page)

Create a 3-panel zoom sequence showing mechanotransduction at increasing magnification.

PANEL 1 (top third) — "MACRO VIEW"
Simple outline of a spine in profile with a hand making contact at one point.
Arrow pointing to contact point.
Label: "Precise Input at Receptive Point"

PANEL 2 (middle third) — "TISSUE VIEW"
Zoomed view showing parallel collagen fibers in a cross-hatch pattern.
Small dots along fibers representing mechanoreceptors.
Arrow showing force direction through fibers.
Label: "Meningeal Tissue with Embedded Mechanoreceptors"

PANEL 3 (bottom third) — "CELLULAR VIEW"
Single fibroblast cell with alpha-SMA fibers shown as internal lines.
TGF-beta1 molecule shown as a small triangle nearby.
Arrow showing the cell transitioning from contracted (left) to relaxed (right).
Label: "Myofibroblast Release — Contraction Resolves"

Connecting arrows between panels showing the "zoom in" progression.
Medical illustration style — clean line art with flat color fills. Blue (#2E5FA3) for structural elements. Teal (#3A8A8C) for cellular elements. Off-white background."""
            }
        ]
    },

    # ═══════════════════════════════════════════════════════════════════════════
    # GRAPHIC 5: Progressive Anatomical Drawings (Meningeal Architecture)
    # ═══════════════════════════════════════════════════════════════════════════
    {
        "id": "05-meningeal-anatomy",
        "title": "Progressive Meningeal Architecture",
        "variations": [
            {
                "suffix": "a-four-panel",
                "prompt": """GRAPHIC TYPE: Four-Panel Progressive Anatomical Diagram (Portrait, full page)

Create 4 panels in a 2x2 grid, each building on the previous to show the meningeal architecture. Medical illustration style — clean line art with flat color fills, NOT photorealistic.

PANEL 1 (top-left) — "BASIC ANATOMY"
Simple sagittal cross-section of the spinal canal showing:
- Vertebral body (gray rectangle)
- Spinal cord (blue #2E5FA3 oval in center)
- Dura mater (teal #3A8A8C line surrounding cord)
- Epidural space (white gap)
Labels with leader lines pointing to each structure.

PANEL 2 (top-right) — "FASCIAL CONTINUITY"
Same cross-section but now showing:
- Everything from Panel 1 PLUS
- Fascial connections extending outward from the dura (thin lines radiating out)
- Arrows showing continuity from dura → fascia → muscle → bone
Label: "The NeuroSpinal Continuum"

PANEL 3 (bottom-left) — "MECHANORECEPTORS"
Same cross-section but now showing:
- Everything from Panel 2 PLUS
- Small dots/circles at key points along the dura and fascial connections representing mechanoreceptors
- Highlighted zones where mechanoreceptors are densest (craniocervical, lumbosacral)
Label: "Receptor-Rich Zones"

PANEL 4 (bottom-right) — "TENSION TRANSMISSION"
Same cross-section but now showing:
- Red/gold (#8A6A1A) stress lines radiating through the meningeal system
- Arrows showing how upstream tension transmits through the continuum
- A vertebra being pulled/displaced by the tension vectors
Label: "How Tension Drives Structure"

Each panel numbered (1, 2, 3, 4) in the corner. Consistent sizing. Off-white background. Thin gray borders between panels."""
            },
            {
                "suffix": "b-longitudinal",
                "prompt": """GRAPHIC TYPE: Longitudinal Spine View (Portrait, full page)

Create a full-length sagittal view of the spine showing the NeuroSpinal System as a continuous tensional structure.

The image shows a simplified lateral/sagittal spine from skull base to sacrum:
- Vertebrae shown as simple stacked rectangles (gray #D1D5DB)
- Spinal cord shown as a continuous blue (#2E5FA3) line running through
- Dura mater shown as a teal (#3A8A8C) sheath surrounding the cord
- Fascial extensions shown as thin lines connecting dura to each vertebra

KEY FEATURES TO HIGHLIGHT:
- At the cranium (top): "Cranial Attachment" label with arrow
- At the sacrum (bottom): "Sacral Attachment" label with arrow
- Between them: "The NeuroSpinal Continuum" label along the length

Show 3 areas of "aberrant tension" as gold (#8A6A1A) highlighted zones where the dura is slightly thicker/contracted, with stress lines radiating outward.

Arrows from these tension zones to adjacent vertebrae showing how meningeal tension pulls on vertebral segments.

Title at top: "THE NEUROSPINAL SYSTEM: PRIMARY TONE-SETTER"

Clean line art. Diagrammatic, not photorealistic. Off-white background."""
            }
        ]
    },

    # ═══════════════════════════════════════════════════════════════════════════
    # GRAPHIC 6: Reframed Technique Comparison Table
    # ═══════════════════════════════════════════════════════════════════════════
    {
        "id": "06-technique-table",
        "title": "Technique Comparison Table",
        "variations": [
            {
                "suffix": "a-four-column",
                "prompt": """GRAPHIC TYPE: Styled Comparison Table (Landscape, half page)

Create a clean, professional comparison table with 4 columns and 7 rows.

COLUMN HEADERS (blue #2E5FA3 fill, white bold text):
| CATEGORY | OSSEOUS | TONAL (TTC) | OSSEOTONAL |

ROW 1: "Primary Input"
| Osseous: "Force to Joint" | TTC: "Information to Meninges" | OsseoTonal: "Articular with Tonal Intent" |

ROW 2: "Goal"
| Osseous: "Move Bone" | TTC: "Release Aberrant Tone" | OsseoTonal: "Modulate Global Tone" |

ROW 3: "Assessment"
| Osseous: "Segmental Palpation" | TTC: "Global Tonal Indicators" | OsseoTonal: "Hybrid Analysis" |

ROW 4: "Force Level"
| Osseous: "High / Moderate" | TTC: "Minimal" | OsseoTonal: "Low / Moderate" |

ROW 5: "Contact Site"
| Osseous: "Vertebral Segment" | TTC: "Meningeal Windows" | OsseoTonal: "Joint / Receptors" |

ROW 6: "Verification"
| Osseous: "Joint Cavitation" | TTC: "Leg Balancing" | OsseoTonal: "Reflex Indicators" |

Alternating row fills: white and light gray (#F3F4F6). Thin borders (#D1D5DB). TTC column slightly highlighted with a subtle teal (#3A8A8C) left border to draw attention. Off-white background. All text in near-black (#1A2A3A)."""
            },
            {
                "suffix": "b-spectrum",
                "prompt": """GRAPHIC TYPE: Technique Spectrum Diagram (Landscape, half page)

Create a horizontal spectrum/continuum showing chiropractic techniques arranged from most structural to most tonal.

A horizontal gradient bar spanning the page:
- Left end: labeled "STRUCTURAL" (blue #2E5FA3)
- Right end: labeled "TONAL" (teal #3A8A8C)

Positioned along the spectrum (as labeled dots/markers):
- Far left: "Diversified"
- Left-center: "Gonstead"
- Center-left: "Thompson"
- Center: "SOT" (labeled "OsseoTonal" below)
- Center-right: "TRT, MC2, BGI" (labeled "OsseoTonal" below)
- Right: "NSA" (labeled "Tonal" below)
- Far right: "TTC" (emphasized with gold #8A6A1A ring, labeled "Pure Tonal" below)

Above the spectrum: a bracket over the right half labeled "Engages NeuroSpinal System"
Below the spectrum: a bracket over the left half labeled "Engages Joint Mechanics"

Title: "THE CHIROPRACTIC TECHNIQUE SPECTRUM"

Clean markers, clear labels, off-white background."""
            }
        ]
    },

    # ═══════════════════════════════════════════════════════════════════════════
    # GRAPHIC 7: Historical Evolution Timeline
    # ═══════════════════════════════════════════════════════════════════════════
    {
        "id": "07-timeline",
        "title": "Historical Evolution Timeline",
        "variations": [
            {
                "suffix": "a-horizontal",
                "prompt": """GRAPHIC TYPE: Horizontal Timeline (Landscape, half page)

Create a classic horizontal timeline showing the evolution of tonal chiropractic concepts.

A bold horizontal line spanning the page with the following milestones. Alternate labels ABOVE and BELOW the line to prevent crowding.

ABOVE the line (with vertical tick marks):
- 1895: "D.D. Palmer — Tone as Foundation"
- 1931: "B.J. Palmer — HIO Toggle Recoil"
- 1936: "Toftness — First Tonal Technique"
- 1978: "Breig — Adverse Mechanical Tension"
- 1995: "Talsky — TRT Co-Developer"
- 2016: "Lelic — 20% Prefrontal Change"

BELOW the line:
- 1923: "Van Rumpt — DNFT / Leg Checks"
- 1930s: "DeJarnette — SOT / Cranial-Sacral"
- 1955: "Thompson — Derifield Leg Checks"
- 1982: "Epstein — NSA / Class A & B"
- 2001: "Talsky — TTC Emerges"

Title above: "FROM TONE TO TTC: A TIMELINE OF TONAL CHIROPRACTIC"

Blue (#2E5FA3) for the timeline line and tick marks. Near-black text. Each milestone label maximum 4 words plus name. Off-white background. Generous spacing."""
            },
            {
                "suffix": "b-river",
                "prompt": """GRAPHIC TYPE: River/Stream Timeline (Portrait, full page)

Create a vertical flowing "river" timeline from top to bottom showing the evolution of tonal chiropractic.

The "river" is a wavy vertical blue (#2E5FA3) band flowing from top to bottom, widening as it goes (representing the broadening of tonal understanding).

Milestones are positioned as "tributaries" flowing into the river from alternating left and right sides:

LEFT SIDE (labeled branches flowing in):
- 1895: "Palmer: Tone" (small stream)
- 1931: "Logan: Sacral Contact" (small stream)
- 1936: "Toftness: First Tonal" (medium stream)
- 1978: "Breig: Mechanical Tension" (medium stream)
- 1995: "Talsky + Holder: TRT" (large stream)

RIGHT SIDE:
- 1923: "Van Rumpt: Leg Checks" (small stream)
- 1930s: "DeJarnette: Meninges" (medium stream)
- 1982: "Epstein: Class A & B" (large stream)
- 1980: "Ward: SCPMU" (medium stream)

The river WIDENS significantly at 2001 and becomes teal (#3A8A8C), labeled "TTC EMERGES — Synthesis"

At the very bottom, the river opens into a wide delta labeled "The Primary Tone-Setter"

Clean, diagrammatic style. Off-white background. Generous whitespace."""
            },
            {
                "suffix": "c-era-blocks",
                "prompt": """GRAPHIC TYPE: Era Block Timeline (Portrait, full page)

Create a vertical timeline divided into distinct historical eras as colored blocks.

From top to bottom:

ERA 1 — "FOUNDATIONS" (1895–1930) — Light blue fill (#2E5FA3 at 20% opacity)
- 1895: D.D. Palmer — "Life is an expression of tone"
- 1923: Van Rumpt — DNFT, pressure testing, leg checks

ERA 2 — "EARLY TONAL PIONEERS" (1930–1960) — Medium blue fill
- 1931: Logan — Low-force sacral contacts
- 1931: B.J. Palmer — HIO upper cervical
- 1936: Toftness — First completely tonal technique
- 1955: Thompson — Derifield leg checks

ERA 3 — "MECHANOBIOLOGICAL BRIDGE" (1960–1995) — Teal fill (#3A8A8C at 30% opacity)
- 1978: Breig — Adverse Mechanical Tension in CNS
- 1980: Ward — Spinal-Column-Pelvic-Meningeal-Unit
- 1982: Epstein — NSA, SMFU, Class A/B

ERA 4 — "TTC" (1995–present) — Bold teal fill (#3A8A8C)
- 1995: Talsky — Co-develops TRT
- 2001: TTC emerges as distinct model
- 2007: Haavik — Neurophysiological evidence
- 2016: Lelic — 20% prefrontal cortex change

Title: "EVOLUTION OF TONAL CHIROPRACTIC"

Each era block has a visible left border in the era's color. Year labels in bold. Descriptions in regular weight. Off-white background."""
            }
        ]
    },

    # ═══════════════════════════════════════════════════════════════════════════
    # GRAPHIC 8: Full-Page Summary Infographic
    # ═══════════════════════════════════════════════════════════════════════════
    {
        "id": "08-summary-infographic",
        "title": "Full-Page Summary Infographic",
        "variations": [
            {
                "suffix": "a-zones",
                "prompt": """GRAPHIC TYPE: Full-Page Summary Infographic (Portrait, full page)

Create a magazine-style full-page infographic summarizing the TTC paradigm. Three distinct zones:

ZONE 1 — TOP 20% — HEADLINE
Large title: "THE PRIMARY TONE-SETTER"
Subtitle: "How Talsky Tonal Chiropractic Reframes Subluxation"
Blue (#2E5FA3) text on off-white background. Bold, authoritative.

ZONE 2 — CENTER 50% — CORE VISUAL
A central downward flow diagram showing the TTC model:

Top: "STRESS / THREAT" (in a dark box)
↓ Arrow
"MENINGEAL CONTRACTION" (in a blue box)
↓ Arrow
"ABERRANT NEUROSPINAL TONE" (in a large teal box — this is the PRIMARY TONE-SETTER, make it largest)
↓ Arrow branching into 5 smaller boxes:
"Dyskinesia" → "Dysafferentation" → "Dysponesis" → "Dysautonomia" → "Degeneration"

Below the 5 D's, an upward arrow labeled "TTC INPUT" pointing back to "ABERRANT NEUROSPINAL TONE" — showing where TTC intervenes.

ZONE 3 — BOTTOM 30% — THREE KEY PRINCIPLES
Three columns with icons:
Column 1: "UPSTREAM" — "Subluxation is secondary. Meningeal tone is primary."
Column 2: "INFORMATION" — "Not force to move bones. Precise input to engage intelligence."
Column 3: "RECEPTIVITY" — "Not finding fixation. Finding the best window in."

Off-white background throughout. Blue and teal palette. Near-black text."""
            },
            {
                "suffix": "b-visual-abstract",
                "prompt": """GRAPHIC TYPE: Visual Abstract / Graphical Summary (Portrait, full page)

Create a visual abstract in the style of journal graphical abstracts — a single-page summary that a reader can scan in 30 seconds.

HEADER BAR: Blue (#2E5FA3) banner across the top
"THE PRIMARY TONE-SETTER — Visual Summary"
White text, bold

SECTION 1 — "THE PROBLEM" (left third of upper area)
Simple icon: a bone with an X through it
Text: "Starting at the bone misses the cause"

SECTION 2 — "THE MODEL" (center third of upper area)
Simple icon: concentric circles (like ripples)
Text: "NeuroSpinal tone drives structure"

SECTION 3 — "THE EVIDENCE" (right third of upper area)
Simple icon: a brain outline
Text: "20% prefrontal change after adjustment"

CENTER — Large horizontal arrow diagram:
"Stress" → "Meningeal Tension" → "Aberrant Tone" → "5 D's Cascade" → "Subluxation"
With a reverse arrow below: "TTC Input" → "Safety Signal" → "Tone Release" → "Self-Correction"

BOTTOM — "CLINICAL IMPLICATIONS"
4 short bullet points in two columns:
- "Assess tone, not fixation"
- "Find receptivity, not resistance"
- "Deliver information, not force"
- "Allow self-correction"

Off-white background. Blue, teal, near-black only. No decorative elements."""
            },
            {
                "suffix": "c-paradigm-shift",
                "prompt": """GRAPHIC TYPE: Before/After Paradigm Shift Infographic (Portrait, full page)

Create a dramatic before/after split-page infographic.

LEFT HALF — "THE OLD PARADIGM" — slightly grayed out / muted tones
Background: very light gray (#F3F4F6)
Icon at top: simple vertebra outline
Below, stacked elements:
- "Find the fixation"
- "Apply force"
- "Move the bone"
- "Check positioning"
- "Repeat"
At bottom: "Starting point: STRUCTURE"

VERTICAL DIVIDER: Bold line down center with a large arrow pointing from left to right, labeled "PARADIGM SHIFT"

RIGHT HALF — "THE TTC MODEL" — full color, vibrant
Background: warm off-white (#F8F8F6)
Icon at top: concentric wave pattern
Below, stacked elements:
- "Assess global tone"
- "Find receptivity"
- "Deliver information"
- "Allow integration"
- "Monitor reorganization"
At bottom: "Starting point: TONE"

FOOTER spanning full width:
"Bones move because of tension. Address the tension, and the body moves the bones."

Blue (#2E5FA3) for structural elements. Teal (#3A8A8C) for TTC elements. Off-white background."""
            }
        ]
    },

    # ═══════════════════════════════════════════════════════════════════════════
    # BONUS GRAPHIC 9: The 5 D's Cascade (replaces ASCII flowchart)
    # ═══════════════════════════════════════════════════════════════════════════
    {
        "id": "09-five-ds-cascade",
        "title": "5 D's Cascade (replaces ASCII flowchart)",
        "variations": [
            {
                "suffix": "a-vertical-flow",
                "prompt": """GRAPHIC TYPE: Vertical Cascade Flowchart (Portrait, full page)

Create a professional flowchart replacing the ASCII diagram in the paper. This shows the pathophysiology cascade.

TOP SECTION — "INITIATION"
Two parallel entry points:

LEFT: "CLASS B" box (teal #3A8A8C)
Below: "Threat Perception" → Arrow → "Protective Meningeal Contraction"

RIGHT: "CLASS A" box (blue #2E5FA3)
Below: "Blunt Trauma" → Arrow → "Direct VSC + Meningeal Contraction"

Both arrows converge to a central large box:

CENTER: Large emphasized box (teal fill)
"ABERRANT NEUROSPINAL TONE"
Subtitle below: "The Primary Tone-Setter"

Arrow down to: "Stuck Pattern — Cannot Self-Correct"

Arrow down branching into the 5 D's cascade (5 boxes in a staircase/cascade pattern, each slightly lower and to the right):
1. "DYSKINESIA" (movement dysfunction)
2. "DYSAFFERENTATION" (distorted sensory input)
3. "DYSPONESIS" (misdirected neural effort)
4. "DYSAUTONOMIA" (autonomic dysregulation)
5. "DEGENERATION" (structural decline)

Curved feedback arrows from later stages back to earlier ones, labeled "Self-Reinforcing"

BOTTOM SECTION — "RESOLUTION"
Arrow from "Stuck Pattern" down to:
"TTC INPUT" (gold #8A6A1A box) → "Safety Signal" → "Meningeal Release" → "Cascade of Adaptation"

Standard flowchart symbols. Rounded rectangles. Clear arrows. Off-white background. Near-black text."""
            },
            {
                "suffix": "b-circular-cascade",
                "prompt": """GRAPHIC TYPE: Circular Cascade Diagram (Portrait, full page)

Create a circular diagram showing the self-reinforcing nature of the 5 D's cascade.

CENTER: Large circle with "ABERRANT NEUROSPINAL TONE" in bold. This is the hub.

5 concentric rings radiating outward from center, each containing one D:
Ring 1 (innermost): "DYSKINESIA"
Ring 2: "DYSAFFERENTATION"
Ring 3: "DYSPONESIS"
Ring 4: "DYSAUTONOMIA"
Ring 5 (outermost): "DEGENERATION"

Curved arrows between rings showing the cascade flows OUTWARD (cause → effect).
Additional curved arrows flowing INWARD showing the self-reinforcing feedback loops.

At the very center of the center circle: a small gold (#8A6A1A) star labeled "TTC INPUT" — the intervention point.

TWO ENTRY ARROWS coming into the center circle from top:
- Left entry: "CLASS A — Trauma" (blue)
- Right entry: "CLASS B — Threat" (teal)

Title: "THE CASCADE OF DYSFUNCTION"
Subtitle: "Self-Reinforcing — Specific Input Required for Resolution"

Blue for structural elements. Teal for the center and TTC. Gold for intervention point. Off-white background."""
            },
            {
                "suffix": "c-threat-to-release",
                "prompt": """GRAPHIC TYPE: 8-Step Process Diagram (Portrait, full page)

Create a numbered 8-step vertical process diagram showing the complete Threat-to-Release Sequence.

Title: "FROM THREAT TO RELEASE: THE COMPLETE SEQUENCE"

8 numbered steps in rounded rectangles, connected by downward arrows:

1. "THREAT APPRAISAL" — Blue box
   Sublabel: "CNS perceives danger"

2. "MYOFIBROBLAST CONVERSION" — Blue box
   Sublabel: "TGF-beta1 locks contraction"

3. "NEURAL GUARDING" — Blue box
   Sublabel: "Altered reflex thresholds"

4. "INFORMATIONAL INTERFERENCE" — Blue box
   Sublabel: "Distorted afferent/efferent signals"

5. "PERSISTENT HOLDING" — Dark blue box (emphasized)
   Sublabel: "Awaiting safety information"

A horizontal dashed line here labeled "── TTC INTERVENTION POINT ──"

6. "SPECIFIC INPUT" — Teal box
   Sublabel: "Vector of release + congruent intent"

7. "SAFETY SIGNAL" — Teal box
   Sublabel: "Updated CNS threat model"

8. "CASCADE OF RELEASE" — Large teal box (emphasized)
   Sublabel: "Myofibroblasts de-tension, global tone reorganizes"

Steps 1-5 use blue (#2E5FA3) fill. Steps 6-8 use teal (#3A8A8C) fill. The dashed intervention line uses gold (#8A6A1A). Off-white background. Near-black text. Clear downward flow."""
            }
        ]
    },
]


# ─── GENERATION FUNCTIONS ──────────────────────────────────────────────────────

def load_image_as_base64(path):
    """Load an image file and return base64 encoded string."""
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def get_mime_type(path):
    """Get MIME type based on file extension."""
    ext = path.lower()
    if ext.endswith(".png"):
        return "image/png"
    elif ext.endswith((".jpg", ".jpeg")):
        return "image/jpeg"
    return "image/png"


def generate_image(prompt, output_path, name, reference_image_path=None, max_retries=3):
    """Generate an image using the Gemini API."""
    print(f"\n{'='*70}")
    print(f"Generating: {name}")
    print(f"Output: {output_path}")
    if reference_image_path:
        print(f"Reference: {reference_image_path}")
    print(f"{'='*70}")

    full_prompt = f"""{STYLE_GUIDE}

CRITICAL TEXT INSTRUCTION: Before rendering the final image, carefully verify ALL text. Ensure each word is spelled correctly. Render the text EXACTLY as specified — character by character, word by word. Keep all labels short (maximum 5 words). Use large, legible font sizes.

{prompt}

Generate this as a high-resolution image suitable for print in a professional white paper."""

    parts = []

    # Add reference image if provided
    if reference_image_path and os.path.exists(reference_image_path):
        ref_b64 = load_image_as_base64(reference_image_path)
        ref_mime = get_mime_type(reference_image_path)
        parts.append({
            "inlineData": {
                "mimeType": ref_mime,
                "data": ref_b64
            }
        })
        full_prompt = f"REFERENCE IMAGE: Match the visual style and color palette of this reference image exactly.\n\n{full_prompt}"

    parts.append({"text": full_prompt})

    request_body = {
        "contents": [{"parts": parts}],
        "generationConfig": {
            "responseModalities": ["TEXT", "IMAGE"]
        }
    }

    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(
                ENDPOINT,
                data=json.dumps(request_body).encode("utf-8"),
                headers={"Content-Type": "application/json"},
                method="POST"
            )

            print(f"  Attempt {attempt + 1}/{max_retries}...")
            with urllib.request.urlopen(req, timeout=180) as resp:
                result = json.loads(resp.read().decode("utf-8"))

            candidates = result.get("candidates", [])
            if not candidates:
                print("  ERROR: No candidates in response")
                if attempt < max_retries - 1:
                    time.sleep(10)
                    continue
                return False

            parts_resp = candidates[0].get("content", {}).get("parts", [])
            image_saved = False
            for part in parts_resp:
                if "inlineData" in part:
                    img_data = base64.b64decode(part["inlineData"]["data"])
                    os.makedirs(os.path.dirname(output_path), exist_ok=True)
                    with open(output_path, "wb") as f:
                        f.write(img_data)
                    size_kb = len(img_data) / 1024
                    print(f"  SUCCESS: Saved ({size_kb:.0f} KB)")
                    image_saved = True
                elif "text" in part:
                    print(f"  Model note: {part['text'][:200]}")

            if image_saved:
                return True
            else:
                print("  ERROR: No image in response")
                if attempt < max_retries - 1:
                    time.sleep(10)

        except urllib.error.HTTPError as e:
            error_body = e.read().decode("utf-8") if e.fp else "No body"
            print(f"  HTTP Error {e.code}: {error_body[:300]}")
            if e.code == 429:
                wait = 60 if attempt > 0 else 30
                print(f"  Rate limited. Waiting {wait}s...")
                time.sleep(wait)
            elif attempt < max_retries - 1:
                time.sleep(10)
        except Exception as e:
            print(f"  Error: {e}")
            if attempt < max_retries - 1:
                time.sleep(10)

    return False


def main():
    # Parse arguments
    graphic_filter = None
    variation_filter = None
    start_idx = 0
    end_idx = len(GRAPHICS)

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--graphic":
            graphic_filter = int(args[i + 1])
            i += 2
        elif args[i] == "--variation":
            variation_filter = args[i + 1]
            i += 2
        elif args[i].isdigit():
            start_idx = int(args[i]) - 1  # 1-indexed input
            if i + 1 < len(args) and args[i + 1].isdigit():
                end_idx = int(args[i + 1])
                i += 1
            else:
                end_idx = start_idx + 1
            i += 1
        else:
            i += 1

    if graphic_filter is not None:
        start_idx = graphic_filter - 1
        end_idx = graphic_filter

    # Check for first approved reference image
    reference_image = None
    ref_files = sorted([
        f for f in os.listdir(REFERENCE_DIR)
        if f.endswith((".png", ".jpg", ".jpeg"))
    ]) if os.path.exists(REFERENCE_DIR) else []
    if ref_files:
        reference_image = os.path.join(REFERENCE_DIR, ref_files[0])
        print(f"Using reference image: {reference_image}")

    # Generate
    total = 0
    successes = 0
    failures = 0

    for graphic in GRAPHICS[start_idx:end_idx]:
        for var in graphic["variations"]:
            if variation_filter and not var["suffix"].startswith(variation_filter):
                continue

            total += 1
            output_path = os.path.join(
                OUTPUT_BASE,
                graphic["id"],
                f"{graphic['id']}-{var['suffix']}.png"
            )

            success = generate_image(
                prompt=var["prompt"],
                output_path=output_path,
                name=f"{graphic['title']} — Variation {var['suffix']}",
                reference_image_path=reference_image
            )

            if success:
                successes += 1
            else:
                failures += 1

            # Rate limit spacing
            if total < sum(len(g["variations"]) for g in GRAPHICS[start_idx:end_idx]):
                wait = 8
                print(f"  Waiting {wait}s before next request...")
                time.sleep(wait)

    print(f"\n{'='*70}")
    print(f"COMPLETE: {successes}/{total} succeeded, {failures} failed")
    print(f"Output directory: {OUTPUT_BASE}")
    print(f"{'='*70}")


if __name__ == "__main__":
    main()
