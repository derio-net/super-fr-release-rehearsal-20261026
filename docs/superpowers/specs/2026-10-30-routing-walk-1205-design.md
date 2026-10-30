# Disposable Tester routing walk (#1205)

## Goal

Exercise original #1195 Test Plan step 2 on this disposable repository only.
Setup is not a routing PASS, dispatch record, active run or gate pass. The
synthetic rehearsal tree is not product/release-source-equivalence evidence;
the installed RC11 runtime is verified separately.

## Requirements

R1. One genuinely dispatched triage batch opens a new PR after dispatch.
After its reviewed normal merge, the held batch appears under Needs you ·
Tester and stays out of close-out. Disposable
https://github.com/derio-net/super-fr-release-rehearsal-20261026/issues/3
remains open with `fr:awaiting-live`. This pre-transition observation alone
is the linked row's acceptance. After that evidence is genuine and accepted
and the row's dated walk is merged, the second bounded acting pass
automatically replaces only the fixture `gate:tester` with
`gate:tester-passed`. That later transition is a separate overall routing
Test Plan outcome, recorded only after it actually occurs; it is not part
of the row certified before the second pass. Labels alone do not prove routing.

R2. At most three reviewed fixture PRs/normal merges (setup, batch, evidence),
one issue, one real batch, one OpenCode session (`openai/gpt-6.1-sol`, `--auto`)
and two acting passes in a new queue. No subagents, extra target attempts,
close-out, installer/restart/export hooks, release, protection overrides,
original gate pass, real queue, J or six-batch action.

## Verification

strategy: live
gate: tester

- routing-1205-held-then-walked: live — Only the real first driver pass over a genuinely dispatched, merged batch can prove the pre-transition Tester-held/open-awaiting-live/no-closeout observation. This row has the run's live kind and inherits its Tester gate, without a separate row gate. The later automatic transition is a separate overall Test Plan outcome, not this row's acceptance.

## Test Plan

1. Independently review setup. Verify `ci: none`, empty `post_merge`, restart
   `none`, export `null`, no mirror/version hooks and unchanged GitHub
   protection/workflow settings. Merge normally only after review.
2. In the dedicated execution queue, collect real facts, judge issue #3,
   create batch `routing-1205` and dispatch one session through the shipped
   runner. Retain actual item/session/branch identity, explicit model and
   `--auto`. Never manufacture facts, dispatches, cursors or operator answers.
3. Reuse this reviewed spec/plan with supported real-run lifecycle commands.
   Open one new batch PR after dispatch, with `Refs` issue #3 (never a closing
   keyword), real run artifacts and one bounded observation note. Preserve
   existing draft PR #2 and Dependabot PR #1. No new product work.
4. After reviewed normal batch merge, preview the first specific-batch pass.
   Permit only that batch's claim upkeep, awaiting-live label and held-state
   board output. Run it once; retain the real Tester lane, open issue with
   awaiting-live, and no close-out. Unexpected actions stop the test.
5. After genuine held-state evidence is accepted, record only this
   pre-transition row's dated live walk via `fr acceptance set-status`;
   independently review and merge the third fixture PR. Its evidence must
   not claim that the later automatic transition has already happened.
6. Preview the second specific-batch pass. Permit claim upkeep, automatic
   fixture Tester pass and board refresh only. Run once; require the actual
   gate-pass comment and label swap before recording the overall routing
   outcome. Retain that later proof separately for coordinator acceptance;
   no fourth fixture PR is authorized. Stop before any later close-out. Do not
   close issue #3 or original #1205, or pass original #1195/#1217 gates.

## Failure boundaries

Read current `herdr --skill`; use only a new owned no-focus target. Partial,
failed or ambiguous allocation/submission stops the single attempt without
retry, repair or model/provider substitution. Coordinator handles actual
questions and independent reviews. If the shipped workflow requires extra
AI sessions, stop rather than expanding the one-session cap. Exact sequence:
`docs/rehearsal/routing-1205/README.md`.

## Implementation Plans

| Plan | Repo | File | Depends on |
|------|------|------|------------|
| 2026-10-30-routing-walk-1205 | `derio-net/super-fr-release-rehearsal-20261026` | `2026-10-30-routing-walk-1205` | — |
