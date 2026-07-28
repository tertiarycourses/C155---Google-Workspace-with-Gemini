"""Single source of truth for Google Workspace with Gemini (C155)."""

TITLE = "Google Workspace with Gemini"
SHORT_TITLE = "Google Workspace with Gemini"
COURSE_CODE = "C155"
COURSE_URL = "https://www.tertiarycourses.com.sg/google-workspace-with-gemini.html"
VERSION = "v1.0"
VERSION_DATE = "28 July 2026"
ORG = "Tertiary Infotech Academy Pte Ltd"
UEN = "UEN: 201200696W"
TRAINER = "Truman Ng"
DAYS = 2
DAY_MINUTES = 480
INSTRUCTIONAL_MINUTES = 450
MODE = "Instructor-led, hands-on practical labs"
DAILY_TIMING = (
    "9:30 am - 6:30 pm (1-hour lunch; two 15-minute tea breaks; "
    "7.5 instructional hours)"
)
DARK_THEME = False

LEARNING_OUTCOMES = [
    "LO1: Explain how Gemini works across Google Workspace, write effective prompts and apply responsible data, privacy and verification controls.",
    "LO2: Draft, rewrite, summarise and refine workplace content in Docs, Slides and Gmail while preserving source accuracy, audience fit and human approval.",
    "LO3: Clean, organise, analyse and visualise spreadsheet data with Gemini in Sheets, formulas and reproducible checks.",
    "LO4: Design an AI-assisted workflow across Meet, Drive, Sheets, Docs and Gmail, then implement and verify a bounded Workspace automation.",
]

LO_TITLES = [
    "Prompt & Protect",
    "Write & Present",
    "Analyse & Visualise",
    "Connect & Automate",
]


def _section(title, definition, why, how, example, use_when, avoid_when, quality):
    return dict(
        title=title,
        definition=definition,
        why=why,
        how=how,
        example=example,
        use_when=use_when,
        avoid_when=avoid_when,
        quality=quality,
    )


