---
schema_version: 1
fr_version: 6.0.0rc2
---
# Strict total units for the standalone fixture

## Background

Refs derio-net/super-fr-release-rehearsal-20261026#9.
The standalone project currently has a working CLI and three baseline tests.
This change adds only quantity aggregation, not the independent labels task.
The operator confirmed this contract in the native brainstorm question round.

## Requirements

R1. Add `docs/rehearsal/collected-closeout-1206/project/quantities.py` with `total_units(values)` consuming an iterable of nonnegative Python integers once and returning their sum without coercion; empty input returns 0, generators work and integer size is unbounded.
R2. Reject boolean and non-integer elements with TypeError and negative integer elements with ValueError.
R3. Add unittest discovery tests for empty input, [2, 0, 3], generator consumption, large integers, negatives, both booleans, floats and strings; preserve the baseline CLI and its tests.
R4. Deliver one draft PR referencing issue #9 only, leaving it open for later collected housekeeping; create this task's own acceptance row, initially not-implemented and then unwired after local tests, without modifying existing routing rows.
R5. Use ordinary native fr-goal, independent spec/code reviews and one serial TDD implementation phase; retain all existing workspaces, containers, environments and retention notes, with at most six reviewer/executor children total and no allocation retry.
R6. Run all builds and tests through plain host fr isolation exec in the corrected prebuilt Python 3.14.10 environment with frozen dependencies, UV_NO_BUILD=1, one build/install/download worker and zero HTTP retries. Targeted/TDD/standalone checks have a 15-minute aggregate ceiling; the complete inherited serial pytest suite has a 30-minute ceiling with no automatic rerun on failure or timeout. Unexpected failures or uncertainty stop the run.

## Design

Use a single pass with an integer accumulator. For each element, check for bool
or a non-int before checking negativity, then add it. Do not materialize input,
coerce elements, add dependencies or modify the CLI. Complexity is O(n) element
visits and constant auxiliary element storage (integer arithmetic scales with
operand size). Accept int subclasses other than bool; reject merely int-like
objects that are not Python ints. Iterator exceptions propagate normally.

Tests live in `project/tests/test_quantities.py` alongside
`project/tests/test_fixture_app.py`. Named TestTotalUnits methods cover each
required case and consume a generator to exhaustion. Only the fixture module,
tests and native spec/plan/journal/run/acceptance artifacts are changed.
Tracked profiles, lockfiles, product tooling, Actions and routing resources
remain untouched. No labels-task launch, Ready/merge, gate pass, driver,
collection, closeout, release, install or cleanup is authorized.

Native cursor and usage commands use `/Users/derio/.local/bin/fr` directly on
the host. Never use host uv run; retain the mistaken host .venv untouched.
Forge I/O uses logged-in host gh; no credentials enter the container.

## Verification

strategy: none
gate: closeout-1206-total-units=tester
- closeout-1206-total-units: none — The standalone function is tested directly by unittest discovery and the inherited pytest suite, not installed as fr; Actions are disabled and the operator additionally reruns the standalone suite on merged main before Tester pass.

The acceptance row binds issue #9 and R1–R3. It stays unwired after local
evidence: neither CI nor a live walked status is claimed. Validate native exit
with `fr verification exit --run 2026-10-31-feat-batch-closeout-1206-quantities`;
it must name this row, Tester and issue #9. Stop if gate/Refs validation fails.

Pre-merge standalone command from repository root, through isolation exec:
`uv run --no-project python -m unittest discover -s docs/rehearsal/collected-closeout-1206/project/tests -t docs/rehearsal/collected-closeout-1206/project -v`.
The complete inherited suite is additionally required:
`uv run pytest -q --no-cov -n 0`.
Run it once on the final committed code tree with a host-visible log; reuse
that native phase evidence for deliver only if the native gate accepts it.

## Test Plan

1. Post-merge — operator-driven: rerun the complete standalone unittest
   discovery command above on merged default branch, including baseline CLI
   tests, before recording this batch's Tester pass. This checks integration
   with merged main, which a pre-merge checkout cannot establish. Issue #9
   stays open until the later collected housekeeping PR merges.
