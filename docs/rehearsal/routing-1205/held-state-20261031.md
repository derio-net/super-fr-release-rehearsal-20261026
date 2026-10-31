# Accepted first Tester-held observation — 2026-10-31

**PASS only for `routing-1205-held-then-walked`: the first held state.**
This is not proof of the later automatic gate transition, completed delivery,
closeout, or discharge of original #1205 / #1195 / #1217. No second acting
pass, gate pass, issue closure or target input is authorized by this record.

## Actual run, not a fresh replay

One exclusive native `fr triage batch drive routing-1205` ran with `--once
--keep-sessions --yes` against `derio-net/super-fr-release-rehearsal-20261026`
and its dedicated private execution queue. It started
**2026-10-31T05:10:00.208701Z**, ended **2026-10-31T05:10:17.873595Z**, exit 0.
The dated CLI walk uses `2026-10-31T05:10:17Z`, the accepted first pass's
completion second, not the later evidence-preparation time.

The actual installed runtime was **6.0.0rc15**, product release/tag commit
`97db8586048da07a4c1a578d234b502efeecbdef`. The independent acceptance checked
all 42 packet hashes and exact correspondence of 362 runtime source files to
that release (zero mismatches). The authentic inherited identity pin stayed
intact. This synthetic fixture's source is not claimed equivalent to RC15;
the evidence-preparation branch starts at fixture main
`face5e98f67432063ad3010c19dbf54f9aa2614c` and uses its own supported CLI in
the `dev` isolation container, without version or runtime changes.

## Retained observations

- Exact native stdout is in `held-receipts-20261031/acting-native.stdout`.
  Only the existing claim heartbeat refresh and `fr:awaiting-live` addition
  occurred. No new issue/PR comment was created; one existing claim comment
  was refreshed (heartbeat `2026-10-31T05:10:11Z`).
- The native ledger retains PR #6 with `verification:live`, `gate:tester`,
  no passed label, and the specific cited row `walked: false` at observation.
  Native Needs you is `needs-tester`. These are retained verbatim JSON receipts,
  not a reconstructed current ledger after recording the row.
- Issue [#3](https://github.com/derio-net/super-fr-release-rehearsal-20261026/issues/3)
  was OPEN with awaiting-live. [PR #6](https://github.com/derio-net/super-fr-release-rehearsal-20261026/pull/6)
  was MERGED at `face5e98f67432063ad3010c19dbf54f9aa2614c`, still Tester-held.
  The packet's post-run forge reads were at 05:10:32.208933–05:10:33.424467Z;
  these are observations after the run, not acting-run timestamps. No new
  forge read or mutation is needed to certify this historical observation.
- Native counts: merged 1, gated 1, closing 0. Dispatch event count 1;
  closeout records 0. Post-run nonacting preview (05:10:17.900810–05:10:28.512350Z)
  exited 0 with no actions. `held-receipts-20261031/observations.json` is an
  explicitly selected/normalized projection of the original packet, not raw
  native output. Source hashes are in `source-sha256.json`.
- Target `ses_e71210cceffeiBPvi1x6z8VEG7` remained idle, attached `--auto`,
  `deliver/running`; its cursor and worktree were unchanged during the pass.
  One of at most three reviewer children had been used. All three manual
  steps remained unticked and incomplete. Recording this one row does not
  complete those steps or the run.

## Independent acceptance and limits

Reviewer `ses_e6fa16643ffewnUs94wY6erI1F` independently accepted only this
first-pass held observation. Its nonblocking permission finding on private
`act-once.py` (0644) was corrected by the coordinator to 0600; content hash
unchanged. The accepted observation is not an independent review of this
evidence branch: that review, push and one draft PR belong to the coordinator.

Warnings about local-only scope state and the unplaced issue are retained as
warnings, not invented prerequisites or authorization for broader work.
The later automatic Tester label swap/comment remains **unproven**. Do not
execute close/unlabel suggestions printed by the acceptance CLI.

Private original packet (local additional evidence, not the sole proof):
`/Users/derio/.cache/fr/coord/artifacts/derio-net-recovery-2026-10-14/release-control-2026-10-24/1205/first-routing-acting-pass-20261031T050853Z`.
Only selected receipts are retained here; no environment values, credentials,
other panes or wholesale private packet dump are included.

## Current permission boundary

See the dated budget addenda in the spec, plan prose and README. Three normal
fixture merges are already used: setup #4, alignment #5, batch #6. The fourth
merge slot is reserved, **not consumed or authorized for merge by this draft**.
Two acting passes remain the cap, one used; this preparation runs none.
No additional allocation beyond the original four used, no fifth allocation,
no extra issue, target input, cleanup, or original gate completion is allowed.
The target's genuine untracked evidence/retention note must remain until a
separate cleanup grant; it prevents known GC loss of the merged workspace.