TOPICS = [
    dict(
        num=1,
        code="01",
        title="Getting Started with Gemini in Google Workspace",
        subtitle="Generative AI and Gemini - Access across apps - Effective prompting - Responsible, secure and private use",
        weighting="Day 1 morning - 2 labs",
        concepts=[
            ("Generative AI", "A probabilistic system that creates a candidate output from instructions and context; it does not guarantee truth."),
            ("Workspace grounding", "Gemini can use selected Workspace sources and the user's existing permissions to add relevant context."),
            ("P-T-C-F prompt", "Persona, Task, Context and Format make the request, evidence boundary and expected output explicit."),
            ("Human review gate", "A named person verifies facts, privacy, permissions, tone and destination before output is used."),
        ],
        sections=[
            _section(
                "Introduction to Generative AI and Gemini in Workspace",
                "Generative AI predicts and assembles a useful candidate response from patterns in data, instructions and supplied context. Gemini in Google Workspace places this capability inside familiar apps so a user can draft, summarise, organise and analyse without treating the generated output as an authoritative record.",
                "The productivity gain comes from reducing the first-pass effort, not from transferring accountability to the model. A useful mental model is assistant, source and reviewer: Gemini proposes, approved Workspace material grounds the task, and a person decides what is accurate and appropriate.",
                [
                    "Define the workplace task and the decision the output will support.",
                    "Select the minimum approved source material needed for context.",
                    "Ask Gemini for a bounded candidate in a specified format.",
                    "Compare every material statement with the source or an independent record.",
                    "Edit, approve and share through the normal Workspace controls.",
                ],
                [
                    "Aster & Finch is planning a synthetic partner briefing and has an approved project brief.",
                    "Gemini converts the brief into a draft agenda, but labels missing venue and speaker details as open questions.",
                    "The coordinator verifies those fields before the agenda becomes a shared document.",
                ],
                [
                    "A repetitive drafting or synthesis task has approved source material and a human owner.",
                    "The output can be checked before it influences a customer, employee or business decision.",
                ],
                [
                    "The task needs a guaranteed fact but no trustworthy source is available.",
                    "The user intends to send or publish the first response without review.",
                ],
                [
                    ("FAILURE SIGNAL", "The response sounds confident but cannot show where a key statement came from."),
                    ("REPAIR MOVE", "Constrain the prompt to named sources and require UNKNOWN for unsupported details."),
                    ("QUALITY EVIDENCE", "A reviewer can trace each material statement to an approved file or record."),
                ],
            ),
            _section(
                "Setting Up and Accessing Gemini Across Workspace Apps",
                "Gemini features appear according to the user's Google account, eligible plan, administrator settings, language, region and app. Common entry points include an Ask Gemini side panel or an in-context create, refine, summarise or visualise control; exact labels may change as Workspace evolves.",
                "A workflow that assumes every account has the same controls will fail in a real class or organisation. Separating the durable job from a particular button lets users verify availability, protect permissions and use a manual or trainer-provided fallback without losing the learning objective.",
                [
                    "Sign in with the intended account and identify whether it is personal or organisation-managed.",
                    "Check Gmail, Docs, Sheets, Slides, Drive and Meet for the relevant Gemini entry point.",
                    "Confirm that the source files are accessible only to the intended account and collaborators.",
                    "Record unavailable features, language limitations and any administrator restriction.",
                    "Choose a fallback: trainer demonstration, manual app feature or provided sample output.",
                ],
                [
                    "A learner can open Gemini in Docs and Sheets but not Take notes for me in Meet.",
                    "The learner records the gap, uses the supplied meeting transcript and still completes the notes-review workflow.",
                    "No account credentials or protected organisation files are moved to another service.",
                ],
                [
                    "You are validating a repeatable workflow for a known account and Workspace plan.",
                    "A fallback can preserve the same evidence, review and output requirements.",
                ],
                [
                    "A feature is assumed available because it appears in a demonstration or help page.",
                    "The workaround would copy restricted information into an unapproved account or tool.",
                ],
                [
                    ("FAILURE SIGNAL", "The lab stops at a missing sparkle icon or unavailable control."),
                    ("REPAIR MOVE", "Name the job, use the documented fallback and capture the same final artifact."),
                    ("QUALITY EVIDENCE", "The access matrix shows account, app, feature, status and safe fallback."),
                ],
            ),
            _section(
                "Effective Prompting for Everyday Work Tasks",
                "An effective prompt communicates four core elements: Persona, Task, Context and Format. The course adds a Source boundary and Review criteria so the response is useful for work: who Gemini should help, what to do, which facts to use, what the result should look like, and how a person will check it.",
                "Vague prompts hide assumptions and make quality subjective. A structured prompt creates an observable contract, supports iteration and lets another person reproduce the request rather than guessing what the author intended.",
                [
                    "Set the persona and intended audience only when they improve tone or domain framing.",
                    "Use a precise action verb and define the finished artifact or decision.",
                    "Provide approved context and state which sources take priority.",
                    "Specify length, structure, tone and fields that must remain UNKNOWN when absent.",
                    "Review the first response, name the defect and change one instruction at a time.",
                ],
                [
                    "Persona: workplace coordinator writing for external partners.",
                    "Task and context: draft a concise invitation using only the Aster & Finch project brief.",
                    "Format and review: subject plus 150-word email; flag unsupported details and list a final fact check.",
                ],
                [
                    "The task, audience, sources and desired structure can be stated clearly.",
                    "Several iterations can be compared against the same quality criteria.",
                ],
                [
                    "The prompt asks Gemini to invent missing evidence or imitate a real person's private style.",
                    "The user keeps adding conflicting instructions without resolving priorities.",
                ],
                [
                    ("FAILURE SIGNAL", "The output is generic, long or filled with invented specifics."),
                    ("REPAIR MOVE", "Add the missing P-T-C-F element, a source boundary and observable constraints."),
                    ("QUALITY EVIDENCE", "The final response satisfies a checklist another learner can apply consistently."),
                ],
            ),
            _section(
                "Responsible, Secure and Private Use of AI at Work",
                "Responsible use combines data classification, least-privilege access, appropriate sharing, source verification, disclosure where needed and a human decision owner. Workspace protections matter, but they do not replace an organisation's policies or the user's duty to choose suitable inputs and recipients.",
                "Gemini can accelerate a mistake as easily as a good workflow. A privacy-safe prompt can still produce an inaccurate claim, and an accurate draft can still be overshared; controls must therefore cover the full path from source selection to final destination.",
                [
                    "Classify the intended input as public, internal, confidential or restricted under local policy.",
                    "Minimise the content and remove unnecessary personal or sensitive fields.",
                    "Check source-file access and the destination's sharing permissions.",
                    "Verify facts, calculations, tone, bias, rights and any required disclosure.",
                    "Record the reviewer, decision and final approved version.",
                ],
                [
                    "The synthetic registration sheet contains names and contact fields that the analysis does not need.",
                    "The learner works from a minimised training copy, reports only grouped counts and shares results with named collaborators.",
                    "A control log records sources, checks, approver and destination.",
                ],
                [
                    "The organisation permits the data and task, and a defined reviewer can inspect the result.",
                    "The output remains inside an approved access and sharing boundary.",
                ],
                [
                    "The prompt includes passwords, secrets, protected personal records or information outside the user's authority.",
                    "The workflow hides uncertainty or makes a high-impact decision without qualified human review.",
                ],
                [
                    ("FAILURE SIGNAL", "The draft is accurate but visible to people who do not need it."),
                    ("REPAIR MOVE", "Apply least privilege, remove unnecessary data and check the destination before sharing."),
                    ("QUALITY EVIDENCE", "The control log proves input authority, source checks, reviewer and recipient scope."),
                ],
            ),
        ],
    ),
    dict(
        num=2,
        code="02",
        title="Gemini in Docs, Slides and Gmail",
        subtitle="Drafting, rewriting and summarising - Slides and images - Gmail threads and replies - Reviewing generated content",
        weighting="Day 1 afternoon - 2 labs",
        concepts=[
            ("Source-led draft", "A first version whose facts and constraints come from named approved material."),
            ("Message architecture", "Audience need, core message, supporting evidence and next action shape documents, slides and email."),
            ("Visual brief", "Purpose, subject, composition, aspect ratio, style and exclusions guide image generation."),
            ("Review ledger", "Claim, source, status, edit and approver make human refinement visible."),
        ],
        sections=[
            _section(
                "Drafting, Rewriting and Summarising in Docs",
                "Gemini in Docs can create a starting draft, transform selected text and summarise information from a document or referenced Workspace sources. Drafting creates new structure, rewriting changes an existing passage, and summarising compresses meaning; each operation requires a different instruction and review test.",
                "Treating the three operations as interchangeable produces vague or distorted content. Naming the operation, audience and source boundary preserves intent and makes it easier to compare the generated passage with the evidence.",
                [
                    "Choose create, rewrite or summarise according to the actual communication need.",
                    "Reference the approved file or paste a bounded source excerpt.",
                    "Specify audience, purpose, tone, length and required headings.",
                    "Insert only the useful candidate text into the working document.",
                    "Compare facts and meaning with the source, then edit in the document.",
                ],
                [
                    "The coordinator asks for a one-page partner briefing using the project brief and facts file.",
                    "Gemini produces Objectives, Audience, Agenda, Logistics and Open Questions.",
                    "The coordinator rejects an invented capacity figure and keeps the verified structure.",
                ],
                [
                    "The source is known and the output is a draft that will be edited.",
                    "A rewrite can be judged for meaning, tone and audience accessibility.",
                ],
                [
                    "A summary would remove contractual nuance or a required qualification.",
                    "The prompt gives only a title and expects correct organisation-specific facts.",
                ],
                [
                    ("FAILURE SIGNAL", "A polished paragraph changes or omits a material source condition."),
                    ("REPAIR MOVE", "Quote the controlling source, require open questions and compare sentence by sentence."),
                    ("QUALITY EVIDENCE", "The document's claim ledger shows the source and final edit for every material fact."),
                ],
            ),
            _section(
                "Generating Slides, Layouts and Images in Slides",
                "A useful presentation turns a decision or story into a sequence of claims, evidence and actions. Gemini can help create slide candidates, rewrite text and generate images, but the presenter still controls narrative, factual support, accessibility, brand fit and whether a generated visual represents reality appropriately.",
                "A collection of attractive slides is not automatically a coherent presentation. Starting from audience and message architecture prevents decorative output from replacing the business purpose, while a visual brief reduces generic or misleading imagery.",
                [
                    "Define the audience question and one-sentence presentation promise.",
                    "Create a slide outline with one message and evidence need per slide.",
                    "Generate or refine only the slide text that has approved support.",
                    "Write a visual brief with subject, composition, aspect ratio, style and exclusions.",
                    "Review the full sequence for evidence, hierarchy, accessibility and next action.",
                ],
                [
                    "The partner briefing uses six slides: purpose, audience need, agenda, participation data, action plan and next steps.",
                    "A wide abstract collaboration image supports the title without depicting a real attendee or unsupported venue.",
                    "All figures point to the registration sheet and all open details remain visibly pending.",
                ],
                [
                    "The deck has a defined audience, message and evidence source.",
                    "Generated imagery is illustrative, appropriate and reviewed before use.",
                ],
                [
                    "The image could be mistaken for documentary proof of a real person, place or event.",
                    "Slide generation is used to hide missing analysis or compress unreadable amounts of text.",
                ],
                [
                    ("FAILURE SIGNAL", "Each slide looks acceptable alone but the sequence has no decision path."),
                    ("REPAIR MOVE", "Restate the audience question and give every slide one message and one role."),
                    ("QUALITY EVIDENCE", "A slide map links message, evidence, visual purpose and audience action."),
                ],
            ),
            _section(
                "Writing, Replying and Summarising Emails in Gmail",
                "Gemini in Gmail can summarise a thread, draft a new message, suggest a reply and retrieve relevant information from permitted Workspace sources. The output must still respect thread history, recipient scope, commitments, tone and the difference between a suggested action and an approved promise.",
                "Email is an external action surface: a small invented date, price or commitment can create real consequences. A safe workflow separates understanding the thread, deciding the response and drafting the message, then requires a final recipient and attachment check.",
                [
                    "Summarise the thread into facts, requests, decisions, owners and unresolved questions.",
                    "Verify the summary against the original messages and named files.",
                    "Decide what the organisation can commit to before asking for a reply.",
                    "Draft with a clear subject, context, response, owner, date and next action.",
                    "Check To, Cc, attachments, links and every commitment before sending.",
                ],
                [
                    "A synthetic partner thread asks about capacity, accessibility and the final agenda.",
                    "Gemini separates confirmed facts from open questions and drafts a holding reply.",
                    "The coordinator removes an unapproved promise and saves the message as a draft for review.",
                ],
                [
                    "The thread is bounded and the sender has authority to prepare a response.",
                    "The final message can remain a draft until facts and recipients are checked.",
                ],
                [
                    "The response would commit money, legal terms or sensitive information without an owner.",
                    "The thread includes recipients or content the user is not authorised to expose to another tool or group.",
                ],
                [
                    ("FAILURE SIGNAL", "The draft promises a date or deliverable not agreed in the thread."),
                    ("REPAIR MOVE", "Convert unverified commitments to questions and name the decision owner."),
                    ("QUALITY EVIDENCE", "The saved draft matches the verified thread summary and has a completed send checklist."),
                ],
            ),
            _section(
                "Reviewing and Refining AI-Generated Content",
                "Review is a structured comparison between the output, the source, the intended audience and the use context. The G-E-A-R loop used in this course checks Grounding, Evidence, Audience and Risk before a human approves, edits or rejects the candidate.",
                "Fluency makes generated content feel finished earlier than it is. An explicit loop catches factual drift, missing qualifications, inappropriate tone, inaccessible design, privacy exposure and unsupported actions across Docs, Slides and Gmail.",
                [
                    "Grounding: identify the sources and the exact task the response should satisfy.",
                    "Evidence: verify claims, numbers, names, dates, links and calculations.",
                    "Audience: test clarity, tone, structure, accessibility and next action.",
                    "Risk: inspect privacy, permissions, bias, rights, commitments and destination.",
                    "Record the change and approver, then review the final assembled artifact again.",
                ],
                [
                    "The deck states that 48 partners confirmed attendance, while the sheet contains 46 valid confirmations.",
                    "The reviewer records the mismatch, corrects the slide and adds the sheet range to the source note.",
                    "A second pass confirms the email and document use the same verified count.",
                ],
                [
                    "The output will inform another person or become an organisation record.",
                    "A reviewer can access both source and final artifact.",
                ],
                [
                    "The review is reduced to spelling and visual polish only.",
                    "The final combined document is never checked after individually approved parts are merged.",
                ],
                [
                    ("FAILURE SIGNAL", "Different Workspace artifacts contain different versions of the same fact."),
                    ("REPAIR MOVE", "Choose one controlling source, correct every consumer and re-run the final review."),
                    ("QUALITY EVIDENCE", "A cross-artifact ledger shows one verified value and every place it appears."),
                ],
            ),
        ],
    ),
    dict(
        num=3,
        code="03",
        title="Gemini in Sheets and Data Analysis",
        subtitle="Formulas and tables - Analysis and summaries - Charts and visualisations - Cleaning and organising data",
        weighting="Day 2 morning - 2 labs",
        concepts=[
            ("Data grain", "What one row represents; every formula, summary and chart must respect that level."),
            ("Reproducible transformation", "A visible formula, rule or step that another person can rerun and inspect."),
            ("Analysis question", "A precise metric, population, dimension and time scope that makes a result interpretable."),
            ("Chart contract", "Title, axes, units, series and source must faithfully encode the stated comparison."),
        ],
        sections=[
            _section(
                "Generating Formulas, Tables and Insights in Sheets",
                "Gemini in Sheets can help create tables, formulas and actions such as filters, formatting, pivots and dropdowns. The result is useful only when the data grain, field meaning, formula references and expected output are explicit and the inserted change is tested on known rows.",
                "A syntactically valid formula can still answer the wrong question. Starting with a plain-language calculation and sample expected result makes it possible to review a suggestion instead of accepting it because the cell displays a number.",
                [
                    "State what one row represents and define each input column.",
                    "Write the intended calculation in plain language with units and exclusions.",
                    "Ask for a formula or table using exact sheet and column references.",
                    "Inspect relative and absolute references before filling the formula.",
                    "Test normal, blank, duplicate and boundary rows against manual expectations.",
                ],
                [
                    "Each row is one synthetic partner registration; Seats is the requested quantity.",
                    "A clean formula standardises status and flags Confirmed rows with missing dietary information.",
                    "The learner tests one confirmed, one waitlisted and one blank row before filling down.",
                ],
                [
                    "The data fields and expected result can be described precisely.",
                    "The proposed formula remains visible and can be tested on sample rows.",
                ],
                [
                    "The sheet mixes several row types or merged headers without a defined grain.",
                    "A generated formula is filled across the dataset before its references are reviewed.",
                ],
                [
                    ("FAILURE SIGNAL", "The formula returns values but changes meaning when copied down."),
                    ("REPAIR MOVE", "Review row grain and lock only the references that should remain fixed."),
                    ("QUALITY EVIDENCE", "A test table shows input, expected result, actual result and status."),
                ],
            ),
            _section(
                "Analysing and Summarising Data with Gemini",
                "Data analysis turns a stated question into defined metrics, comparisons and evidence. Gemini can propose pivots, calculations and narrative insights, but the analyst must define the population, denominator, filters, time scope and uncertainty before interpreting a pattern.",
                "Narrative summaries often sound causal even when the sheet only shows association. Keeping metric definitions and calculation evidence beside the insight prevents plausible wording from outrunning the data.",
                [
                    "Write the decision question and define the valid population.",
                    "Specify each metric, denominator, grouping and material exclusion.",
                    "Create a pivot or formula output that exposes the calculation.",
                    "Ask Gemini for observations grounded only in the visible result.",
                    "Label facts, hypotheses and recommended follow-up separately.",
                ],
                [
                    "Question: which partner segment needs the most follow-up before the briefing?",
                    "Metrics: valid registrations, confirmation rate and missing-information count by segment.",
                    "The summary states the observed gap and proposes a follow-up check without claiming why it occurred.",
                ],
                [
                    "The dataset is clean enough for the defined question and calculations are visible.",
                    "The narrative distinguishes observed evidence from a possible explanation.",
                ],
                [
                    "The prompt asks for insights before defining valid rows or metrics.",
                    "A small synthetic sample is used to claim a universal business trend.",
                ],
                [
                    ("FAILURE SIGNAL", "The insight has no metric definition or supporting range."),
                    ("REPAIR MOVE", "Add population, formula, grouping, time scope and source range."),
                    ("QUALITY EVIDENCE", "Another learner reproduces the value from the same clean table."),
                ],
            ),
            _section(
                "Creating Charts and Visualisations",
                "A chart encodes a comparison through position, length, colour or shape. Gemini can propose and create visualisations in Sheets, but the user must choose a chart type that matches the question, display units and categories clearly, and verify every plotted value against the source table.",
                "Visuals compress data and therefore amplify both clarity and error. A neutral descriptive title, readable labels and an honest axis help viewers understand what is plotted without implying a conclusion the data cannot support.",
                [
                    "Name the comparison: trend, ranking, composition, distribution or relationship.",
                    "Choose the smallest chart type that visibly encodes that comparison.",
                    "Use a clean source range at one consistent grain.",
                    "Set title, axis labels, units, legend and category order.",
                    "Compare plotted points with the table and add a concise evidence-based takeaway.",
                ],
                [
                    "A horizontal bar chart ranks valid registrations by partner segment.",
                    "The title states 'Valid registrations by partner segment'; the x-axis shows registrations.",
                    "The learner checks each bar against the pivot and avoids a truncated scale that exaggerates differences.",
                ],
                [
                    "A visual makes three or more values or a pattern easier to compare.",
                    "The source table and metric definition can remain available to the reader.",
                ],
                [
                    "A single number would be clearer as text or a compact table.",
                    "A decorative 3D or dual-axis treatment could distort the comparison.",
                ],
                [
                    ("FAILURE SIGNAL", "The title claims a cause or trend that the chart does not encode."),
                    ("REPAIR MOVE", "Use a neutral title and put the bounded observation in a separate note."),
                    ("QUALITY EVIDENCE", "Title, axes, marks and source table all describe the same metric and grain."),
                ],
            ),
            _section(
                "Cleaning and Organising Data with AI",
                "Data cleaning makes values consistent without hiding the original evidence. Typical operations include trimming spaces, standardising categories, parsing dates, handling blanks, identifying duplicates and validating allowed values; every change needs a rule and a retained raw source.",
                "Analysis quality is limited by the inputs. Asking Gemini to 'clean this' without rules can silently merge distinct values or fill unknowns, so a safe workflow profiles first, proposes rules, transforms a copy and reconciles row counts.",
                [
                    "Duplicate the raw tab and record the original row count and key fields.",
                    "Profile blanks, category variants, date formats, duplicates and invalid values.",
                    "Write a rule table with before, after, reason and treatment of uncertainty.",
                    "Apply formulas or bounded actions to a clean tab while preserving raw values.",
                    "Reconcile row counts, totals and exception counts before analysis.",
                ],
                [
                    "The raw Segment field contains SME, sme and Small business.",
                    "The rule maps approved variants to SME but leaves an unfamiliar value as REVIEW.",
                    "A reconciliation confirms that no valid registration disappeared during deduplication.",
                ],
                [
                    "The organisation can define acceptable values and retain the raw source.",
                    "Exceptions can be reviewed instead of guessed.",
                ],
                [
                    "Missing values are silently invented or duplicate rules are not documented.",
                    "The only copy of the source is overwritten before totals are reconciled.",
                ],
                [
                    ("FAILURE SIGNAL", "The clean table has fewer rows and no explanation for the difference."),
                    ("REPAIR MOVE", "Restore the raw copy, log every excluded or merged row and reconcile totals."),
                    ("QUALITY EVIDENCE", "The rule table, exception list and reconciliation explain every change."),
                ],
            ),
        ],
    ),
    dict(
        num=4,
        code="04",
        title="AI-Powered Workflows and Automation in Workspace",
        subtitle="Meet notes - Drive search and organisation - Connecting apps and simple automations - Practical workflow design",
        weighting="Day 2 afternoon - 2 labs",
        concepts=[
            ("Workflow state", "Input, owner, action, output and approval status make work visible across apps."),
            ("Permission-aware retrieval", "Gemini can only be useful and safe when sources and recipients match authorised access."),
            ("Bounded automation", "A trigger performs a narrow action with explicit fields, logs and stop conditions."),
            ("Observe before scaling", "Run, inspect evidence, handle exceptions and expand only after a controlled test."),
        ],
        sections=[
            _section(
                "AI-Assisted Meetings and Notes in Google Meet",
                "Eligible Google Workspace accounts can use Gemini-supported meeting features to capture notes, summarise discussion and identify next steps. The notes are a generated record that must be announced, shared deliberately and reviewed against the conversation before becoming an official source.",
                "Meeting summaries can save transcription and follow-up time, but they may omit context, misattribute an action or expose notes to the wrong invitees. Consent, host control, language support, sharing settings and post-meeting review are part of the workflow rather than optional administration.",
                [
                    "Confirm feature availability, meeting purpose, permitted content and participant notice.",
                    "Choose who should receive the notes and apply the minimum sharing scope.",
                    "Capture or use the provided synthetic transcript when the feature is unavailable.",
                    "Review decisions, owners, dates, unresolved points and wording against the conversation.",
                    "Publish an approved recap and retain exceptions or corrections visibly.",
                ],
                [
                    "The partner-briefing rehearsal has a synthetic ten-minute transcript and three proposed actions.",
                    "The coordinator corrects one owner, changes an uncertain date to pending and restricts the notes to the internal team.",
                    "Only the approved action table is copied to the shared follow-up document.",
                ],
                [
                    "Participants are informed and the organisation permits the meeting feature.",
                    "A host or owner will review the generated notes before wider sharing.",
                ],
                [
                    "The conversation contains restricted material outside the approved note-taking purpose.",
                    "Invite visibility is mistaken for permission to access the generated notes document.",
                ],
                [
                    ("FAILURE SIGNAL", "A generated action item has the wrong owner or an invented deadline."),
                    ("REPAIR MOVE", "Check the relevant transcript segment and mark unresolved fields as pending."),
                    ("QUALITY EVIDENCE", "The review log records original text, correction, source and approver."),
                ],
            ),
            _section(
                "Organising and Searching Drive with Gemini",
                "Gemini in Drive can summarise files or folders, answer questions across permitted sources and help locate or organise material. Retrieval is permission-aware but still depends on clear folder scope, current file versions, meaningful names and a user who verifies the cited sources.",
                "Search becomes unreliable when a folder mixes drafts, duplicates and unclear ownership. A simple information architecture and source register let Gemini retrieve relevant evidence without treating an obsolete file as the controlling record.",
                [
                    "Define the project folder, owner, audience and naming convention.",
                    "Separate source, working, approved and archive states.",
                    "Select the smallest relevant files or folder as Gemini context.",
                    "Ask for an answer with source filenames, open questions and no unsupported inference.",
                    "Open the cited files, verify the response and store the approved output in its correct state.",
                ],
                [
                    "The C155 project folder contains 01-Source, 02-Working, 03-Approved and 04-Archive.",
                    "Gemini summarises only the approved brief and reviewed registration insight, citing both filenames.",
                    "An older agenda remains in Archive and is not used as the final event source.",
                ],
                [
                    "The folder has clear ownership, versions and access controls.",
                    "The response can show which files supplied the relevant information.",
                ],
                [
                    "A broad Drive query could mix personal, obsolete or unrelated content.",
                    "The user assumes retrieval proves the answer is complete or current.",
                ],
                [
                    ("FAILURE SIGNAL", "The answer cites a draft that should no longer govern the project."),
                    ("REPAIR MOVE", "Clarify file states, narrow the source scope and identify the controlling record."),
                    ("QUALITY EVIDENCE", "Every answer links to an accessible current source in the project register."),
                ],
            ),
            _section(
                "Connecting Apps and Building Simple Automations",
                "Google Apps Script is a cloud-based JavaScript platform for extending and automating Workspace. A simple automation reads defined fields, applies a narrow rule and creates an observable action such as a Gmail draft or status update; it should include a dry-run mode, log and explicit authorisation.",
                "Automation removes repeated clicks but also repeats defects at speed. Restricting the trigger, recipient, data fields and action surface makes a beginner workflow easier to understand, test, stop and review before it affects other people.",
                [
                    "Draw the event, input, rule, action, owner and failure path before writing code.",
                    "Use Gemini to explain or draft a small script against an explicit specification.",
                    "Inspect permissions and keep live sending disabled during the first run.",
                    "Test one synthetic row and compare the draft, sheet update and execution log.",
                    "Handle blanks, duplicates and errors before considering a wider trigger.",
                ],
                [
                    "A bound Sheets script reads one READY row and creates a Gmail draft to the learner's own address.",
                    "Dry-run mode records the intended recipient and subject without creating the draft.",
                    "A live test creates one draft, writes DRAFTED and stores a timestamp so the row is not processed twice.",
                ],
                [
                    "The process is repetitive, rule-based, low-risk and has an observable success condition.",
                    "The user can review scopes, logs and every action before expanding the run.",
                ],
                [
                    "The automation would bulk-send, delete, change access or process confidential data as a first test.",
                    "The workflow lacks an owner, idempotency rule or way to stop and inspect failures.",
                ],
                [
                    ("FAILURE SIGNAL", "Running the script twice creates duplicate external actions."),
                    ("REPAIR MOVE", "Add a processed status or unique key and skip rows already handled."),
                    ("QUALITY EVIDENCE", "The test log shows one input row, one intended action and one final status."),
                ],
            ),
            _section(
                "Designing Practical AI Productivity Workflows",
                "A practical workflow links a business trigger to approved sources, human and AI steps, outputs, controls and evidence. The C-O-N-T-R-O-L canvas used here captures Context, Owner, Needed inputs, Task sequence, Review, Output destination and Learning signal.",
                "Tool-first automation often optimises an unclear process. Designing the state changes and review gates first reveals where Gemini adds value, where a person must decide, and which evidence proves the workflow is safe and useful.",
                [
                    "Context: define the trigger, audience, desired outcome and boundary.",
                    "Owner and inputs: name authority, sources, permissions and required fields.",
                    "Task sequence: separate generation, deterministic operations and human decisions.",
                    "Review and output: set gates, destination, sharing scope and exception path.",
                    "Learning signal: measure time, correction rate, completion and recurring failure.",
                ],
                [
                    "A READY registration row triggers a proposed follow-up, not an automatic external send.",
                    "Gemini helps draft the message; Apps Script creates a Gmail draft; the coordinator reviews and sends manually.",
                    "The log records draft creation, corrections and whether the workflow saved time without increasing errors.",
                ],
                [
                    "The process has a stable trigger, bounded inputs and a human owner.",
                    "Success, correction and exception evidence can be collected.",
                ],
                [
                    "The process is still ambiguous or relies on unrecorded personal judgement.",
                    "Productivity is measured only by output volume rather than quality and risk.",
                ],
                [
                    ("FAILURE SIGNAL", "The workflow is fast but no one can explain who approved the result."),
                    ("REPAIR MOVE", "Add a named gate, status field and evidence artifact before the output leaves Draft."),
                    ("QUALITY EVIDENCE", "The canvas and run log link trigger, sources, actions, reviewer, output and learning."),
                ],
            ),
        ],
    ),
]

