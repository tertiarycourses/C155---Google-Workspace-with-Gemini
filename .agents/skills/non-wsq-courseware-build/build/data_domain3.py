"""Topic 3 labs for C155."""

DOMAIN3 = [
    dict(
        num=5,
        topic=3,
        title="Clean the Registration Tracker and Generate Formulas",
        duration=75,
        objective="LO3: clean and organise spreadsheet data with documented rules, Gemini suggestions and reproducible formulas",
        goal="Preserve the raw synthetic registrations, standardise key fields and create a reconciled valid-analysis table.",
        workflow=["Profile raw data", "Define rules", "Apply formulas", "Reconcile outputs"],
        desc=(
            "You will import a deliberately inconsistent registration CSV into Sheets, define the row "
            "grain and cleaning rules, ask Gemini for formula help and verify every formula before filling "
            "it down. A separate Valid tab and reconciliation make exclusions visible."
        ),
        build=(
            "A 05-registration-analysis Google Sheet with Raw, Clean, Valid, Rules and Formula-tests "
            "tabs. The workbook preserves 24 raw rows, produces 20 valid rows, flags exceptions and "
            "documents the exact formula and reason for every transformation."
        ),
        services="Google Sheets - Gemini in Sheets where available - Drive - registration-data.csv",
        prerequisites=[
            "Download or open labs/assets/registration-data.csv; it contains only synthetic contacts and non-routable example.com addresses.",
            "The C155-Aster-Finch folder and state subfolders from Lab 1 are available.",
            "Use a native Google Sheet because Gemini in Sheets works best with native Sheets files.",
        ],
        steps=[
            (
                "In 02-Working create a Google Sheet named 05-registration-analysis. Import "
                "registration-data.csv into a tab named Raw and freeze row 1. Confirm that the row grain "
                "is one submitted registration and record 24 data rows. Duplicate Raw as Clean; never "
                "edit Raw. Add Rules, Formula-tests and Valid tabs.",
                "Control totals:\nRaw data rows = 24\nUnique registration IDs expected before rule review = 23",
            ),
            (
                "On Rules add columns Field, Observed issue, Before, After, Rule, Unknown treatment and "
                "Owner. Profile Segment, Status, Email and Registration_ID using filters or Gemini in "
                "Sheets. Record category variants, one later duplicate, one invalid email and any value "
                "outside the approved mappings. Do not ask Gemini to replace unknowns automatically.",
                "Approved Segment values: SME | Enterprise | Non-profit\n"
                "Approved Status values: Confirmed | Waitlisted | Cancelled\n"
                "Unknown treatment: REVIEW",
            ),
            (
                "In Clean add headers in K1:P1: Segment_Clean, Status_Clean, Email_Valid, Duplicate_Flag, "
                "Info_Flag and Date_Clean. Ask Gemini for formulas using these exact columns, then compare "
                "the suggestion with the formulas below. Enter the reviewed formulas in row 2.",
                "K2 =SWITCH(LOWER(TRIM(C2)),\"sme\",\"SME\",\"small business\",\"SME\",\"enterprise\",\"Enterprise\",\"nonprofit\",\"Non-profit\",\"non-profit\",\"Non-profit\",\"REVIEW\")\n"
                "L2 =SWITCH(LOWER(TRIM(F2)),\"confirmed\",\"Confirmed\",\"confirm\",\"Confirmed\",\"waitlist\",\"Waitlisted\",\"waitlisted\",\"Waitlisted\",\"cancelled\",\"Cancelled\",\"REVIEW\")\n"
                "M2 =REGEXMATCH(LOWER(TRIM(E2)),\"^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$\")\n"
                "N2 =COUNTIF($A$2:A2,A2)>1\n"
                "O2 =IF(AND(L2=\"Confirmed\",TRIM(H2)=\"\"),\"MISSING DIETARY\",\"OK\")\n"
                "P2 =IF(J2=\"\",\"REVIEW\",IF(ISNUMBER(J2),J2,IFERROR(DATE(VALUE(LEFT(TO_TEXT(J2),4)),VALUE(MID(TO_TEXT(J2),6,2)),VALUE(RIGHT(TO_TEXT(J2),2))),\"REVIEW\")))",
            ),
            (
                "Before filling down, use Formula-tests to create six rows with Test, Input row, Expected "
                "result, Actual result, Formula and PASS/REPAIR. Cover a Small business segment, confirm "
                "status, invalid email, later duplicate, confirmed row with blank Dietary and a valid date. "
                "Use 2026-07-20 for the sixth input and expect 20 July 2026; format Date_Clean as dd mmm yyyy. "
                "Repair any formula that fails, then fill K2:P2 down through row 25.",
                "Required test examples:\n"
                "Segment ' Small Business ' -> SME\nStatus 'confirm' -> Confirmed\n"
                "Email without @ -> FALSE\nSecond AF-010 -> TRUE\nConfirmed plus blank Dietary -> MISSING DIETARY\n"
                "Date 2026-07-20 -> 20 Jul 2026",
            ),
            (
                "Copy Clean row 1 to Valid row 1. In Valid A2 enter the FILTER formula below. This table "
                "keeps records with a valid email, first occurrence of the registration ID and approved "
                "clean Segment and Status. It does not remove rows from Raw or Clean.",
                "=FILTER(Clean!A2:P,Clean!A2:A<>\"\",Clean!M2:M=TRUE,Clean!N2:N=FALSE,Clean!K2:K<>\"REVIEW\",Clean!L2:L<>\"REVIEW\")",
            ),
            (
                "At the top of Rules add a Reconciliation block. Record Raw rows, Valid rows, Invalid "
                "email exclusions, Later duplicate exclusions, Segment REVIEW exclusions and Status "
                "REVIEW exclusions. Add the check Raw = Valid + exclusions. Use filters to name each "
                "excluded Registration_ID and the exact rule.",
                "Expected reconciliation:\nRaw 24 = Valid 20 + Invalid email 1 + Later duplicate 1 + Segment REVIEW 1 + Status REVIEW 1",
            ),
            (
                "Apply a filter and conditional formatting to Clean so REVIEW, FALSE and TRUE duplicate "
                "flags are visible. Protect the Raw tab with a warning if your account permits it. Record "
                "the reviewer and move the Sheet to 03-Approved only when all six formula tests and the "
                "reconciliation pass.",
                "Approval checks: Raw unchanged | 6 formula tests PASS | Valid rows 20 | reconciliation balances | exclusions named",
            ),
        ],
        test=(
            "Raw must contain 24 data rows and remain unchanged; Clean must contain six new formula columns; "
            "Formula-tests must show six PASS rows; Valid must contain 20 data rows; and Rules must reconcile "
            "24 = 20 + 1 + 1 + 1 + 1 with every excluded Registration_ID named. A count of MISSING DIETARY "
            "in Valid must equal 3."
        ),
        checkpoint=(
            "Keep 05-registration-analysis in 03-Approved with Raw, Clean, Valid, Rules and Formula-tests. "
            "Lab 6 uses only Valid for metrics and cites the Rules reconciliation for exclusions."
        ),
        troubleshooting=[
            (
                "The CSV opens as an Excel file and Gemini controls are unavailable.",
                "Use File > Save as Google Sheets, rename the imported tab Raw and continue from the native file.",
            ),
            (
                "The duplicate formula marks both AF-010 rows.",
                "Use the expanding range $A$2:A2 so only the later occurrence returns TRUE.",
            ),
            (
                "The Valid tab returns no rows or a range-size error.",
                "Confirm every FILTER condition starts on row 2 and covers the same open-ended row range.",
            ),
        ],
        challenge=(
            "Add a reusable data-validation dropdown for a manually reviewed Clean_Status_Override field. "
            "Explain why an override needs owner, reason and timestamp rather than silently replacing the formula."
        ),
        reflection=(
            "Which cleaning decision could most change the later insight, and what evidence makes that decision auditable?"
        ),
    ),
    dict(
        num=6,
        topic=3,
        title="Analyse Registrations and Build the Decision Dashboard",
        duration=45,
        objective="LO3: define metrics, analyse clean data and create a truthful chart and bounded narrative in Sheets",
        goal="Answer which partner segment needs follow-up using visible metrics, a reproducible pivot and a chart that matches the source table.",
        workflow=["Define question", "Build pivot", "Verify metrics", "Create chart and insight"],
        desc=(
            "You will define the valid population and metrics before asking Gemini for insights, create "
            "a pivot table and confirmation-rate calculations, then build a simple chart. The final "
            "narrative separates observations from hypotheses and updates the approved Slides deck."
        ),
        build=(
            "Analysis and Dashboard tabs inside 05-registration-analysis containing a verified pivot, "
            "metric definitions, confirmation rates, one horizontal bar chart and a three-part insight "
            "note, plus the linked chart inserted into slide 3 of 04-partner-briefing-deck."
        ),
        services="Google Sheets - Gemini in Sheets where available - Google Slides - Drive",
        prerequisites=[
            "Approved 05-registration-analysis with 20 valid rows and a balanced reconciliation.",
            "Approved 04-partner-briefing-deck from Lab 4.",
            "Do not analyse the Raw or Clean exception rows as if they belong to the valid population.",
        ],
        steps=[
            (
                "Add Analysis and Dashboard tabs. At the top of Analysis write the question: Which partner "
                "segment needs the most follow-up before the briefing? Define Valid registrations, Confirmed "
                "registrations, Confirmation rate, Missing-information count, population, time scope and "
                "material exclusions. Cite Valid and Rules.",
                "Confirmation rate = Confirmed valid registrations / All valid registrations in the segment\n"
                "Population = 20 rows in Valid\nExclusions = 4 rows documented in Rules",
            ),
            (
                "Create a pivot table from Valid A1:P on Analysis. Set Rows to Segment_Clean, Columns to "
                "Status_Clean and Values to COUNTA of Registration_ID. Turn off totals only if the counts "
                "remain visible elsewhere. Compare every pivot cell with a filtered count in Valid.",
                "Expected counts:\nSME: Confirmed 5 | Waitlisted 2 | Cancelled 1 | Total 8\n"
                "Enterprise: Confirmed 5 | Waitlisted 2 | Cancelled 1 | Total 8\n"
                "Non-profit: Confirmed 2 | Waitlisted 1 | Cancelled 1 | Total 4",
            ),
            (
                "Beside the pivot create a metric table with Segment, Valid registrations, Confirmed, "
                "Confirmation rate and Missing information. Use cell references to the pivot and a "
                "COUNTIFS against Valid for Info_Flag. Format confirmation rate as a percentage with one "
                "decimal place.",
                "Expected rates:\nSME 62.5%\nEnterprise 62.5%\nNon-profit 50.0%\n"
                "Expected total MISSING DIETARY = 3",
            ),
            (
                "Ask Gemini in Sheets for three observations using only the metric table. Require each "
                "sentence to show the number, comparison and limitation, and require explanations to be "
                "labelled HYPOTHESIS. Verify the response and write a final note with Observed, Hypothesis "
                "and Recommended follow-up as separate headings. If Gemini in Sheets is unavailable, manually "
                "write two factual comparisons from the visible metric table, one explicitly labelled hypothesis "
                "and one proportionate follow-up; apply the same number, comparison and limitation checks.",
                "Using only this metric table, write: (1) two factual observations with values, (2) one "
                "clearly labelled hypothesis, and (3) one proportionate follow-up. Do not claim causation. "
                "Mention that the Non-profit segment has only four valid registrations.",
            ),
            (
                "On Dashboard copy or reference Segment and Valid registrations. Insert a horizontal bar "
                "chart, order segments by valid registrations descending and title it Valid registrations "
                "by partner segment. Label the horizontal axis Registrations, start it at zero and keep one "
                "series with no 3D effect. Check all three bars against the metric table.",
                "Expected bar values: Enterprise 8 | SME 8 | Non-profit 4",
            ),
            (
                "Open the approved 04-partner-briefing-deck. On slide 3 replace only the labelled DATA "
                "PLACEHOLDER with the chart from Sheets as a linked chart and add a short note: 20 valid "
                "registrations after 4 documented exclusions. "
                "Add the Sheet name, Valid population and Rules exclusions to the slide speaker notes. "
                "Run the deck Source match and Visual accuracy checks again.",
                "Speaker-note source: 05-registration-analysis > Analysis metric table; population 20; "
                "exclusions documented in Rules; chart linked from Dashboard.",
            ),
        ],
        test=(
            "The pivot must reproduce 8/8/4 valid registrations and 5/5/2 confirmations by segment; the "
            "rates must be 62.5%, 62.5% and 50.0%; total missing information must be 3; the chart must have "
            "one series, a zero baseline and the neutral title; the insight must separate observation, "
            "hypothesis and follow-up; and slide 3 must contain the linked chart with the population and "
            "exclusion source note."
        ),
        checkpoint=(
            "Keep the updated Sheet and Slides file in 03-Approved. Lab 7 uses the verified counts and "
            "approved deck as sources for the rehearsal meeting and Drive synthesis."
        ),
        troubleshooting=[
            (
                "The pivot counts 24 rather than 20 rows.",
                "Change the source range to Valid A1:P and confirm that the Valid tab still passes the reconciliation.",
            ),
            (
                "The chart title or note says performance improved.",
                "Use a neutral descriptive title and keep the bounded observation separate from any hypothesis.",
            ),
            (
                "The linked chart in Slides shows stale values.",
                "Select the chart and click Update, then compare each bar with the current Analysis metric table.",
            ),
        ],
        challenge=(
            "Create a second chart of confirmation rate by segment. Decide whether the small Non-profit "
            "denominator needs a direct label or note and explain your choice."
        ),
        reflection=(
            "Which statement in your insight is evidence and which is interpretation, and how can the reader tell?"
        ),
    ),
]
