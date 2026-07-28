# P-T-C-F and G-E-A-R Quality Checklist

## Prompt contract

| Element | Check |
|---|---|
| Persona | Does the role improve the response without inventing authority? |
| Task | Is the requested action and finished artifact explicit? |
| Context | Are the approved sources, audience and constraints named? |
| Format | Are structure, length, tone and required fields observable? |
| Source boundary | Must missing facts become `UNKNOWN` or `PENDING`? |
| Review criteria | Does the prompt name the checks that determine whether the result is usable? |

## G-E-A-R review

| Check | Questions |
|---|---|
| Grounding | Which files, ranges or messages control each material statement? |
| Evidence | Do names, dates, numbers, links, formulas and commitments match the source? |
| Audience | Is the structure, tone, accessibility and next action suitable for the intended reader? |
| Risk | Are privacy, permissions, recipients, bias, rights, uncertainty and approval handled? |

## Decision

- `PASS`: evidence is visible and the result is ready for the stated course workflow.
- `REPAIR`: edit and repeat the check.
- `HOLD`: authority, source or risk cannot be resolved yet.
