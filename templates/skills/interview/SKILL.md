---
name: interview
description: Interview the user about a feature before any plan or code. Use when the user says "interview me", "grill me", "ask me questions first", or starts a non-trivial feature with an underspecified request.
---

Don't write code or a plan yet.

1. Read enough of the codebase to know what already exists and which choices are genuinely open.
2. List the decisions that a wrong guess would make expensive to undo. Drop anything the codebase
   or the request already answers.
3. Ask them one at a time with the question tool, most expensive first, your recommendation as the
   first option. Stop at about ten.
4. Then list the assumptions you're making that you didn't ask about, so the user can veto them.
5. Write the answers into `plans/<name>.md` under Decisions and Assumptions (template: plan.md).
