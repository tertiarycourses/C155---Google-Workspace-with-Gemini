# Lab 8 — Automate the Approved Follow-Up from Sheets

**Course:** Google Workspace with Gemini  
**Course Code:** C155  
**Version:** v1.0 (28 July 2026)  
**Topic 4:** AI-Powered Workflows and Automation in Workspace  
**Maps to:** LO4: design, implement and verify a bounded Apps Script automation that connects Sheets and Gmail  
**Duration:** 75 minutes  
**Tools:** Google Sheets - Apps Script - Gmail Drafts - Gemini in Workspace where available

---

## Goal

Create and verify one reviewed Gmail draft when Apps Script is available, or complete an evidence-labelled code trace when it is blocked, while keeping sending manual.

## What You Will Do

You will use the approved follow-up evidence to specify a low-risk automation, ask Gemini to explain or draft the code and compare it with the supplied safe script. When Apps Script is available, the script first logs an intended action, then creates one Gmail draft to your own address and refuses to duplicate it. When access is blocked, you trace the same controls and clearly leave live evidence pending.

## What You Will Build

An Automation tab and CONTROL canvas in 05-registration-analysis plus either (a) a bound Apps Script project using apps-script-draft.gs, one reviewed Gmail draft to the learner's own account and a run log, or (b) a four-case code trace with live evidence explicitly pending. Both paths cover dry-run, live-run, HOLD and duplicate-prevention behaviour.

## Prerequisites

- Approved 07-approved-follow-up-brief and three verified actions from Lab 7.
- Open labs/assets/apps-script-draft.gs and labs/assets/workflow-control-checklist.md.
- Apps Script access may require administrator approval; use the code walk-through fallback if blocked.
- Know the learner's own training email address; no other live recipient is permitted.

> **Data note.** Use only the supplied synthetic scenario and an account you are authorised to use. Do not paste passwords, secrets, protected personal data or confidential workplace content into a prompt. Keep live sending disabled until the lab explicitly calls for one reviewed draft to your own account.

## Steps

### 1. In 05-registration-analysis add a tab named CONTROL. Copy the headings Context, Owner, Needed inputs, Task sequence, Review, Output destination and Learning signal. Define a manual trigger that reads one READY row, creates a Gmail draft only, writes DRAFTED plus an ID and timestamp, skips HOLD or processed rows and leaves Send as a human action.

```text
Required limits: manual run | one learner-owned recipient | no auto-send | no delete | no permission change | log every result
```

### 2. Add an Automation tab with headers Status, Email, Contact_Name, Subject, Body, Draft_Status, Draft_ID, Drafted_At and Last_Run_Note. In row 2 enter READY, your own training email, Your Name, [C155 TEST] Aster & Finch partner follow-up and a 100-150 word body based on one verified Lab 7 action. In row 3 enter HOLD and hold@example.com.

```text
Row 2 recipient must be the learner's own account.
Row 3 is a synthetic HOLD row and must never produce a draft.
Leave Draft_Status, Draft_ID, Drafted_At and Last_Run_Note blank.
```

### 3. Ask Gemini in Docs, Sheets or the trainer demonstration to explain how a bound Apps Script could satisfy the CONTROL canvas. Require a dry-run constant, header-based columns, email validation, signed-in-user recipient check, a one-eligible-row limit, READY filter, duplicate prevention, Gmail draft instead of send and an execution log. Compare the response line by line with apps-script-draft.gs and list any missing control before using the supplied script.

```text
Explain a beginner Google Apps Script for a Sheet named Automation. It must process only READY rows with blank Draft_Status, stop when more than one row is eligible, require the recipient to match Session.getEffectiveUser(), validate the email, support DRY_RUN, use GmailApp.createDraft only when live, write DRAFTED/ID/timestamp, log each outcome, skip HOLD and skip processed rows. Do not use GmailApp.sendEmail, delete, share or change file permissions.
```

### 4. If Apps Script access is available, choose Extensions > Apps Script, replace the editor content with apps-script-draft.gs, save the project as C155 Follow-Up Draft Lab and confirm const DRY_RUN = true. Select runFollowUpDrafts and click Run, review permissions before allowing them, then open the execution log and Automation row 2. If Apps Script is blocked, do not paste or run code; record Access blocked and proceed to the four-case trace in Step 6.

