<!-- fr:journal-schema=3 -->
# Journal: 2026-10-31-closeout-1206-quantities

<!-- fr:journal kind=discovery scope=spec id=quantities-input created=2026-10-31T12:27:57+00:00 input=true -->
### quantities-input · discovery · Fixture total_units with strict nonnegative integer inputs

Fixture total_units with strict nonnegative integer inputs

Implement project/quantities.py total_units(values) for iterable nonnegative integers: sum, empty 0, generators and large ints; TypeError for booleans/non-integers, ValueError for negatives. Project is docs/rehearsal/collected-closeout-1206/project. Exact real contract and tests are in issue #9 and this batch rationale.

<!-- fr:journal kind=decision scope=spec id=quantities-contract created=2026-10-31T12:27:57+00:00 decided_by=operator -->
### quantities-contract · decision · Operator confirmed design and verification contract

Round 1 question 1 confirmed strict total_units, baseline CLI preservation,
full standalone and inherited suites, strategy none, the own issue-9-bound
row's explicit Tester gate, unwired status with Actions disabled, and one
Refs-only draft PR. No issue closure or Tester answer is authorized.
