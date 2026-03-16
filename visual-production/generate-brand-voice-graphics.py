#!/usr/bin/env python3
"""Generate brand-voice-aligned graphics from deep paper analysis.

These graphics capture TTC's most compelling visual moments — the rhetorical
patterns, paradigm-shifting concepts, and clinical insights that define
the paper's distinctive voice.

Usage:
    export GEMINI_API_KEY=$(op item get 'Google Gemini API' --fields 'credential' --reveal)
    python3 visual-production/generate-brand-voice-graphics.py
    python3 visual-production/generate-brand-voice-graphics.py 1 5    # generate slides 1-5 only
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
    raise RuntimeError("Set GEMINI_API_KEY before running.")
MODEL = "gemini-3-pro-image-preview"
ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"
OUTPUT_BASE = "/Users/zachconnermba/Code/TTC-White-Paper/visual-production/output"

STYLE_GUIDE = """STYLE GUIDE -- TTC WHITE PAPER GRAPHICS

Role: You are a clinical medical illustrator producing graphics for a peer-reviewed chiropractic white paper. Your output must look like it belongs in JAMA, Spine, or the Journal of Manipulative and Physiological Therapeutics.

Style: Clean, academic, professional. Flat design. No decorative elements, no gradients, no drop shadows, no stock clip art, no photorealism.

COLOR PALETTE (strict):
- Background: #F8F8F6 (warm off-white)
- Primary structure/text: #1A2A3A (near-black navy)
- Primary accent: #2E5FA3 (clinical blue)
- Secondary accent: #3A8A8C (muted teal)
- Tertiary accent: #8A6A1A (dark gold — sparingly)
- Gray: #6B7280 (support), #D1D5DB (borders), #F3F4F6 (alt rows)

TYPOGRAPHY: Helvetica/Arial sans-serif. Minimum 30px labels. Max 5 words per label. Text on solid backgrounds only.

DO NOT include: text not in prompt, hex codes as visible text, decorative elements, photorealism, clip art, logos."""


SLIDES = [
    # ═══ 10: "WE SAID TONE, ADJUSTED BONES" — Three-Column Contrast ═══
    {
        "name": "10 Said-Tone — A (Three Column)",
        "output": f"{OUTPUT_BASE}/10-said-tone-adjusted-bones/10-said-tone-a-three-column.png",
        "prompt": """GRAPHIC TYPE: Three-Column Contrast Table (Portrait, full page)

Title at top: "WE SAID TONE, ADJUSTED BONES"

