# #1205 disposable routing deployment plan

One manual phase covers actual runner deployment and forge observations;
all steps remain pending during setup. No product implementation, full test
suite, additional model session or new feature pipeline is added. Original
step-1 artifacts are historical context, not a triage dispatch.

Follow docs/rehearsal/routing-1205/README.md. Use actual issue #3, batch
routing-1205, the committed routing spec and the one linked live row. Only
the coordinator obtains independent review and actual operator answers.
At most setup, batch and evidence PRs may merge under the approved bounds.

## Current target execution clarification

The paragraphs above describe the original setup bounds. For the current
target, spec R2–R4 and the target-local operator confirmation govern: one
OpenCode target may dispatch at most three genuine read-only
`fr-spec-reviewer` children after the required review unit opens. Those
children may not delegate. No implementation worker or further delegation
is allowed. The target must obtain its own answered question and actual
reviewer dispatch/return witnesses; coordinator answers or reviews cannot
substitute. Coordinator independent review before normal merge is separate.

Reuse this existing manual-only plan under the installed released RC15
runtime and unchanged inherited identity pin. Stop at `deliver/running` or
an earlier unmet lifecycle gate, with no full suite or done delivery claim.
The CLI may complete only the empty agentic group. All manual steps remain
unticked and incomplete, all live observations and the row remain owed,
and the coordinator alone owns the two future bounded acting passes.
Historical setup evidence is not rewritten by this scoped clarification.