```text
Available-path dry run: log contains DRY RUN; Last_Run_Note starts DRY RUN OK; Draft_Status, Draft_ID and Drafted_At remain blank; Gmail has no new C155 TEST draft.
Blocked path: Access blocked recorded; no execution or Gmail-draft claim.
```

### 5. On the available path, change only const DRY_RUN = true to const DRY_RUN = false, save and run runFollowUpDrafts again. Open Gmail Drafts and inspect the message without sending it. Verify recipient, subject, body, source facts and absence of unintended Cc/Bcc or attachment. On the blocked path, skip this execution and keep Draft_Status, Draft_ID and Drafted_At blank.

```text
Available-path live run: exactly one unsent draft with subject [C155 TEST] Aster & Finch partner follow-up; row 2 Draft_Status = DRAFTED; Draft_ID and Drafted_At are populated.
Blocked path: no draft created; all live-result fields remain blank.
```

### 6. If Apps Script access is available, run runFollowUpDrafts a third time without changing the Sheet. Confirm that no second draft is created and row 3 remains HOLD with blank draft fields. Record all three runs in CONTROL with Mode, Input row, Intended action, Observed result, Evidence and Decision. If Apps Script is blocked, use the supplied script and CONTROL to trace four cases: dry READY self, live READY self, repeat DRAFTED and HOLD. For each case record the expected code branch, Sheet writes and Gmail effect; keep live evidence fields blank and do not claim a draft ran.

```text
Available path: 1 DRY_RUN -> no draft | 2 LIVE -> one draft and DRAFTED | 3 LIVE repeat -> no duplicate | HOLD -> no action
Blocked path: four traced cases with expected branch, Sheet writes and Gmail effect; live result remains PENDING
```

### 7. Complete the final G-E-A-R and CONTROL review. Keep the Gmail item as a draft or delete it manually after documenting the test; do not send it. Record which authorisation scope was requested, which data fields the script reads, how it stops duplicates and what would need manager or administrator approval before any workplace pilot.

```text
Final decision values: SAFE COURSE TEST COMPLETE | CODE WALK-THROUGH COMPLETE - LIVE TEST PENDING | HOLD FOR REPAIR
Workplace expansion is outside this lab and requires a new owner, data and recipient review.
```

## Test It

CONTROL must define all seven fields and the stated limits; Automation must contain one READY self-addressed row and one HOLD synthetic row. On the available path, dry run must create no draft, live run must create exactly one unsent C155 TEST Gmail draft and write DRAFTED, ID and timestamp, the repeat run must create no duplicate and HOLD must remain untouched. On the blocked path, CONTROL must trace dry READY self, live READY self, repeat DRAFTED and HOLD with the expected branch, Sheet writes and Gmail effect; live evidence fields must remain blank and the decision must be CODE WALK-THROUGH COMPLETE - LIVE TEST PENDING. The relevant run record and final human decision must be complete.

## Checkpoint and Rejoin Point

Retain the Sheet, supplied script and either the available-path execution evidence and unsent test draft or the blocked-path four-case trace with live evidence pending. Do not enable a time trigger, bulk rows or external recipients in this course.

## Troubleshooting

| If this happens | Fix |
|---|---|
| Extensions > Apps Script is blocked. | Use the four-case alternative trace in Step 6, leave live evidence blank and record CODE WALK-THROUGH COMPLETE - LIVE TEST PENDING. |
| The script says a required header is missing. | Compare the nine Automation headers character for character and remove leading or trailing spaces. |
| A second draft appears after the repeat run. | Stop, keep sending disabled and confirm the script skips any row whose Draft_Status is not blank. |
| The script reports more than one unprocessed READY row. | Keep DRY_RUN true, change every unintended row to HOLD and continue only when exactly one self-addressed READY row remains. |
| The script cannot confirm the signed-in user or rejects the recipient. | Do not bypass the safety stop. Sign in with the intended training account and make row 2 Email exactly match that account; otherwise use the blocked-path trace. |

## Challenge

Add an approved Preview column that stores the subject and first 60 body characters during dry run. Explain why preview evidence is useful and why it still does not authorise sending.

## Reflection

Which control made the automation observable and reversible, and what new risk would appear if the workflow sent messages automatically?

---

[← Lab 7](lab-07-run-the-meeting-to-drive-follow-up-workflow.md) · [Labs index →](README.md)