Three columns with headers in blue (#2E5FA3) banner bars with white text:

COLUMN 1 — "PHILOSOPHY"
Rows (rounded rectangle boxes, stacked vertically):
- "Innate Intelligence"
- "Tone Is Primary"
- "Body Self-Corrects"
- "Vitalistic Principles"

COLUMN 2 — "WHAT WE SAID"
Rows (same height as Column 1):
- "The body heals itself"
- "Tone drives function"
- "Trust the process"
- "Above-down, inside-out"

COLUMN 3 — "WHAT WE DID"
Rows (same height, with subtle gold #8A6A1A left border to highlight the gap):
- "Structural correction"
- "Segmental adjustment"
- "Force-based input"
- "Outside-in application"

Below the table, a horizontal arrow pointing right from Column 2 to a teal (#3A8A8C) box:
"TTC closes this gap"

Bottom text: "What if our methods matched our philosophy?"

Alternating row fills: white and #F3F4F6. Thin #D1D5DB borders. Off-white background."""
    },
    {
        "name": "10 Said-Tone — B (Bridge)",
        "output": f"{OUTPUT_BASE}/10-said-tone-adjusted-bones/10-said-tone-b-bridge.png",
        "prompt": """GRAPHIC TYPE: Bridge Diagram (Portrait, full page)

LEFT SIDE — tall rounded rectangle labeled "OUR PHILOSOPHY" (blue #2E5FA3 fill, white text)
Contains stacked items:
- "Tone is primary"
- "Body self-corrects"
- "Innate intelligence"

RIGHT SIDE — tall rounded rectangle labeled "OUR METHODS" (gray #6B7280 fill, white text)
Contains stacked items:
- "Structural correction"
- "Segmental adjustment"
- "Force-based input"

BETWEEN THEM — a GAP (visible empty space)

Above the gap, small text: "The historical disconnect"

BELOW — a teal (#3A8A8C) bridge/arch spanning the gap, labeled:
"TTC: Methods That Match the Philosophy"

Under the bridge: "Direct meningeal engagement. Minimal force. Body's intelligence organizes."

Off-white background. Clean lines. No decorative elements."""
    },

    # ═══ 11: "NOT ABOUT / ABOUT" — Two-Column Contrast ═══
    {
        "name": "11 Not-About — A (Two Column)",
        "output": f"{OUTPUT_BASE}/11-not-about/11-not-about-a-two-column.png",
        "prompt": """GRAPHIC TYPE: Two-Column Contrast List (Portrait, full page)

Title: "TTC IS..."

LEFT COLUMN — Header: "NOT ABOUT" (gray #6B7280 banner, white text)
Each item is a rounded rectangle with a thin left border in gray:
1. "Replacing structural methods"
2. "Dismissing articular work"
3. "More force or technique"
4. "A new correction protocol"
5. "Treating symptoms"

RIGHT COLUMN — Header: "ABOUT" (teal #3A8A8C banner, white text)
Each item is a rounded rectangle with a thin left border in teal:
1. "Engaging the NeuroSpinal System"
2. "Honoring the body's intelligence"
3. "Least amount, most effective"
4. "Direct meningeal contact"
5. "Addressing tone at its source"

A subtle vertical dividing line between columns.

Bottom center callout in blue (#2E5FA3) rounded box:
"Same goal. Different access point."

Off-white background. Clean sans-serif labels."""
    },
    {
        "name": "11 Not-About — B (Checklist)",
        "output": f"{OUTPUT_BASE}/11-not-about/11-not-about-b-checklist.png",
        "prompt": """GRAPHIC TYPE: Visual Checklist (Portrait, full page)

Title: "WHAT TTC IS — AND ISN'T"

Two sections, stacked vertically:

TOP SECTION — "TTC IS NOT:" (near-black header)
5 items, each with a gray X icon on the left:
- "A rejection of structural chiropractic"
- "More force or more technique"
- "A symptom-based protocol"
- "A replacement for articular care"
- "A claim of superiority"

Thin horizontal divider line (#D1D5DB)

BOTTOM SECTION — "TTC IS:" (teal #3A8A8C header)
5 items, each with a teal checkmark icon on the left:
- "Direct meningeal engagement"
- "Minimal force, maximum respect"
- "Tone-first methodology"
- "The body's intelligence organizes"
- "Philosophy made clinical"

Off-white background. Clean, generous spacing."""
    },

    # ═══ 12: SELF-TUNING GUITAR — Illustrated Metaphor ═══
    {
        "name": "12 Guitar — A (Instrument)",
        "output": f"{OUTPUT_BASE}/12-guitar-metaphor/12-guitar-a-instrument.png",
        "prompt": """GRAPHIC TYPE: Illustrated Metaphor Diagram (Portrait, full page)

A clean, flat-design illustration of an acoustic guitar in profile.

The NECK of the guitar is labeled: "The Spine"
The STRINGS are labeled: "Meningeal Tissues"
The TUNING PEGS are labeled: "NeuroSpinal Tone"
The BODY/SOUNDBOARD is labeled: "The Whole Person"

TWO APPROACHES shown side by side below the guitar:

LEFT (blue #2E5FA3 box):
"ARTICULAR APPROACH"
"Adjust the frets and bridge"
Small text: "Influences string tension indirectly"

RIGHT (teal #3A8A8C box):
"TTC APPROACH"
"Tune the strings directly"
Small text: "Engages meningeal tone at its source"

Bottom text: "You don't tune a guitar by reshaping the wood."

Medical illustration style — clean line art with flat color fills. NOT photorealistic.
Off-white background. Labeled with leader lines."""
    },
    {
        "name": "12 Guitar — B (Before After)",
        "output": f"{OUTPUT_BASE}/12-guitar-metaphor/12-guitar-b-before-after.png",
        "prompt": """GRAPHIC TYPE: Before/After Split (Landscape, half page)

LEFT PANEL — "BEFORE: OUT OF TUNE"
Simple flat-design guitar with wavy, misaligned strings (drawn with irregular curves).
Strings colored in gold (#8A6A1A) to indicate tension/dissonance.
Label below: "Aberrant NeuroSpinal Tone"

RIGHT PANEL — "AFTER: IN TUNE"
Same guitar with straight, evenly spaced strings.
Strings colored in teal (#3A8A8C) to indicate resolved tone.
Label below: "Organized NeuroSpinal Tone"

Center dividing line with arrow pointing right.
Small text above arrow: "TTC Contact"

Bottom center: "The body is a self-tuning instrument. TTC removes the interference."

Clean line art. Off-white background. Blue (#2E5FA3) guitar outlines."""
    },

    # ═══ 13: ANESTHESIA FINDING — "The Limitation Is Neural" ═══
    {
        "name": "13 Anesthesia — A (Split Finding)",
        "output": f"{OUTPUT_BASE}/13-anesthesia-finding/13-anesthesia-a-split.png",
        "prompt": """GRAPHIC TYPE: Split Comparison Diagram (Portrait, half page)

Title: "THE ANESTHESIA FINDING"

LEFT PANEL — blue (#2E5FA3) thin border:
Header: "EXPECTED"
Simple diagram: vertebra icon with an arrow labeled "Manual Adjustment"
Below: arrow down to "Structural Correction"
Text: "If subluxation is structural, anesthesia should help"

RIGHT PANEL — teal (#3A8A8C) thin border:
Header: "OBSERVED"
Simple diagram: vertebra icon with X mark labeled "Under Anesthesia"
Below: arrow down to "No Lasting Correction"
Text: "Muscle relaxation did not resolve subluxation"

Bottom callout box (teal fill, white text):
"The limitation is neural, not structural."

Below: "Crelin, 1973; Haldeman, 1983"

Off-white background. Clean flat design."""
    },
    {
        "name": "13 Anesthesia — B (Implication)",
        "output": f"{OUTPUT_BASE}/13-anesthesia-finding/13-anesthesia-b-implication.png",
        "prompt": """GRAPHIC TYPE: Logic Chain Diagram (Portrait, half page)

Title: "IF SUBLUXATION WERE PURELY STRUCTURAL..."

Vertical flow with arrows connecting each step:

Step 1 (blue #2E5FA3 box): "Subluxation = structural misalignment"

Step 2 (blue box): "Remove muscle guarding (anesthesia)"

Step 3 (blue box): "Adjustment should hold"

Step 4 (large gold #8A6A1A outlined box with X):
"BUT: Adjustments under anesthesia fail to hold"
(Crelin 1973, Haldeman 1983)

Step 5 (teal #3A8A8C box, large):
"THEREFORE: Something beyond structure maintains subluxation"

Arrow down to final box (teal fill, white text):
"Aberrant NeuroSpinal Tone"

Off-white background. Clean arrows with arrowheads."""
    },

    # ═══ 14: SAFETY SIGNAL TRAP — Circular Lock ═══
    {
        "name": "14 Safety Signal — A (Circular)",
        "output": f"{OUTPUT_BASE}/14-safety-signal-trap/14-safety-signal-a-circular.png",
        "prompt": """GRAPHIC TYPE: Circular Feedback Diagram (Portrait, half page)

Title: "THE SAFETY SIGNAL TRAP"

A circular loop with 4 nodes connected by curved arrows forming a cycle:

Node 1 (top, blue #2E5FA3 box):
"Aberrant Meningeal Tone"

Arrow clockwise to →

Node 2 (right, blue box):
"Restricted Movement"

Arrow clockwise to →

Node 3 (bottom, blue box):
"Reduced Sensory Input"

Arrow clockwise to →

Node 4 (left, blue box):
"No Safety Signal"

Arrow clockwise back to Node 1

In the CENTER of the circle:
Teal (#3A8A8C) circle with white text:
"LOCKED"

Below the circular diagram:
Arrow breaking out of the cycle pointing down to:
Teal box: "TTC Contact — Provides the safety signal directly"

Bottom text: "Restriction prevents the very feedback that would allow release."

Off-white background. Clean, clinical design."""
    },
    {
        "name": "14 Safety Signal — B (Linear Trap)",
        "output": f"{OUTPUT_BASE}/14-safety-signal-trap/14-safety-signal-b-linear.png",
        "prompt": """GRAPHIC TYPE: Linear Trap Diagram (Landscape, half page)

Title: "WHY SOME SUBLUXATIONS PERSIST"

Horizontal flow with a loop-back:

Box 1: "Meningeal Tension" (blue #2E5FA3)
→ Box 2: "Restricted Range"
→ Box 3: "Fewer Mechanoreceptor Signals"
→ Box 4: "No Safety Feedback"
→ curved arrow BACK to Box 1 (forming a visible loop)

Label on the loop-back arrow: "THE TRAP"

BELOW the loop, a separate path:
Teal (#3A8A8C) box: "TTC Meningeal Contact"
→ "Provides Direct Safety Signal"
→ "Bypasses the Trap"
→ "Tone Reorganizes"

Bottom text: "The articular approach needs movement to generate feedback. TTC provides it directly."

Off-white background. Clean design."""
    },

    # ═══ 15: CONTACT PARAMETERS — Body Silhouette ═══
    {
        "name": "15 Contact Params — A (Silhouette)",
        "output": f"{OUTPUT_BASE}/15-contact-parameters/15-contact-params-a-silhouette.png",
        "prompt": """GRAPHIC TYPE: Annotated Body Diagram (Portrait, full page)

Title: "THE FIVE CONTACT PARAMETERS"

Center: A simple, clean posterior view silhouette of a human body (flat design, blue #2E5FA3 outline, no anatomical detail — just a clean body outline). The spine is shown as a simple vertical line with slight curves.

FIVE callout labels with leader lines pointing to the spine/body:

1. "LOCATION" — leader line to upper cervical area
   Sub-text: "Where to contact"

2. "VECTOR" — leader line to mid-thoracic area with a small directional arrow
   Sub-text: "Direction of input"

3. "AMOUNT" — leader line to lower thoracic area
   Sub-text: "Least effective force"

4. "INTENT" — leader line to lumbar area with a small wave/signal icon
   Sub-text: "Congruent awareness"

5. "TIMING" — leader line to sacral area with a small clock icon
   Sub-text: "Window of receptivity"

Bottom text box (teal #3A8A8C fill, white text):
"Not how much force — how precise the engagement."

Off-white background. Medical illustration style — clean and diagrammatic."""
    },
    {
        "name": "15 Contact Params — B (Dial Panel)",
        "output": f"{OUTPUT_BASE}/15-contact-parameters/15-contact-params-b-dials.png",
        "prompt": """GRAPHIC TYPE: Five-Panel Parameter Display (Landscape, full page)

Title: "TTC CONTACT PARAMETERS"

Five equal panels in a horizontal row, each containing:

PANEL 1 — "LOCATION" (blue #2E5FA3 header)
Icon: crosshair/target symbol
Text: "Best window in"

PANEL 2 — "VECTOR" (blue header)
Icon: directional arrow
Text: "Precise direction"

PANEL 3 — "AMOUNT" (teal #3A8A8C header)
Icon: small wave (representing minimal force)
Text: "Least amount"

PANEL 4 — "INTENT" (teal header)
Icon: concentric circles (representing awareness)
Text: "Congruent presence"

PANEL 5 — "TIMING" (gold #8A6A1A header)
Icon: clock or pulse symbol
Text: "Receptive moment"

Below all panels, a single line:
"Each parameter is essential. None is sufficient alone."

Thin gray borders between panels. Off-white background."""
    },

    # ═══ 16: "MORE FORCE = MORE NOISE" — Signal Integrity ═══
    {
        "name": "16 Force-Noise — A (Waveform)",
        "output": f"{OUTPUT_BASE}/16-force-noise/16-force-noise-a-waveform.png",
        "prompt": """GRAPHIC TYPE: Waveform Comparison (Landscape, half page)

Title: "SIGNAL INTEGRITY"

TWO WAVEFORM PANELS stacked vertically:

TOP PANEL — "HIGH FORCE INPUT"
A jagged, noisy, high-amplitude waveform (blue #2E5FA3 line on white).
Multiple sharp peaks and chaotic oscillations.
Label right: "Signal lost in noise"
Amplitude scale on left axis.

BOTTOM PANEL — "MINIMAL FORCE INPUT (TTC)"
A clean, smooth, low-amplitude waveform (teal #3A8A8C line on white).
Clear, readable signal pattern.
Label right: "Signal preserved"
Same amplitude scale on left axis.

Bottom text: "The body responds to precision, not power."

Thin gray (#D1D5DB) gridlines. Off-white background. Clean data-viz style."""
    },
    {
        "name": "16 Force-Noise — B (Slider)",
        "output": f"{OUTPUT_BASE}/16-force-noise/16-force-noise-b-slider.png",
        "prompt": """GRAPHIC TYPE: Inverse Relationship Diagram (Landscape, half page)

Title: "THE FORCE-CLARITY RELATIONSHIP"

A horizontal bar/slider with:

LEFT END — labeled "MORE FORCE" (blue #2E5FA3)
Large, bold arrow icon. Filled heavily.
Below: "Overwhelms receptors"

RIGHT END — labeled "LESS FORCE" (teal #3A8A8C)
Small, precise dot icon.
Below: "Engages receptors"

BELOW the slider, an INVERTED bar showing:
LEFT END — "LESS CLARITY" (gray, faded)
RIGHT END — "MORE CLARITY" (teal, vivid)

These two bars show the inverse relationship: as force decreases, signal clarity increases.

A marker/indicator dot sits at the right end of both bars, labeled "TTC"

Bottom text: "Least amount of most effective input."

Off-white background. Clean, minimal design."""
    },

    # ═══ 17: LAYERS OF COMPENSATION — Concentric Rings ═══
    {
        "name": "17 Layers — A (Concentric)",
        "output": f"{OUTPUT_BASE}/17-layers-of-compensation/17-layers-a-concentric.png",
        "prompt": """GRAPHIC TYPE: Concentric Ring Diagram (Portrait, full page)

Title: "LAYERS OF COMPENSATION"

Concentric circles, smallest in center, largest outside:

CENTER CIRCLE (teal #3A8A8C fill, white text):
"Aberrant NeuroSpinal Tone"
Label: "THE SOURCE"

RING 2 (blue #2E5FA3 fill, white text):
"Meningeal Contracture"

RING 3 (lighter blue fill):
"Vertebral Displacement"

RING 4 (gray #6B7280 fill):
"Muscular Guarding"

RING 5 (light gray #D1D5DB fill, dark text):
"Postural Compensation"

OUTERMOST RING (very light #F3F4F6 fill):
"Symptoms"

Two arrows on the sides:
LEFT ARROW pointing inward: "TTC engages here" (pointing to center)
RIGHT ARROW pointing at outer rings: "Articular approaches engage here"

Bottom text: "Symptoms are the outermost layer. Tone is the innermost."

Off-white background."""
    },
    {
        "name": "17 Layers — B (Peel-Back)",
        "output": f"{OUTPUT_BASE}/17-layers-of-compensation/17-layers-b-peel-back.png",
        "prompt": """GRAPHIC TYPE: Layered Peel Diagram (Portrait, full page)

Title: "PEELING BACK THE LAYERS"

A vertical stack of horizontal bands, each slightly narrower than the one above, creating a pyramid/peel effect:

TOP LAYER (widest, light gray #F3F4F6):
"SYMPTOMS" — "What the patient reports"

LAYER 2 (gray #D1D5DB):
"POSTURAL COMPENSATION" — "What you observe"

LAYER 3 (medium gray #6B7280, white text):
"MUSCULAR GUARDING" — "What you palpate"

LAYER 4 (blue #2E5FA3, white text):
"VERTEBRAL DISPLACEMENT" — "What you adjust"

LAYER 5 (teal #3A8A8C, white text):
"MENINGEAL CONTRACTURE" — "What drives the displacement"

BOTTOM LAYER (narrowest, dark teal, white bold text):
"ABERRANT NEUROSPINAL TONE" — "The primary tone-setter"

Left side bracket spanning top 4 layers: "Accessible to articular approach"
Left side bracket spanning bottom 2 layers: "TTC's direct domain"

Bottom text: "Each layer compensates for the one beneath it."

Off-white background."""
    },

    # ═══ 18: D.D. PALMER PULL-QUOTE — Typographic Opener ═══
    {
        "name": "18 Palmer Quote — A (Typographic)",
        "output": f"{OUTPUT_BASE}/18-dd-palmer-quote/18-dd-palmer-a-typographic.png",
        "prompt": """GRAPHIC TYPE: Pull-Quote Typography (Landscape, half page)

A clean, elegant typographic layout:

Large opening quotation mark in blue (#2E5FA3), oversized (decorative but minimal).

Main quote text in near-black (#1A2A3A), large sans-serif:
"The determining causes of disease are traumatism, poison, and autosuggestion."

Below, in smaller text, same color:
"Life is the expression of tone."

Attribution line in gray (#6B7280), italic:
"— D.D. Palmer, 1910"

Below the quote, a thin teal (#3A8A8C) horizontal line separator.

Below the line, small teal text:
"The founder saw it. TTC builds the clinical bridge."

Generous whitespace. Off-white (#F8F8F6) background. No borders, no boxes — purely typographic.
The quote should feel authoritative and timeless."""
    },
    {
        "name": "18 Palmer Quote — B (Framed)",
        "output": f"{OUTPUT_BASE}/18-dd-palmer-quote/18-dd-palmer-b-framed.png",
        "prompt": """GRAPHIC TYPE: Framed Quote Card (Portrait, half page)

A card-style layout with thin blue (#2E5FA3) border, 2px, rounded corners.

Inside the card:

Top section — quote area with generous padding:
Large text: "Life is the expression of tone."
Medium text below: "The determining causes of disease are traumatism, poison, and autosuggestion."
Attribution: "— D.D. Palmer, The Chiropractor's Adjuster, 1910"

Thin horizontal divider (#D1D5DB)

Bottom section — context:
Three short lines:
"Palmer identified tone as foundational."
"The profession developed structural methods."
"TTC returns to tone — with clinical precision."

Each line has a small teal (#3A8A8C) bullet point.

Off-white background inside card. Slightly darker off-white outside."""
    },

    # ═══ 19: UPSTREAM INSIGHT — "Before the 5 D's" ═══
    {
        "name": "19 Upstream — A (Cascade)",
        "output": f"{OUTPUT_BASE}/19-upstream-insight/19-upstream-a-cascade.png",
        "prompt": """GRAPHIC TYPE: Extended Cascade Diagram (Portrait, full page)

Title: "WHAT COMES BEFORE THE 5 D'S?"

A vertical cascade flowing downward:

FIRST BOX (teal #3A8A8C fill, white text, LARGEST):
"ABERRANT NEUROSPINAL TONE"
Small label: "TTC's focus — the upstream cause"

Arrow down (dashed, indicating "leads to")

Then the classic 5 D's cascade, each in blue (#2E5FA3) outlined boxes:

D1: "DYSKINESIA" — "Altered movement"
Arrow down
D2: "DYSAFFERENTATION" — "Altered sensory input"
Arrow down
D3: "DYSPONESIS" — "Altered motor output"
Arrow down
D4: "DYSAUTONOMIA" — "Altered autonomic function"
Arrow down
D5: "DEGENERATION" — "Tissue breakdown"

LEFT BRACKET spanning D1-D5: "The accepted cascade"
RIGHT BRACKET spanning the top teal box: "What drives it"

Bottom text: "The 5 D's describe the progression. TTC addresses what initiates it."

Off-white background. Clean clinical design."""
    },
    {
        "name": "19 Upstream — B (Reveal)",
        "output": f"{OUTPUT_BASE}/19-upstream-insight/19-upstream-b-reveal.png",
        "prompt": """GRAPHIC TYPE: Reveal Diagram (Portrait, full page)

Title: "THE MISSING STEP"

Two versions of the same cascade, side by side:

LEFT — "CONVENTIONAL MODEL" (blue #2E5FA3 header):
Vertical flow:
"Subluxation" → D1 → D2 → D3 → D4 → D5
Standard boxes with arrows.
A question mark icon at the top above "Subluxation": "What initiates it?"

RIGHT — "TTC MODEL" (teal #3A8A8C header):
Vertical flow with ONE EXTRA BOX at top:
"Aberrant NeuroSpinal Tone" (teal fill, white text, highlighted)
→ "Subluxation" → D1 → D2 → D3 → D4 → D5

Arrow from left question mark pointing to the right's top box.

Bottom text: "TTC identifies what the conventional model leaves unexplained."

Off-white background. Clean arrows."""
    },
]


def generate_image(prompt, output_path, name, max_retries=3):
    """Generate an image using the Gemini API."""
    print(f"\n{'='*70}")
    print(f"Generating: {name}")
    print(f"{'='*70}")

    full_prompt = f"""{STYLE_GUIDE}

CRITICAL: Spell-check ALL text. Render text EXACTLY as specified. Keep labels short and legible.

{prompt}

Generate as a high-resolution print-quality image."""

    request_body = {
        "contents": [{"parts": [{"text": full_prompt}]}],
        "generationConfig": {"responseModalities": ["TEXT", "IMAGE"]}
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
                print("  No candidates")
                if attempt < max_retries - 1:
                    time.sleep(10)
                continue

            for part in candidates[0].get("content", {}).get("parts", []):
                if "inlineData" in part:
                    img_data = base64.b64decode(part["inlineData"]["data"])
                    os.makedirs(os.path.dirname(output_path), exist_ok=True)
                    with open(output_path, "wb") as f:
                        f.write(img_data)
                    print(f"  SUCCESS ({len(img_data)//1024} KB)")
                    return True
                elif "text" in part:
                    print(f"  Note: {part['text'][:150]}")

            print("  No image in response")
            if attempt < max_retries - 1:
                time.sleep(10)

        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8")[:200] if e.fp else ""
            print(f"  HTTP {e.code}: {body}")
            time.sleep(30 if e.code == 429 else 10)
        except Exception as e:
            print(f"  Error: {e}")
            if attempt < max_retries - 1:
                time.sleep(10)

    return False


def main():
    start = int(sys.argv[1]) - 1 if len(sys.argv) > 1 else 0
    end = int(sys.argv[2]) if len(sys.argv) > 2 else len(SLIDES)
    slides = SLIDES[start:end]

    print(f"Generating {len(slides)} graphics (slides {start+1}-{end})...")
    successes = 0
    for i, slide in enumerate(slides):
        success = generate_image(slide["prompt"], slide["output"], slide["name"])
        successes += int(success)
        if i < len(slides) - 1:
            time.sleep(8)

    print(f"\n{'='*70}")
    print(f"COMPLETE: {successes}/{len(slides)} succeeded")
    print(f"{'='*70}")


if __name__ == "__main__":
    main()
