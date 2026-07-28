# Lab 2 — Produce and Verify a Grounded Workspace Briefing

**Course:** Google Workspace with Gemini  
**Course Code:** C155  
**Version:** v1.0 (28 July 2026)  
**Topic 1:** Getting Started with Gemini in Google Workspace  
**Maps to:** LO1: use an effective prompt and a human review gate to create a source-grounded workplace briefing  
**Duration:** 55 minutes  
**Tools:** Google Docs - Google Sheets - Gemini in Docs or supplied fallback - Drive

---

## Goal

Turn the approved synthetic sources into a concise briefing while recording every material fact, question and correction.

## What You Will Do

You will apply the Lab 1 charter to create a structured partner-briefing candidate. You will then build a claim ledger, test the response against the sources and move only the reviewed version into the approved state.

## What You Will Build

A 02-grounded-briefing Google Doc with seven required sections and a 02-claim-review-ledger Google Sheet that traces every material statement to a source, marks unsupported details and records the final human decision.

## Prerequisites

- Completed 01-prompt-charter and 01-access-matrix from Lab 1.
- aster-finch-project-brief.md and facts-and-policies.md remain unchanged in 01-Source.
- Open labs/assets/prompt-quality-checklist.md for the final review.
- Open labs/assets/sample-lab2-grounded-briefing.md for the complete fallback candidate.
- Plan a trainer or peer reviewer; if working solo, use the bounded self-review in Step 5.

> **Data note.** Use only the supplied synthetic scenario and an account you are authorised to use. Do not paste passwords, secrets, protected personal data or confidential workplace content into a prompt. Keep live sending disabled until the lab explicitly calls for one reviewed draft to your own account.

## Steps

### 1. Create a Google Doc in 02-Working named 02-grounded-briefing. Add headings Executive summary, Purpose and audience, Confirmed plan, Participant experience, Open questions, Next actions and Source note. Under Source note list the exact two source filenames and their folder state.

```text
Sources:
01-Source/aster-finch-project-brief.md
01-Source/facts-and-policies.md
```

### 2. Use the Lab 1 P-T-C-F charter in Gemini in Docs. Reference or paste only the two approved sources. Ask for 450-600 words across the required headings, a neutral professional tone, no invented details and a final table of open questions with Owner and Needed by. If Gemini is unavailable, copy sample-lab2-grounded-briefing.md as the candidate and perform the same claim-ledger and G-E-A-R review; do not reuse the short Lab 1 fallback.

```text
Persona: I am the Aster & Finch workplace coordinator writing for invited partner representatives.
Task: Draft a 450-600 word operations briefing that enables partners to prepare.
Context: Use only the two named source files below. The facts file overrides a conflicting draft statement. Write UNKNOWN for absent information.
Format: Use the seven document headings already present. Finish with an Open question | Owner | Needed by table.
Review: Flag every number, date, place, commitment and named owner for source checking. Do not add a quotation or testimonial.
```

### 3. Insert the candidate under the document headings. Create a Google Sheet in 02-Working named 02-claim-review-ledger with columns ID, Claim, Source file, Source excerpt or field, Status, Required edit and Reviewer. Add one row for every number, date, venue statement, commitment, audience condition and action owner in the candidate.

```text
Status values: VERIFIED | NEEDS EDIT | UNKNOWN
A VERIFIED row must name a source file and an exact excerpt or field.
```

### 4. Check each ledger row against the source files. Change unsupported content in the Doc to UNKNOWN or an explicit open question. Where the two sources differ, apply the priority rule in facts-and-policies.md and record the conflict in Required edit. Do not mark a claim VERIFIED merely because Gemini repeated it.

```text
Minimum checks: event purpose | audience | date | delivery mode | duration | accessibility | participant data rule | named owner | next action
```

### 5. Apply the G-E-A-R review to the complete revised Doc. Add a final table with Grounding, Evidence, Audience and Risk as rows, each with Check, Evidence and Result. Ask a trainer or peer to read only the briefing and state the event purpose, confirmed details and open questions; record their answer under Audience check. If working solo, hide the source files, read only the briefing and write those same three items before comparing them with the sources; label the evidence Bounded self-review.

```text
Result values: PASS | REPAIR
All four rows must be PASS before the document can move to 03-Approved.
```

### 6. If every material claim is VERIFIED or visibly UNKNOWN and all four G-E-A-R rows pass, move the final Doc and ledger to 03-Approved. In the Doc add Decision: APPROVED FOR COURSE WORKFLOW, Reviewer and date. Otherwise leave both in 02-Working and add Decision: HOLD with the unresolved item.

```text
Final state rule:
APPROVED FOR COURSE WORKFLOW -> 03-Approved
HOLD -> 02-Working
```

## Test It

The briefing must contain all seven headings, 450-600 words, the two exact source paths, an open-question table and a four-row G-E-A-R table. The ledger must cover at least nine material claims and contain no VERIFIED row without a source excerpt. The Drive state must match the recorded APPROVED FOR COURSE WORKFLOW or HOLD decision.

## Checkpoint and Rejoin Point

Labs 3 and 4 use the final 02-grounded-briefing and 02-claim-review-ledger as their controlling content sources. Do not draft from the earlier Gemini response.

## Troubleshooting

| If this happens | Fix |
|---|---|
| Gemini cannot reference the Markdown files directly. | Open each source, copy only the relevant synthetic text into the prompt and preserve the exact filename in the source boundary. |
| The candidate is too long or repeats the same information. | Assign one purpose to each heading and set a word budget before rerunning or editing manually. |
| The reviewer cannot find where a claim came from. | Downgrade the row to NEEDS EDIT or UNKNOWN until an exact source excerpt is recorded. |

## Challenge

Create a second version capped at 250 words. Compare which details were removed and explain whether the shorter version still supports the same partner decisions.

## Reflection

Which sentence required the most human judgement, and why could source grounding alone not finish that decision?

---

[← Lab 1](lab-01-confirm-access-and-build-a-safe-prompt-charter.md) · [Lab 3 →](lab-03-draft-the-partner-communication-pack-in-docs-and-gmail.md)
