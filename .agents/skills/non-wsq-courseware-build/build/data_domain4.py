"""Topic 4 labs for C155."""

DOMAIN4 = [
    dict(
        num=7,
        topic=4,
        title="Run the Meeting-to-Drive Follow-Up Workflow",
        duration=70,
        objective="LO4: review AI-assisted meeting notes, organise approved Drive sources and produce a permission-aware follow-up brief",
        goal="Convert a synthetic rehearsal meeting into verified actions and a source-cited Drive brief without confusing generated notes with an approved record.",
        workflow=["Set note controls", "Review transcript", "Organise Drive", "Synthesize approved follow-up"],
        desc=(
            "You will configure or simulate a Gemini-supported meeting-notes workflow, review a supplied "
            "transcript, correct owners and dates, and organise the project's approved Drive sources. "
            "Gemini in Drive or a manual fallback then produces a source-cited follow-up brief."
        ),
        build=(
            "A 07-meeting-notes-review Google Doc, a 07-source-register Google Sheet and a "
            "07-approved-follow-up-brief Google Doc containing three verified actions, one open question, "
            "source citations, sharing controls and a correction log."
        ),
        services="Google Meet - Gemini meeting features where available - Google Drive - Docs - Sheets",
        prerequisites=[
            "Approved communication pack, Slides deck and 05-registration-analysis from Labs 3-6.",
            "Open labs/assets/meeting-transcript.txt and labs/assets/workflow-control-checklist.md.",
            "Use the supplied transcript if Take notes for me is unavailable or not enabled by the administrator.",
        ],
        steps=[
            (
                "Create a Google Doc in 02-Working named 07-meeting-notes-review. Add headings Controls, "
                "Generated or practice notes, Verified decisions, Verified actions, Open questions, "
                "Correction log and Sharing decision. Under Controls record feature status, host, participant "
                "notice, permitted content, note recipients, language, source and reviewer.",
                "Feature status: Available demonstration | Transcript fallback\n"
                "Sharing default for this lab: Restricted; learner and named reviewer only",
            ),
            (
                "If Take notes for me is available in a trainer-hosted practice meeting, observe the notice "
                "and sharing controls and export the notes after the demonstration. Otherwise copy the "
                "Meeting notes candidate section from meeting-transcript.txt into Generated or practice "
                "notes. Do not create a real meeting with external people for this lab.",
                "Fallback source: labs/assets/meeting-transcript.txt\n"
                "Generated notes remain a candidate until checked against the transcript.",
            ),
            (
                "Read the full transcript and create tables for Verified decisions and Verified actions. "
                "Actions must have Action, Owner, Due or PENDING, Source lines, Status and Reviewer. Compare "
                "the candidate notes with the transcript and record each wrong owner, wrong date, omitted "
                "qualification or unsupported commitment in the Correction log.",
                "Expected action owners after review: Jamie | Marcus | Noor\n"
                "Expected open question: final facilitator confirmation\n"
                "Do not change a PENDING field without transcript evidence.",
            ),
            (
                "Create a Google Sheet in 02-Working named 07-source-register with columns File, State, "
                "Owner, Purpose, Controlling section or range, Last reviewed, Access and Used by. Add the "
                "approved grounded briefing, communication pack, Slides deck and registration Sheet. Add "
                "07-meeting-notes-review as WORKING until its correction log is complete.",
                "State values: SOURCE | WORKING | APPROVED | ARCHIVE\n"
                "Access values: Restricted | Named collaborators | Link viewer",
            ),
            (
                "Organise C155-Aster-Finch so original supplied sources remain in 01-Source, current "
                "work-in-progress files remain in 02-Working, reviewed course outputs are in 03-Approved "
                "and no obsolete file remains mixed with current work. Do not delete files; move a superseded "
                "copy to 04-Archive and update the register if one exists.",
                "Control check: every registered file has one current state, one owner and one controlling section or range.",
            ),
            (
                "Create a Google Doc in 02-Working named 07-approved-follow-up-brief. In Gemini in Drive, "
                "select only the approved communication pack, Slides deck, registration Sheet and reviewed "
                "meeting notes, then ask for the structure below. If Gemini in Drive is unavailable, open "
                "the registered files and create the same brief manually.",
                "Using only the four selected C155 project sources, create a follow-up brief with Confirmed "
                "event plan, Verified registration insight, Decisions, Actions, Open question and Source "
                "citations. For every section name the exact source filename and section or range. Do not "
                "use files in 04-Archive. Preserve PENDING and distinguish an observed metric from a meeting decision.",
            ),
            (
                "Open every source cited by the follow-up brief and verify the statement. Apply G-E-A-R, "
                "record the final reviewer and change the sharing setting to Restricted or named training "
                "collaborators only. Move the reviewed meeting notes, source register and follow-up brief "
                "to 03-Approved when all checks pass.",
                "Final checks: 3 actions | 1 open question | counts 20 valid and 4 exclusions | chart values 8/8/4 | "
                "all citations open | no Archive source | sharing matches the recorded decision",
            ),
        ],
        test=(
            "The meeting-notes review must show control settings, three verified actions owned by Jamie, "
            "Marcus and Noor, one facilitator open question and a correction log. The source register must "
            "cover five current project artifacts with state, owner, range and access. The follow-up brief "
            "must cite exact filenames, retain 20 valid/4 excluded and 8/8/4 segment counts, use no Archive "
            "source and have a sharing setting that matches the recorded decision."
        ),
        checkpoint=(
            "Keep 07-meeting-notes-review, 07-source-register and 07-approved-follow-up-brief in "
            "03-Approved. Lab 8 uses the three verified actions and source register to define one draft-only automation."
        ),
        troubleshooting=[
            (
                "Take notes for me is unavailable or requires a different plan.",
                "Record Transcript fallback and use meeting-transcript.txt; do not change accounts or move restricted content.",
            ),
            (
                "Gemini in Drive cites a draft or an Archive file.",
                "Clear selected sources, choose only files marked APPROVED in the register and rerun with the explicit state rule.",
            ),
            (
                "An invitee can see the notes attachment but cannot open it.",
                "Remember that event visibility is not file permission; set access according to the recorded sharing decision.",
            ),
        ],
        challenge=(
            "Create a before-and-after table that shows the candidate note, corrected note, evidence line and "
            "possible consequence for each correction. Use it to propose one prompt or meeting practice improvement."
        ),
        reflection=(
            "Which meeting-note error would have caused the largest downstream problem, and where did the workflow stop it?"
        ),
    ),
    dict(
        num=8,
        topic=4,
        title="Automate the Approved Follow-Up from Sheets",
        duration=75,
        objective="LO4: design, implement and verify a bounded Apps Script automation that connects Sheets and Gmail",
        goal="Create and verify one reviewed Gmail draft when Apps Script is available, or complete an evidence-labelled code trace when it is blocked, while keeping sending manual.",
        workflow=["Design CONTROL canvas", "Prepare one row", "Run or trace dry test", "Verify draft or blocked-path evidence"],
        desc=(
            "You will use the approved follow-up evidence to specify a low-risk automation, ask Gemini to "
            "explain or draft the code and compare it with the supplied safe script. When Apps Script is "
            "available, the script first logs an intended action, then creates one Gmail draft to your own "
            "address and refuses to duplicate it. When access is blocked, you trace the same controls and "
            "clearly leave live evidence pending."
        ),
        build=(
            "An Automation tab and CONTROL canvas in 05-registration-analysis plus either (a) a bound Apps "
            "Script project using apps-script-draft.gs, one reviewed Gmail draft to the learner's own account "
            "and a run log, or (b) a four-case code trace with live evidence explicitly pending. Both paths "
            "cover dry-run, live-run, HOLD and duplicate-prevention behaviour."
        ),
        services="Google Sheets - Apps Script - Gmail Drafts - Gemini in Workspace where available",
        prerequisites=[
            "Approved 07-approved-follow-up-brief and three verified actions from Lab 7.",
            "Open labs/assets/apps-script-draft.gs and labs/assets/workflow-control-checklist.md.",
            "Apps Script access may require administrator approval; use the code walk-through fallback if blocked.",
            "Know the learner's own training email address; no other live recipient is permitted.",
        ],
        steps=[
            (
                "In 05-registration-analysis add a tab named CONTROL. Copy the headings Context, Owner, "
                "Needed inputs, Task sequence, Review, Output destination and Learning signal. Define a "
                "manual trigger that reads one READY row, creates a Gmail draft only, writes DRAFTED plus "
                "an ID and timestamp, skips HOLD or processed rows and leaves Send as a human action.",
                "Required limits: manual run | one learner-owned recipient | no auto-send | no delete | no permission change | log every result",
            ),
            (
                "Add an Automation tab with headers Status, Email, Contact_Name, Subject, Body, "
                "Draft_Status, Draft_ID, Drafted_At and Last_Run_Note. In row 2 enter READY, your own "
                "training email, Your Name, [C155 TEST] Aster & Finch partner follow-up and a 100-150 word "
                "body based on one verified Lab 7 action. In row 3 enter HOLD and hold@example.com.",
                "Row 2 recipient must be the learner's own account.\n"
                "Row 3 is a synthetic HOLD row and must never produce a draft.\n"
                "Leave Draft_Status, Draft_ID, Drafted_At and Last_Run_Note blank.",
            ),
            (
                "Ask Gemini in Docs, Sheets or the trainer demonstration to explain how a bound Apps Script "
                "could satisfy the CONTROL canvas. Require a dry-run constant, header-based columns, email "
                "validation, signed-in-user recipient check, a one-eligible-row limit, READY filter, duplicate "
                "prevention, Gmail draft instead of send and an execution log. Compare the response line by "
                "line with apps-script-draft.gs and list any missing control before using the supplied script.",
                "Explain a beginner Google Apps Script for a Sheet named Automation. It must process only "
                "READY rows with blank Draft_Status, stop when more than one row is eligible, require the "
                "recipient to match Session.getEffectiveUser(), validate the email, support DRY_RUN, use "
                "GmailApp.createDraft only when live, write DRAFTED/ID/timestamp, log each outcome, skip HOLD "
                "and skip processed rows. "
                "Do not use GmailApp.sendEmail, delete, share or change file permissions.",
            ),
            (
                "If Apps Script access is available, choose Extensions > Apps Script, replace the editor "
                "content with apps-script-draft.gs, save the project as C155 Follow-Up Draft Lab and confirm "
                "const DRY_RUN = true. Select runFollowUpDrafts and click Run, review permissions before "
                "allowing them, then open the execution log and Automation row 2. If Apps Script is blocked, "
                "do not paste or run code; record Access blocked and proceed to the four-case trace in Step 6.",
                "Available-path dry run: log contains DRY RUN; Last_Run_Note starts DRY RUN OK; Draft_Status, "
                "Draft_ID and Drafted_At remain blank; Gmail has no new C155 TEST draft.\n"
                "Blocked path: Access blocked recorded; no execution or Gmail-draft claim.",
            ),
            (
                "On the available path, change only const DRY_RUN = true to const DRY_RUN = false, save and "
                "run runFollowUpDrafts again. Open Gmail Drafts and inspect the message without sending it. "
                "Verify recipient, subject, body, source facts and absence of unintended Cc/Bcc or attachment. "
                "On the blocked path, skip this execution and keep Draft_Status, Draft_ID and Drafted_At blank.",
                "Available-path live run: exactly one unsent draft with subject [C155 TEST] Aster & Finch "
                "partner follow-up; row 2 Draft_Status = DRAFTED; Draft_ID and Drafted_At are populated.\n"
                "Blocked path: no draft created; all live-result fields remain blank.",
            ),
            (
                "If Apps Script access is available, run runFollowUpDrafts a third time without changing the "
                "Sheet. Confirm that no second draft is created and row 3 remains HOLD with blank draft fields. "
                "Record all three runs in CONTROL with Mode, Input row, Intended action, Observed result, Evidence "
                "and Decision. If Apps Script is blocked, use the supplied script and CONTROL to trace four cases: "
                "dry READY self, live READY self, repeat DRAFTED and HOLD. For each case record the expected code "
                "branch, Sheet writes and Gmail effect; keep live evidence fields blank and do not claim a draft ran.",
                "Available path: 1 DRY_RUN -> no draft | 2 LIVE -> one draft and DRAFTED | 3 LIVE repeat -> no duplicate | HOLD -> no action\n"
                "Blocked path: four traced cases with expected branch, Sheet writes and Gmail effect; live result remains PENDING",
            ),
            (
                "Complete the final G-E-A-R and CONTROL review. Keep the Gmail item as a draft or delete it "
                "manually after documenting the test; do not send it. Record which authorisation scope was "
                "requested, which data fields the script reads, how it stops duplicates and what would need "
                "manager or administrator approval before any workplace pilot.",
                "Final decision values: SAFE COURSE TEST COMPLETE | CODE WALK-THROUGH COMPLETE - LIVE TEST PENDING | HOLD FOR REPAIR\n"
                "Workplace expansion is outside this lab and requires a new owner, data and recipient review.",
            ),
        ],
        test=(
            "CONTROL must define all seven fields and the stated limits; Automation must contain one READY "
            "self-addressed row and one HOLD synthetic row. On the available path, dry run must create no draft, "
            "live run must create exactly one unsent C155 TEST Gmail draft and write DRAFTED, ID and timestamp, "
            "the repeat run must create no duplicate and HOLD must remain untouched. On the blocked path, CONTROL "
            "must trace dry READY self, live READY self, repeat DRAFTED and HOLD with the expected branch, Sheet "
            "writes and Gmail effect; live evidence fields must remain blank and the decision must be CODE "
            "WALK-THROUGH COMPLETE - LIVE TEST PENDING. The relevant run record and final human decision must be complete."
        ),
        checkpoint=(
            "Retain the Sheet, supplied script and either the available-path execution evidence and unsent "
            "test draft or the blocked-path four-case trace with live evidence pending. Do not enable a time "
            "trigger, bulk rows or external recipients in this course."
        ),
        troubleshooting=[
            (
                "Extensions > Apps Script is blocked.",
                "Use the four-case alternative trace in Step 6, leave live evidence blank and record CODE WALK-THROUGH COMPLETE - LIVE TEST PENDING.",
            ),
            (
                "The script says a required header is missing.",
                "Compare the nine Automation headers character for character and remove leading or trailing spaces.",
            ),
            (
                "A second draft appears after the repeat run.",
                "Stop, keep sending disabled and confirm the script skips any row whose Draft_Status is not blank.",
            ),
            (
                "The script reports more than one unprocessed READY row.",
                "Keep DRY_RUN true, change every unintended row to HOLD and continue only when exactly one self-addressed READY row remains.",
            ),
            (
                "The script cannot confirm the signed-in user or rejects the recipient.",
                "Do not bypass the safety stop. Sign in with the intended training account and make row 2 Email exactly match that account; otherwise use the blocked-path trace.",
            ),
        ],
        challenge=(
            "Add an approved Preview column that stores the subject and first 60 body characters during dry "
            "run. Explain why preview evidence is useful and why it still does not authorise sending."
        ),
        reflection=(
            "Which control made the automation observable and reversible, and what new risk would appear if the workflow sent messages automatically?"
        ),
    ),
]
