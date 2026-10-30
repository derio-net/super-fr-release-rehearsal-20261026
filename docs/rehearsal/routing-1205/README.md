# Bounded routing fixture: execution brief

Setup only; no routing PASS, batch dispatch or run completion is claimed.
Actual member issue: https://github.com/derio-net/super-fr-release-rehearsal-20261026/issues/3.
Original https://github.com/derio-net/super-fr/issues/1205 remains owed.

## Identity and bounds

- Repo `derio-net/super-fr-release-rehearsal-20261026`, ID `1434822196`;
  rehearsal base `1325f612635dcbd17c9ccfdd25be721f9be00038`.
- Runtime `fr 6.0.0rc11`, product pin
  `cc133a53b3ed6dcaa8f6e6d64e2bb8b04c6c53b8`: 336 fr and 10 fr-herdr files
  verified separately. No fixture/product-source equivalence claim.
- The inherited matrix keeps its `repo: super-fr` reference namespace; the
  new origin uses that namespace to cite the local routing spec. The actual
  routing issue, forge target and plan target are the rehearsal repository.
- Preserve genuine RC7 harness pin; activate RC11 venv and PATH through
  isolation exec, with no bypasses, installs or global changes.
- One batch `routing-1205`, expected branch `feat/batch-routing-1205`;
  actual item/session identity comes from the runner, never a predicted ID.
- At most setup, batch and evidence PRs; each needs coordinator independent
  review before normal merge. One actual session, two acting driver passes.
  No reviewer/subagent launch by this author or the target.
- Keep PRs #1 and #2 unchanged. No release, close-out, original gate pass,
  original queue, J or six-batch operations.

## Sequence after setup review and merge

1. Refresh the independent rehearsal clone's main and verify the merged
   default config: `ci: none`, `post_merge: []`, restart `none`, export
   `null`, mirrors `[]`, no version block. GitHub protections, disabled
   Actions and disabled static workflows stay unchanged. No fake `ci-ok`.
   Dispatch needs a clean primary clone actually on rehearsal main: the
   historical `local-fixture` primary still has its product-based local main.
   Preserve it and its existing worktrees. Use a fresh disposable primary
   clone of the rehearsal repository for `$C`, not a reset/rebase of that
   historical primary and not the setup worktree as a substitute primary.
2. Use a NEW private execution queue outside Git clones. Collect real facts
   via a non-acting drive preview; write only the genuine issue #3 judgement
   permitted by fr-triage. Never author facts, batch events or stages. The
   judgement's detail must name this spec/plan and these exact bounds.
3. With `$R` this repo, `$Q` that queue and `$C` the independent clone:

```sh
fr triage batch create routing-1205 --repo "$R" --dir "$Q" \
  --title 'Disposable Tester routing walk #1205' \
  --issue 'super-fr-release-rehearsal-20261026#3' \
  --runner herdr --harness opencode --model openai/gpt-6.1-sol \
  --rationale 'Reuse the committed routing-1205 spec/plan only; one session, no subagents; new batch PR with Refs issue #3, never Closes; stop on conflicting workflow requirements.'
fr triage batch dispatch routing-1205 --repo "$R" --dir "$Q" \
  --checkout "$C" --to herdr
```

Inspect the generated brief BEFORE adding `--yes` once to dispatch. Its
normal `/fr-goal` entrypoint and default closing-keyword instruction do not
authorize an extra feature pipeline, extra session or closing issue #3.
The reviewed post-merge live-row/Refs contract must be honored; otherwise
stop before launch. Real questions go to the coordinator, not inferred
answers. Record the existing spec/plan through supported real-run commands;
never hand-author a run or copy a review result into an unreviewed unit.

Read current `herdr --skill` first; the caller must actually be in Herdr.
Do NOT run an extra `herdr agent start`: shipped dispatch creates the one
session with explicit model and attaches `--session <actual-id> --auto`.
Keep readiness/identity checks and `--no-focus`; a partial/unknown allocation
or submission stops without retry, repair or provider/model rerouting.

4. The actual target opens the new batch PR AFTER dispatch with its genuine
   run artifacts and one small observation note, not a routing PASS. Stop for
   coordinator review, real questions as needed, and normal merge. No PR #2
   adoption, branch rename, superseding PR or forged dispatch metadata.
5. Preview the first pass against the already-merged, Tester-held batch:

```sh
fr triage batch drive routing-1205 --once --repo "$R" --dir "$Q" \
  --checkout "$R=$C" --keep-sessions
```

Act once with `--yes` ONLY if the plan contains that batch's claim upkeep,
awaiting-live and held board output. Retain actual Tester lane, open issue
with awaiting-live and no close-out. Any dispatch, merge, recovery, restart,
installer, export, close-out or unrelated action is a hard stop.

6. After the held observation is genuine and accepted, record the linked
   row's dated live walk via shipped CLI, with actual model/harness/evidence.
   Independently review and normally merge the THIRD fixture PR. Do not
   close issue #3 because a CLI prints a close suggestion.
7. Preview the same command again. The second and last `--yes` pass may
   maintain claims, automatically pass only this fixture Tester gate and
   refresh its board. Retain the actual gate-pass comment and label swap;
   stop immediately after the pass, before any later close-out. No loop,
   `--single-pass`, manual gate pass or session cleanup is authorized.

Scope-local facts/board/lease metadata is allowed; publishing commands are
not. The new queue must contain no publish hook or product/org state. Both
the row and run use `live`, so the row inherits Tester; its `issues` names
actual issue #3. Every step and acceptance status remains pending at setup.
