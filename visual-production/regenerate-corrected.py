#!/usr/bin/env python3
"""Regenerate graphics 1, 2, 3, 5 with corrected framing.

Fixes:
- "Bone-First" → "Articular Approach" (respectful of osseous practitioners)
- Fascia de-emphasized → focus on meningeal system
- Acknowledges osseous works through mechanoreceptor-rich joint spaces

Usage:
    export GEMINI_API_KEY=$(op item get 'Google Gemini API' --fields 'credential' --reveal)
    python3 visual-production/regenerate-corrected.py
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
    # ═══ GRAPHIC 1: Concept Map (REFRAMED) ═══
    {
        "name": "01 Concept Map — A (Split)",
        "output": f"{OUTPUT_BASE}/01-concept-map/01-concept-map-a-split-v2.png",
        "prompt": """GRAPHIC TYPE: Two-Column Comparison (Portrait, full page)

Create a split comparison diagram with a bold vertical dividing line.

LEFT COLUMN — Header: "ARTICULAR APPROACH" (blue #2E5FA3 banner, white text)
Downward cascade with arrows:
1. "Segmental Analysis" (top box)
2. "Articular Adjustment" (arrow down)
3. "Mechanoreceptor Activation" (arrow down)
4. "Body's Intelligence Organizes" (arrow down)
5. "Indirect NeuroSpinal Effect" (bottom box, blue fill)

RIGHT COLUMN — Header: "MENINGEAL APPROACH (TTC)" (blue banner, white text)
Downward cascade with arrows:
1. "Global Tone Assessment" (top box)
2. "Meningeal Contact" (arrow down)
3. "Direct NeuroSpinal Engagement" (arrow down)
4. "Body's Intelligence Organizes" (arrow down)
5. "Direct Tone Reorganization" (bottom box, teal #3A8A8C fill)

Note: Step 4 is IDENTICAL in both columns — both approaches rely on the body's intelligence.

At the bottom center: "Both facilitate the body's intelligence. TTC engages the NeuroSpinal System directly."

Rounded rectangles. Near-black text. Off-white background."""
    },
    {
        "name": "01 Concept Map — B (Circular)",
        "output": f"{OUTPUT_BASE}/01-concept-map/01-concept-map-b-circular-v2.png",
        "prompt": """GRAPHIC TYPE: Dual Pathway Diagram (Portrait, full page)

TWO PATHWAYS, both starting from the same point and ending at the same destination.

TOP CENTER: Large oval "BODY'S INTELLIGENCE" — this is the shared foundation.

Two pathways descend from it:

LEFT PATH — "ARTICULAR PATHWAY" (blue #2E5FA3)
Vertical flow:
"Joint Space Contact" → "Mechanoreceptor Input" → "Indirect NeuroSpinal Influence"

RIGHT PATH — "MENINGEAL PATHWAY (TTC)" (teal #3A8A8C)
Vertical flow:
"Meningeal Contact" → "Direct NeuroSpinal Engagement" → "Direct Tone Reorganization"

BOTH PATHS CONVERGE at bottom to: "Self-Correction and Adaptation"

Between the two paths at center: "Different access point. Same intelligence."

Clean arrows, rounded rectangles. Off-white background."""
    },
    {
        "name": "01 Concept Map — C (Iceberg)",
        "output": f"{OUTPUT_BASE}/01-concept-map/01-concept-map-c-iceberg-v2.png",
        "prompt": """GRAPHIC TYPE: Iceberg / Depth Diagram (Portrait, full page)

An iceberg diagram showing depth of access to the NeuroSpinal System.

ABOVE THE WATERLINE (labeled "ARTICULAR ACCESS"):
- "Joint Mechanics" (in a box)
- "Segmental Correction" (in a box)
- "Mechanoreceptor Input" (in a box)
- Small text: "Influences NeuroSpinal tone indirectly"

THE WATERLINE: A horizontal wavy blue line, labeled "Surface"

BELOW THE WATERLINE (labeled "MENINGEAL ACCESS (TTC)"):
- "Aberrant NeuroSpinal Tone" (largest box, teal fill)
- "Meningeal Contracture" (medium box below)
- "Dural Tension Patterns" (deepest box)
- Small text: "Engages NeuroSpinal System directly"

Left side text: "Articular approaches reach here" with arrow to above waterline
Right side text: "TTC engages here" with arrow to below waterline

IMPORTANT: Both approaches are valid. The distinction is depth of access, not quality of care.

Blue (#2E5FA3) for water. Off-white above. Near-black text."""
    },

    # ═══ GRAPHIC 2: Outcome Variance (REFRAMED — no fascia) ═══
    {
        "name": "02 Outcome Variance — A (Stacked Bar)",
        "output": f"{OUTPUT_BASE}/02-outcome-variance/02-outcome-variance-a-stacked-bar-v2.png",
        "prompt": """GRAPHIC TYPE: Stacked Bar Chart (Landscape, half page)

Single horizontal stacked bar:
- Left segment (40%, blue #2E5FA3): "Segmental Mechanics"
- Middle segment (35%, teal #3A8A8C): "NeuroSpinal Tone"
- Right segment (25%, dark gold #8A6A1A): "Other Variables"

Title: "WHAT EXPLAINS CLINICAL OUTCOMES?"

Below the bar, callout arrow to teal segment: "Articular approaches influence tone indirectly. TTC engages the NeuroSpinal System directly."

Flat color fills, thin gray borders. Off-white background."""
    },
    {
        "name": "02 Outcome Variance — B (Pie)",
        "output": f"{OUTPUT_BASE}/02-outcome-variance/02-outcome-variance-b-pie-v2.png",
        "prompt": """GRAPHIC TYPE: Pie Chart (Landscape, half page)

Pie chart with 3 segments:
- 40% (blue #2E5FA3): "Segmental Mechanics"
- 35% (teal #3A8A8C): "NeuroSpinal Tone"
- 25% (gray #6B7280): "Other Factors"

Teal segment "exploded" (pulled out). Leader line to callout: "Where TTC focuses directly"

Title: "FACTORS IN CLINICAL OUTCOMES"

Flat design, no 3D. Percentage labels in white bold inside segments. Off-white background."""
    },
    {
        "name": "02 Outcome Variance — C (Scale)",
        "output": f"{OUTPUT_BASE}/02-outcome-variance/02-outcome-variance-c-scale-v2.png",
        "prompt": """GRAPHIC TYPE: Balance Scale (Portrait, half page)

Balance/seesaw diagram.

LEFT SIDE (tilting down, heavier):
Stack of 3 boxes: "NeuroSpinal Tone", "Meningeal State", "Dural Tension"
Label: "TONAL FACTORS"

RIGHT SIDE (tilting up, lighter):
Single box: "Segmental Mechanics"
Label: "STRUCTURAL FACTORS"

Title: "WHAT DRIVES CLINICAL OUTCOMES?"
Subtitle: "Articular approaches influence tone through joint mechanics. TTC addresses it directly."

Blue boxes left. Teal box right. Gray fulcrum. Off-white background."""
    },

    # ═══ GRAPHIC 3: Clinical Flowcharts (REFRAMED — respectful) ═══
    {
        "name": "03 Clinical Flowchart — A (Parallel)",
        "output": f"{OUTPUT_BASE}/03-clinical-flowchart/03-clinical-flowchart-a-parallel-v2.png",
        "prompt": """GRAPHIC TYPE: Parallel Flowcharts (Portrait, full page)

LEFT FLOWCHART — Title: "ARTICULAR APPROACH"
Blue (#2E5FA3) outlines:
1. [Oval] "Patient Presents"
2. → [Rectangle] "Segmental Analysis"
3. → [Diamond] "Subluxation Found?"
4. YES → [Rectangle] "Articular Adjustment"
5. → [Rectangle] "Mechanoreceptor Input"
6. → [Diamond] "Body Reorganizing?"
7. YES → [Oval] "Monitor Progress"
7. NO → [Rectangle] "Reassess and Adjust"

RIGHT FLOWCHART — Title: "TTC APPROACH"
Teal (#3A8A8C) outlines:
1. [Oval] "Patient Presents"
2. → [Rectangle] "Assess Global Tone"
3. → [Rectangle] "Tonal Pressure Testing"
4. → [Diamond] "Receptivity Found?"
5. YES → [Rectangle] "Meningeal Contact"
6. → [Rectangle] "Allow Integration"
7. → [Diamond] "Tone Reorganizing?"
8. YES → [Oval] "Monitor Tone"

Standard flowchart symbols. Off-white background. Near-black text."""
    },
    {
        "name": "03 Clinical Flowchart — B (Diverging)",
        "output": f"{OUTPUT_BASE}/03-clinical-flowchart/03-clinical-flowchart-b-diverging-v2.png",
        "prompt": """GRAPHIC TYPE: Diverging Pathway (Portrait, full page)

START (top center):
[Oval] "Patient with Subluxation"
[Arrow down]
[Diamond] "Assessment Approach?"

LEFT BRANCH (blue #2E5FA3) — "ARTICULAR":
[Rectangle] "Segmental Analysis"
→ [Rectangle] "Articular Adjustment"
→ [Rectangle] "Mechanoreceptors Engaged"
→ [Oval] "Body's Intelligence Organizes"

RIGHT BRANCH (teal #3A8A8C) — "TTC":
[Rectangle] "Global Tone Assessment"
→ [Rectangle] "Find Receptivity"
→ [Rectangle] "Meningeal Contact"
→ [Oval] "Body's Intelligence Organizes"

Note: BOTH endpoints read "Body's Intelligence Organizes" — identical.

Bottom bracket: "Same destination. Different access point."

Off-white background. Standard flowchart symbols."""
    },

    # ═══ GRAPHIC 5: Meningeal Anatomy (REFRAMED — meningeal focus) ═══
    {
        "name": "05 Meningeal Anatomy — A (Four Panel)",
        "output": f"{OUTPUT_BASE}/05-meningeal-anatomy/05-meningeal-anatomy-a-four-panel-v2.png",
        "prompt": """GRAPHIC TYPE: Four-Panel Progressive Anatomy (Portrait, full page)

2x2 grid, each panel building on the previous. Medical illustration style — clean line art, NOT photorealistic.

PANEL 1 (top-left) — "BASIC ANATOMY"
Sagittal cross-section of spinal canal:
- Vertebral body (gray rectangle)
- Spinal cord (blue #2E5FA3 oval center)
- Dura mater (teal #3A8A8C line surrounding cord)
- Epidural space (white gap)
Labels with leader lines.

PANEL 2 (top-right) — "MENINGEAL LAYERS"
Same cross-section showing the THREE meningeal layers:
- Pia mater (innermost, thin green line on cord surface)
- Arachnoid (middle, dotted line)
- Dura mater (outermost, thick teal line)
- CSF space between pia and arachnoid
- Dentate ligaments connecting pia to dura
Label: "The Multilayered Meningeal System"

PANEL 3 (bottom-left) — "MECHANORECEPTORS"
Same view plus:
- Small dots along the dura representing mechanoreceptors
- Highlighted receptor-dense zones
- Arrows showing mechanoreceptor signaling to CNS
Label: "Receptor-Rich Meningeal Tissues"

PANEL 4 (bottom-right) — "TENSION TRANSMISSION"
Same view plus:
- Gold (#8A6A1A) stress lines through meningeal system
- Arrows showing how meningeal tension transmits to vertebral structures
- A vertebra being displaced by tension vectors
Label: "How Meningeal Tension Drives Structure"

Numbered panels (1-4). Off-white background. Thin gray borders."""
    },
    {
        "name": "05 Meningeal Anatomy — B (Longitudinal)",
        "output": f"{OUTPUT_BASE}/05-meningeal-anatomy/05-meningeal-anatomy-b-longitudinal-v2.png",
        "prompt": """GRAPHIC TYPE: Longitudinal Spine View (Portrait, full page)

Full-length sagittal spine from skull base to sacrum:
- Vertebrae as stacked rectangles (gray #D1D5DB)
- Spinal cord as continuous blue (#2E5FA3) line
- Dura mater as teal (#3A8A8C) sheath surrounding cord
- Pia mater as thin inner line on cord surface

KEY FEATURES:
- Top: "Cranial Dural Attachment" label with arrow
- Bottom: "Sacral Dural Attachment" label with arrow
- Along the length: "The NeuroSpinal Continuum" label

Show 3 areas of "aberrant meningeal tension" as gold (#8A6A1A) highlighted zones where the dura is contracted, with stress lines radiating outward to adjacent vertebrae.

Brief note at bottom: "The outer dural sheath extends into surrounding fascia, positioning the NeuroSpinal System as a primary tone-setter for the entire body."

Title: "THE NEUROSPINAL SYSTEM: PRIMARY TONE-SETTER"

Clean line art. Off-white background."""
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
    successes = 0
    for i, slide in enumerate(SLIDES):
        success = generate_image(slide["prompt"], slide["output"], slide["name"])
        successes += int(success)
        if i < len(SLIDES) - 1:
            time.sleep(8)

    print(f"\n{'='*70}")
    print(f"COMPLETE: {successes}/{len(SLIDES)} succeeded")
    print(f"{'='*70}")


if __name__ == "__main__":
    main()
