# Local evidence-preparation verification — 2026-10-31

This verifies bookkeeping, not another live acting pass or a gate transition.
All execution below used host `fr isolation exec --branch
docs/routing-1205-held-evidence -- ...`, profile `dev`, running container.
Git inspection/commits used the host. No identity bypass or migration was used.

- Before: `uv run fr acceptance check` exited 0, 550 rows; walk-owed 22,
  walked 28. `set-status --help` confirmed all dated-walk options.
- Once only: `uv run fr acceptance set-status --id
  routing-1205-held-then-walked --status walked --notes <first-hold-only reason>
  --walk docs/rehearsal/routing-1205/held-state-20261031.md --harness opencode
  --model openai/gpt-6.1-sol --strategy live --walk-outcome pass
  --walk-at 2026-10-31T05:10:17Z` exited 0 and changed the row/reports.
  Its automatic commit failed because the container had no Git author identity.
  The exact generated files were committed with the existing host identity;
  the status command was not rerun. Printed issue-close/unlabel suggestions
  were NOT executed.
- After: `uv run fr acceptance check` exited 0, 550 rows; walk-owed 21,
  walked 29. Existing unrelated acceptance-debt warnings remain.
- `uv run fr acceptance report --check` exited 0: all three committed reports
  in sync. Host `git diff --check` passed.
- In-container Python compared parsed matrix rows with fixture base
  `face5e98f67432063ad3010c19dbf54f9aa2614c`: exactly this one row changed;
  all other 549 rows identical, no additions/deletions. Its one walk exactly
  matches the harness/model/strategy/outcome/evidence/timestamp above.
- SHA-256 checks of all three verbatim selected receipts match the original
  packet manifest. Projection checks confirm zero closeout records, no
  post-run native actions and no second acting pass.
- Run YAML, manual phase `01.yaml` and plan `_meta.yaml` remain byte-identical
  to fixture base. No phase ticks, completion or cursor writes occurred.
- Host target inspection still shows HEAD
  `e4b65108ed5c7449425f3cc27c0b07095790dcab`, no tracked differences and only
  the authorized untracked
  `docs/rehearsal/routing-1205/coordinator-held-evidence-retention.md`.
  That file was verified untracked before isolation `up`; it remains in the
  living target worktree. No target input/focus/restart/resume was sent.

No product source, version, journal finding, new acceptance row, forge state
or target history was changed. No new full suite or test machine was required
for this evidence-only change. Independent evidence-branch review has NOT
yet occurred; coordinator owns that review, push and one draft PR. No merge,
cleanup or reserved fourth-slot consumption occurred.