DAY_THEMES = {
    1: "Prompt safely, then create and refine a partner communication pack",
    2: "Turn clean data and meeting evidence into a controlled cross-app workflow",
}


def SCHEDULE(lab_titles):
    return {
        1: (DAY_THEMES[1], [
            ("9:30", "9:50", 20, "admin", "Welcome, course orientation, access check and learning agreement"),
            ("9:50", "10:50", 60, "topic", "Topic 1 - " + TOPICS[0]["title"] + " (concepts and demonstration)"),
            ("10:50", "11:05", 15, "break", "Tea break"),
            ("11:05", "12:05", 60, "lab", "Hands-on: " + lab_titles([1])),
            ("12:05", "13:00", 55, "lab", "Hands-on: " + lab_titles([2])),
            ("13:00", "14:00", 60, "lunch", "Lunch break"),
            ("14:00", "14:55", 55, "topic", "Topic 2 - " + TOPICS[1]["title"] + " (concepts and demonstration)"),
            ("14:55", "15:10", 15, "break", "Tea break"),
            ("15:10", "16:25", 75, "lab", "Hands-on: " + lab_titles([3])),
            ("16:25", "17:35", 70, "lab", "Hands-on: " + lab_titles([4])),
            ("17:35", "18:20", 45, "topic", "Cross-app review clinic - apply the G-E-A-R loop to Docs, Slides and Gmail"),
            ("18:20", "18:30", 10, "recap", "Day 1 recap, artifact checkpoint and questions"),
        ]),
        2: (DAY_THEMES[2], [
            ("9:30", "9:45", 15, "recap", "Day 1 retrieval practice and Day 2 data boundary check"),
            ("9:45", "10:45", 60, "topic", "Topic 3 - " + TOPICS[2]["title"] + " (concepts and demonstration)"),
            ("10:45", "11:00", 15, "break", "Tea break"),
            ("11:00", "12:15", 75, "lab", "Hands-on: " + lab_titles([5])),
            ("12:15", "13:00", 45, "lab", "Hands-on: " + lab_titles([6])),
            ("13:00", "14:00", 60, "lunch", "Lunch break"),
            ("14:00", "15:00", 60, "topic", "Topic 4 - " + TOPICS[3]["title"] + " (concepts and demonstration)"),
            ("15:00", "15:15", 15, "break", "Tea break"),
            ("15:15", "16:25", 70, "lab", "Hands-on: " + lab_titles([7])),
            ("16:25", "17:40", 75, "lab", "Hands-on: " + lab_titles([8])),
            ("17:40", "18:15", 35, "topic", "Workflow clinic - CONTROL canvas, exception handling and adoption plan"),
            ("18:15", "18:30", 15, "recap", "Course recap, next steps and Q&A"),
        ]),
    }


