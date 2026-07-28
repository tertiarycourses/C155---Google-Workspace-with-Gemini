# Google Workspace with Gemini — Learner Guide

**Course Code:** C155  |  **Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)  |  **Version v1.0 · 28 July 2026**

## Contents

- [Introduction](#introduction)
- [Course Learning Outcomes](#course-learning-outcomes)
- [Before You Start — Preparation](#before-you-start--preparation)
- [Topic 01 — Getting Started with Gemini in Google Workspace  (Day 1 morning - 2 labs)](#topic-01--getting-started-with-gemini-in-google-workspace--day-1-morning---2-labs)
  - [Introduction to Generative AI and Gemini in Workspace](#introduction-to-generative-ai-and-gemini-in-workspace)
  - [Setting Up and Accessing Gemini Across Workspace Apps](#setting-up-and-accessing-gemini-across-workspace-apps)
  - [Effective Prompting for Everyday Work Tasks](#effective-prompting-for-everyday-work-tasks)
  - [Responsible, Secure and Private Use of AI at Work](#responsible-secure-and-private-use-of-ai-at-work)
  - [Lab 1 — Confirm Access and Build a Safe Prompt Charter](#lab-1--confirm-access-and-build-a-safe-prompt-charter)
  - [Lab 2 — Produce and Verify a Grounded Workspace Briefing](#lab-2--produce-and-verify-a-grounded-workspace-briefing)
- [Topic 02 — Gemini in Docs, Slides and Gmail  (Day 1 afternoon - 2 labs)](#topic-02--gemini-in-docs-slides-and-gmail--day-1-afternoon---2-labs)
  - [Drafting, Rewriting and Summarising in Docs](#drafting-rewriting-and-summarising-in-docs)
  - [Generating Slides, Layouts and Images in Slides](#generating-slides-layouts-and-images-in-slides)
  - [Writing, Replying and Summarising Emails in Gmail](#writing-replying-and-summarising-emails-in-gmail)
  - [Reviewing and Refining AI-Generated Content](#reviewing-and-refining-ai-generated-content)
  - [Lab 3 — Draft the Partner Communication Pack in Docs and Gmail](#lab-3--draft-the-partner-communication-pack-in-docs-and-gmail)
  - [Lab 4 — Build the Partner Briefing Deck in Slides](#lab-4--build-the-partner-briefing-deck-in-slides)
- [Topic 03 — Gemini in Sheets and Data Analysis  (Day 2 morning - 2 labs)](#topic-03--gemini-in-sheets-and-data-analysis--day-2-morning---2-labs)
  - [Generating Formulas, Tables and Insights in Sheets](#generating-formulas-tables-and-insights-in-sheets)
  - [Analysing and Summarising Data with Gemini](#analysing-and-summarising-data-with-gemini)
  - [Creating Charts and Visualisations](#creating-charts-and-visualisations)
  - [Cleaning and Organising Data with AI](#cleaning-and-organising-data-with-ai)
  - [Lab 5 — Clean the Registration Tracker and Generate Formulas](#lab-5--clean-the-registration-tracker-and-generate-formulas)
  - [Lab 6 — Analyse Registrations and Build the Decision Dashboard](#lab-6--analyse-registrations-and-build-the-decision-dashboard)
- [Topic 04 — AI-Powered Workflows and Automation in Workspace  (Day 2 afternoon - 2 labs)](#topic-04--ai-powered-workflows-and-automation-in-workspace--day-2-afternoon---2-labs)
  - [AI-Assisted Meetings and Notes in Google Meet](#ai-assisted-meetings-and-notes-in-google-meet)
  - [Organising and Searching Drive with Gemini](#organising-and-searching-drive-with-gemini)
  - [Connecting Apps and Building Simple Automations](#connecting-apps-and-building-simple-automations)
  - [Designing Practical AI Productivity Workflows](#designing-practical-ai-productivity-workflows)
  - [Lab 7 — Run the Meeting-to-Drive Follow-Up Workflow](#lab-7--run-the-meeting-to-drive-follow-up-workflow)
  - [Lab 8 — Automate the Approved Follow-Up from Sheets](#lab-8--automate-the-approved-follow-up-from-sheets)
- [Wrap-Up - From Helpful Feature to Reliable Workflow](#wrap-up---from-helpful-feature-to-reliable-workflow)
- [Next Steps](#next-steps)
- [Glossary](#glossary)


## Introduction

This Learner Guide is the self-contained study text for Google Workspace with Gemini (C155). It explains the concepts behind prompting, grounded drafting, spreadsheet analysis, meeting notes, Drive retrieval and bounded automation before giving the aligned steps for eight connected hands-on labs.

The course uses a fictional Aster & Finch partner briefing and synthetic data. Work through the labs in order because each checkpoint supplies the approved inputs for the next activity. Gemini labels and availability can vary by account, plan, language, administrator setting and product release; use the documented fallback while preserving the same source, review and output requirements.


## Course Learning Outcomes

- LO1: Explain how Gemini works across Google Workspace, write effective prompts and apply responsible data, privacy and verification controls.
- LO2: Draft, rewrite, summarise and refine workplace content in Docs, Slides and Gmail while preserving source accuracy, audience fit and human approval.
- LO3: Clean, organise, analyse and visualise spreadsheet data with Gemini in Sheets, formulas and reproducible checks.
- LO4: Design an AI-assisted workflow across Meet, Drive, Sheets, Docs and Gmail, then implement and verify a bounded Workspace automation.


## Before You Start — Preparation

**What you need**

- A Windows or Mac laptop with a current Chrome, Edge, Firefox or Safari browser and reliable internet access.
- A Google account authorised for training; an eligible Workspace plan is preferred for in-app Gemini features.
- Access to Gmail, Drive, Docs, Sheets, Slides and Meet. Google Apps Script access may require administrator approval.
- The supplied synthetic files in labs/assets/. Do not substitute workplace records during the class.
- A plain-text editor for the prompt charter, review ledger and workflow control log.

**Verify your setup**

Open Drive, create a temporary Doc and Sheet, and check whether Ask Gemini or the relevant AI control appears. Record each app as Available, Trainer demo or Manual fallback. Confirm that Extensions > Apps Script opens from the practice Sheet.

```bash
Access matrix columns:
App | Account used | Gemini feature | Status | Safe fallback | Admin issue
Gmail | Docs | Sheets | Slides | Drive | Meet | Apps Script
```

**Conventions used in every lab**

- P-T-C-F means Persona, Task, Context and Format; every material prompt also names its sources and review criteria.
- UNKNOWN or PENDING is safer than inventing a missing date, person, metric or commitment.
- A generated output remains a candidate until the G-E-A-R review records Grounding, Evidence, Audience and Risk.
- Keep 01-Source, 02-Working, 03-Approved and 04-Archive folders separate throughout the connected scenario.
- Run automation first in DRY_RUN mode and to your own address; never bulk-send during the lab.


## Topic 01 — Getting Started with Gemini in Google Workspace  (Day 1 morning - 2 labs)

Generative AI and Gemini - Access across apps - Effective prompting - Responsible, secure and private use

**Key concepts**

- Generative AI — A probabilistic system that creates a candidate output from instructions and context; it does not guarantee truth.
- Workspace grounding — Gemini can use selected Workspace sources and the user's existing permissions to add relevant context.
- P-T-C-F prompt — Persona, Task, Context and Format make the request, evidence boundary and expected output explicit.
- Human review gate — A named person verifies facts, privacy, permissions, tone and destination before output is used.


### Introduction to Generative AI and Gemini in Workspace

Generative AI predicts and assembles a useful candidate response from patterns in data, instructions and supplied context. Gemini in Google Workspace places this capability inside familiar apps so a user can draft, summarise, organise and analyse without treating the generated output as an authoritative record.

The productivity gain comes from reducing the first-pass effort, not from transferring accountability to the model. A useful mental model is assistant, source and reviewer: Gemini proposes, approved Workspace material grounds the task, and a person decides what is accurate and appropriate.

**How it works**

- Define the workplace task and the decision the output will support.
- Select the minimum approved source material needed for context.
- Ask Gemini for a bounded candidate in a specified format.
- Compare every material statement with the source or an independent record.
- Edit, approve and share through the normal Workspace controls.

**Worked example**

- Aster & Finch is planning a synthetic partner briefing and has an approved project brief.
- Gemini converts the brief into a draft agenda, but labels missing venue and speaker details as open questions.
- The coordinator verifies those fields before the agenda becomes a shared document.

**Decision guide**

| Use when | Avoid when |
|---|---|
| A repetitive drafting or synthesis task has approved source material and a human owner. | The task needs a guaranteed fact but no trustworthy source is available. |
| The output can be checked before it influences a customer, employee or business decision. | The user intends to send or publish the first response without review. |

**Practitioner quality lens**

- FAILURE SIGNAL: The response sounds confident but cannot show where a key statement came from.
- REPAIR MOVE: Constrain the prompt to named sources and require UNKNOWN for unsupported details.
- QUALITY EVIDENCE: A reviewer can trace each material statement to an approved file or record.

---


### Setting Up and Accessing Gemini Across Workspace Apps

Gemini features appear according to the user's Google account, eligible plan, administrator settings, language, region and app. Common entry points include an Ask Gemini side panel or an in-context create, refine, summarise or visualise control; exact labels may change as Workspace evolves.

A workflow that assumes every account has the same controls will fail in a real class or organisation. Separating the durable job from a particular button lets users verify availability, protect permissions and use a manual or trainer-provided fallback without losing the learning objective.

**How it works**

- Sign in with the intended account and identify whether it is personal or organisation-managed.
- Check Gmail, Docs, Sheets, Slides, Drive and Meet for the relevant Gemini entry point.
- Confirm that the source files are accessible only to the intended account and collaborators.
- Record unavailable features, language limitations and any administrator restriction.
- Choose a fallback: trainer demonstration, manual app feature or provided sample output.

**Worked example**

- A learner can open Gemini in Docs and Sheets but not Take notes for me in Meet.
- The learner records the gap, uses the supplied meeting transcript and still completes the notes-review workflow.
- No account credentials or protected organisation files are moved to another service.

**Decision guide**

| Use when | Avoid when |
|---|---|
| You are validating a repeatable workflow for a known account and Workspace plan. | A feature is assumed available because it appears in a demonstration or help page. |
| A fallback can preserve the same evidence, review and output requirements. | The workaround would copy restricted information into an unapproved account or tool. |

**Practitioner quality lens**

- FAILURE SIGNAL: The lab stops at a missing sparkle icon or unavailable control.
- REPAIR MOVE: Name the job, use the documented fallback and capture the same final artifact.
- QUALITY EVIDENCE: The access matrix shows account, app, feature, status and safe fallback.

---


### Effective Prompting for Everyday Work Tasks

An effective prompt communicates four core elements: Persona, Task, Context and Format. The course adds a Source boundary and Review criteria so the response is useful for work: who Gemini should help, what to do, which facts to use, what the result should look like, and how a person will check it.

Vague prompts hide assumptions and make quality subjective. A structured prompt creates an observable contract, supports iteration and lets another person reproduce the request rather than guessing what the author intended.

**How it works**

- Set the persona and intended audience only when they improve tone or domain framing.
- Use a precise action verb and define the finished artifact or decision.
- Provide approved context and state which sources take priority.
- Specify length, structure, tone and fields that must remain UNKNOWN when absent.
- Review the first response, name the defect and change one instruction at a time.

**Worked example**

- Persona: workplace coordinator writing for external partners.
- Task and context: draft a concise invitation using only the Aster & Finch project brief.
- Format and review: subject plus 150-word email; flag unsupported details and list a final fact check.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The task, audience, sources and desired structure can be stated clearly. | The prompt asks Gemini to invent missing evidence or imitate a real person's private style. |
| Several iterations can be compared against the same quality criteria. | The user keeps adding conflicting instructions without resolving priorities. |

**Practitioner quality lens**

- FAILURE SIGNAL: The output is generic, long or filled with invented specifics.
- REPAIR MOVE: Add the missing P-T-C-F element, a source boundary and observable constraints.
- QUALITY EVIDENCE: The final response satisfies a checklist another learner can apply consistently.

---


### Responsible, Secure and Private Use of AI at Work

Responsible use combines data classification, least-privilege access, appropriate sharing, source verification, disclosure where needed and a human decision owner. Workspace protections matter, but they do not replace an organisation's policies or the user's duty to choose suitable inputs and recipients.

Gemini can accelerate a mistake as easily as a good workflow. A privacy-safe prompt can still produce an inaccurate claim, and an accurate draft can still be overshared; controls must therefore cover the full path from source selection to final destination.

**How it works**

- Classify the intended input as public, internal, confidential or restricted under local policy.
- Minimise the content and remove unnecessary personal or sensitive fields.
- Check source-file access and the destination's sharing permissions.
- Verify facts, calculations, tone, bias, rights and any required disclosure.
- Record the reviewer, decision and final approved version.

**Worked example**

- The synthetic registration sheet contains names and contact fields that the analysis does not need.
- The learner works from a minimised training copy, reports only grouped counts and shares results with named collaborators.
- A control log records sources, checks, approver and destination.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The organisation permits the data and task, and a defined reviewer can inspect the result. | The prompt includes passwords, secrets, protected personal records or information outside the user's authority. |
| The output remains inside an approved access and sharing boundary. | The workflow hides uncertainty or makes a high-impact decision without qualified human review. |

**Practitioner quality lens**

- FAILURE SIGNAL: The draft is accurate but visible to people who do not need it.
- REPAIR MOVE: Apply least privilege, remove unnecessary data and check the destination before sharing.
- QUALITY EVIDENCE: The control log proves input authority, source checks, reviewer and recipient scope.

---


### Lab 1 — Confirm Access and Build a Safe Prompt Charter

Learning outcome: LO1: explain Gemini access, prompt structure and responsible controls across Google Workspace.

Goal: Verify the available Workspace features and create the source, prompt and review rules that govern every later lab.

You will create the C155 project folder, check Gemini and fallback availability across Workspace, classify the supplied synthetic sources and write a reusable P-T-C-F prompt charter. The charter keeps sources, uncertainty, sharing and human approval visible.

**What you'll build**

A C155-Aster-Finch Drive folder with four state subfolders, an 01-access-matrix sheet and a 01-prompt-charter document containing approved sources, prohibited inputs, a reusable prompt pattern and the G-E-A-R review gate.   (Tools: Google Drive - Docs - Sheets - Gemini features where available - supplied synthetic source pack.)

**Prerequisites**

- Sign in to a Google account authorised for training and open labs/assets/aster-finch-project-brief.md.
- Open labs/assets/facts-and-policies.md and labs/assets/prompt-quality-checklist.md.
- Do not use workplace records; the supplied files are entirely synthetic.

**Step-by-step**

1. In Google Drive, create a folder named C155-Aster-Finch. Inside it create exactly 01-Source, 02-Working, 03-Approved and 04-Archive. Upload aster-finch-project-brief.md, facts-and-policies.md and prompt-quality-checklist.md to 01-Source. Keep sharing set to Restricted.

   ```bash
   Expected path:
C155-Aster-Finch/
  01-Source/
  02-Working/
  03-Approved/
  04-Archive/
   ```

2. Create a Google Sheet in 02-Working named 01-access-matrix. Add the headers App, Account type, Gemini entry point, Status, Safe fallback and Admin issue. Create rows for Gmail, Docs, Sheets, Slides, Drive, Meet and Apps Script. Open each app in a new tab and record Available, Trainer demo or Manual fallback; do not guess from a help page.

   ```bash
   Status values: Available | Trainer demo | Manual fallback
Safe fallbacks: supplied source or transcript | normal app feature | trainer demonstration
   ```

3. In 01-access-matrix add a second tab named Data boundary. Enter Public, Internal, Confidential and Restricted as four rows. For each row add Allowed training example, Handling rule and Not allowed. Classify the three supplied files as Synthetic training data. Explicitly prohibit passwords, access tokens, private customer records and unapproved confidential content.

   ```bash
   Rule: use the minimum approved fields for the stated task; UNKNOWN replaces an unsupported detail.
   ```

4. Create a Google Doc in 02-Working named 01-prompt-charter. Add headings Purpose, Approved sources, Prohibited inputs, Persona, Task, Context, Format, Source boundary, Review criteria, Output destination and Human approver. Fill every heading from the project brief and facts file. Use PENDING for the approver name if no role has been assigned.

   ```bash
   Persona: I am a workplace coordinator preparing a synthetic partner briefing.
Task: Create <ARTIFACT> for <AUDIENCE> so they can <DECISION OR ACTION>.
Context: Use only <NAMED APPROVED FILES OR EXCERPTS>.
Format: Return <STRUCTURE, LENGTH, TONE AND REQUIRED FIELDS>.
Source boundary: If a detail is absent, write UNKNOWN and list the question; do not infer it.
Review: End with a G-E-A-R table for Grounding, Evidence, Audience and Risk.
   ```

5. Run the charter prompt in Gemini in Docs or another available in-app Gemini control. Ask for a five-bullet briefing outline using only the two approved source files. If the feature is unavailable, use the trainer demonstration response in labs/assets/sample-gemini-output.md. Paste the result under Initial response.

   ```bash
   Create a five-bullet outline for the Aster & Finch Partner Operations Briefing. Use only the attached or pasted project brief and facts file. Include Purpose, Audience, Confirmed facts, Open questions and Next action. Write UNKNOWN for unsupported details and end with a G-E-A-R review table.
   ```

6. Compare the response with prompt-quality-checklist.md. Under Review record at least one source check, one audience edit and one risk check. Write a refined prompt that repairs the largest defect. If Gemini is available, run the refined prompt once and paste the result under Refined response. If Gemini is unavailable, duplicate the initial fallback, manually apply the refined instruction, label it Manual refined fallback and record every edit. Finish with Approver, Decision and Destination; keep Decision as WORKING until a partner checks it.

   ```bash
   Iteration record:
Defect: <OBSERVED PROBLEM>
Changed instruction: <ONE CHANGE>
Result: <OBSERVABLE IMPROVEMENT>
Approver: <ROLE OR PENDING>
Decision: WORKING
Destination: 02-Working
   ```


**Test it**

Open the Drive folder and both artifacts. There must be four correctly named state folders; 01-access-matrix must have seven app rows and four data-boundary rows; 01-prompt-charter must contain all eleven headings, one initial and one generated or manually refined second response, UNKNOWN for unsupported details, four G-E-A-R checks and a visible WORKING decision.

**Checkpoint and rejoin point**

Keep the approved source files in 01-Source and the two Lab 1 artifacts in 02-Working. Labs 2-8 must reuse the same source boundary, P-T-C-F structure and G-E-A-R review.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| Ask Gemini or another AI control is missing. | Record the feature as Trainer demo or Manual fallback and use sample-gemini-output.md without moving the source to an unapproved service. |
| The response invents a date, venue or speaker. | Replace it with UNKNOWN and add the exact source-boundary instruction before rerunning. |
| A source file is visible from the wrong account. | Stop, remove unintended sharing and continue only from the authorised training account. |

**Challenge**

Rewrite the prompt for a senior leader and for an operations coordinator. Keep the same facts and compare which Persona, Format and Audience instructions legitimately change.

**Reflection**

Which control in your charter prevents the most consequential failure, and what evidence shows that it was applied?

> **Note:** The complete lab and its support-file references are in labs/lab-01-*.md. Use only the supplied synthetic scenario and an account you are authorised to use. Do not paste passwords, secrets, protected personal data or confidential workplace content into a prompt. Keep live sending disabled until the lab explicitly calls for one reviewed draft to your own account.

---


### Lab 2 — Produce and Verify a Grounded Workspace Briefing

Learning outcome: LO1: use an effective prompt and a human review gate to create a source-grounded workplace briefing.

Goal: Turn the approved synthetic sources into a concise briefing while recording every material fact, question and correction.

You will apply the Lab 1 charter to create a structured partner-briefing candidate. You will then build a claim ledger, test the response against the sources and move only the reviewed version into the approved state.

**What you'll build**

A 02-grounded-briefing Google Doc with seven required sections and a 02-claim-review-ledger Google Sheet that traces every material statement to a source, marks unsupported details and records the final human decision.   (Tools: Google Docs - Google Sheets - Gemini in Docs or supplied fallback - Drive.)

**Prerequisites**

- Completed 01-prompt-charter and 01-access-matrix from Lab 1.
- aster-finch-project-brief.md and facts-and-policies.md remain unchanged in 01-Source.
- Open labs/assets/prompt-quality-checklist.md for the final review.
- Open labs/assets/sample-lab2-grounded-briefing.md for the complete fallback candidate.
- Plan a trainer or peer reviewer; if working solo, use the bounded self-review in Step 5.

**Step-by-step**

1. Create a Google Doc in 02-Working named 02-grounded-briefing. Add headings Executive summary, Purpose and audience, Confirmed plan, Participant experience, Open questions, Next actions and Source note. Under Source note list the exact two source filenames and their folder state.

   ```bash
   Sources:
01-Source/aster-finch-project-brief.md
01-Source/facts-and-policies.md
   ```

2. Use the Lab 1 P-T-C-F charter in Gemini in Docs. Reference or paste only the two approved sources. Ask for 450-600 words across the required headings, a neutral professional tone, no invented details and a final table of open questions with Owner and Needed by. If Gemini is unavailable, copy sample-lab2-grounded-briefing.md as the candidate and perform the same claim-ledger and G-E-A-R review; do not reuse the short Lab 1 fallback.

   ```bash
   Persona: I am the Aster & Finch workplace coordinator writing for invited partner representatives.
Task: Draft a 450-600 word operations briefing that enables partners to prepare.
Context: Use only the two named source files below. The facts file overrides a conflicting draft statement. Write UNKNOWN for absent information.
Format: Use the seven document headings already present. Finish with an Open question | Owner | Needed by table.
Review: Flag every number, date, place, commitment and named owner for source checking. Do not add a quotation or testimonial.
   ```

3. Insert the candidate under the document headings. Create a Google Sheet in 02-Working named 02-claim-review-ledger with columns ID, Claim, Source file, Source excerpt or field, Status, Required edit and Reviewer. Add one row for every number, date, venue statement, commitment, audience condition and action owner in the candidate.

   ```bash
   Status values: VERIFIED | NEEDS EDIT | UNKNOWN
A VERIFIED row must name a source file and an exact excerpt or field.
   ```

4. Check each ledger row against the source files. Change unsupported content in the Doc to UNKNOWN or an explicit open question. Where the two sources differ, apply the priority rule in facts-and-policies.md and record the conflict in Required edit. Do not mark a claim VERIFIED merely because Gemini repeated it.

   ```bash
   Minimum checks: event purpose | audience | date | delivery mode | duration | accessibility | participant data rule | named owner | next action
   ```

5. Apply the G-E-A-R review to the complete revised Doc. Add a final table with Grounding, Evidence, Audience and Risk as rows, each with Check, Evidence and Result. Ask a trainer or peer to read only the briefing and state the event purpose, confirmed details and open questions; record their answer under Audience check. If working solo, hide the source files, read only the briefing and write those same three items before comparing them with the sources; label the evidence Bounded self-review.

   ```bash
   Result values: PASS | REPAIR
All four rows must be PASS before the document can move to 03-Approved.
   ```

6. If every material claim is VERIFIED or visibly UNKNOWN and all four G-E-A-R rows pass, move the final Doc and ledger to 03-Approved. In the Doc add Decision: APPROVED FOR COURSE WORKFLOW, Reviewer and date. Otherwise leave both in 02-Working and add Decision: HOLD with the unresolved item.

   ```bash
   Final state rule:
APPROVED FOR COURSE WORKFLOW -> 03-Approved
HOLD -> 02-Working
   ```


**Test it**

The briefing must contain all seven headings, 450-600 words, the two exact source paths, an open-question table and a four-row G-E-A-R table. The ledger must cover at least nine material claims and contain no VERIFIED row without a source excerpt. The Drive state must match the recorded APPROVED FOR COURSE WORKFLOW or HOLD decision.

**Checkpoint and rejoin point**

Labs 3 and 4 use the final 02-grounded-briefing and 02-claim-review-ledger as their controlling content sources. Do not draft from the earlier Gemini response.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| Gemini cannot reference the Markdown files directly. | Open each source, copy only the relevant synthetic text into the prompt and preserve the exact filename in the source boundary. |
| The candidate is too long or repeats the same information. | Assign one purpose to each heading and set a word budget before rerunning or editing manually. |
| The reviewer cannot find where a claim came from. | Downgrade the row to NEEDS EDIT or UNKNOWN until an exact source excerpt is recorded. |

**Challenge**

Create a second version capped at 250 words. Compare which details were removed and explain whether the shorter version still supports the same partner decisions.

**Reflection**

Which sentence required the most human judgement, and why could source grounding alone not finish that decision?

> **Note:** The complete lab and its support-file references are in labs/lab-02-*.md. Use only the supplied synthetic scenario and an account you are authorised to use. Do not paste passwords, secrets, protected personal data or confidential workplace content into a prompt. Keep live sending disabled until the lab explicitly calls for one reviewed draft to your own account.

---


## Topic 02 — Gemini in Docs, Slides and Gmail  (Day 1 afternoon - 2 labs)

Drafting, rewriting and summarising - Slides and images - Gmail threads and replies - Reviewing generated content

**Key concepts**

- Source-led draft — A first version whose facts and constraints come from named approved material.
- Message architecture — Audience need, core message, supporting evidence and next action shape documents, slides and email.
- Visual brief — Purpose, subject, composition, aspect ratio, style and exclusions guide image generation.
- Review ledger — Claim, source, status, edit and approver make human refinement visible.


### Drafting, Rewriting and Summarising in Docs

Gemini in Docs can create a starting draft, transform selected text and summarise information from a document or referenced Workspace sources. Drafting creates new structure, rewriting changes an existing passage, and summarising compresses meaning; each operation requires a different instruction and review test.

Treating the three operations as interchangeable produces vague or distorted content. Naming the operation, audience and source boundary preserves intent and makes it easier to compare the generated passage with the evidence.

**How it works**

- Choose create, rewrite or summarise according to the actual communication need.
- Reference the approved file or paste a bounded source excerpt.
- Specify audience, purpose, tone, length and required headings.
- Insert only the useful candidate text into the working document.
- Compare facts and meaning with the source, then edit in the document.

**Worked example**

- The coordinator asks for a one-page partner briefing using the project brief and facts file.
- Gemini produces Objectives, Audience, Agenda, Logistics and Open Questions.
- The coordinator rejects an invented capacity figure and keeps the verified structure.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The source is known and the output is a draft that will be edited. | A summary would remove contractual nuance or a required qualification. |
| A rewrite can be judged for meaning, tone and audience accessibility. | The prompt gives only a title and expects correct organisation-specific facts. |

**Practitioner quality lens**

- FAILURE SIGNAL: A polished paragraph changes or omits a material source condition.
- REPAIR MOVE: Quote the controlling source, require open questions and compare sentence by sentence.
- QUALITY EVIDENCE: The document's claim ledger shows the source and final edit for every material fact.

---


### Generating Slides, Layouts and Images in Slides

A useful presentation turns a decision or story into a sequence of claims, evidence and actions. Gemini can help create slide candidates, rewrite text and generate images, but the presenter still controls narrative, factual support, accessibility, brand fit and whether a generated visual represents reality appropriately.

A collection of attractive slides is not automatically a coherent presentation. Starting from audience and message architecture prevents decorative output from replacing the business purpose, while a visual brief reduces generic or misleading imagery.

**How it works**

- Define the audience question and one-sentence presentation promise.
- Create a slide outline with one message and evidence need per slide.
- Generate or refine only the slide text that has approved support.
- Write a visual brief with subject, composition, aspect ratio, style and exclusions.
- Review the full sequence for evidence, hierarchy, accessibility and next action.

**Worked example**

- The partner briefing uses six slides: purpose, audience need, agenda, participation data, action plan and next steps.
- A wide abstract collaboration image supports the title without depicting a real attendee or unsupported venue.
- All figures point to the registration sheet and all open details remain visibly pending.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The deck has a defined audience, message and evidence source. | The image could be mistaken for documentary proof of a real person, place or event. |
| Generated imagery is illustrative, appropriate and reviewed before use. | Slide generation is used to hide missing analysis or compress unreadable amounts of text. |

**Practitioner quality lens**

- FAILURE SIGNAL: Each slide looks acceptable alone but the sequence has no decision path.
- REPAIR MOVE: Restate the audience question and give every slide one message and one role.
- QUALITY EVIDENCE: A slide map links message, evidence, visual purpose and audience action.

---


### Writing, Replying and Summarising Emails in Gmail

Gemini in Gmail can summarise a thread, draft a new message, suggest a reply and retrieve relevant information from permitted Workspace sources. The output must still respect thread history, recipient scope, commitments, tone and the difference between a suggested action and an approved promise.

Email is an external action surface: a small invented date, price or commitment can create real consequences. A safe workflow separates understanding the thread, deciding the response and drafting the message, then requires a final recipient and attachment check.

**How it works**

- Summarise the thread into facts, requests, decisions, owners and unresolved questions.
- Verify the summary against the original messages and named files.
- Decide what the organisation can commit to before asking for a reply.
- Draft with a clear subject, context, response, owner, date and next action.
- Check To, Cc, attachments, links and every commitment before sending.

**Worked example**

- A synthetic partner thread asks about capacity, accessibility and the final agenda.
- Gemini separates confirmed facts from open questions and drafts a holding reply.
- The coordinator removes an unapproved promise and saves the message as a draft for review.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The thread is bounded and the sender has authority to prepare a response. | The response would commit money, legal terms or sensitive information without an owner. |
| The final message can remain a draft until facts and recipients are checked. | The thread includes recipients or content the user is not authorised to expose to another tool or group. |

**Practitioner quality lens**

- FAILURE SIGNAL: The draft promises a date or deliverable not agreed in the thread.
- REPAIR MOVE: Convert unverified commitments to questions and name the decision owner.
- QUALITY EVIDENCE: The saved draft matches the verified thread summary and has a completed send checklist.

---


### Reviewing and Refining AI-Generated Content

Review is a structured comparison between the output, the source, the intended audience and the use context. The G-E-A-R loop used in this course checks Grounding, Evidence, Audience and Risk before a human approves, edits or rejects the candidate.

Fluency makes generated content feel finished earlier than it is. An explicit loop catches factual drift, missing qualifications, inappropriate tone, inaccessible design, privacy exposure and unsupported actions across Docs, Slides and Gmail.

**How it works**

- Grounding: identify the sources and the exact task the response should satisfy.
- Evidence: verify claims, numbers, names, dates, links and calculations.
- Audience: test clarity, tone, structure, accessibility and next action.
- Risk: inspect privacy, permissions, bias, rights, commitments and destination.
- Record the change and approver, then review the final assembled artifact again.

**Worked example**

- The deck states that 48 partners confirmed attendance, while the sheet contains 46 valid confirmations.
- The reviewer records the mismatch, corrects the slide and adds the sheet range to the source note.
- A second pass confirms the email and document use the same verified count.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The output will inform another person or become an organisation record. | The review is reduced to spelling and visual polish only. |
| A reviewer can access both source and final artifact. | The final combined document is never checked after individually approved parts are merged. |

**Practitioner quality lens**

- FAILURE SIGNAL: Different Workspace artifacts contain different versions of the same fact.
- REPAIR MOVE: Choose one controlling source, correct every consumer and re-run the final review.
- QUALITY EVIDENCE: A cross-artifact ledger shows one verified value and every place it appears.

---


### Lab 3 — Draft the Partner Communication Pack in Docs and Gmail

Learning outcome: LO2: draft, summarise and refine source-led workplace content in Docs and Gmail.

Goal: Convert the approved briefing and a synthetic email thread into a reviewed partner invitation, internal summary and Gmail draft.

You will distinguish thread facts from requests and commitments, use Gemini to draft a partner invitation from approved sources, refine it in Docs and prepare a Gmail draft. The message remains unsent so recipient, attachment and commitment checks stay visible.

**What you'll build**

A 03-partner-communication-pack Google Doc containing a verified thread summary, partner invitation and internal hand-off note, plus one reviewed Gmail draft to the learner's own address with a completed send checklist.   (Tools: Google Docs - Gmail - Gemini in Gmail or Docs where available - Drive.)

**Prerequisites**

- Approved 02-grounded-briefing and 02-claim-review-ledger from Lab 2.
- Open labs/assets/partner-email-thread.txt; it is a synthetic thread and is not sent to real recipients.
- Know the email address of the same training account; it is the only permitted recipient in this lab.

**Step-by-step**

1. Create a Google Doc in 02-Working named 03-partner-communication-pack. Add headings Thread summary, Partner invitation, Internal hand-off, Cross-artifact ledger and Send checklist. Under Thread summary create a table with Type, Statement, Owner, Due or PENDING and Source message.

   ```bash
   Required thread categories: confirmed facts | partner requests | proposed but unapproved commitments | open questions
   ```

2. Paste partner-email-thread.txt into Gemini in Gmail, Gemini in Docs or the documented fallback. Ask for a bounded summary. If no Gemini control is available, read each numbered message and manually add one table row per fact, request, decision, proposal or open question; copy the message number and use PENDING for a missing owner or due date. Insert the result into the summary table, then read the original thread and correct any missed qualification, wrong owner or proposed detail presented as confirmed.

   ```bash
   Summarise this synthetic email thread into a table with Type, Statement, Owner, Due or PENDING and Source message number. Separate confirmed facts, requests, decisions and proposals. Do not turn a proposal into a commitment. End with unresolved questions.
   ```

3. Under Partner invitation use the approved grounded briefing and corrected thread summary as the only sources. Ask Gemini for a subject line and 180-220 word invitation with purpose, confirmed logistics, preparation request, accessibility contact and next action. Require PENDING for any unresolved detail. If Gemini is unavailable, draft the same artifact manually: write the subject, two short purpose/logistics paragraphs, a three-item preparation list, accessibility line and next action, then count and edit it to 180-220 words.

   ```bash
   Persona: I am the Aster & Finch coordinator writing to invited partner representatives.
Task: Draft a clear invitation that explains why to attend and what to prepare.
Context: Use only the approved briefing and corrected thread summary below. Confirmed information overrides proposals; unresolved details remain PENDING.
Format: Subject line plus 180-220 word email with short paragraphs and a three-item preparation list.
Review: List every commitment, date, link, attachment and recipient assumption.
   ```

4. Edit the invitation in Docs. Use the G-E-A-R loop and the 02-claim-review-ledger to verify every event fact. Replace jargon, remove duplicate sentences and make the next action specific. Under Cross-artifact ledger add rows for Date, Delivery mode, Audience, Preparation request and Accessibility; show the value in Briefing, Thread and Final email.

   ```bash
   Ledger columns: Field | Briefing value | Thread value | Final email value | Result | Edit made
Result values: MATCH | PENDING | REPAIRED
   ```

5. Under Internal hand-off ask Gemini to turn the final invitation into a 120-word note for the operations team. Require Owner, Action, Due or PENDING, Source and Risk as a table. If Gemini is unavailable, manually restate only the invitation's confirmed actions in the same table and edit the surrounding note to 120 words. Verify that the note does not create a new external commitment and record the responsible human reviewer.

   ```bash
   Create a 120-word internal hand-off from the approved invitation. Use a table with Owner, Action, Due or PENDING, Source and Risk. Do not invent an owner, date or approved budget.
   ```

6. In Gmail start a new message addressed only to your own training account. Paste the reviewed subject and invitation, then save it as a draft; do not click Send. In the Doc complete the checklist rows To, Cc/Bcc, Subject, Dates, Commitments, Links, Attachments, Accessibility, Tone and Approver. Record the Gmail draft timestamp.

   ```bash
   Checklist result values: PASS | NOT USED | REPAIR
Required final state: Gmail Draft; recipient is the learner's own training address.
   ```


**Test it**

The communication pack must include all five headings, a thread summary that separates proposals from confirmed facts, a 180-220 word invitation, a five-field cross-artifact ledger, an internal hand-off with Owner/Action/Due/Source/Risk and a ten-row send checklist. Gmail must contain exactly one new unsent draft addressed only to the learner's own training account.

**Checkpoint and rejoin point**

Move the reviewed 03-partner-communication-pack to 03-Approved and leave the email unsent in Gmail Drafts. Lab 4 uses the approved message architecture and facts; it does not use the raw thread.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| The summary treats a proposed date or deliverable as confirmed. | Return to the source message, label it PROPOSAL and change the final text to PENDING until the approved briefing confirms it. |
| Gemini in Gmail cannot access the approved Drive file. | Use Gemini in Docs or paste the approved excerpt; do not broaden Drive sharing to solve the feature gap. |
| The draft is addressed to a synthetic email from the thread. | Remove it immediately and use only your own training address; synthetic addresses are source text, not live recipients. |

**Challenge**

Create a 90-word mobile-first version of the invitation. Preserve all confirmed logistics and compare which formatting changes improve scanning without removing required context.

**Reflection**

Which part of the email required authority rather than language skill, and how did you keep that decision with a person?

> **Note:** The complete lab and its support-file references are in labs/lab-03-*.md. Use only the supplied synthetic scenario and an account you are authorised to use. Do not paste passwords, secrets, protected personal data or confidential workplace content into a prompt. Keep live sending disabled until the lab explicitly calls for one reviewed draft to your own account.

---


### Lab 4 — Build the Partner Briefing Deck in Slides

Learning outcome: LO2: create and refine a coherent source-backed presentation and appropriate generated visual in Google Slides.

Goal: Turn the approved communication pack into a concise six-slide story with traceable evidence, accessible design and a reviewed visual.

You will design a slide sequence before generating content, build six low-density slides from approved facts and create one illustrative visual with Gemini or a native-shape fallback. A slide map and G-E-A-R ledger keep the story, evidence and audience action aligned.

**What you'll build**

A Google Slides file named 04-partner-briefing-deck with six slides, speaker notes and one reviewed visual, plus a slide-map table in 03-partner-communication-pack linking each slide to its message, source, visual purpose and audience action.   (Tools: Google Slides - Gemini in Slides where available - Google Docs - Drive.)

**Prerequisites**

- Approved 03-partner-communication-pack and approved 02-grounded-briefing.
- The Gmail message remains an unsent draft; use the approved Doc as the source.
- Open labs/assets/prompt-quality-checklist.md for the final sequence review.

**Step-by-step**

1. In the approved communication pack add a heading Slide map and a table with Slide, Audience question, One-sentence message, Evidence source, Visual purpose and Audience action. Create exactly six rows: Welcome, Why this briefing, Confirmed plan, How partners prepare, Coordination workflow and Next steps.

   ```bash
   Rule: each slide has one primary message and names an approved source or SOURCE NOT REQUIRED.
   ```

2. Create a blank Google Slides presentation in 02-Working named 04-partner-briefing-deck. Add six slides using the slide-map titles. Use a 16:9 layout, one consistent theme, title text of at least 28 pt and body text of at least 18 pt. Add the source filename and section to the speaker notes of slides 2-6.

   ```bash
   Deck order:
1 Welcome
2 Why this briefing
3 Confirmed plan
4 How partners prepare
5 Coordination workflow
6 Next steps
   ```

3. In Gemini in Slides, or in Gemini in Docs if the Slides control is unavailable, ask for candidate content for slides 2-6 using only the approved briefing and communication pack. Require one headline, no more than three short bullets and one evidence note per slide. If neither Gemini control is available, manually convert each slide-map row into that same headline, bullet and evidence-note structure using only the two approved artifacts. Insert only content that matches the slide map and source ledger.

   ```bash
   Create candidate text for slides 2-6. Use only the approved Aster & Finch briefing and communication pack. For each slide return Title, one-sentence headline, up to three bullets and Source. Preserve PENDING fields; do not invent a venue, speaker, URL, quotation or result.
   ```

4. Create one wide illustrative image for slide 1 or 2 with Gemini in Slides. Use an abstract collaboration scene with no logos, text, faces, real venue or documentary claim. If image generation is unavailable, build a native visual with three labelled circles: Partners, Evidence and Action, connected by arrows. Add alt text that explains the visual purpose.

   ```bash
   Visual prompt: Wide 16:9 editorial illustration of diverse abstract shapes collaborating around shared documents and data, calm blue and green palette, generous empty space on the left for a title, no text, no logos, no identifiable people, no photorealistic event venue.
   ```

5. Design slides 3-5 with one simple visual structure each: a confirmed-versus-pending table, a three-step preparation flow and a Source-to-Action workflow. Keep every PENDING field visible and do not shrink text below the stated sizes. On slide 3, add a bordered rectangle beside or below the confirmed-versus-pending table labelled DATA PLACEHOLDER - verified registration chart added in Lab 6. Add a final action and owner to slide 6.

   ```bash
   Slide 3 placeholder: DATA PLACEHOLDER - verified registration chart added in Lab 6
Preparation flow: Review brief -> Bring questions -> Confirm accessibility needs
Workflow: Approved source -> Gemini candidate -> Human review -> Partner action
   ```

6. Run a full-deck G-E-A-R review. Compare each slide with the slide map and speaker-note source, check titles and numbers against the claim ledger, then present the deck in full screen. Record PASS or REPAIR for Story sequence, Source match, Text readability, Visual accuracy, Alt text, PENDING fields and Final action. Apply repairs before moving the file. Record the seven checks in 03-partner-communication-pack under a Deck review heading.

   ```bash
   Required review rows: Story sequence | Source match | Text readability | Visual accuracy | Alt text | PENDING fields | Final action
   ```


**Test it**

The Slides file must contain exactly six slides in the mapped order; slides 2-6 must each have a speaker-note source; no slide may exceed one headline and three bullets; one reviewed visual must have alt text; the preparation and workflow visuals must use the stated sequence; slide 3 must include the labelled DATA PLACEHOLDER; and all seven final review rows must be recorded under Deck review in 03-partner-communication-pack and show PASS.

**Checkpoint and rejoin point**

Move 04-partner-briefing-deck to 03-Approved and keep the completed slide map in the approved communication pack. Lab 6 will replace only the labelled DATA PLACEHOLDER on slide 3 with a verified Sheets chart.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| Gemini creates unsupported speakers, dates or results. | Remove them, add the source filenames and require PENDING for absent fields before generating again. |
| The generated visual looks like a photograph of a real event. | Regenerate as an abstract editorial illustration or use the native-shape fallback and label it illustrative. |
| The slide title or bullets wrap into a crowded layout. | Shorten the message, split no additional slides and keep the minimum font sizes instead of shrinking text. |

**Challenge**

Create an alternate title-slide visual for a senior executive audience. Explain how the visual purpose changes while the approved facts and slide sequence remain constant.

**Reflection**

Which slide contributes most to the decision path, and what would be lost if it were replaced by a decorative image?

> **Note:** The complete lab and its support-file references are in labs/lab-04-*.md. Use only the supplied synthetic scenario and an account you are authorised to use. Do not paste passwords, secrets, protected personal data or confidential workplace content into a prompt. Keep live sending disabled until the lab explicitly calls for one reviewed draft to your own account.

---


## Topic 03 — Gemini in Sheets and Data Analysis  (Day 2 morning - 2 labs)

Formulas and tables - Analysis and summaries - Charts and visualisations - Cleaning and organising data

**Key concepts**

- Data grain — What one row represents; every formula, summary and chart must respect that level.
- Reproducible transformation — A visible formula, rule or step that another person can rerun and inspect.
- Analysis question — A precise metric, population, dimension and time scope that makes a result interpretable.
- Chart contract — Title, axes, units, series and source must faithfully encode the stated comparison.


### Generating Formulas, Tables and Insights in Sheets

Gemini in Sheets can help create tables, formulas and actions such as filters, formatting, pivots and dropdowns. The result is useful only when the data grain, field meaning, formula references and expected output are explicit and the inserted change is tested on known rows.

A syntactically valid formula can still answer the wrong question. Starting with a plain-language calculation and sample expected result makes it possible to review a suggestion instead of accepting it because the cell displays a number.

**How it works**

- State what one row represents and define each input column.
- Write the intended calculation in plain language with units and exclusions.
- Ask for a formula or table using exact sheet and column references.
- Inspect relative and absolute references before filling the formula.
- Test normal, blank, duplicate and boundary rows against manual expectations.

**Worked example**

- Each row is one synthetic partner registration; Seats is the requested quantity.
- A clean formula standardises status and flags Confirmed rows with missing dietary information.
- The learner tests one confirmed, one waitlisted and one blank row before filling down.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The data fields and expected result can be described precisely. | The sheet mixes several row types or merged headers without a defined grain. |
| The proposed formula remains visible and can be tested on sample rows. | A generated formula is filled across the dataset before its references are reviewed. |

**Practitioner quality lens**

- FAILURE SIGNAL: The formula returns values but changes meaning when copied down.
- REPAIR MOVE: Review row grain and lock only the references that should remain fixed.
- QUALITY EVIDENCE: A test table shows input, expected result, actual result and status.

---


### Analysing and Summarising Data with Gemini

Data analysis turns a stated question into defined metrics, comparisons and evidence. Gemini can propose pivots, calculations and narrative insights, but the analyst must define the population, denominator, filters, time scope and uncertainty before interpreting a pattern.

Narrative summaries often sound causal even when the sheet only shows association. Keeping metric definitions and calculation evidence beside the insight prevents plausible wording from outrunning the data.

**How it works**

- Write the decision question and define the valid population.
- Specify each metric, denominator, grouping and material exclusion.
- Create a pivot or formula output that exposes the calculation.
- Ask Gemini for observations grounded only in the visible result.
- Label facts, hypotheses and recommended follow-up separately.

**Worked example**

- Question: which partner segment needs the most follow-up before the briefing?
- Metrics: valid registrations, confirmation rate and missing-information count by segment.
- The summary states the observed gap and proposes a follow-up check without claiming why it occurred.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The dataset is clean enough for the defined question and calculations are visible. | The prompt asks for insights before defining valid rows or metrics. |
| The narrative distinguishes observed evidence from a possible explanation. | A small synthetic sample is used to claim a universal business trend. |

**Practitioner quality lens**

- FAILURE SIGNAL: The insight has no metric definition or supporting range.
- REPAIR MOVE: Add population, formula, grouping, time scope and source range.
- QUALITY EVIDENCE: Another learner reproduces the value from the same clean table.

---


### Creating Charts and Visualisations

A chart encodes a comparison through position, length, colour or shape. Gemini can propose and create visualisations in Sheets, but the user must choose a chart type that matches the question, display units and categories clearly, and verify every plotted value against the source table.

Visuals compress data and therefore amplify both clarity and error. A neutral descriptive title, readable labels and an honest axis help viewers understand what is plotted without implying a conclusion the data cannot support.

**How it works**

- Name the comparison: trend, ranking, composition, distribution or relationship.
- Choose the smallest chart type that visibly encodes that comparison.
- Use a clean source range at one consistent grain.
- Set title, axis labels, units, legend and category order.
- Compare plotted points with the table and add a concise evidence-based takeaway.

**Worked example**

- A horizontal bar chart ranks valid registrations by partner segment.
- The title states 'Valid registrations by partner segment'; the x-axis shows registrations.
- The learner checks each bar against the pivot and avoids a truncated scale that exaggerates differences.

**Decision guide**

| Use when | Avoid when |
|---|---|
| A visual makes three or more values or a pattern easier to compare. | A single number would be clearer as text or a compact table. |
| The source table and metric definition can remain available to the reader. | A decorative 3D or dual-axis treatment could distort the comparison. |

**Practitioner quality lens**

- FAILURE SIGNAL: The title claims a cause or trend that the chart does not encode.
- REPAIR MOVE: Use a neutral title and put the bounded observation in a separate note.
- QUALITY EVIDENCE: Title, axes, marks and source table all describe the same metric and grain.

---


### Cleaning and Organising Data with AI

Data cleaning makes values consistent without hiding the original evidence. Typical operations include trimming spaces, standardising categories, parsing dates, handling blanks, identifying duplicates and validating allowed values; every change needs a rule and a retained raw source.

Analysis quality is limited by the inputs. Asking Gemini to 'clean this' without rules can silently merge distinct values or fill unknowns, so a safe workflow profiles first, proposes rules, transforms a copy and reconciles row counts.

**How it works**

- Duplicate the raw tab and record the original row count and key fields.
- Profile blanks, category variants, date formats, duplicates and invalid values.
- Write a rule table with before, after, reason and treatment of uncertainty.
- Apply formulas or bounded actions to a clean tab while preserving raw values.
- Reconcile row counts, totals and exception counts before analysis.

**Worked example**

- The raw Segment field contains SME, sme and Small business.
- The rule maps approved variants to SME but leaves an unfamiliar value as REVIEW.
- A reconciliation confirms that no valid registration disappeared during deduplication.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The organisation can define acceptable values and retain the raw source. | Missing values are silently invented or duplicate rules are not documented. |
| Exceptions can be reviewed instead of guessed. | The only copy of the source is overwritten before totals are reconciled. |

**Practitioner quality lens**

- FAILURE SIGNAL: The clean table has fewer rows and no explanation for the difference.
- REPAIR MOVE: Restore the raw copy, log every excluded or merged row and reconcile totals.
- QUALITY EVIDENCE: The rule table, exception list and reconciliation explain every change.

---


### Lab 5 — Clean the Registration Tracker and Generate Formulas

Learning outcome: LO3: clean and organise spreadsheet data with documented rules, Gemini suggestions and reproducible formulas.

Goal: Preserve the raw synthetic registrations, standardise key fields and create a reconciled valid-analysis table.

You will import a deliberately inconsistent registration CSV into Sheets, define the row grain and cleaning rules, ask Gemini for formula help and verify every formula before filling it down. A separate Valid tab and reconciliation make exclusions visible.

**What you'll build**

A 05-registration-analysis Google Sheet with Raw, Clean, Valid, Rules and Formula-tests tabs. The workbook preserves 24 raw rows, produces 20 valid rows, flags exceptions and documents the exact formula and reason for every transformation.   (Tools: Google Sheets - Gemini in Sheets where available - Drive - registration-data.csv.)

**Prerequisites**

- Download or open labs/assets/registration-data.csv; it contains only synthetic contacts and non-routable example.com addresses.
- The C155-Aster-Finch folder and state subfolders from Lab 1 are available.
- Use a native Google Sheet because Gemini in Sheets works best with native Sheets files.

**Step-by-step**

1. In 02-Working create a Google Sheet named 05-registration-analysis. Import registration-data.csv into a tab named Raw and freeze row 1. Confirm that the row grain is one submitted registration and record 24 data rows. Duplicate Raw as Clean; never edit Raw. Add Rules, Formula-tests and Valid tabs.

   ```bash
   Control totals:
Raw data rows = 24
Unique registration IDs expected before rule review = 23
   ```

2. On Rules add columns Field, Observed issue, Before, After, Rule, Unknown treatment and Owner. Profile Segment, Status, Email and Registration_ID using filters or Gemini in Sheets. Record category variants, one later duplicate, one invalid email and any value outside the approved mappings. Do not ask Gemini to replace unknowns automatically.

   ```bash
   Approved Segment values: SME | Enterprise | Non-profit
Approved Status values: Confirmed | Waitlisted | Cancelled
Unknown treatment: REVIEW
   ```

3. In Clean add headers in K1:P1: Segment_Clean, Status_Clean, Email_Valid, Duplicate_Flag, Info_Flag and Date_Clean. Ask Gemini for formulas using these exact columns, then compare the suggestion with the formulas below. Enter the reviewed formulas in row 2.

   ```bash
   K2 =SWITCH(LOWER(TRIM(C2)),"sme","SME","small business","SME","enterprise","Enterprise","nonprofit","Non-profit","non-profit","Non-profit","REVIEW")
L2 =SWITCH(LOWER(TRIM(F2)),"confirmed","Confirmed","confirm","Confirmed","waitlist","Waitlisted","waitlisted","Waitlisted","cancelled","Cancelled","REVIEW")
M2 =REGEXMATCH(LOWER(TRIM(E2)),"^[^@\s]+@[^@\s]+\.[^@\s]+$")
N2 =COUNTIF($A$2:A2,A2)>1
O2 =IF(AND(L2="Confirmed",TRIM(H2)=""),"MISSING DIETARY","OK")
P2 =IF(J2="","REVIEW",IF(ISNUMBER(J2),J2,IFERROR(DATE(VALUE(LEFT(TO_TEXT(J2),4)),VALUE(MID(TO_TEXT(J2),6,2)),VALUE(RIGHT(TO_TEXT(J2),2))),"REVIEW")))
   ```

4. Before filling down, use Formula-tests to create six rows with Test, Input row, Expected result, Actual result, Formula and PASS/REPAIR. Cover a Small business segment, confirm status, invalid email, later duplicate, confirmed row with blank Dietary and a valid date. Use 2026-07-20 for the sixth input and expect 20 July 2026; format Date_Clean as dd mmm yyyy. Repair any formula that fails, then fill K2:P2 down through row 25.

   ```bash
   Required test examples:
Segment ' Small Business ' -> SME
Status 'confirm' -> Confirmed
Email without @ -> FALSE
Second AF-010 -> TRUE
Confirmed plus blank Dietary -> MISSING DIETARY
Date 2026-07-20 -> 20 Jul 2026
   ```

5. Copy Clean row 1 to Valid row 1. In Valid A2 enter the FILTER formula below. This table keeps records with a valid email, first occurrence of the registration ID and approved clean Segment and Status. It does not remove rows from Raw or Clean.

   ```bash
   =FILTER(Clean!A2:P,Clean!A2:A<>"",Clean!M2:M=TRUE,Clean!N2:N=FALSE,Clean!K2:K<>"REVIEW",Clean!L2:L<>"REVIEW")
   ```

6. At the top of Rules add a Reconciliation block. Record Raw rows, Valid rows, Invalid email exclusions, Later duplicate exclusions, Segment REVIEW exclusions and Status REVIEW exclusions. Add the check Raw = Valid + exclusions. Use filters to name each excluded Registration_ID and the exact rule.

   ```bash
   Expected reconciliation:
Raw 24 = Valid 20 + Invalid email 1 + Later duplicate 1 + Segment REVIEW 1 + Status REVIEW 1
   ```

7. Apply a filter and conditional formatting to Clean so REVIEW, FALSE and TRUE duplicate flags are visible. Protect the Raw tab with a warning if your account permits it. Record the reviewer and move the Sheet to 03-Approved only when all six formula tests and the reconciliation pass.

   ```bash
   Approval checks: Raw unchanged | 6 formula tests PASS | Valid rows 20 | reconciliation balances | exclusions named
   ```


**Test it**

Raw must contain 24 data rows and remain unchanged; Clean must contain six new formula columns; Formula-tests must show six PASS rows; Valid must contain 20 data rows; and Rules must reconcile 24 = 20 + 1 + 1 + 1 + 1 with every excluded Registration_ID named. A count of MISSING DIETARY in Valid must equal 3.

**Checkpoint and rejoin point**

Keep 05-registration-analysis in 03-Approved with Raw, Clean, Valid, Rules and Formula-tests. Lab 6 uses only Valid for metrics and cites the Rules reconciliation for exclusions.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| The CSV opens as an Excel file and Gemini controls are unavailable. | Use File > Save as Google Sheets, rename the imported tab Raw and continue from the native file. |
| The duplicate formula marks both AF-010 rows. | Use the expanding range $A$2:A2 so only the later occurrence returns TRUE. |
| The Valid tab returns no rows or a range-size error. | Confirm every FILTER condition starts on row 2 and covers the same open-ended row range. |

**Challenge**

Add a reusable data-validation dropdown for a manually reviewed Clean_Status_Override field. Explain why an override needs owner, reason and timestamp rather than silently replacing the formula.

**Reflection**

Which cleaning decision could most change the later insight, and what evidence makes that decision auditable?

> **Note:** The complete lab and its support-file references are in labs/lab-05-*.md. Use only the supplied synthetic scenario and an account you are authorised to use. Do not paste passwords, secrets, protected personal data or confidential workplace content into a prompt. Keep live sending disabled until the lab explicitly calls for one reviewed draft to your own account.

---


### Lab 6 — Analyse Registrations and Build the Decision Dashboard

Learning outcome: LO3: define metrics, analyse clean data and create a truthful chart and bounded narrative in Sheets.

Goal: Answer which partner segment needs follow-up using visible metrics, a reproducible pivot and a chart that matches the source table.

You will define the valid population and metrics before asking Gemini for insights, create a pivot table and confirmation-rate calculations, then build a simple chart. The final narrative separates observations from hypotheses and updates the approved Slides deck.

**What you'll build**

Analysis and Dashboard tabs inside 05-registration-analysis containing a verified pivot, metric definitions, confirmation rates, one horizontal bar chart and a three-part insight note, plus the linked chart inserted into slide 3 of 04-partner-briefing-deck.   (Tools: Google Sheets - Gemini in Sheets where available - Google Slides - Drive.)

**Prerequisites**

- Approved 05-registration-analysis with 20 valid rows and a balanced reconciliation.
- Approved 04-partner-briefing-deck from Lab 4.
- Do not analyse the Raw or Clean exception rows as if they belong to the valid population.

**Step-by-step**

1. Add Analysis and Dashboard tabs. At the top of Analysis write the question: Which partner segment needs the most follow-up before the briefing? Define Valid registrations, Confirmed registrations, Confirmation rate, Missing-information count, population, time scope and material exclusions. Cite Valid and Rules.

   ```bash
   Confirmation rate = Confirmed valid registrations / All valid registrations in the segment
Population = 20 rows in Valid
Exclusions = 4 rows documented in Rules
   ```

2. Create a pivot table from Valid A1:P on Analysis. Set Rows to Segment_Clean, Columns to Status_Clean and Values to COUNTA of Registration_ID. Turn off totals only if the counts remain visible elsewhere. Compare every pivot cell with a filtered count in Valid.

   ```bash
   Expected counts:
SME: Confirmed 5 | Waitlisted 2 | Cancelled 1 | Total 8
Enterprise: Confirmed 5 | Waitlisted 2 | Cancelled 1 | Total 8
Non-profit: Confirmed 2 | Waitlisted 1 | Cancelled 1 | Total 4
   ```

3. Beside the pivot create a metric table with Segment, Valid registrations, Confirmed, Confirmation rate and Missing information. Use cell references to the pivot and a COUNTIFS against Valid for Info_Flag. Format confirmation rate as a percentage with one decimal place.

   ```bash
   Expected rates:
SME 62.5%
Enterprise 62.5%
Non-profit 50.0%
Expected total MISSING DIETARY = 3
   ```

4. Ask Gemini in Sheets for three observations using only the metric table. Require each sentence to show the number, comparison and limitation, and require explanations to be labelled HYPOTHESIS. Verify the response and write a final note with Observed, Hypothesis and Recommended follow-up as separate headings. If Gemini in Sheets is unavailable, manually write two factual comparisons from the visible metric table, one explicitly labelled hypothesis and one proportionate follow-up; apply the same number, comparison and limitation checks.

   ```bash
   Using only this metric table, write: (1) two factual observations with values, (2) one clearly labelled hypothesis, and (3) one proportionate follow-up. Do not claim causation. Mention that the Non-profit segment has only four valid registrations.
   ```

5. On Dashboard copy or reference Segment and Valid registrations. Insert a horizontal bar chart, order segments by valid registrations descending and title it Valid registrations by partner segment. Label the horizontal axis Registrations, start it at zero and keep one series with no 3D effect. Check all three bars against the metric table.

   ```bash
   Expected bar values: Enterprise 8 | SME 8 | Non-profit 4
   ```

6. Open the approved 04-partner-briefing-deck. On slide 3 replace only the labelled DATA PLACEHOLDER with the chart from Sheets as a linked chart and add a short note: 20 valid registrations after 4 documented exclusions. Add the Sheet name, Valid population and Rules exclusions to the slide speaker notes. Run the deck Source match and Visual accuracy checks again.

   ```bash
   Speaker-note source: 05-registration-analysis > Analysis metric table; population 20; exclusions documented in Rules; chart linked from Dashboard.
   ```


**Test it**

The pivot must reproduce 8/8/4 valid registrations and 5/5/2 confirmations by segment; the rates must be 62.5%, 62.5% and 50.0%; total missing information must be 3; the chart must have one series, a zero baseline and the neutral title; the insight must separate observation, hypothesis and follow-up; and slide 3 must contain the linked chart with the population and exclusion source note.

**Checkpoint and rejoin point**

Keep the updated Sheet and Slides file in 03-Approved. Lab 7 uses the verified counts and approved deck as sources for the rehearsal meeting and Drive synthesis.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| The pivot counts 24 rather than 20 rows. | Change the source range to Valid A1:P and confirm that the Valid tab still passes the reconciliation. |
| The chart title or note says performance improved. | Use a neutral descriptive title and keep the bounded observation separate from any hypothesis. |
| The linked chart in Slides shows stale values. | Select the chart and click Update, then compare each bar with the current Analysis metric table. |

**Challenge**

Create a second chart of confirmation rate by segment. Decide whether the small Non-profit denominator needs a direct label or note and explain your choice.

**Reflection**

Which statement in your insight is evidence and which is interpretation, and how can the reader tell?

> **Note:** The complete lab and its support-file references are in labs/lab-06-*.md. Use only the supplied synthetic scenario and an account you are authorised to use. Do not paste passwords, secrets, protected personal data or confidential workplace content into a prompt. Keep live sending disabled until the lab explicitly calls for one reviewed draft to your own account.

---


## Topic 04 — AI-Powered Workflows and Automation in Workspace  (Day 2 afternoon - 2 labs)

Meet notes - Drive search and organisation - Connecting apps and simple automations - Practical workflow design

**Key concepts**

- Workflow state — Input, owner, action, output and approval status make work visible across apps.
- Permission-aware retrieval — Gemini can only be useful and safe when sources and recipients match authorised access.
- Bounded automation — A trigger performs a narrow action with explicit fields, logs and stop conditions.
- Observe before scaling — Run, inspect evidence, handle exceptions and expand only after a controlled test.


### AI-Assisted Meetings and Notes in Google Meet

Eligible Google Workspace accounts can use Gemini-supported meeting features to capture notes, summarise discussion and identify next steps. The notes are a generated record that must be announced, shared deliberately and reviewed against the conversation before becoming an official source.

Meeting summaries can save transcription and follow-up time, but they may omit context, misattribute an action or expose notes to the wrong invitees. Consent, host control, language support, sharing settings and post-meeting review are part of the workflow rather than optional administration.

**How it works**

- Confirm feature availability, meeting purpose, permitted content and participant notice.
- Choose who should receive the notes and apply the minimum sharing scope.
- Capture or use the provided synthetic transcript when the feature is unavailable.
- Review decisions, owners, dates, unresolved points and wording against the conversation.
- Publish an approved recap and retain exceptions or corrections visibly.

**Worked example**

- The partner-briefing rehearsal has a synthetic ten-minute transcript and three proposed actions.
- The coordinator corrects one owner, changes an uncertain date to pending and restricts the notes to the internal team.
- Only the approved action table is copied to the shared follow-up document.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Participants are informed and the organisation permits the meeting feature. | The conversation contains restricted material outside the approved note-taking purpose. |
| A host or owner will review the generated notes before wider sharing. | Invite visibility is mistaken for permission to access the generated notes document. |

**Practitioner quality lens**

- FAILURE SIGNAL: A generated action item has the wrong owner or an invented deadline.
- REPAIR MOVE: Check the relevant transcript segment and mark unresolved fields as pending.
- QUALITY EVIDENCE: The review log records original text, correction, source and approver.

---


### Organising and Searching Drive with Gemini

Gemini in Drive can summarise files or folders, answer questions across permitted sources and help locate or organise material. Retrieval is permission-aware but still depends on clear folder scope, current file versions, meaningful names and a user who verifies the cited sources.

Search becomes unreliable when a folder mixes drafts, duplicates and unclear ownership. A simple information architecture and source register let Gemini retrieve relevant evidence without treating an obsolete file as the controlling record.

**How it works**

- Define the project folder, owner, audience and naming convention.
- Separate source, working, approved and archive states.
- Select the smallest relevant files or folder as Gemini context.
- Ask for an answer with source filenames, open questions and no unsupported inference.
- Open the cited files, verify the response and store the approved output in its correct state.

**Worked example**

- The C155 project folder contains 01-Source, 02-Working, 03-Approved and 04-Archive.
- Gemini summarises only the approved brief and reviewed registration insight, citing both filenames.
- An older agenda remains in Archive and is not used as the final event source.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The folder has clear ownership, versions and access controls. | A broad Drive query could mix personal, obsolete or unrelated content. |
| The response can show which files supplied the relevant information. | The user assumes retrieval proves the answer is complete or current. |

**Practitioner quality lens**

- FAILURE SIGNAL: The answer cites a draft that should no longer govern the project.
- REPAIR MOVE: Clarify file states, narrow the source scope and identify the controlling record.
- QUALITY EVIDENCE: Every answer links to an accessible current source in the project register.

---


### Connecting Apps and Building Simple Automations

Google Apps Script is a cloud-based JavaScript platform for extending and automating Workspace. A simple automation reads defined fields, applies a narrow rule and creates an observable action such as a Gmail draft or status update; it should include a dry-run mode, log and explicit authorisation.

Automation removes repeated clicks but also repeats defects at speed. Restricting the trigger, recipient, data fields and action surface makes a beginner workflow easier to understand, test, stop and review before it affects other people.

**How it works**

- Draw the event, input, rule, action, owner and failure path before writing code.
- Use Gemini to explain or draft a small script against an explicit specification.
- Inspect permissions and keep live sending disabled during the first run.
- Test one synthetic row and compare the draft, sheet update and execution log.
- Handle blanks, duplicates and errors before considering a wider trigger.

**Worked example**

- A bound Sheets script reads one READY row and creates a Gmail draft to the learner's own address.
- Dry-run mode records the intended recipient and subject without creating the draft.
- A live test creates one draft, writes DRAFTED and stores a timestamp so the row is not processed twice.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The process is repetitive, rule-based, low-risk and has an observable success condition. | The automation would bulk-send, delete, change access or process confidential data as a first test. |
| The user can review scopes, logs and every action before expanding the run. | The workflow lacks an owner, idempotency rule or way to stop and inspect failures. |

**Practitioner quality lens**

- FAILURE SIGNAL: Running the script twice creates duplicate external actions.
- REPAIR MOVE: Add a processed status or unique key and skip rows already handled.
- QUALITY EVIDENCE: The test log shows one input row, one intended action and one final status.

---


### Designing Practical AI Productivity Workflows

A practical workflow links a business trigger to approved sources, human and AI steps, outputs, controls and evidence. The C-O-N-T-R-O-L canvas used here captures Context, Owner, Needed inputs, Task sequence, Review, Output destination and Learning signal.

Tool-first automation often optimises an unclear process. Designing the state changes and review gates first reveals where Gemini adds value, where a person must decide, and which evidence proves the workflow is safe and useful.

**How it works**

- Context: define the trigger, audience, desired outcome and boundary.
- Owner and inputs: name authority, sources, permissions and required fields.
- Task sequence: separate generation, deterministic operations and human decisions.
- Review and output: set gates, destination, sharing scope and exception path.
- Learning signal: measure time, correction rate, completion and recurring failure.

**Worked example**

- A READY registration row triggers a proposed follow-up, not an automatic external send.
- Gemini helps draft the message; Apps Script creates a Gmail draft; the coordinator reviews and sends manually.
- The log records draft creation, corrections and whether the workflow saved time without increasing errors.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The process has a stable trigger, bounded inputs and a human owner. | The process is still ambiguous or relies on unrecorded personal judgement. |
| Success, correction and exception evidence can be collected. | Productivity is measured only by output volume rather than quality and risk. |

**Practitioner quality lens**

- FAILURE SIGNAL: The workflow is fast but no one can explain who approved the result.
- REPAIR MOVE: Add a named gate, status field and evidence artifact before the output leaves Draft.
- QUALITY EVIDENCE: The canvas and run log link trigger, sources, actions, reviewer, output and learning.

---


### Lab 7 — Run the Meeting-to-Drive Follow-Up Workflow

Learning outcome: LO4: review AI-assisted meeting notes, organise approved Drive sources and produce a permission-aware follow-up brief.

Goal: Convert a synthetic rehearsal meeting into verified actions and a source-cited Drive brief without confusing generated notes with an approved record.

You will configure or simulate a Gemini-supported meeting-notes workflow, review a supplied transcript, correct owners and dates, and organise the project's approved Drive sources. Gemini in Drive or a manual fallback then produces a source-cited follow-up brief.

**What you'll build**

A 07-meeting-notes-review Google Doc, a 07-source-register Google Sheet and a 07-approved-follow-up-brief Google Doc containing three verified actions, one open question, source citations, sharing controls and a correction log.   (Tools: Google Meet - Gemini meeting features where available - Google Drive - Docs - Sheets.)

**Prerequisites**

- Approved communication pack, Slides deck and 05-registration-analysis from Labs 3-6.
- Open labs/assets/meeting-transcript.txt and labs/assets/workflow-control-checklist.md.
- Use the supplied transcript if Take notes for me is unavailable or not enabled by the administrator.

**Step-by-step**

1. Create a Google Doc in 02-Working named 07-meeting-notes-review. Add headings Controls, Generated or practice notes, Verified decisions, Verified actions, Open questions, Correction log and Sharing decision. Under Controls record feature status, host, participant notice, permitted content, note recipients, language, source and reviewer.

   ```bash
   Feature status: Available demonstration | Transcript fallback
Sharing default for this lab: Restricted; learner and named reviewer only
   ```

2. If Take notes for me is available in a trainer-hosted practice meeting, observe the notice and sharing controls and export the notes after the demonstration. Otherwise copy the Meeting notes candidate section from meeting-transcript.txt into Generated or practice notes. Do not create a real meeting with external people for this lab.

   ```bash
   Fallback source: labs/assets/meeting-transcript.txt
Generated notes remain a candidate until checked against the transcript.
   ```

3. Read the full transcript and create tables for Verified decisions and Verified actions. Actions must have Action, Owner, Due or PENDING, Source lines, Status and Reviewer. Compare the candidate notes with the transcript and record each wrong owner, wrong date, omitted qualification or unsupported commitment in the Correction log.

   ```bash
   Expected action owners after review: Jamie | Marcus | Noor
Expected open question: final facilitator confirmation
Do not change a PENDING field without transcript evidence.
   ```

4. Create a Google Sheet in 02-Working named 07-source-register with columns File, State, Owner, Purpose, Controlling section or range, Last reviewed, Access and Used by. Add the approved grounded briefing, communication pack, Slides deck and registration Sheet. Add 07-meeting-notes-review as WORKING until its correction log is complete.

   ```bash
   State values: SOURCE | WORKING | APPROVED | ARCHIVE
Access values: Restricted | Named collaborators | Link viewer
   ```

5. Organise C155-Aster-Finch so original supplied sources remain in 01-Source, current work-in-progress files remain in 02-Working, reviewed course outputs are in 03-Approved and no obsolete file remains mixed with current work. Do not delete files; move a superseded copy to 04-Archive and update the register if one exists.

   ```bash
   Control check: every registered file has one current state, one owner and one controlling section or range.
   ```

6. Create a Google Doc in 02-Working named 07-approved-follow-up-brief. In Gemini in Drive, select only the approved communication pack, Slides deck, registration Sheet and reviewed meeting notes, then ask for the structure below. If Gemini in Drive is unavailable, open the registered files and create the same brief manually.

   ```bash
   Using only the four selected C155 project sources, create a follow-up brief with Confirmed event plan, Verified registration insight, Decisions, Actions, Open question and Source citations. For every section name the exact source filename and section or range. Do not use files in 04-Archive. Preserve PENDING and distinguish an observed metric from a meeting decision.
   ```

7. Open every source cited by the follow-up brief and verify the statement. Apply G-E-A-R, record the final reviewer and change the sharing setting to Restricted or named training collaborators only. Move the reviewed meeting notes, source register and follow-up brief to 03-Approved when all checks pass.

   ```bash
   Final checks: 3 actions | 1 open question | counts 20 valid and 4 exclusions | chart values 8/8/4 | all citations open | no Archive source | sharing matches the recorded decision
   ```


**Test it**

The meeting-notes review must show control settings, three verified actions owned by Jamie, Marcus and Noor, one facilitator open question and a correction log. The source register must cover five current project artifacts with state, owner, range and access. The follow-up brief must cite exact filenames, retain 20 valid/4 excluded and 8/8/4 segment counts, use no Archive source and have a sharing setting that matches the recorded decision.

**Checkpoint and rejoin point**

Keep 07-meeting-notes-review, 07-source-register and 07-approved-follow-up-brief in 03-Approved. Lab 8 uses the three verified actions and source register to define one draft-only automation.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| Take notes for me is unavailable or requires a different plan. | Record Transcript fallback and use meeting-transcript.txt; do not change accounts or move restricted content. |
| Gemini in Drive cites a draft or an Archive file. | Clear selected sources, choose only files marked APPROVED in the register and rerun with the explicit state rule. |
| An invitee can see the notes attachment but cannot open it. | Remember that event visibility is not file permission; set access according to the recorded sharing decision. |

**Challenge**

Create a before-and-after table that shows the candidate note, corrected note, evidence line and possible consequence for each correction. Use it to propose one prompt or meeting practice improvement.

**Reflection**

Which meeting-note error would have caused the largest downstream problem, and where did the workflow stop it?

> **Note:** The complete lab and its support-file references are in labs/lab-07-*.md. Use only the supplied synthetic scenario and an account you are authorised to use. Do not paste passwords, secrets, protected personal data or confidential workplace content into a prompt. Keep live sending disabled until the lab explicitly calls for one reviewed draft to your own account.

---


### Lab 8 — Automate the Approved Follow-Up from Sheets

Learning outcome: LO4: design, implement and verify a bounded Apps Script automation that connects Sheets and Gmail.

Goal: Create and verify one reviewed Gmail draft when Apps Script is available, or complete an evidence-labelled code trace when it is blocked, while keeping sending manual.

You will use the approved follow-up evidence to specify a low-risk automation, ask Gemini to explain or draft the code and compare it with the supplied safe script. When Apps Script is available, the script first logs an intended action, then creates one Gmail draft to your own address and refuses to duplicate it. When access is blocked, you trace the same controls and clearly leave live evidence pending.

**What you'll build**

An Automation tab and CONTROL canvas in 05-registration-analysis plus either (a) a bound Apps Script project using apps-script-draft.gs, one reviewed Gmail draft to the learner's own account and a run log, or (b) a four-case code trace with live evidence explicitly pending. Both paths cover dry-run, live-run, HOLD and duplicate-prevention behaviour.   (Tools: Google Sheets - Apps Script - Gmail Drafts - Gemini in Workspace where available.)

**Prerequisites**

- Approved 07-approved-follow-up-brief and three verified actions from Lab 7.
- Open labs/assets/apps-script-draft.gs and labs/assets/workflow-control-checklist.md.
- Apps Script access may require administrator approval; use the code walk-through fallback if blocked.
- Know the learner's own training email address; no other live recipient is permitted.

**Step-by-step**

1. In 05-registration-analysis add a tab named CONTROL. Copy the headings Context, Owner, Needed inputs, Task sequence, Review, Output destination and Learning signal. Define a manual trigger that reads one READY row, creates a Gmail draft only, writes DRAFTED plus an ID and timestamp, skips HOLD or processed rows and leaves Send as a human action.

   ```bash
   Required limits: manual run | one learner-owned recipient | no auto-send | no delete | no permission change | log every result
   ```

2. Add an Automation tab with headers Status, Email, Contact_Name, Subject, Body, Draft_Status, Draft_ID, Drafted_At and Last_Run_Note. In row 2 enter READY, your own training email, Your Name, [C155 TEST] Aster & Finch partner follow-up and a 100-150 word body based on one verified Lab 7 action. In row 3 enter HOLD and hold@example.com.

   ```bash
   Row 2 recipient must be the learner's own account.
Row 3 is a synthetic HOLD row and must never produce a draft.
Leave Draft_Status, Draft_ID, Drafted_At and Last_Run_Note blank.
   ```

3. Ask Gemini in Docs, Sheets or the trainer demonstration to explain how a bound Apps Script could satisfy the CONTROL canvas. Require a dry-run constant, header-based columns, email validation, signed-in-user recipient check, a one-eligible-row limit, READY filter, duplicate prevention, Gmail draft instead of send and an execution log. Compare the response line by line with apps-script-draft.gs and list any missing control before using the supplied script.

   ```bash
   Explain a beginner Google Apps Script for a Sheet named Automation. It must process only READY rows with blank Draft_Status, stop when more than one row is eligible, require the recipient to match Session.getEffectiveUser(), validate the email, support DRY_RUN, use GmailApp.createDraft only when live, write DRAFTED/ID/timestamp, log each outcome, skip HOLD and skip processed rows. Do not use GmailApp.sendEmail, delete, share or change file permissions.
   ```

4. If Apps Script access is available, choose Extensions > Apps Script, replace the editor content with apps-script-draft.gs, save the project as C155 Follow-Up Draft Lab and confirm const DRY_RUN = true. Select runFollowUpDrafts and click Run, review permissions before allowing them, then open the execution log and Automation row 2. If Apps Script is blocked, do not paste or run code; record Access blocked and proceed to the four-case trace in Step 6.

   ```bash
   Available-path dry run: log contains DRY RUN; Last_Run_Note starts DRY RUN OK; Draft_Status, Draft_ID and Drafted_At remain blank; Gmail has no new C155 TEST draft.
Blocked path: Access blocked recorded; no execution or Gmail-draft claim.
   ```

5. On the available path, change only const DRY_RUN = true to const DRY_RUN = false, save and run runFollowUpDrafts again. Open Gmail Drafts and inspect the message without sending it. Verify recipient, subject, body, source facts and absence of unintended Cc/Bcc or attachment. On the blocked path, skip this execution and keep Draft_Status, Draft_ID and Drafted_At blank.

   ```bash
   Available-path live run: exactly one unsent draft with subject [C155 TEST] Aster & Finch partner follow-up; row 2 Draft_Status = DRAFTED; Draft_ID and Drafted_At are populated.
Blocked path: no draft created; all live-result fields remain blank.
   ```

6. If Apps Script access is available, run runFollowUpDrafts a third time without changing the Sheet. Confirm that no second draft is created and row 3 remains HOLD with blank draft fields. Record all three runs in CONTROL with Mode, Input row, Intended action, Observed result, Evidence and Decision. If Apps Script is blocked, use the supplied script and CONTROL to trace four cases: dry READY self, live READY self, repeat DRAFTED and HOLD. For each case record the expected code branch, Sheet writes and Gmail effect; keep live evidence fields blank and do not claim a draft ran.

   ```bash
   Available path: 1 DRY_RUN -> no draft | 2 LIVE -> one draft and DRAFTED | 3 LIVE repeat -> no duplicate | HOLD -> no action
Blocked path: four traced cases with expected branch, Sheet writes and Gmail effect; live result remains PENDING
   ```

7. Complete the final G-E-A-R and CONTROL review. Keep the Gmail item as a draft or delete it manually after documenting the test; do not send it. Record which authorisation scope was requested, which data fields the script reads, how it stops duplicates and what would need manager or administrator approval before any workplace pilot.

   ```bash
   Final decision values: SAFE COURSE TEST COMPLETE | CODE WALK-THROUGH COMPLETE - LIVE TEST PENDING | HOLD FOR REPAIR
Workplace expansion is outside this lab and requires a new owner, data and recipient review.
   ```


**Test it**

CONTROL must define all seven fields and the stated limits; Automation must contain one READY self-addressed row and one HOLD synthetic row. On the available path, dry run must create no draft, live run must create exactly one unsent C155 TEST Gmail draft and write DRAFTED, ID and timestamp, the repeat run must create no duplicate and HOLD must remain untouched. On the blocked path, CONTROL must trace dry READY self, live READY self, repeat DRAFTED and HOLD with the expected branch, Sheet writes and Gmail effect; live evidence fields must remain blank and the decision must be CODE WALK-THROUGH COMPLETE - LIVE TEST PENDING. The relevant run record and final human decision must be complete.

**Checkpoint and rejoin point**

Retain the Sheet, supplied script and either the available-path execution evidence and unsent test draft or the blocked-path four-case trace with live evidence pending. Do not enable a time trigger, bulk rows or external recipients in this course.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| Extensions > Apps Script is blocked. | Use the four-case alternative trace in Step 6, leave live evidence blank and record CODE WALK-THROUGH COMPLETE - LIVE TEST PENDING. |
| The script says a required header is missing. | Compare the nine Automation headers character for character and remove leading or trailing spaces. |
| A second draft appears after the repeat run. | Stop, keep sending disabled and confirm the script skips any row whose Draft_Status is not blank. |
| The script reports more than one unprocessed READY row. | Keep DRY_RUN true, change every unintended row to HOLD and continue only when exactly one self-addressed READY row remains. |
| The script cannot confirm the signed-in user or rejects the recipient. | Do not bypass the safety stop. Sign in with the intended training account and make row 2 Email exactly match that account; otherwise use the blocked-path trace. |

**Challenge**

Add an approved Preview column that stores the subject and first 60 body characters during dry run. Explain why preview evidence is useful and why it still does not authorise sending.

**Reflection**

Which control made the automation observable and reversible, and what new risk would appear if the workflow sent messages automatically?

> **Note:** The complete lab and its support-file references are in labs/lab-08-*.md. Use only the supplied synthetic scenario and an account you are authorised to use. Do not paste passwords, secrets, protected personal data or confidential workplace content into a prompt. Keep live sending disabled until the lab explicitly calls for one reviewed draft to your own account.

---


## Wrap-Up - From Helpful Feature to Reliable Workflow

The course artifacts form one traceable chain: approved sources and a prompt charter feed the communication pack; the clean Sheet feeds the data story; the reviewed meeting recap and Drive register feed one bounded follow-up automation.

**A reusable operating pattern**

- Define the task, decision owner, approved sources and destination before opening Gemini.
- Generate a bounded candidate with P-T-C-F, source limits and explicit review criteria.
- Keep calculations, transformations and file states visible and reproducible.
- Apply G-E-A-R to the final assembled artifact, not only to individual fragments.
- Automate one low-risk action in dry-run mode, inspect evidence and expand only with approval.

**Authoritative references used**

- Course outline: https://www.tertiarycourses.com.sg/google-workspace-with-gemini.html
- Google Workspace prompting guidance: https://workspace.google.com/resources/ai/writing-effective-prompts/
- Gemini in Docs: https://support.google.com/docs/answer/14206696
- Gemini in Sheets: https://support.google.com/docs/answer/14356410
- Gemini in Gmail: https://support.google.com/mail/answer/14355636
- Gemini in Drive: https://support.google.com/drive/answer/14217860
- Gemini in Meet notes: https://support.google.com/meet/answer/14754931
- Workspace data protection: https://support.google.com/mail/answer/14615114
- Apps Script overview: https://developers.google.com/apps-script
- Apps Script automation quickstart: https://developers.google.com/apps-script/quickstart/automation

**Feature availability reminder**

- Google Workspace features, labels and plan eligibility change over time.
- Check the current Google help page and your administrator settings before deployment.
- A trainer demo or supplied fallback preserves the learning task when an in-app feature is unavailable.

---


## Next Steps

- Re-run the eight labs from a fresh copy of the synthetic source pack and compare the correction log with your first attempt.
- Choose one real low-risk workplace workflow and complete a CONTROL canvas before using any organisation data.
- Agree with your manager or administrator which data classes, Workspace plans, sharing settings and approval gates are permitted.
- Build a prompt library that stores purpose, approved source type, output format, review criteria, owner and last review date.
- Pilot one draft-only automation with a small group, measure correction and exception rates, then decide whether to expand.


## Glossary

- **Apps Script** — Google's cloud-based JavaScript platform for extending and automating Workspace.
- **Approval gate** — A named decision point where a person checks evidence and authorises the next state.
- **Bounded automation** — An automation restricted to defined inputs, actions, recipients, logs and stop conditions.
- **Candidate output** — Generated material that must still be checked and approved before use.
- **Chart contract** — The explicit relationship among question, source table, chart type, title, axes, units and series.
- **CONTROL canvas** — Context, Owner, Needed inputs, Task sequence, Review, Output destination and Learning signal.
- **Data grain** — What one row or observation represents.
- **Data minimisation** — Using only the fields required for the stated purpose.
- **Dry run** — A mode that records intended actions without performing their external effect.
- **Grounding** — Using specific permitted sources as context for a response.
- **G-E-A-R** — Grounding, Evidence, Audience and Risk - the course review loop.
- **Idempotency** — A control that prevents the same input from causing duplicate actions when processed again.
- **Least privilege** — Giving users, files and processes only the access needed for the task.
- **Metric definition** — The calculation, population, denominator, units, time scope and exclusions behind a number.
- **P-T-C-F** — Persona, Task, Context and Format - the core prompt structure used in the course.
- **Reconciliation** — Comparing counts and totals before and after a transformation to explain every change.
- **Source boundary** — The explicit set of files or facts a generated response may use.
- **Synthetic data** — Artificial practice data that does not describe real people or confidential operations.
- **Workspace grounding** — Gemini's use of permitted Workspace content selected or retrieved for a task.
- **Workflow state** — A visible stage such as Source, Working, Approved, Drafted, Sent or Exception.
