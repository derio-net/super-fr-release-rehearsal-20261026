# Collected closeout rehearsal: setup draft

This draft prepares two **future** genuine batches in
`derio-net/super-fr-release-rehearsal-20261026` (repository ID `1434822196`).
The setup base is `a1631551d7605503a2c010db88499eecce6ad9dd`.
It proves neither batch execution nor super-fr issue #1206. There are no new
issue numbers, batch judgements, run cursors, walked rows, or gate passes here.

## Current permission boundary

Only local setup, scoped baseline checks, independent setup review, and at most
one **draft setup PR** are authorized. The coordinator owns the review, push,
and draft PR. The draft requires review and a separate merge grant. This agent
does not push or open it.

No issue creation, model allocation, driver pass, CI enablement, merge,
collected closeout, original gate change, or cleanup is authorized. Keep Actions
disabled. Leave `.fr/triage.yaml`, `.devcontainer/fr-profiles.yaml`, workflow
manifests, hooks, installer, release metadata, and existing acceptance rows
unchanged. In particular retain `post_merge: []`, `post_merge_restart: none`,
`export: null`, `mirrors: []`, and declared `ci.type: none`.

## Isolation from routing

Use a new primary clone and a separate, initially **empty** triage state
directory. Do not copy the old facts, judgements, durable state configuration,
claims, collected markers, or driver lock. An empty directory is intentional:
native collection and real issue bindings wait for the execution grant.

Keep routing issue #3 open and preserve its claim, session and reviewer child,
live `deliver: running` cursor, unticked manual plan, worktree, and genuine
untracked retention note. Never select `routing-1205`. PRs #1/#2, routing PR #6,
and setup/evidence PRs are not the new batches. J and the six paused queues are
outside this rehearsal.

Before any future `fr isolation up`, verify that the old target's genuine
retention note is still present; `up` can trigger automatic isolation GC. Do not
add a substitute marker, remove the note, or change the old target.

Source reason: `archive_plan_dir()` calls `_archive_run()` and then
`archive_run_cursor()` in `packages/fr/src/fr/archive.py`. Archiving the old
plan also moves its owning run file, even if its cursor still says running.
Truthful manual-step recording would not preserve the canonical live owner.
Only the two new, actually finished runs may be archived in a later grant.

## Two independent future tasks

The following are draft names, **not existing native batch IDs or issues**:

| Proposed batch ID | Real task | Required new tests |
|---|---|---|
| `closeout-1206-quantities` | Add `project/quantities.py`: `total_units(values)` consumes an iterable of nonnegative integers and returns their sum. Reject booleans and non-integers with `TypeError`; negatives with `ValueError`. | Empty iterable gives 0; `[2, 0, 3]` gives 5; generator and large integers work; negative, boolean, float and string elements are rejected. |
| `closeout-1206-labels` | Add `project/labels.py`: `display_label(text)` accepts a string, collapses all whitespace runs to one ASCII space, and preserves case, Unicode characters and punctuation. Reject non-strings with `TypeError`. | Empty/whitespace-only gives empty; tabs/newlines and outer whitespace collapse; already-normal text, Unicode, case and punctuation survive; `None`, numbers and bytes are rejected. |

Paths above are relative to this runbook's directory. The functions, modules,
and their tests are deliberately **not implemented by setup**. Neither task
depends on the other. Do not seed failing/skipped tests for missing modules.
The baseline is a small working CLI that prints its name or version, with
three real tests, no external dependencies, and no installed command shim.

Each future batch gets one real issue, one ordinary shipped `fr-goal` run, a
spec and CLI-created acceptance row bound to that issue, a small agentic plan,
independent native reviews, actual tests, and one batch PR using `Refs` that
issue (not `Closes`). Resolve deliver through the normal evidence gates; do
not retain the earlier routing rehearsal's deliberate incomplete handoff.
Do not invent a workflow shape, set a fake done state, or bypass provenance.

## Verification contract and suite scope

From the repository root, this is the **complete standalone fixture suite**:

