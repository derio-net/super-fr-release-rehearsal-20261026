# Quantities implementation plan

One independently reviewable ask, one standard-tier agentic phase. Link the own
closeout-1206-total-units acceptance row; no member issue tracking_issue.
The spec is the contract. Keep all preexisting rows and protected resources.

Use TDD and the corrected container environment only, via plain host
/Users/derio/.local/bin/fr isolation exec. Never HOST uv run or install.
Native host cursor commands use /Users/derio/.local/bin/fr directly.
All external dependencies stay frozen and wheel-only with Python 3.14.10,
UV_NO_BUILD=1, single workers and zero HTTP retries. No other build worker.
No allocation retry; cap six total children, including spec and code reviewers.
No cleanup, labels task, Ready/merge, gate answer, driver or closeout.

Run the full standalone discovery command in the spec for red and green.
The inherited suite already failed (commit 1fca788, exit=2; 1 failed, 595 passed,
4 skipped, 46 errors, interrupted after 21m40s). Preserve it and its raw log;
do not repair, retry or call it a passing baseline. The operator-approved
scope revision in the spec journal now defines the complete standalone project
as the application boundary. Add only project/pytest.ini with [pytest] and
testpaths = tests. Host-commit final code/config before the same executor runs
the complete application pytest command in the revised spec exactly once,
at most two minutes within remaining aggregate budget, with a fresh external
host-visible log. Stop on failure/timeout/load or native evidence refusal.
The parent will set the own row unwired with named tests after actual passing
evidence, then independently review and validate Tester/Refs and normal delivery.
Actions remain disabled; post-merge verification is operator-owned, not a phase.
