"""Topic 1 labs for C155."""

DOMAIN1 = [
    dict(
        num=1,
        topic=1,
        title="Confirm Access and Build a Safe Prompt Charter",
        duration=60,
        objective="LO1: explain Gemini access, prompt structure and responsible controls across Google Workspace",
        goal="Verify the available Workspace features and create the source, prompt and review rules that govern every later lab.",
        workflow=["Check access", "Classify inputs", "Write P-T-C-F", "Set review gates"],
        desc=(
            "You will create the C155 project folder, check Gemini and fallback availability across "
            "Workspace, classify the supplied synthetic sources and write a reusable P-T-C-F prompt "
            "charter. The charter keeps sources, uncertainty, sharing and human approval visible."
        ),
        build=(
            "A C155-Aster-Finch Drive folder with four state subfolders, an "
            "01-access-matrix sheet and a 01-prompt-charter document containing approved sources, "
            "prohibited inputs, a reusable prompt pattern and the G-E-A-R review gate."
        ),
        services="Google Drive - Docs - Sheets - Gemini features where available - supplied synthetic source pack",
        prerequisites=[
            "Sign in to a Google account authorised for training and open labs/assets/aster-finch-project-brief.md.",
            "Open labs/assets/facts-and-policies.md and labs/assets/prompt-quality-checklist.md.",
            "Do not use workplace records; the supplied files are entirely synthetic.",
        ],
        steps=[
            (
                "In Google Drive, create a folder named C155-Aster-Finch. Inside it create exactly "
                "01-Source, 02-Working, 03-Approved and 04-Archive. Upload "
                "aster-finch-project-brief.md, facts-and-policies.md and prompt-quality-checklist.md "
                "to 01-Source. Keep sharing set to Restricted.",
                "Expected path:\nC155-Aster-Finch/\n  01-Source/\n  02-Working/\n  03-Approved/\n  04-Archive/",
            ),
            (
                "Create a Google Sheet in 02-Working named 01-access-matrix. Add the headers App, "
                "Account type, Gemini entry point, Status, Safe fallback and Admin issue. Create rows "
                "for Gmail, Docs, Sheets, Slides, Drive, Meet and Apps Script. Open each app in a new "
                "tab and record Available, Trainer demo or Manual fallback; do not guess from a help page.",
                "Status values: Available | Trainer demo | Manual fallback\nSafe fallbacks: supplied source or transcript | normal app feature | trainer demonstration",
            ),
            (
                "In 01-access-matrix add a second tab named Data boundary. Enter Public, Internal, "
                "Confidential and Restricted as four rows. For each row add Allowed training example, "
                "Handling rule and Not allowed. Classify the three supplied files as Synthetic training "
                "data. Explicitly prohibit passwords, access tokens, private customer records and "
                "unapproved confidential content.",
                "Rule: use the minimum approved fields for the stated task; UNKNOWN replaces an unsupported detail.",
            ),
            (
                "Create a Google Doc in 02-Working named 01-prompt-charter. Add headings Purpose, "
                "Approved sources, Prohibited inputs, Persona, Task, Context, Format, Source boundary, "
                "Review criteria, Output destination and Human approver. Fill every heading from the "
                "project brief and facts file. Use PENDING for the approver name if no role has been assigned.",
                "Persona: I am a workplace coordinator preparing a synthetic partner briefing.\n"
                "Task: Create <ARTIFACT> for <AUDIENCE> so they can <DECISION OR ACTION>.\n"
                "Context: Use only <NAMED APPROVED FILES OR EXCERPTS>.\n"
                "Format: Return <STRUCTURE, LENGTH, TONE AND REQUIRED FIELDS>.\n"
                "Source boundary: If a detail is absent, write UNKNOWN and list the question; do not infer it.\n"
                "Review: End with a G-E-A-R table for Grounding, Evidence, Audience and Risk.",
            ),
            (
                "Run the charter prompt in Gemini in Docs or another available in-app Gemini control. "
                "Ask for a five-bullet briefing outline using only the two approved source files. If the "
                "feature is unavailable, use the trainer demonstration response in "
                "labs/assets/sample-gemini-output.md. Paste the result under Initial response.",
                "Create a five-bullet outline for the Aster & Finch Partner Operations Briefing. Use only "
                "the attached or pasted project brief and facts file. Include Purpose, Audience, Confirmed "
                "facts, Open questions and Next action. Write UNKNOWN for unsupported details and end with "
                "a G-E-A-R review table.",
            ),
            (
                "Compare the response with prompt-quality-checklist.md. Under Review record at least one "
                "source check, one audience edit and one risk check. Write a refined prompt that repairs "
                "the largest defect. If Gemini is available, run the refined prompt once and paste the result "
                "under Refined response. If Gemini is unavailable, duplicate the initial fallback, manually "
                "apply the refined instruction, label it Manual refined fallback and record every edit. "
                "Finish with Approver, Decision and Destination; keep Decision as WORKING until a partner checks it.",
                "Iteration record:\nDefect: <OBSERVED PROBLEM>\nChanged instruction: <ONE CHANGE>\nResult: <OBSERVABLE IMPROVEMENT>\nApprover: <ROLE OR PENDING>\nDecision: WORKING\nDestination: 02-Working",
            ),
        ],
        test=(
            "Open the Drive folder and both artifacts. There must be four correctly named state folders; "
            "01-access-matrix must have seven app rows and four data-boundary rows; 01-prompt-charter must "
            "contain all eleven headings, one initial and one generated or manually refined second response, UNKNOWN for unsupported "
            "details, four G-E-A-R checks and a visible WORKING decision."
        ),
        checkpoint=(
            "Keep the approved source files in 01-Source and the two Lab 1 artifacts in 02-Working. "
            "Labs 2-8 must reuse the same source boundary, P-T-C-F structure and G-E-A-R review."
        ),
        troubleshooting=[
            (
                "Ask Gemini or another AI control is missing.",
                "Record the feature as Trainer demo or Manual fallback and use sample-gemini-output.md without moving the source to an unapproved service.",
            ),
            (
                "The response invents a date, venue or speaker.",
                "Replace it with UNKNOWN and add the exact source-boundary instruction before rerunning.",
            ),
            (
                "A source file is visible from the wrong account.",
                "Stop, remove unintended sharing and continue only from the authorised training account.",
            ),
        ],
        challenge=(
            "Rewrite the prompt for a senior leader and for an operations coordinator. Keep the same "
            "facts and compare which Persona, Format and Audience instructions legitimately change."
        ),
        reflection=(
            "Which control in your charter prevents the most consequential failure, and what evidence shows that it was applied?"
        ),
    ),
    dict(
        num=2,
        topic=1,
        title="Produce and Verify a Grounded Workspace Briefing",
        duration=55,
        objective="LO1: use an effective prompt and a human review gate to create a source-grounded workplace briefing",
        goal="Turn the approved synthetic sources into a concise briefing while recording every material fact, question and correction.",
        workflow=["Scope sources", "Generate candidate", "Trace claims", "Approve or hold"],
        desc=(
            "You will apply the Lab 1 charter to create a structured partner-briefing candidate. You "
            "will then build a claim ledger, test the response against the sources and move only the "
            "reviewed version into the approved state."
        ),
        build=(
            "A 02-grounded-briefing Google Doc with seven required sections and a "
            "02-claim-review-ledger Google Sheet that traces every material statement to a source, "
            "marks unsupported details and records the final human decision."
        ),
        services="Google Docs - Google Sheets - Gemini in Docs or supplied fallback - Drive",
        prerequisites=[
            "Completed 01-prompt-charter and 01-access-matrix from Lab 1.",
            "aster-finch-project-brief.md and facts-and-policies.md remain unchanged in 01-Source.",
            "Open labs/assets/prompt-quality-checklist.md for the final review.",
            "Open labs/assets/sample-lab2-grounded-briefing.md for the complete fallback candidate.",
            "Plan a trainer or peer reviewer; if working solo, use the bounded self-review in Step 5.",
        ],
        steps=[
            (
                "Create a Google Doc in 02-Working named 02-grounded-briefing. Add headings Executive "
                "summary, Purpose and audience, Confirmed plan, Participant experience, Open questions, "
                "Next actions and Source note. Under Source note list the exact two source filenames and "
                "their folder state.",
                "Sources:\n01-Source/aster-finch-project-brief.md\n01-Source/facts-and-policies.md",
            ),
            (
                "Use the Lab 1 P-T-C-F charter in Gemini in Docs. Reference or paste only the two approved "
                "sources. Ask for 450-600 words across the required headings, a neutral professional tone, "
                "no invented details and a final table of open questions with Owner and Needed by. If Gemini "
                "is unavailable, copy sample-lab2-grounded-briefing.md as the candidate and perform the same "
                "claim-ledger and G-E-A-R review; do not reuse the short Lab 1 fallback.",
                "Persona: I am the Aster & Finch workplace coordinator writing for invited partner representatives.\n"
                "Task: Draft a 450-600 word operations briefing that enables partners to prepare.\n"
                "Context: Use only the two named source files below. The facts file overrides a conflicting "
                "draft statement. Write UNKNOWN for absent information.\n"
                "Format: Use the seven document headings already present. Finish with an Open question | "
                "Owner | Needed by table.\nReview: Flag every number, date, place, commitment and named owner "
                "for source checking. Do not add a quotation or testimonial.",
            ),
            (
                "Insert the candidate under the document headings. Create a Google Sheet in 02-Working "
                "named 02-claim-review-ledger with columns ID, Claim, Source file, Source excerpt or field, "
                "Status, Required edit and Reviewer. Add one row for every number, date, venue statement, "
                "commitment, audience condition and action owner in the candidate.",
                "Status values: VERIFIED | NEEDS EDIT | UNKNOWN\nA VERIFIED row must name a source file and an exact excerpt or field.",
            ),
            (
                "Check each ledger row against the source files. Change unsupported content in the Doc to "
                "UNKNOWN or an explicit open question. Where the two sources differ, apply the priority rule "
                "in facts-and-policies.md and record the conflict in Required edit. Do not mark a claim "
                "VERIFIED merely because Gemini repeated it.",
                "Minimum checks: event purpose | audience | date | delivery mode | duration | accessibility | "
                "participant data rule | named owner | next action",
            ),
            (
                "Apply the G-E-A-R review to the complete revised Doc. Add a final table with Grounding, "
                "Evidence, Audience and Risk as rows, each with Check, Evidence and Result. Ask a trainer or "
                "peer to read only the briefing and state the event purpose, confirmed details and open questions; "
                "record their answer under Audience check. If working solo, hide the source files, read only "
                "the briefing and write those same three items before comparing them with the sources; label "
                "the evidence Bounded self-review.",
                "Result values: PASS | REPAIR\nAll four rows must be PASS before the document can move to 03-Approved.",
            ),
            (
                "If every material claim is VERIFIED or visibly UNKNOWN and all four G-E-A-R rows pass, "
                "move the final Doc and ledger to 03-Approved. In the Doc add Decision: APPROVED FOR COURSE "
                "WORKFLOW, Reviewer and date. Otherwise leave both in 02-Working and add Decision: HOLD with "
                "the unresolved item.",
                "Final state rule:\nAPPROVED FOR COURSE WORKFLOW -> 03-Approved\nHOLD -> 02-Working",
            ),
        ],
        test=(
            "The briefing must contain all seven headings, 450-600 words, the two exact source paths, an "
            "open-question table and a four-row G-E-A-R table. The ledger must cover at least nine material "
            "claims and contain no VERIFIED row without a source excerpt. The Drive state must match the "
            "recorded APPROVED FOR COURSE WORKFLOW or HOLD decision."
        ),
        checkpoint=(
            "Labs 3 and 4 use the final 02-grounded-briefing and 02-claim-review-ledger as their controlling "
            "content sources. Do not draft from the earlier Gemini response."
        ),
        troubleshooting=[
            (
                "Gemini cannot reference the Markdown files directly.",
                "Open each source, copy only the relevant synthetic text into the prompt and preserve the exact filename in the source boundary.",
            ),
            (
                "The candidate is too long or repeats the same information.",
                "Assign one purpose to each heading and set a word budget before rerunning or editing manually.",
            ),
            (
                "The reviewer cannot find where a claim came from.",
                "Downgrade the row to NEEDS EDIT or UNKNOWN until an exact source excerpt is recorded.",
            ),
        ],
        challenge=(
            "Create a second version capped at 250 words. Compare which details were removed and explain "
            "whether the shorter version still supports the same partner decisions."
        ),
        reflection=(
            "Which sentence required the most human judgement, and why could source grounding alone not finish that decision?"
        ),
    ),
]
