## Planning and edits

- If my message is a question, answer it. Don't edit checked-in files.
- "I want to…", "Let's…", "What if…" mean we're discussing: propose, ask, don't edit.
  "Do X", "Go", "Implement" mean act.
- Before editing, propose a short plan and wait for my go when the change:
  - touches auth, payments, permissions, a shared schema, a migration, infra or CI;
  - deletes or rewrites data, or runs anything against a non-local environment;
  - spans more than 3 files or adds a dependency.
  Otherwise just do it and tell me what you did.
- A plan lists: the decisions I need to make (with your recommendation), the assumptions you are
  making that I haven't confirmed, and the commits you'll make. No narrative. Fits on one screen.
- Plan the what and why. Leave code-level detail for implementation.
- When you've tried the same fix twice, stop and list hypotheses before editing again.

## Comments

Only comment on a non-obvious *why*. Never describe the change, its history, or our conversation.

## Glossary

<!-- Term — meaning — names NOT to use. Update when a synonym creeps in. -->
- 
