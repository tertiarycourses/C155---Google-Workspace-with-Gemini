# Lab 3 — Draft the Partner Communication Pack in Docs and Gmail

**Course:** Google Workspace with Gemini  
**Course Code:** C155  
**Version:** v1.0 (28 July 2026)  
**Topic 2:** Gemini in Docs, Slides and Gmail  
**Maps to:** LO2: draft, summarise and refine source-led workplace content in Docs and Gmail  
**Duration:** 75 minutes  
**Tools:** Google Docs - Gmail - Gemini in Gmail or Docs where available - Drive

---

## Goal

Convert the approved briefing and a synthetic email thread into a reviewed partner invitation, internal summary and Gmail draft.

## What You Will Do

You will distinguish thread facts from requests and commitments, use Gemini to draft a partner invitation from approved sources, refine it in Docs and prepare a Gmail draft. The message remains unsent so recipient, attachment and commitment checks stay visible.

## What You Will Build

A 03-partner-communication-pack Google Doc containing a verified thread summary, partner invitation and internal hand-off note, plus one reviewed Gmail draft to the learner's own address with a completed send checklist.

## Prerequisites

- Approved 02-grounded-briefing and 02-claim-review-ledger from Lab 2.
- Open labs/assets/partner-email-thread.txt; it is a synthetic thread and is not sent to real recipients.
- Know the email address of the same training account; it is the only permitted recipient in this lab.

> **Data note.** Use only the supplied synthetic scenario and an account you are authorised to use. Do not paste passwords, secrets, protected personal data or confidential workplace content into a prompt. Keep live sending disabled until the lab explicitly calls for one reviewed draft to your own account.

## Steps

### 1. Create a Google Doc in 02-Working named 03-partner-communication-pack. Add headings Thread summary, Partner invitation, Internal hand-off, Cross-artifact ledger and Send checklist. Under Thread summary create a table with Type, Statement, Owner, Due or PENDING and Source message.

```text
Required thread categories: confirmed facts | partner requests | proposed but unapproved commitments | open questions
```

### 2. Paste partner-email-thread.txt into Gemini in Gmail, Gemini in Docs or the documented fallback. Ask for a bounded summary. If no Gemini control is available, read each numbered message and manually add one table row per fact, request, decision, proposal or open question; copy the message number and use PENDING for a missing owner or due date. Insert the result into the summary table, then read the original thread and correct any missed qualification, wrong owner or proposed detail presented as confirmed.

```text
Summarise this synthetic email thread into a table with Type, Statement, Owner, Due or PENDING and Source message number. Separate confirmed facts, requests, decisions and proposals. Do not turn a proposal into a commitment. End with unresolved questions.
```

### 3. Under Partner invitation use the approved grounded briefing and corrected thread summary as the only sources. Ask Gemini for a subject line and 180-220 word invitation with purpose, confirmed logistics, preparation request, accessibility contact and next action. Require PENDING for any unresolved detail. If Gemini is unavailable, draft the same artifact manually: write the subject, two short purpose/logistics paragraphs, a three-item preparation list, accessibility line and next action, then count and edit it to 180-220 words.

```text
Persona: I am the Aster & Finch coordinator writing to invited partner representatives.
Task: Draft a clear invitation that explains why to attend and what to prepare.
Context: Use only the approved briefing and corrected thread summary below. Confirmed information overrides proposals; unresolved details remain PENDING.
Format: Subject line plus 180-220 word email with short paragraphs and a three-item preparation list.
Review: List every commitment, date, link, attachment and recipient assumption.
```

### 4. Edit the invitation in Docs. Use the G-E-A-R loop and the 02-claim-review-ledger to verify every event fact. Replace jargon, remove duplicate sentences and make the next action specific. Under Cross-artifact ledger add rows for Date, Delivery mode, Audience, Preparation request and Accessibility; show the value in Briefing, Thread and Final email.

```text
Ledger columns: Field | Briefing value | Thread value | Final email value | Result | Edit made
Result values: MATCH | PENDING | REPAIRED
```

### 5. Under Internal hand-off ask Gemini to turn the final invitation into a 120-word note for the operations team. Require Owner, Action, Due or PENDING, Source and Risk as a table. If Gemini is unavailable, manually restate only the invitation's confirmed actions in the same table and edit the surrounding note to 120 words. Verify that the note does not create a new external commitment and record the responsible human reviewer.

```text
Create a 120-word internal hand-off from the approved invitation. Use a table with Owner, Action, Due or PENDING, Source and Risk. Do not invent an owner, date or approved budget.
```

### 6. In Gmail start a new message addressed only to your own training account. Paste the reviewed subject and invitation, then save it as a draft; do not click Send. In the Doc complete the checklist rows To, Cc/Bcc, Subject, Dates, Commitments, Links, Attachments, Accessibility, Tone and Approver. Record the Gmail draft timestamp.

```text
Checklist result values: PASS | NOT USED | REPAIR
Required final state: Gmail Draft; recipient is the learner's own training address.
```

## Test It

The communication pack must include all five headings, a thread summary that separates proposals from confirmed facts, a 180-220 word invitation, a five-field cross-artifact ledger, an internal hand-off with Owner/Action/Due/Source/Risk and a ten-row send checklist. Gmail must contain exactly one new unsent draft addressed only to the learner's own training account.

## Checkpoint and Rejoin Point

Move the reviewed 03-partner-communication-pack to 03-Approved and leave the email unsent in Gmail Drafts. Lab 4 uses the approved message architecture and facts; it does not use the raw thread.

## Troubleshooting

| If this happens | Fix |
|---|---|
| The summary treats a proposed date or deliverable as confirmed. | Return to the source message, label it PROPOSAL and change the final text to PENDING until the approved briefing confirms it. |
| Gemini in Gmail cannot access the approved Drive file. | Use Gemini in Docs or paste the approved excerpt; do not broaden Drive sharing to solve the feature gap. |
| The draft is addressed to a synthetic email from the thread. | Remove it immediately and use only your own training address; synthetic addresses are source text, not live recipients. |

## Challenge

Create a 90-word mobile-first version of the invitation. Preserve all confirmed logistics and compare which formatting changes improve scanning without removing required context.

## Reflection

Which part of the email required authority rather than language skill, and how did you keep that decision with a person?

---

[← Lab 2](lab-02-produce-and-verify-a-grounded-workspace-briefing.md) · [Lab 4 →](lab-04-build-the-partner-briefing-deck-in-slides.md)
