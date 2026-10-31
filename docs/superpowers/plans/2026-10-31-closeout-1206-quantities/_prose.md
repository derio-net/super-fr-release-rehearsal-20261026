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
Commit the code before the full inherited suite and capture its real output
outside the repository in a host-visible log. Run that full suite once at most
30 minutes, no rerun after failure/timeout; return blocked on unexpected failures.
The parent will set the own row unwired with named tests after actual passing
evidence, then independently review and validate Tester/Refs and normal delivery.
Actions remain disabled; post-merge verification is operator-owned, not a phase.
