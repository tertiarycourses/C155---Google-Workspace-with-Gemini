# Lab 6 — Analyse Registrations and Build the Decision Dashboard

**Course:** Google Workspace with Gemini  
**Course Code:** C155  
**Version:** v1.0 (28 July 2026)  
**Topic 3:** Gemini in Sheets and Data Analysis  
**Maps to:** LO3: define metrics, analyse clean data and create a truthful chart and bounded narrative in Sheets  
**Duration:** 45 minutes  
**Tools:** Google Sheets - Gemini in Sheets where available - Google Slides - Drive

---

## Goal

Answer which partner segment needs follow-up using visible metrics, a reproducible pivot and a chart that matches the source table.

## What You Will Do

You will define the valid population and metrics before asking Gemini for insights, create a pivot table and confirmation-rate calculations, then build a simple chart. The final narrative separates observations from hypotheses and updates the approved Slides deck.

## What You Will Build

Analysis and Dashboard tabs inside 05-registration-analysis containing a verified pivot, metric definitions, confirmation rates, one horizontal bar chart and a three-part insight note, plus the linked chart inserted into slide 3 of 04-partner-briefing-deck.

## Prerequisites

- Approved 05-registration-analysis with 20 valid rows and a balanced reconciliation.
- Approved 04-partner-briefing-deck from Lab 4.
- Do not analyse the Raw or Clean exception rows as if they belong to the valid population.

> **Data note.** Use only the supplied synthetic scenario and an account you are authorised to use. Do not paste passwords, secrets, protected personal data or confidential workplace content into a prompt. Keep live sending disabled until the lab explicitly calls for one reviewed draft to your own account.

## Steps

### 1. Add Analysis and Dashboard tabs. At the top of Analysis write the question: Which partner segment needs the most follow-up before the briefing? Define Valid registrations, Confirmed registrations, Confirmation rate, Missing-information count, population, time scope and material exclusions. Cite Valid and Rules.

```text
Confirmation rate = Confirmed valid registrations / All valid registrations in the segment
Population = 20 rows in Valid
Exclusions = 4 rows documented in Rules
```

### 2. Create a pivot table from Valid A1:P on Analysis. Set Rows to Segment_Clean, Columns to Status_Clean and Values to COUNTA of Registration_ID. Turn off totals only if the counts remain visible elsewhere. Compare every pivot cell with a filtered count in Valid.

```text
Expected counts:
SME: Confirmed 5 | Waitlisted 2 | Cancelled 1 | Total 8
Enterprise: Confirmed 5 | Waitlisted 2 | Cancelled 1 | Total 8
Non-profit: Confirmed 2 | Waitlisted 1 | Cancelled 1 | Total 4
```

### 3. Beside the pivot create a metric table with Segment, Valid registrations, Confirmed, Confirmation rate and Missing information. Use cell references to the pivot and a COUNTIFS against Valid for Info_Flag. Format confirmation rate as a percentage with one decimal place.

```text
Expected rates:
SME 62.5%
Enterprise 62.5%
Non-profit 50.0%
Expected total MISSING DIETARY = 3
```

### 4. Ask Gemini in Sheets for three observations using only the metric table. Require each sentence to show the number, comparison and limitation, and require explanations to be labelled HYPOTHESIS. Verify the response and write a final note with Observed, Hypothesis and Recommended follow-up as separate headings. If Gemini in Sheets is unavailable, manually write two factual comparisons from the visible metric table, one explicitly labelled hypothesis and one proportionate follow-up; apply the same number, comparison and limitation checks.

```text
Using only this metric table, write: (1) two factual observations with values, (2) one clearly labelled hypothesis, and (3) one proportionate follow-up. Do not claim causation. Mention that the Non-profit segment has only four valid registrations.
```

### 5. On Dashboard copy or reference Segment and Valid registrations. Insert a horizontal bar chart, order segments by valid registrations descending and title it Valid registrations by partner segment. Label the horizontal axis Registrations, start it at zero and keep one series with no 3D effect. Check all three bars against the metric table.

```text
Expected bar values: Enterprise 8 | SME 8 | Non-profit 4
```

### 6. Open the approved 04-partner-briefing-deck. On slide 3 replace only the labelled DATA PLACEHOLDER with the chart from Sheets as a linked chart and add a short note: 20 valid registrations after 4 documented exclusions. Add the Sheet name, Valid population and Rules exclusions to the slide speaker notes. Run the deck Source match and Visual accuracy checks again.

```text
Speaker-note source: 05-registration-analysis > Analysis metric table; population 20; exclusions documented in Rules; chart linked from Dashboard.
```

## Test It

The pivot must reproduce 8/8/4 valid registrations and 5/5/2 confirmations by segment; the rates must be 62.5%, 62.5% and 50.0%; total missing information must be 3; the chart must have one series, a zero baseline and the neutral title; the insight must separate observation, hypothesis and follow-up; and slide 3 must contain the linked chart with the population and exclusion source note.

## Checkpoint and Rejoin Point

Keep the updated Sheet and Slides file in 03-Approved. Lab 7 uses the verified counts and approved deck as sources for the rehearsal meeting and Drive synthesis.

## Troubleshooting

| If this happens | Fix |
|---|---|
| The pivot counts 24 rather than 20 rows. | Change the source range to Valid A1:P and confirm that the Valid tab still passes the reconciliation. |
| The chart title or note says performance improved. | Use a neutral descriptive title and keep the bounded observation separate from any hypothesis. |
| The linked chart in Slides shows stale values. | Select the chart and click Update, then compare each bar with the current Analysis metric table. |

## Challenge

Create a second chart of confirmation rate by segment. Decide whether the small Non-profit denominator needs a direct label or note and explain your choice.

## Reflection

Which statement in your insight is evidence and which is interpretation, and how can the reader tell?

---

[← Lab 5](lab-05-clean-the-registration-tracker-and-generate-formulas.md) · [Lab 7 →](lab-07-run-the-meeting-to-drive-follow-up-workflow.md)
