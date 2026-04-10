# Repo Artifact Overview

This artifact is a runnable **Module 1** teaching repo prepared for continued refinement across Module 1~4.

## What is included

- minimal runnable FastAPI app
- main Module 1 case for `/profile`
- downstream consumer comparison via `/checkout-eligibility`
- expanded demo page at `/demo/profile-ui`
- Module 1 teaching materials
- two micro-transfer packs for Module 1
- tests that cover the main behaviors and the new demo panel

## Why this artifact exists

It is meant to support the next design steps without losing current decisions:

- Module 1 focuses on task brief outer structure, not BRIEF/RAISE naming
- Module 1 now lightly includes: do not let AI act too early; this also relates to capability and cost
- Module 1 now has a visible UI contrast between:
  - hard backend failure
  - safe profile fallback
  - stricter downstream consumer requirement
- the repo is small enough to keep using in live demos and workshop iteration

## Good next refinement targets

- adjust micro-transfer prompts and facilitator notes
- tune the UI copy to fit the final teaching script
- add Module 2 bridge notes, without introducing BRIEF/RAISE into Module 1 learner artifacts
- keep this repo as the concrete Module 1 reference artifact, then branch or fork for later modules

## Added in this version

- `course_design_sync/` top-level synchronized markdown drafts for Module 1
- `materials/module1/module1_teacher_guide_v1.md`
- `materials/module1/module1_learner_handout_v1.md`
- `materials/module1/module1_coverage_check_v1.md`