```sh
uv run --no-project python -m unittest discover -s docs/rehearsal/collected-closeout-1206/project/tests -t docs/rehearsal/collected-closeout-1206/project -v
```

Run it through plain host `fr isolation exec --branch <owned-branch> -- ...`.
The three baseline tests are not the inherited super-fr suite. Future task
tests must join this same discovery tree, and every task runs the whole tree.
`--no-project` runs this dependency-free application without resolving the
inherited workspace; it is not used for the inherited suite or native `fr`.

The ordinary shipped `fr-goal` manifest requires full-suite delivery evidence.
There is no `--test-command` or fixture-suite substitution in this proposal.
**A future full-run grant must additionally authorize the full inherited
Python suite**, run serially inside each new batch's isolation:

```sh
uv run pytest -q --no-cov -n 0
```

That command names the entire inherited pytest suite, not just the fixture.
It can be expensive. Run one build/test process at a time, with an explicit
operator-agreed time/CPU limit; stop rather than fall back to a targeted run
or fabricate passing evidence. No inherited full suite runs during setup.
No plugin/Bun coverage is claimed by a Python run; retain any additional
checks required by the normal workflow or changed paths.

Setup's required `uv run fr acceptance status --brief` did not complete:
workspace dependency setup selected Python 3.15 and started a native dependency
compile. The timed-out setup process and its compiler children were cancelled
to bound load. No acceptance-status pass, inherited suite, lint or native
exit-validation result is claimed. Resolve that dependency/resource preflight
under appropriate permission **before allocating the future batches**; do not
use an identity override, host install or credential detour. The standalone
suite's result does not resolve this blocker.

For each future spec, explicitly choose `strategy: none` for this standalone
application, which is tested directly rather than installed as the `fr` tool.
This is the shipped supported `none` strategy, not a replacement manifest or
an exemption from tests. Also declare `gate: <actual-row-id>=tester` for its
own row: the operator must re-run the fixture suite on the merged default
branch before recording that batch's Tester pass. Explain this additional
post-merge integration check in the spec. Validate the resulting exit with
`fr verification exit --run <actual-run-id>`; it must name the intended row,
Tester gate and issue only. Stop if normal native validation disagrees.

Create the future row with `fr acceptance add` only after a real issue and spec
exist; use `--issue owner/repo#N`, `--verify none`, actual origin and test-name
refs. Use `not-implemented` before implementation and `unwired` once tested
but not run by CI. Actions being disabled is not `ci` or `walked` evidence.
Use the supported CLI for status/report changes; never hand-edit matrix YAML.
No spec with a Test Plan or new acceptance row is created by setup, so no
unbound issue refs or preclaimed outcomes enter the matrix.

After both batch PRs merge and the real post-merge checks pass, the proposed
operator route is `fr gate pass --repo <fixture> --pr <actual-batch-pr> --gate
tester --notes <actual-evidence>`, preview first and `--yes` only under a grant.
This native route comments and swaps the merged PR's labels without an extra
evidence PR. It does not mark an unwalked row walked. Do not dispatch the
release command it prints. Reconfirm the two new gates are actually passed.

## Future ceilings: proposed, not granted

- Exactly two new issues; no reuse of issue #3 or PRs #1/#2.
- Three parent allocations: two batch parents and one collected parent.
- At most six children per batch and two for closeout: fourteen total.
  These are ceilings, not proof that every review fits. Stop at the cap.
- Harness `opencode`, model `openai/gpt-6.1-sol`, autonomous `--auto`,
  no-focus launch. The shipped runner supplies `--auto` in
  `fr_herdr/opencode.py` and `--no-focus` in `fr_herdr/runner.py`; do not invent
  those flags on `fr triage batch dispatch` or start sessions by hand.
- No allocation retries, replacement sessions, unattended loops, timers or
  watchers. A failed/uncertain allocation stops for human disposition.
- At most four PRs **including setup**: setup, two batch PRs, one housekeeping
  PR. At most four corresponding merges, each requiring its stage's grant.
  An extra evidence/fix PR needs a new grant; do not repurpose an old PR.
