# Lab 7 — Run the Meeting-to-Drive Follow-Up Workflow

**Course:** Google Workspace with Gemini  
**Course Code:** C155  
**Version:** v1.0 (28 July 2026)  
**Topic 4:** AI-Powered Workflows and Automation in Workspace  
**Maps to:** LO4: review AI-assisted meeting notes, organise approved Drive sources and produce a permission-aware follow-up brief  
**Duration:** 70 minutes  
**Tools:** Google Meet - Gemini meeting features where available - Google Drive - Docs - Sheets

---

## Goal

Convert a synthetic rehearsal meeting into verified actions and a source-cited Drive brief without confusing generated notes with an approved record.

## What You Will Do

You will configure or simulate a Gemini-supported meeting-notes workflow, review a supplied transcript, correct owners and dates, and organise the project's approved Drive sources. Gemini in Drive or a manual fallback then produces a source-cited follow-up brief.

## What You Will Build

A 07-meeting-notes-review Google Doc, a 07-source-register Google Sheet and a 07-approved-follow-up-brief Google Doc containing three verified actions, one open question, source citations, sharing controls and a correction log.

## Prerequisites

- Approved communication pack, Slides deck and 05-registration-analysis from Labs 3-6.
- Open labs/assets/meeting-transcript.txt and labs/assets/workflow-control-checklist.md.
- Use the supplied transcript if Take notes for me is unavailable or not enabled by the administrator.

> **Data note.** Use only the supplied synthetic scenario and an account you are authorised to use. Do not paste passwords, secrets, protected personal data or confidential workplace content into a prompt. Keep live sending disabled until the lab explicitly calls for one reviewed draft to your own account.

## Steps

### 1. Create a Google Doc in 02-Working named 07-meeting-notes-review. Add headings Controls, Generated or practice notes, Verified decisions, Verified actions, Open questions, Correction log and Sharing decision. Under Controls record feature status, host, participant notice, permitted content, note recipients, language, source and reviewer.

```text
Feature status: Available demonstration | Transcript fallback
Sharing default for this lab: Restricted; learner and named reviewer only
```

### 2. If Take notes for me is available in a trainer-hosted practice meeting, observe the notice and sharing controls and export the notes after the demonstration. Otherwise copy the Meeting notes candidate section from meeting-transcript.txt into Generated or practice notes. Do not create a real meeting with external people for this lab.

```text
Fallback source: labs/assets/meeting-transcript.txt
Generated notes remain a candidate until checked against the transcript.
```

### 3. Read the full transcript and create tables for Verified decisions and Verified actions. Actions must have Action, Owner, Due or PENDING, Source lines, Status and Reviewer. Compare the candidate notes with the transcript and record each wrong owner, wrong date, omitted qualification or unsupported commitment in the Correction log.

```text
Expected action owners after review: Jamie | Marcus | Noor
Expected open question: final facilitator confirmation
Do not change a PENDING field without transcript evidence.
```

### 4. Create a Google Sheet in 02-Working named 07-source-register with columns File, State, Owner, Purpose, Controlling section or range, Last reviewed, Access and Used by. Add the approved grounded briefing, communication pack, Slides deck and registration Sheet. Add 07-meeting-notes-review as WORKING until its correction log is complete.

```text
State values: SOURCE | WORKING | APPROVED | ARCHIVE
Access values: Restricted | Named collaborators | Link viewer
```

### 5. Organise C155-Aster-Finch so original supplied sources remain in 01-Source, current work-in-progress files remain in 02-Working, reviewed course outputs are in 03-Approved and no obsolete file remains mixed with current work. Do not delete files; move a superseded copy to 04-Archive and update the register if one exists.

```text
Control check: every registered file has one current state, one owner and one controlling section or range.
```

### 6. Create a Google Doc in 02-Working named 07-approved-follow-up-brief. In Gemini in Drive, select only the approved communication pack, Slides deck, registration Sheet and reviewed meeting notes, then ask for the structure below. If Gemini in Drive is unavailable, open the registered files and create the same brief manually.

```text
Using only the four selected C155 project sources, create a follow-up brief with Confirmed event plan, Verified registration insight, Decisions, Actions, Open question and Source citations. For every section name the exact source filename and section or range. Do not use files in 04-Archive. Preserve PENDING and distinguish an observed metric from a meeting decision.
```

### 7. Open every source cited by the follow-up brief and verify the statement. Apply G-E-A-R, record the final reviewer and change the sharing setting to Restricted or named training collaborators only. Move the reviewed meeting notes, source register and follow-up brief to 03-Approved when all checks pass.

```text
Final checks: 3 actions | 1 open question | counts 20 valid and 4 exclusions | chart values 8/8/4 | all citations open | no Archive source | sharing matches the recorded decision
```

## Test It

The meeting-notes review must show control settings, three verified actions owned by Jamie, Marcus and Noor, one facilitator open question and a correction log. The source register must cover five current project artifacts with state, owner, range and access. The follow-up brief must cite exact filenames, retain 20 valid/4 excluded and 8/8/4 segment counts, use no Archive source and have a sharing setting that matches the recorded decision.

## Checkpoint and Rejoin Point

Keep 07-meeting-notes-review, 07-source-register and 07-approved-follow-up-brief in 03-Approved. Lab 8 uses the three verified actions and source register to define one draft-only automation.

## Troubleshooting

| If this happens | Fix |
|---|---|
| Take notes for me is unavailable or requires a different plan. | Record Transcript fallback and use meeting-transcript.txt; do not change accounts or move restricted content. |
| Gemini in Drive cites a draft or an Archive file. | Clear selected sources, choose only files marked APPROVED in the register and rerun with the explicit state rule. |
| An invitee can see the notes attachment but cannot open it. | Remember that event visibility is not file permission; set access according to the recorded sharing decision. |

## Challenge

Create a before-and-after table that shows the candidate note, corrected note, evidence line and possible consequence for each correction. Use it to propose one prompt or meeting practice improvement.

## Reflection

Which meeting-note error would have caused the largest downstream problem, and where did the workflow stop it?

---

[← Lab 6](lab-06-analyse-registrations-and-build-the-decision-dashboard.md) · [Lab 8 →](lab-08-automate-the-approved-follow-up-from-sheets.md)
