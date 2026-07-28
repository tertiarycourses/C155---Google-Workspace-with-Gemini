# C155---Google-Workspace-with-Gemini

Aligned non-WSQ courseware for **Google Workspace with Gemini** (Course Code: **C155**).

## Deliverables

- Trainer Slides and Learner Slides
- Learner Guide
- Lesson Plan
- Eight connected hands-on labs with synthetic practice assets

## Source of truth

All learner-facing artifacts are generated from:

- `.agents/skills/non-wsq-courseware-build/build/course_data.py`
- `.agents/skills/non-wsq-courseware-build/build/data_domain1.py` through `data_domain4.py`

This keeps the PPT, Learner Guide, Lesson Plan and labs aligned on course identity, topic order, learning outcomes and lab sequence.

## Build

From Git Bash on Windows:

```bash
COURSE_REPO="$PWD" bash ".agents/skills/non-wsq-courseware-build/build/build_courseware.sh"
```

## Course outline

https://www.tertiarycourses.com.sg/google-workspace-with-gemini.html