COURSE_OVERVIEW = dict(
    section_title="Work Smarter Without Giving Up Control",
    concepts_title="Four Ideas That Govern the Course",
    concepts=[
        ("Candidate, not conclusion", "Gemini creates a first pass; a human still verifies and decides."),
        ("Permission-aware context", "Use the minimum approved Workspace sources and keep sharing deliberate."),
        ("Visible evidence", "Sources, formulas, logs and review notes make work reproducible."),
        ("Bounded action", "Draft, test and observe before any workflow scales or reaches others."),
    ],
    framework_title="The P-T-C-F + G-E-A-R Pattern",
    framework=[
        ("PERSONA + TASK", "Who needs help and what finished action or artifact is required?"),
        ("CONTEXT + FORMAT", "Which approved sources, constraints and output structure govern the response?"),
        ("GROUNDING + EVIDENCE", "Can every material claim, number and action be traced and reproduced?"),
        ("AUDIENCE + RISK", "Is the result clear, permitted, appropriately shared and ready for human approval?"),
    ],
    statement=dict(
        headline="AI speed is useful only when the evidence and decision owner stay visible.",
        body="Across every Workspace app, the durable workflow is select approved context, generate a bounded candidate, verify it, and act through normal controls.",
        kicker="COURSE PRINCIPLE",
    ),
    pillars_title="What You Will Build",
    pillars=[
        ("Communication pack", ["Prompt charter and verified briefing", "Docs, Gmail and Slides artifacts"]),
        ("Data decision pack", ["Clean registration tracker", "Metrics, pivot and chart"]),
        ("Workflow pack", ["Reviewed meeting recap", "Drive structure and controlled automation"]),
    ],
    arc_title="How Every Lab Progresses",
    arc=[
        "Start from the previous checkpoint and the same synthetic Aster & Finch partner-briefing scenario.",
        "Use a structured prompt or deterministic rule against named approved sources.",
        "Create an observable artifact inside Workspace or a supplied fallback.",
        "Run a Test It check, record exceptions and save the checkpoint for the next lab.",
    ],
    deep_dives=[
        dict(
            title="Human Checks Across the Workspace Flow",
            kicker="CONTROL MAP",
            items=[
                ("INPUT", "Authority, data class, minimum fields, file permissions and source version."),
                ("GENERATION", "Prompt contract, source boundary, uncertainty and unsuitable-content check."),
                ("TRANSFORMATION", "Formula logic, row grain, duplicates, ranges and reproducible rules."),
                ("OUTPUT", "Fact review, recipients, sharing, accessibility, approvals and audit evidence."),
            ],
        ),
    ],
)

