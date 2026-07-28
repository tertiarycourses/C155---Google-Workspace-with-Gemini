# Aster & Finch Controlling Facts and Practice Policies

> Synthetic training control file. When this file conflicts with an earlier draft, this file takes priority.

## Controlling facts

| Field | Controlling value |
|---|---|
| Event title | Aster & Finch Partner Operations Briefing |
| Date | 14 August 2026 |
| Time | 2:00 pm-3:30 pm Singapore time |
| Delivery mode | Online using Google Meet |
| Physical or hybrid option | Not approved |
| Partner confirmation deadline | 7 August 2026 |
| Accessibility-request deadline | 5 August 2026 |
| Accessibility route | partner-support@aster-finch.example |
| Event coordinator | Priya Shah |
| Final facilitator | PENDING |
| Final Google Meet link | PENDING |
| Recording | Not approved |

## Data rules

- The supplied registration CSV is synthetic training data.
- Analysis uses only the `Valid` tab created through the documented cleaning rules.
- Partner-facing outputs use grouped values only and do not expose a contact name or email.
- Unknown or conflicting details remain `UNKNOWN` or `PENDING`.
- No password, access token, private key or protected workplace record belongs in a prompt.

## Sharing rules

- Source and working files start as Restricted.
- Named training collaborators receive only the access needed for their role.
- Event invitation drafts remain unsent until a human checks recipients, commitments, links and attachments.
- Meeting notes remain a candidate until reviewed against the conversation or transcript.
- Files in `04-Archive` are never controlling sources.

## Automation rules

- The course automation creates Gmail drafts only.
- The first live action uses the learner's own training email address.
- A `HOLD` or processed row is skipped.
- Dry-run evidence is required before a live draft.
- Bulk actions, automatic sending, deletion and permission changes are outside the course workflow.
