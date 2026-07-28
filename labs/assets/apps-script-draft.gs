/*
 * C155 Google Workspace with Gemini
 * Safe course automation: create at most one Gmail draft for the signed-in user.
 * Start with DRY_RUN = true. Never change createDraft to sendEmail in this lab.
 */

const DRY_RUN = true;
const SHEET_NAME = 'Automation';

function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('C155 Lab')
    .addItem('Run follow-up draft', 'runFollowUpDrafts')
    .addToUi();
}

function runFollowUpDrafts() {
  const spreadsheet = SpreadsheetApp.getActive();
  const sheet = spreadsheet.getSheetByName(SHEET_NAME);
  if (!sheet) {
    throw new Error(`Missing sheet: ${SHEET_NAME}`);
  }

  const values = sheet.getDataRange().getValues();
  if (values.length < 2) {
    throw new Error('Automation has no data rows.');
  }

  const headers = values[0].map(value => String(value).trim());
  const required = [
    'Status',
    'Email',
    'Contact_Name',
    'Subject',
    'Body',
    'Draft_Status',
    'Draft_ID',
    'Drafted_At',
    'Last_Run_Note',
  ];
  const column = {};
  required.forEach(name => {
    const index = headers.indexOf(name);
    if (index === -1) {
      throw new Error(`Missing required header: ${name}`);
    }
    column[name] = index;
  });

  const eligible = [];
  for (let rowIndex = 1; rowIndex < values.length; rowIndex += 1) {
    const row = values[rowIndex];
    const status = String(row[column.Status] || '').trim().toUpperCase();
    const draftStatus = String(row[column.Draft_Status] || '').trim();
    if (status === 'READY' && !draftStatus) {
      eligible.push({ rowIndex, row });
    } else {
      console.log(
        `Row ${rowIndex + 1}: skipped status ${status || 'BLANK'}; ` +
        `draft status ${draftStatus || 'BLANK'}.`
      );
    }
  }

  if (eligible.length > 1) {
    throw new Error(
      `Safety stop: ${eligible.length} unprocessed READY rows found; this lab permits exactly one.`
    );
  }
  if (eligible.length === 0) {
    console.log('No unprocessed READY row; no action taken.');
    return;
  }

  const item = eligible[0];
  const rowNumber = item.rowIndex + 1;
  const email = String(item.row[column.Email] || '').trim().toLowerCase();
  const subject = String(item.row[column.Subject] || '').trim();
  const body = String(item.row[column.Body] || '').trim();
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  const allowedRecipient = String(Session.getEffectiveUser().getEmail() || '')
    .trim()
    .toLowerCase();

  if (!allowedRecipient) {
    throw new Error('Cannot confirm the signed-in user email; no draft was created.');
  }
  if (!emailPattern.test(email) || email !== allowedRecipient) {
    throw new Error(
      `Safety stop: row ${rowNumber} must use the signed-in user email only.`
    );
  }
  if (!subject || !body) {
    throw new Error(`Row ${rowNumber} requires both Subject and Body.`);
  }

  if (DRY_RUN) {
    const note = `DRY RUN OK: would create one draft to ${allowedRecipient} with subject ${subject}`;
    sheet.getRange(rowNumber, column.Last_Run_Note + 1).setValue(note);
    console.log(note);
    return;
  }

  const draft = GmailApp.createDraft(allowedRecipient, subject, body);
  sheet.getRange(rowNumber, column.Draft_Status + 1).setValue('DRAFTED');
  sheet.getRange(rowNumber, column.Draft_ID + 1).setValue(draft.getId());
  sheet.getRange(rowNumber, column.Drafted_At + 1).setValue(new Date());
  sheet.getRange(rowNumber, column.Last_Run_Note + 1)
    .setValue('LIVE OK: one Gmail draft created for the signed-in user.');
  console.log(`Row ${rowNumber}: created draft ${draft.getId()}.`);
}