LAB_SHOTS = {}

LG_INTRO = (
    "This Learner Guide is the self-contained study text for Google Workspace with Gemini "
    "(C155). It explains the concepts behind prompting, grounded drafting, spreadsheet "
    "analysis, meeting notes, Drive retrieval and bounded automation before giving the "
    "aligned steps for eight connected hands-on labs."
)
LG_INTRO2 = (
    "The course uses a fictional Aster & Finch partner briefing and synthetic data. Work "
    "through the labs in order because each checkpoint supplies the approved inputs for the "
    "next activity. Gemini labels and availability can vary by account, plan, language, "
    "administrator setting and product release; use the documented fallback while preserving "
    "the same source, review and output requirements."
)

LG_SETUP = dict(
    needs=[
        "A Windows or Mac laptop with a current Chrome, Edge, Firefox or Safari browser and reliable internet access.",
        "A Google account authorised for training; an eligible Workspace plan is preferred for in-app Gemini features.",
        "Access to Gmail, Drive, Docs, Sheets, Slides and Meet. Google Apps Script access may require administrator approval.",
        "The supplied synthetic files in labs/assets/. Do not substitute workplace records during the class.",
        "A plain-text editor for the prompt charter, review ledger and workflow control log.",
    ],
    verify_text=(
        "Open Drive, create a temporary Doc and Sheet, and check whether Ask Gemini or the "
        "relevant AI control appears. Record each app as Available, Trainer demo or Manual "
        "fallback. Confirm that Extensions > Apps Script opens from the practice Sheet."
    ),
    verify_code=(
        "Access matrix columns:\n"
        "App | Account used | Gemini feature | Status | Safe fallback | Admin issue\n"
        "Gmail | Docs | Sheets | Slides | Drive | Meet | Apps Script"
    ),
    conventions=[
        "P-T-C-F means Persona, Task, Context and Format; every material prompt also names its sources and review criteria.",
        "UNKNOWN or PENDING is safer than inventing a missing date, person, metric or commitment.",
        "A generated output remains a candidate until the G-E-A-R review records Grounding, Evidence, Audience and Risk.",
        "Keep 01-Source, 02-Working, 03-Approved and 04-Archive folders separate throughout the connected scenario.",
        "Run automation first in DRY_RUN mode and to your own address; never bulk-send during the lab.",
    ],
)

