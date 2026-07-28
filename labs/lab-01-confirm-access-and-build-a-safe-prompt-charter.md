# Lab 1 — Confirm Access and Build a Safe Prompt Charter

**Course:** Google Workspace with Gemini  
**Course Code:** C155  
**Version:** v1.0 (28 July 2026)  
**Topic 1:** Getting Started with Gemini in Google Workspace  
**Maps to:** LO1: explain Gemini access, prompt structure and responsible controls across Google Workspace  
**Duration:** 60 minutes  
**Tools:** Google Drive - Docs - Sheets - Gemini features where available - supplied synthetic source pack

---

## Goal

Verify the available Workspace features and create the source, prompt and review rules that govern every later lab.

## What You Will Do

You will create the C155 project folder, check Gemini and fallback availability across Workspace, classify the supplied synthetic sources and write a reusable P-T-C-F prompt charter. The charter keeps sources, uncertainty, sharing and human approval visible.

## What You Will Build

A C155-Aster-Finch Drive folder with four state subfolders, an 01-access-matrix sheet and a 01-prompt-charter document containing approved sources, prohibited inputs, a reusable prompt pattern and the G-E-A-R review gate.

## Prerequisites

- Sign in to a Google account authorised for training and open labs/assets/aster-finch-project-brief.md.
- Open labs/assets/facts-and-policies.md and labs/assets/prompt-quality-checklist.md.
- Do not use workplace records; the supplied files are entirely synthetic.

> **Data note.** Use only the supplied synthetic scenario and an account you are authorised to use. Do not paste passwords, secrets, protected personal data or confidential workplace content into a prompt. Keep live sending disabled until the lab explicitly calls for one reviewed draft to your own account.

## Steps

### 1. In Google Drive, create a folder named C155-Aster-Finch. Inside it create exactly 01-Source, 02-Working, 03-Approved and 04-Archive. Upload aster-finch-project-brief.md, facts-and-policies.md and prompt-quality-checklist.md to 01-Source. Keep sharing set to Restricted.

```text
Expected path:
C155-Aster-Finch/
  01-Source/
  02-Working/
  03-Approved/
  04-Archive/
```

### 2. Create a Google Sheet in 02-Working named 01-access-matrix. Add the headers App, Account type, Gemini entry point, Status, Safe fallback and Admin issue. Create rows for Gmail, Docs, Sheets, Slides, Drive, Meet and Apps Script. Open each app in a new tab and record Available, Trainer demo or Manual fallback; do not guess from a help page.

```text
Status values: Available | Trainer demo | Manual fallback
Safe fallbacks: supplied source or transcript | normal app feature | trainer demonstration
```

### 3. In 01-access-matrix add a second tab named Data boundary. Enter Public, Internal, Confidential and Restricted as four rows. For each row add Allowed training example, Handling rule and Not allowed. Classify the three supplied files as Synthetic training data. Explicitly prohibit passwords, access tokens, private customer records and unapproved confidential content.

```text
Rule: use the minimum approved fields for the stated task; UNKNOWN replaces an unsupported detail.
```

### 4. Create a Google Doc in 02-Working named 01-prompt-charter. Add headings Purpose, Approved sources, Prohibited inputs, Persona, Task, Context, Format, Source boundary, Review criteria, Output destination and Human approver. Fill every heading from the project brief and facts file. Use PENDING for the approver name if no role has been assigned.

```text
Persona: I am a workplace coordinator preparing a synthetic partner briefing.
Task: Create <ARTIFACT> for <AUDIENCE> so they can <DECISION OR ACTION>.
Context: Use only <NAMED APPROVED FILES OR EXCERPTS>.
Format: Return <STRUCTURE, LENGTH, TONE AND REQUIRED FIELDS>.
Source boundary: If a detail is absent, write UNKNOWN and list the question; do not infer it.
Review: End with a G-E-A-R table for Grounding, Evidence, Audience and Risk.
```

### 5. Run the charter prompt in Gemini in Docs or another available in-app Gemini control. Ask for a five-bullet briefing outline using only the two approved source files. If the feature is unavailable, use the trainer demonstration response in labs/assets/sample-gemini-output.md. Paste the result under Initial response.

```text
Create a five-bullet outline for the Aster & Finch Partner Operations Briefing. Use only the attached or pasted project brief and facts file. Include Purpose, Audience, Confirmed facts, Open questions and Next action. Write UNKNOWN for unsupported details and end with a G-E-A-R review table.
```

### 6. Compare the response with prompt-quality-checklist.md. Under Review record at least one source check, one audience edit and one risk check. Write a refined prompt that repairs the largest defect. If Gemini is available, run the refined prompt once and paste the result under Refined response. If Gemini is unavailable, duplicate the initial fallback, manually apply the refined instruction, label it Manual refined fallback and record every edit. Finish with Approver, Decision and Destination; keep Decision as WORKING until a partner checks it.

```text
Iteration record:
Defect: <OBSERVED PROBLEM>
Changed instruction: <ONE CHANGE>
Result: <OBSERVABLE IMPROVEMENT>
Approver: <ROLE OR PENDING>
Decision: WORKING
Destination: 02-Working
```

## Test It

Open the Drive folder and both artifacts. There must be four correctly named state folders; 01-access-matrix must have seven app rows and four data-boundary rows; 01-prompt-charter must contain all eleven headings, one initial and one generated or manually refined second response, UNKNOWN for unsupported details, four G-E-A-R checks and a visible WORKING decision.

## Checkpoint and Rejoin Point

Keep the approved source files in 01-Source and the two Lab 1 artifacts in 02-Working. Labs 2-8 must reuse the same source boundary, P-T-C-F structure and G-E-A-R review.

## Troubleshooting

| If this happens | Fix |
|---|---|
| Ask Gemini or another AI control is missing. | Record the feature as Trainer demo or Manual fallback and use sample-gemini-output.md without moving the source to an unapproved service. |
| The response invents a date, venue or speaker. | Replace it with UNKNOWN and add the exact source-boundary instruction before rerunning. |
| A source file is visible from the wrong account. | Stop, remove unintended sharing and continue only from the authorised training account. |

## Challenge

Rewrite the prompt for a senior leader and for an operations coordinator. Keep the same facts and compare which Persona, Format and Audience instructions legitimately change.

## Reflection

Which control in your charter prevents the most consequential failure, and what evidence shows that it was applied?

---

[← Labs index](README.md) · [Lab 2 →](lab-02-produce-and-verify-a-grounded-workspace-briefing.md)
