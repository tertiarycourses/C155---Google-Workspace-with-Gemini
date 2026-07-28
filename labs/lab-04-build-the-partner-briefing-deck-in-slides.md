# Lab 4 — Build the Partner Briefing Deck in Slides

**Course:** Google Workspace with Gemini  
**Course Code:** C155  
**Version:** v1.0 (28 July 2026)  
**Topic 2:** Gemini in Docs, Slides and Gmail  
**Maps to:** LO2: create and refine a coherent source-backed presentation and appropriate generated visual in Google Slides  
**Duration:** 70 minutes  
**Tools:** Google Slides - Gemini in Slides where available - Google Docs - Drive

---

## Goal

Turn the approved communication pack into a concise six-slide story with traceable evidence, accessible design and a reviewed visual.

## What You Will Do

You will design a slide sequence before generating content, build six low-density slides from approved facts and create one illustrative visual with Gemini or a native-shape fallback. A slide map and G-E-A-R ledger keep the story, evidence and audience action aligned.

## What You Will Build

A Google Slides file named 04-partner-briefing-deck with six slides, speaker notes and one reviewed visual, plus a slide-map table in 03-partner-communication-pack linking each slide to its message, source, visual purpose and audience action.

## Prerequisites

- Approved 03-partner-communication-pack and approved 02-grounded-briefing.
- The Gmail message remains an unsent draft; use the approved Doc as the source.
- Open labs/assets/prompt-quality-checklist.md for the final sequence review.

> **Data note.** Use only the supplied synthetic scenario and an account you are authorised to use. Do not paste passwords, secrets, protected personal data or confidential workplace content into a prompt. Keep live sending disabled until the lab explicitly calls for one reviewed draft to your own account.

## Steps

### 1. In the approved communication pack add a heading Slide map and a table with Slide, Audience question, One-sentence message, Evidence source, Visual purpose and Audience action. Create exactly six rows: Welcome, Why this briefing, Confirmed plan, How partners prepare, Coordination workflow and Next steps.

```text
Rule: each slide has one primary message and names an approved source or SOURCE NOT REQUIRED.
```

### 2. Create a blank Google Slides presentation in 02-Working named 04-partner-briefing-deck. Add six slides using the slide-map titles. Use a 16:9 layout, one consistent theme, title text of at least 28 pt and body text of at least 18 pt. Add the source filename and section to the speaker notes of slides 2-6.

```text
Deck order:
1 Welcome
2 Why this briefing
3 Confirmed plan
4 How partners prepare
5 Coordination workflow
6 Next steps
```

### 3. In Gemini in Slides, or in Gemini in Docs if the Slides control is unavailable, ask for candidate content for slides 2-6 using only the approved briefing and communication pack. Require one headline, no more than three short bullets and one evidence note per slide. If neither Gemini control is available, manually convert each slide-map row into that same headline, bullet and evidence-note structure using only the two approved artifacts. Insert only content that matches the slide map and source ledger.

```text
Create candidate text for slides 2-6. Use only the approved Aster & Finch briefing and communication pack. For each slide return Title, one-sentence headline, up to three bullets and Source. Preserve PENDING fields; do not invent a venue, speaker, URL, quotation or result.
```

### 4. Create one wide illustrative image for slide 1 or 2 with Gemini in Slides. Use an abstract collaboration scene with no logos, text, faces, real venue or documentary claim. If image generation is unavailable, build a native visual with three labelled circles: Partners, Evidence and Action, connected by arrows. Add alt text that explains the visual purpose.

```text
Visual prompt: Wide 16:9 editorial illustration of diverse abstract shapes collaborating around shared documents and data, calm blue and green palette, generous empty space on the left for a title, no text, no logos, no identifiable people, no photorealistic event venue.
```

### 5. Design slides 3-5 with one simple visual structure each: a confirmed-versus-pending table, a three-step preparation flow and a Source-to-Action workflow. Keep every PENDING field visible and do not shrink text below the stated sizes. On slide 3, add a bordered rectangle beside or below the confirmed-versus-pending table labelled DATA PLACEHOLDER - verified registration chart added in Lab 6. Add a final action and owner to slide 6.

```text
Slide 3 placeholder: DATA PLACEHOLDER - verified registration chart added in Lab 6
Preparation flow: Review brief -> Bring questions -> Confirm accessibility needs
Workflow: Approved source -> Gemini candidate -> Human review -> Partner action
```

### 6. Run a full-deck G-E-A-R review. Compare each slide with the slide map and speaker-note source, check titles and numbers against the claim ledger, then present the deck in full screen. Record PASS or REPAIR for Story sequence, Source match, Text readability, Visual accuracy, Alt text, PENDING fields and Final action. Apply repairs before moving the file. Record the seven checks in 03-partner-communication-pack under a Deck review heading.

```text
Required review rows: Story sequence | Source match | Text readability | Visual accuracy | Alt text | PENDING fields | Final action
```

## Test It

The Slides file must contain exactly six slides in the mapped order; slides 2-6 must each have a speaker-note source; no slide may exceed one headline and three bullets; one reviewed visual must have alt text; the preparation and workflow visuals must use the stated sequence; slide 3 must include the labelled DATA PLACEHOLDER; and all seven final review rows must be recorded under Deck review in 03-partner-communication-pack and show PASS.

## Checkpoint and Rejoin Point

Move 04-partner-briefing-deck to 03-Approved and keep the completed slide map in the approved communication pack. Lab 6 will replace only the labelled DATA PLACEHOLDER on slide 3 with a verified Sheets chart.

## Troubleshooting

| If this happens | Fix |
|---|---|
| Gemini creates unsupported speakers, dates or results. | Remove them, add the source filenames and require PENDING for absent fields before generating again. |
| The generated visual looks like a photograph of a real event. | Regenerate as an abstract editorial illustration or use the native-shape fallback and label it illustrative. |
| The slide title or bullets wrap into a crowded layout. | Shorten the message, split no additional slides and keep the minimum font sizes instead of shrinking text. |

## Challenge

Create an alternate title-slide visual for a senior executive audience. Explain how the visual purpose changes while the approved facts and slide sequence remain constant.

## Reflection

Which slide contributes most to the decision path, and what would be lost if it were replaced by a decorative image?

---

[← Lab 3](lab-03-draft-the-partner-communication-pack-in-docs-and-gmail.md) · [Lab 5 →](lab-05-clean-the-registration-tracker-and-generate-formulas.md)