LAB_NOTE = (
    "Use only the supplied synthetic scenario and an account you are authorised to use. "
    "Do not paste passwords, secrets, protected personal data or confidential workplace "
    "content into a prompt. Keep live sending disabled until the lab explicitly calls for "
    "one reviewed draft to your own account."
)

LG_WRAPUP = dict(
    title="Wrap-Up - From Helpful Feature to Reliable Workflow",
    intro=(
        "The course artifacts form one traceable chain: approved sources and a prompt "
        "charter feed the communication pack; the clean Sheet feeds the data story; the "
        "reviewed meeting recap and Drive register feed one bounded follow-up automation."
    ),
    sections=[
        dict(
            title="A reusable operating pattern",
            bullets=[
                "Define the task, decision owner, approved sources and destination before opening Gemini.",
                "Generate a bounded candidate with P-T-C-F, source limits and explicit review criteria.",
                "Keep calculations, transformations and file states visible and reproducible.",
                "Apply G-E-A-R to the final assembled artifact, not only to individual fragments.",
                "Automate one low-risk action in dry-run mode, inspect evidence and expand only with approval.",
            ],
        ),
        dict(
            title="Authoritative references used",
            bullets=[
                "Course outline: https://www.tertiarycourses.com.sg/google-workspace-with-gemini.html",
                "Google Workspace prompting guidance: https://workspace.google.com/resources/ai/writing-effective-prompts/",
                "Gemini in Docs: https://support.google.com/docs/answer/14206696",
                "Gemini in Sheets: https://support.google.com/docs/answer/14356410",
                "Gemini in Gmail: https://support.google.com/mail/answer/14355636",
                "Gemini in Drive: https://support.google.com/drive/answer/14217860",
                "Gemini in Meet notes: https://support.google.com/meet/answer/14754931",
                "Workspace data protection: https://support.google.com/mail/answer/14615114",
                "Apps Script overview: https://developers.google.com/apps-script",
                "Apps Script automation quickstart: https://developers.google.com/apps-script/quickstart/automation",
            ],
        ),
        dict(
            title="Feature availability reminder",
            bullets=[
                "Google Workspace features, labels and plan eligibility change over time.",
                "Check the current Google help page and your administrator settings before deployment.",
                "A trainer demo or supplied fallback preserves the learning task when an in-app feature is unavailable.",
            ],
        ),
    ],
)

