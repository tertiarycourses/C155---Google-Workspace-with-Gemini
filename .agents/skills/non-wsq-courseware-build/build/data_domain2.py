"""Topic 2 labs for C155."""

DOMAIN2 = [
    dict(
        num=3,
        topic=2,
        title="Draft the Partner Communication Pack in Docs and Gmail",
        duration=75,
        objective="LO2: draft, summarise and refine source-led workplace content in Docs and Gmail",
        goal="Convert the approved briefing and a synthetic email thread into a reviewed partner invitation, internal summary and Gmail draft.",
        workflow=["Summarise thread", "Draft in Docs", "Refine for audience", "Save reviewed Gmail draft"],
        desc=(
            "You will distinguish thread facts from requests and commitments, use Gemini to draft a "
            "partner invitation from approved sources, refine it in Docs and prepare a Gmail draft. "
            "The message remains unsent so recipient, attachment and commitment checks stay visible."
        ),
        build=(
            "A 03-partner-communication-pack Google Doc containing a verified thread summary, "
            "partner invitation and internal hand-off note, plus one reviewed Gmail draft to the "
            "learner's own address with a completed send checklist."
        ),
        services="Google Docs - Gmail - Gemini in Gmail or Docs where available - Drive",
        prerequisites=[
            "Approved 02-grounded-briefing and 02-claim-review-ledger from Lab 2.",
            "Open labs/assets/partner-email-thread.txt; it is a synthetic thread and is not sent to real recipients.",
            "Know the email address of the same training account; it is the only permitted recipient in this lab.",
        ],
        steps=[
            (
                "Create a Google Doc in 02-Working named 03-partner-communication-pack. Add headings "
                "Thread summary, Partner invitation, Internal hand-off, Cross-artifact ledger and Send "
                "checklist. Under Thread summary create a table with Type, Statement, Owner, Due or PENDING "
                "and Source message.",
                "Required thread categories: confirmed facts | partner requests | proposed but unapproved commitments | open questions",
            ),
            (
                "Paste partner-email-thread.txt into Gemini in Gmail, Gemini in Docs or the documented "
                "fallback. Ask for a bounded summary. If no Gemini control is available, read each numbered "
                "message and manually add one table row per fact, request, decision, proposal or open question; "
                "copy the message number and use PENDING for a missing owner or due date. Insert the result into "
                "the summary table, then read the original thread and correct any missed qualification, wrong "
                "owner or proposed detail presented as confirmed.",
                "Summarise this synthetic email thread into a table with Type, Statement, Owner, Due or "
                "PENDING and Source message number. Separate confirmed facts, requests, decisions and "
                "proposals. Do not turn a proposal into a commitment. End with unresolved questions.",
            ),
            (
                "Under Partner invitation use the approved grounded briefing and corrected thread summary "
                "as the only sources. Ask Gemini for a subject line and 180-220 word invitation with "
                "purpose, confirmed logistics, preparation request, accessibility contact and next action. "
                "Require PENDING for any unresolved detail. If Gemini is unavailable, draft the same artifact "
                "manually: write the subject, two short purpose/logistics paragraphs, a three-item preparation "
                "list, accessibility line and next action, then count and edit it to 180-220 words.",
                "Persona: I am the Aster & Finch coordinator writing to invited partner representatives.\n"
                "Task: Draft a clear invitation that explains why to attend and what to prepare.\n"
                "Context: Use only the approved briefing and corrected thread summary below. Confirmed "
                "information overrides proposals; unresolved details remain PENDING.\n"
                "Format: Subject line plus 180-220 word email with short paragraphs and a three-item "
                "preparation list.\nReview: List every commitment, date, link, attachment and recipient assumption.",
            ),
            (
                "Edit the invitation in Docs. Use the G-E-A-R loop and the 02-claim-review-ledger to verify "
                "every event fact. Replace jargon, remove duplicate sentences and make the next action "
                "specific. Under Cross-artifact ledger add rows for Date, Delivery mode, Audience, "
                "Preparation request and Accessibility; show the value in Briefing, Thread and Final email.",
                "Ledger columns: Field | Briefing value | Thread value | Final email value | Result | Edit made\nResult values: MATCH | PENDING | REPAIRED",
            ),
            (
                "Under Internal hand-off ask Gemini to turn the final invitation into a 120-word note for "
                "the operations team. Require Owner, Action, Due or PENDING, Source and Risk as a table. "
                "If Gemini is unavailable, manually restate only the invitation's confirmed actions in the "
                "same table and edit the surrounding note to 120 words. Verify that the note does not create "
                "a new external commitment and record the responsible human reviewer.",
                "Create a 120-word internal hand-off from the approved invitation. Use a table with Owner, "
                "Action, Due or PENDING, Source and Risk. Do not invent an owner, date or approved budget.",
            ),
            (
                "In Gmail start a new message addressed only to your own training account. Paste the "
                "reviewed subject and invitation, then save it as a draft; do not click Send. In the Doc "
                "complete the checklist rows To, Cc/Bcc, Subject, Dates, Commitments, Links, Attachments, "
                "Accessibility, Tone and Approver. Record the Gmail draft timestamp.",
                "Checklist result values: PASS | NOT USED | REPAIR\nRequired final state: Gmail Draft; recipient is the learner's own training address.",
            ),
        ],
        test=(
            "The communication pack must include all five headings, a thread summary that separates "
            "proposals from confirmed facts, a 180-220 word invitation, a five-field cross-artifact ledger, "
            "an internal hand-off with Owner/Action/Due/Source/Risk and a ten-row send checklist. Gmail must "
            "contain exactly one new unsent draft addressed only to the learner's own training account."
        ),
        checkpoint=(
            "Move the reviewed 03-partner-communication-pack to 03-Approved and leave the email unsent in "
            "Gmail Drafts. Lab 4 uses the approved message architecture and facts; it does not use the raw thread."
        ),
        troubleshooting=[
            (
                "The summary treats a proposed date or deliverable as confirmed.",
                "Return to the source message, label it PROPOSAL and change the final text to PENDING until the approved briefing confirms it.",
            ),
            (
                "Gemini in Gmail cannot access the approved Drive file.",
                "Use Gemini in Docs or paste the approved excerpt; do not broaden Drive sharing to solve the feature gap.",
            ),
            (
                "The draft is addressed to a synthetic email from the thread.",
                "Remove it immediately and use only your own training address; synthetic addresses are source text, not live recipients.",
            ),
        ],
        challenge=(
            "Create a 90-word mobile-first version of the invitation. Preserve all confirmed logistics and "
            "compare which formatting changes improve scanning without removing required context."
        ),
        reflection=(
            "Which part of the email required authority rather than language skill, and how did you keep that decision with a person?"
        ),
    ),
    dict(
        num=4,
        topic=2,
        title="Build the Partner Briefing Deck in Slides",
        duration=70,
        objective="LO2: create and refine a coherent source-backed presentation and appropriate generated visual in Google Slides",
        goal="Turn the approved communication pack into a concise six-slide story with traceable evidence, accessible design and a reviewed visual.",
        workflow=["Map the story", "Create slide candidates", "Build visual", "Run sequence review"],
        desc=(
            "You will design a slide sequence before generating content, build six low-density slides "
            "from approved facts and create one illustrative visual with Gemini or a native-shape "
            "fallback. A slide map and G-E-A-R ledger keep the story, evidence and audience action aligned."
        ),
        build=(
            "A Google Slides file named 04-partner-briefing-deck with six slides, speaker notes and "
            "one reviewed visual, plus a slide-map table in 03-partner-communication-pack linking each "
            "slide to its message, source, visual purpose and audience action."
        ),
        services="Google Slides - Gemini in Slides where available - Google Docs - Drive",
        prerequisites=[
            "Approved 03-partner-communication-pack and approved 02-grounded-briefing.",
            "The Gmail message remains an unsent draft; use the approved Doc as the source.",
            "Open labs/assets/prompt-quality-checklist.md for the final sequence review.",
        ],
        steps=[
            (
                "In the approved communication pack add a heading Slide map and a table with Slide, "
                "Audience question, One-sentence message, Evidence source, Visual purpose and Audience "
                "action. Create exactly six rows: Welcome, Why this briefing, Confirmed plan, How partners prepare, "
                "Coordination workflow and Next steps.",
                "Rule: each slide has one primary message and names an approved source or SOURCE NOT REQUIRED.",
            ),
            (
                "Create a blank Google Slides presentation in 02-Working named 04-partner-briefing-deck. "
                "Add six slides using the slide-map titles. Use a 16:9 layout, one consistent theme, title "
                "text of at least 28 pt and body text of at least 18 pt. Add the source filename and section "
                "to the speaker notes of slides 2-6.",
                "Deck order:\n1 Welcome\n2 Why this briefing\n3 Confirmed plan\n4 How partners prepare\n5 Coordination workflow\n6 Next steps",
            ),
            (
                "In Gemini in Slides, or in Gemini in Docs if the Slides control is unavailable, ask for "
                "candidate content for slides 2-6 using only the approved briefing and communication pack. "
                "Require one headline, no more than three short bullets and one evidence note per slide. "
                "If neither Gemini control is available, manually convert each slide-map row into that same "
                "headline, bullet and evidence-note structure using only the two approved artifacts. Insert "
                "only content that matches the slide map and source ledger.",
                "Create candidate text for slides 2-6. Use only the approved Aster & Finch briefing and "
                "communication pack. For each slide return Title, one-sentence headline, up to three bullets "
                "and Source. Preserve PENDING fields; do not invent a venue, speaker, URL, quotation or result.",
            ),
            (
                "Create one wide illustrative image for slide 1 or 2 with Gemini in Slides. Use an abstract "
                "collaboration scene with no logos, text, faces, real venue or documentary claim. If image "
                "generation is unavailable, build a native visual with three labelled circles: Partners, "
                "Evidence and Action, connected by arrows. Add alt text that explains the visual purpose.",
                "Visual prompt: Wide 16:9 editorial illustration of diverse abstract shapes collaborating "
                "around shared documents and data, calm blue and green palette, generous empty space on the "
                "left for a title, no text, no logos, no identifiable people, no photorealistic event venue.",
            ),
            (
                "Design slides 3-5 with one simple visual structure each: a confirmed-versus-pending table, "
                "a three-step preparation flow and a Source-to-Action workflow. Keep every PENDING field "
                "visible and do not shrink text below the stated sizes. On slide 3, add a bordered rectangle "
                "beside or below the confirmed-versus-pending table labelled DATA PLACEHOLDER - verified "
                "registration chart added in Lab 6. Add a final action and owner to slide 6.",
                "Slide 3 placeholder: DATA PLACEHOLDER - verified registration chart added in Lab 6\n"
                "Preparation flow: Review brief -> Bring questions -> Confirm accessibility needs\n"
                "Workflow: Approved source -> Gemini candidate -> Human review -> Partner action",
            ),
            (
                "Run a full-deck G-E-A-R review. Compare each slide with the slide map and speaker-note "
                "source, check titles and numbers against the claim ledger, then present the deck in full "
                "screen. Record PASS or REPAIR for Story sequence, Source match, Text readability, Visual "
                "accuracy, Alt text, PENDING fields and Final action. Apply repairs before moving the file. "
                "Record the seven checks in 03-partner-communication-pack under a Deck review heading.",
                "Required review rows: Story sequence | Source match | Text readability | Visual accuracy | "
                "Alt text | PENDING fields | Final action",
            ),
        ],
        test=(
            "The Slides file must contain exactly six slides in the mapped order; slides 2-6 must each "
            "have a speaker-note source; no slide may exceed one headline and three bullets; one reviewed "
            "visual must have alt text; the preparation and workflow visuals must use the stated sequence; "
            "slide 3 must include the labelled DATA PLACEHOLDER; and all seven final review rows must be "
            "recorded under Deck review in 03-partner-communication-pack and show PASS."
        ),
        checkpoint=(
            "Move 04-partner-briefing-deck to 03-Approved and keep the completed slide map in the approved "
            "communication pack. Lab 6 will replace only the labelled DATA PLACEHOLDER on slide 3 with a "
            "verified Sheets chart."
        ),
        troubleshooting=[
            (
                "Gemini creates unsupported speakers, dates or results.",
                "Remove them, add the source filenames and require PENDING for absent fields before generating again.",
            ),
            (
                "The generated visual looks like a photograph of a real event.",
                "Regenerate as an abstract editorial illustration or use the native-shape fallback and label it illustrative.",
            ),
            (
                "The slide title or bullets wrap into a crowded layout.",
                "Shorten the message, split no additional slides and keep the minimum font sizes instead of shrinking text.",
            ),
        ],
        challenge=(
            "Create an alternate title-slide visual for a senior executive audience. Explain how the visual "
            "purpose changes while the approved facts and slide sequence remain constant."
        ),
        reflection=(
            "Which slide contributes most to the decision path, and what would be lost if it were replaced by a decorative image?"
        ),
    ),
]
