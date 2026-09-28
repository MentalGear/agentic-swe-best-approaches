#!/usr/bin/env bash
# PreToolUse hook: blocks file edits while .claude/READONLY exists.
#   touch .claude/READONLY   -> discussion only
#   rm .claude/READONLY      -> edits allowed
# Exit code 2 blocks the tool call and shows stderr to Claude.
if [ -f "${CLAUDE_PROJECT_DIR:-.}/.claude/READONLY" ]; then
  echo "Read-only mode: .claude/READONLY is present. Discuss or plan; don't edit. Ask the user to remove the file to proceed." >&2
  exit 2
fi
exit 0