LG_NEXT_STEPS = [
    "Re-run the eight labs from a fresh copy of the synthetic source pack and compare the correction log with your first attempt.",
    "Choose one real low-risk workplace workflow and complete a CONTROL canvas before using any organisation data.",
    "Agree with your manager or administrator which data classes, Workspace plans, sharing settings and approval gates are permitted.",
    "Build a prompt library that stores purpose, approved source type, output format, review criteria, owner and last review date.",
    "Pilot one draft-only automation with a small group, measure correction and exception rates, then decide whether to expand.",
]

LG_GLOSSARY = [
    ("Apps Script", "Google's cloud-based JavaScript platform for extending and automating Workspace."),
    ("Approval gate", "A named decision point where a person checks evidence and authorises the next state."),
    ("Bounded automation", "An automation restricted to defined inputs, actions, recipients, logs and stop conditions."),
    ("Candidate output", "Generated material that must still be checked and approved before use."),
    ("Chart contract", "The explicit relationship among question, source table, chart type, title, axes, units and series."),
    ("CONTROL canvas", "Context, Owner, Needed inputs, Task sequence, Review, Output destination and Learning signal."),
    ("Data grain", "What one row or observation represents."),
    ("Data minimisation", "Using only the fields required for the stated purpose."),
    ("Dry run", "A mode that records intended actions without performing their external effect."),
    ("Grounding", "Using specific permitted sources as context for a response."),
    ("G-E-A-R", "Grounding, Evidence, Audience and Risk - the course review loop."),
    ("Idempotency", "A control that prevents the same input from causing duplicate actions when processed again."),
    ("Least privilege", "Giving users, files and processes only the access needed for the task."),
    ("Metric definition", "The calculation, population, denominator, units, time scope and exclusions behind a number."),
    ("P-T-C-F", "Persona, Task, Context and Format - the core prompt structure used in the course."),
    ("Reconciliation", "Comparing counts and totals before and after a transformation to explain every change."),
    ("Source boundary", "The explicit set of files or facts a generated response may use."),
    ("Synthetic data", "Artificial practice data that does not describe real people or confidential operations."),
    ("Workspace grounding", "Gemini's use of permitted Workspace content selected or retrieved for a task."),
    ("Workflow state", "A visible stage such as Source, Working, Approved, Drafted, Sent or Exception."),
]