- At most ten one-shot acting driver passes; direct batch dispatch/merge and
  the two native gate passes are separate named future effects, not hidden
  inside that pass budget. No general driver/forge-write permission is implied.
- Only new-batch native archive moves, and native scratch snapshot/worktree
  creation/removal needed for closeout, may be included in the future grant.
  No cleanup of old or finished session/worktree resources.

## Stage boundaries and previews

1. **Setup:** independent review of this local head, at most one draft setup
   PR, then a separate approval to merge it. If base/head or policy changed,
   stop and reconcile with the coordinator; never reset user work.
2. **Full-run grant:** approve the exact two real issue texts/numbers, task
   scope, model/child limits, native dispatch/claim writes, full inherited
   suite resource limit, two batch PRs/reviews/merges, two real post-merge
   Tester checks/pass writes, separate state and scratch effects. Native
   batch creation must populate only these two judgements. Collection may
   show old issue #3 as unplaced facts; never judge, claim or select it.
3. **Collection:** no acting driver until both new batches are landed and
   ungated. Prefer explicit native batch dispatch/merge and gate-pass routes
   during preparation. If a second-only preparation pass is necessary, it
   needs its own preview/grant and must stop before any collection. Do not
   start a driver merely because the first batch is ready.
4. **Housekeeping:** accept a fresh preview naming both new IDs in ONE
   collection. Let the one native collected session open ONE housekeeping PR.
   Before ready/merge, review its recorded head, exactly two members, truthful
   missing spec outcomes, permitted archive-only diff, one recorded commit,
   and exactly the two new issue closures. Confirm checks/mergeability and
   `review_reasons()` are clean. Preview and separately permit native
   ready/merge and subsequent merged-state recording. Stop on conflicts,
   handback, extra children/actions, stale evidence, or cap exhaustion.

The following are **future preview recipes**, not setup commands. Bind `REPO`
to the fixture above, `STATE` to the new dedicated directory, `CHECKOUT` to the
new clone, and `BATCH_A`/`BATCH_B` to the two real native IDs after approval.
Run forge-facing native commands on the host using logged-in user auth; do
not copy credentials into a container. Native run/usage cursor commands also
belong on the host. Builds/tests stay behind the isolation exec bridge.

```sh
fr triage batch list --repo "$REPO" --dir "$STATE"
fr triage batch drive "$BATCH_A" "$BATCH_B" --repo "$REPO" --dir "$STATE" --checkout "$REPO=$CHECKOUT" --once --keep-sessions
fr triage batch closeout "$BATCH_A" "$BATCH_B" --repo "$REPO" --dir "$STATE" --checkout "$CHECKOUT"
```

No `--yes` means no intended acting pass, but these are **not strictly
effect-free**: state sync/collection, fetch and temporary snapshots can write
locally. Require the stage grant before running them. Do not run previews
against the old state. Driver `--once` bounds a **pass**, not its action count;
`--keep-sessions` prevents finished-session closure, not other actions. There
is no closeout-only action-filter flag. Reject a preview containing unrelated
dispatch, batch merge, closeout, restart, export, mirror or cleanup actions.

For the eventual host one-shot dispatching pass, `--single-pass` is supported
with `--once --yes`; it is not a new persistent driver. An acting command is
allowed only after the matching preview and stage permission, never from
copying this document's future ceiling list.

Membership is filtered to named owed batches by
`commands/triage_batch_cmd.py:batch_closeout_command`; driver collection
respects selected batches in `triage/batch_drive.py`. Already-existing
collected markers are processed across the loaded state's snapshot, so the
separate state must contain none inherited from routing. Native
`batch_closeout.recorded_closes()` takes included members' passed-gate row
issues only, within this repository and excluding narrowing decisions. Check
the actual anchor/body; do not assume a PR body marker alone proves membership.

Keep all new `Refs` issues open until that genuine housekeeping PR merges.
Never close issue #3 or either new issue directly. Original #1206 proof
acceptance/journal/matrix/gate changes, any product PR, #1207, release/install,
and all cleanup require separate grants after the actual rehearsal evidence.
