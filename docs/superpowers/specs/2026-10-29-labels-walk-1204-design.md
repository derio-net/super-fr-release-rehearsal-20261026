# Disposable labels and downgrade-refusal walk (#1204)

## Goal

Verify original #1195 Test Plan step 1 using shipped tools and a disposable
fixture run/PR. This is a new, unreviewed specification. No historical review,
active cursor, PR or completed walk is claimed by creating it.

## Requirements

R1. This fixture declares candidate verification and the Tester gate. A future
real fixture PR must receive `verification:candidate` and `gate:tester` through
the shipped label-sync path. Manually adding labels is not proof of that path.

R2. After an actual independent spec review is completed and truthfully recorded
for the new active run, requesting `--gate none` with `fr verification set`,
without `--answered-by operator`, must refuse specifically because it lowers the
reviewed exit. Missing run/spec metadata, stale artifacts or failed forge reads
do not satisfy this requirement.

R3. Preserve exact source/runtime, review and run/PR identities, command outputs,
and before/after local and PR state. A successful refusal must leave the spec,
journal, index, tracked files and PR labels unchanged. No gate pass, issue closure
or acceptance-status write is included in this preparation.

## Verification

strategy: candidate
gate: tester

- labels-1204-automatic-pr-labels: live — Only an actual fixture PR proves that the shipped synchronization path applies the required GitHub labels; local fakes cannot establish that result.
- labels-1204-reviewed-downgrade-refusal: live — This walk checks the installed CLI against the genuinely reviewed active run and real fixture PR, including unchanged PR labels after refusal; pre-merge unit tests do not establish those observations.

## Test Plan

1. Obtain actual independent review of this spec and the generated plan. Then
   establish the new active run only through supported commands under a separate
   local action. Record only genuine review results; never copy archived review
   completion. Confirm `fr verification exit --run <actual-run> --json` reports
   candidate verification and the Tester gate.
2. After separate remote authorization and fresh fixture-state reconciliation,
   use a supported shipped PR/label-sync path. Retain the real fixture PR/head
   identity, exact sync operation/result and raw labels. Do not enable workflows,
   dispatch Release, merge, answer gates or launch a driver for this labels walk.
3. With the reviewed active run and real PR in place, run:
   `fr verification set --run <actual-run> --gate none --reason "1204: verify post-review downgrade refusal"`.
   Omit `--answered-by operator`. Require exit 2 with the specific post-review
   lowering refusal and verify the unchanged state from R3. Preserve failures;
   do not repair metadata or retry a write merely to obtain the expected result.
4. Leave #1204 and original gates/statuses owed until evidence is accepted and a
   separate evidence-recording action is authorized.

## Boundaries

This local preparation authorizes no model/session launch, forge request,
credential use, push, PR, merge, release, driver or recovery operation. The
logical target `derio-net/super-fr-release-rehearsal-20261026` is not a claim that
this independent clone matches the stopped remote fixture's current state.
Origin remains local. J and the six real paused batches are untouched.

## Implementation Plans

| Plan | Repo | File | Depends on |
|------|------|------|------------|
| 2026-10-29-labels-walk-1204 | `derio-net/super-fr-release-rehearsal-20261026` | `2026-10-29-labels-walk-1204` | — |