NEXT_STEPS = dict(
    title="A Practical 30-Day Adoption Plan",
    items=[
        "Week 1 - inventory one repetitive task, its approved sources, data class, owner and current failure points.",
        "Week 2 - test a P-T-C-F prompt and G-E-A-R review on synthetic or minimised data.",
        "Week 3 - pilot a draft-only cross-app workflow with logs, exceptions and a small authorised group.",
        "Week 4 - compare time saved, corrections, completion and risk observations before approving the next scope.",
    ],
)

THANK_YOU = dict(
    body=(
        "You can now use Gemini across Google Workspace as a controlled collaborator: "
        "prompt with context, verify with evidence, share deliberately and automate in small observable steps."
    ),
    kicker="PROMPT WITH PURPOSE - VERIFY WITH EVIDENCE - ACT WITH CONTROL",
)

TRAINER_TEAM = [
    (
        "Truman Ng",
        "ACTA-certified trainer and technology practitioner with extensive experience in cloud, networking, databases, web systems and enterprise implementation.",
    ),
]

ICE_BREAKER = [
    "Your name, role and the Workspace app you use most often.",
    "One repetitive writing, analysis or coordination task you would like to improve.",
    "One data, accuracy or sharing risk that should never be automated away.",
]

VERSION_HISTORY = [
    (
        "1.0",
        VERSION_DATE,
        "Initial aligned release: PPT, Learner Guide, Lesson Plan and eight connected labs.",
        TRAINER,
    ),
]
