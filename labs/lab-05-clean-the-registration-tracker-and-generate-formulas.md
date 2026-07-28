# Lab 5 — Clean the Registration Tracker and Generate Formulas

**Course:** Google Workspace with Gemini  
**Course Code:** C155  
**Version:** v1.0 (28 July 2026)  
**Topic 3:** Gemini in Sheets and Data Analysis  
**Maps to:** LO3: clean and organise spreadsheet data with documented rules, Gemini suggestions and reproducible formulas  
**Duration:** 75 minutes  
**Tools:** Google Sheets - Gemini in Sheets where available - Drive - registration-data.csv

---

## Goal

Preserve the raw synthetic registrations, standardise key fields and create a reconciled valid-analysis table.

## What You Will Do

You will import a deliberately inconsistent registration CSV into Sheets, define the row grain and cleaning rules, ask Gemini for formula help and verify every formula before filling it down. A separate Valid tab and reconciliation make exclusions visible.

## What You Will Build

A 05-registration-analysis Google Sheet with Raw, Clean, Valid, Rules and Formula-tests tabs. The workbook preserves 24 raw rows, produces 20 valid rows, flags exceptions and documents the exact formula and reason for every transformation.

## Prerequisites

- Download or open labs/assets/registration-data.csv; it contains only synthetic contacts and non-routable example.com addresses.
- The C155-Aster-Finch folder and state subfolders from Lab 1 are available.
- Use a native Google Sheet because Gemini in Sheets works best with native Sheets files.

> **Data note.** Use only the supplied synthetic scenario and an account you are authorised to use. Do not paste passwords, secrets, protected personal data or confidential workplace content into a prompt. Keep live sending disabled until the lab explicitly calls for one reviewed draft to your own account.

## Steps

### 1. In 02-Working create a Google Sheet named 05-registration-analysis. Import registration-data.csv into a tab named Raw and freeze row 1. Confirm that the row grain is one submitted registration and record 24 data rows. Duplicate Raw as Clean; never edit Raw. Add Rules, Formula-tests and Valid tabs.

```text
Control totals:
Raw data rows = 24
Unique registration IDs expected before rule review = 23
```

### 2. On Rules add columns Field, Observed issue, Before, After, Rule, Unknown treatment and Owner. Profile Segment, Status, Email and Registration_ID using filters or Gemini in Sheets. Record category variants, one later duplicate, one invalid email and any value outside the approved mappings. Do not ask Gemini to replace unknowns automatically.

```text
Approved Segment values: SME | Enterprise | Non-profit
Approved Status values: Confirmed | Waitlisted | Cancelled
Unknown treatment: REVIEW
```

### 3. In Clean add headers in K1:P1: Segment_Clean, Status_Clean, Email_Valid, Duplicate_Flag, Info_Flag and Date_Clean. Ask Gemini for formulas using these exact columns, then compare the suggestion with the formulas below. Enter the reviewed formulas in row 2.

```text
K2 =SWITCH(LOWER(TRIM(C2)),"sme","SME","small business","SME","enterprise","Enterprise","nonprofit","Non-profit","non-profit","Non-profit","REVIEW")
L2 =SWITCH(LOWER(TRIM(F2)),"confirmed","Confirmed","confirm","Confirmed","waitlist","Waitlisted","waitlisted","Waitlisted","cancelled","Cancelled","REVIEW")
M2 =REGEXMATCH(LOWER(TRIM(E2)),"^[^@\s]+@[^@\s]+\.[^@\s]+$")
N2 =COUNTIF($A$2:A2,A2)>1
O2 =IF(AND(L2="Confirmed",TRIM(H2)=""),"MISSING DIETARY","OK")
P2 =IF(J2="","REVIEW",IF(ISNUMBER(J2),J2,IFERROR(DATE(VALUE(LEFT(TO_TEXT(J2),4)),VALUE(MID(TO_TEXT(J2),6,2)),VALUE(RIGHT(TO_TEXT(J2),2))),"REVIEW")))
```

### 4. Before filling down, use Formula-tests to create six rows with Test, Input row, Expected result, Actual result, Formula and PASS/REPAIR. Cover a Small business segment, confirm status, invalid email, later duplicate, confirmed row with blank Dietary and a valid date. Use 2026-07-20 for the sixth input and expect 20 July 2026; format Date_Clean as dd mmm yyyy. Repair any formula that fails, then fill K2:P2 down through row 25.

```text
Required test examples:
Segment ' Small Business ' -> SME
Status 'confirm' -> Confirmed
Email without @ -> FALSE
Second AF-010 -> TRUE
Confirmed plus blank Dietary -> MISSING DIETARY
Date 2026-07-20 -> 20 Jul 2026
```

### 5. Copy Clean row 1 to Valid row 1. In Valid A2 enter the FILTER formula below. This table keeps records with a valid email, first occurrence of the registration ID and approved clean Segment and Status. It does not remove rows from Raw or Clean.

```text
=FILTER(Clean!A2:P,Clean!A2:A<>"",Clean!M2:M=TRUE,Clean!N2:N=FALSE,Clean!K2:K<>"REVIEW",Clean!L2:L<>"REVIEW")
```

### 6. At the top of Rules add a Reconciliation block. Record Raw rows, Valid rows, Invalid email exclusions, Later duplicate exclusions, Segment REVIEW exclusions and Status REVIEW exclusions. Add the check Raw = Valid + exclusions. Use filters to name each excluded Registration_ID and the exact rule.

```text
Expected reconciliation:
Raw 24 = Valid 20 + Invalid email 1 + Later duplicate 1 + Segment REVIEW 1 + Status REVIEW 1
```

### 7. Apply a filter and conditional formatting to Clean so REVIEW, FALSE and TRUE duplicate flags are visible. Protect the Raw tab with a warning if your account permits it. Record the reviewer and move the Sheet to 03-Approved only when all six formula tests and the reconciliation pass.

```text
Approval checks: Raw unchanged | 6 formula tests PASS | Valid rows 20 | reconciliation balances | exclusions named
```

## Test It

Raw must contain 24 data rows and remain unchanged; Clean must contain six new formula columns; Formula-tests must show six PASS rows; Valid must contain 20 data rows; and Rules must reconcile 24 = 20 + 1 + 1 + 1 + 1 with every excluded Registration_ID named. A count of MISSING DIETARY in Valid must equal 3.

## Checkpoint and Rejoin Point

Keep 05-registration-analysis in 03-Approved with Raw, Clean, Valid, Rules and Formula-tests. Lab 6 uses only Valid for metrics and cites the Rules reconciliation for exclusions.

## Troubleshooting

| If this happens | Fix |
|---|---|
| The CSV opens as an Excel file and Gemini controls are unavailable. | Use File > Save as Google Sheets, rename the imported tab Raw and continue from the native file. |
| The duplicate formula marks both AF-010 rows. | Use the expanding range $A$2:A2 so only the later occurrence returns TRUE. |
| The Valid tab returns no rows or a range-size error. | Confirm every FILTER condition starts on row 2 and covers the same open-ended row range. |

## Challenge

Add a reusable data-validation dropdown for a manually reviewed Clean_Status_Override field. Explain why an override needs owner, reason and timestamp rather than silently replacing the formula.

## Reflection

Which cleaning decision could most change the later insight, and what evidence makes that decision auditable?

---

[← Lab 4](lab-04-build-the-partner-briefing-deck-in-slides.md) · [Lab 6 →](lab-06-analyse-registrations-and-build-the-decision-dashboard.md)
