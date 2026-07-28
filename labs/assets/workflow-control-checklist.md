# CONTROL Workflow Checklist

| Element | Required question |
|---|---|
| Context | What trigger, audience, outcome and boundary define the workflow? |
| Owner | Who has authority to approve the source, action and destination? |
| Needed inputs | Which exact files, fields, permissions and states are required? |
| Task sequence | Which steps are generated, deterministic or human decisions? |
| Review | What evidence must pass before the next state? |
| Output destination | Where does the result land, and who can access it? |
| Learning signal | Which time, correction, completion and exception evidence will be recorded? |

## Bounded automation controls

- Start with a manual trigger.
- Use one synthetic or learner-owned recipient.
- Support `DRY_RUN` before a live action.
- Create a draft; do not automatically send.
- Validate required headers and email format.
- Skip `HOLD`, blank and already-processed rows.
- Write status, identifier, timestamp and a readable run note.
- Run the same input twice to prove duplicate prevention.
- Keep deletion, bulk processing and permission changes outside the lab.
