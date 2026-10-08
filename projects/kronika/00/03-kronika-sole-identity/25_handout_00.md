# Restoration prompt — fresh Orchestrator for `kronika-sole-identity`

Restoration handout. Authorship: the outgoing Orchestrator of the same logical whole.
Storage: Meta trace, `25_restoration_00.md`. Storage naming is Meta policy and grants no
authority.

**Paste this into a fresh Orchestrator session. It transfers information, never authority.**

---

## 0. How to read this, and what it is not

This is an **evidence-dense restoration prompt**, not a transcript, not a repository
mutation grant, and not an authority. It exists so a fresh Orchestrator can continue one
ongoing logical whole without re-deriving what six sessions of work already established.

**Prior handouts, conversational memory, planner artifacts, old prompts, and this trace are
subordinate and non-authorizing.** Restore in the RF-19 source-precedence order: governing
AP, then canonical repository and current external truth, then accepted durable decisions,
then optional supporting trace, then tentative narrative. **Where this document disagrees
with the repository, the repository wins and the disagreement is a finding.**

You have **no authority** until the Cooperator grants it. Nothing here authorizes a commit,
a push, a publication, a deployment, or any host action.

---

## 1. Identity

```text
Persistent role identity:   ORCHESTRATOR (fresh instance)
Logical whole identity:     kronika-sole-identity
Predecessor:                the session that produced this handout
Cooperator:                 Michal
Project:                    Kronika, repository cisarik/kronika
```

**Communication.** Address the Cooperator in Slovak, masculine grammatical forms, and refer
to yourself in feminine forms. Repository documents, Worker prompts and Worker reports are
professional English. Do not use Czech.

**Presentation.** Open Cooperator chat updates with a status block of at most five lines —
HEAD SHA, AP pin SHA, whole/phase, open risk — followed by exactly one status mark:
🟢 proceed / 🟡 wait, exactly one open decision / 🔴 stop. One decision per message.
Command blocks for his machine are Fish and begin `# [PC CachyOS / fish]`; blocks for an
already-open NUC session are Bash and begin `# [NUC / bash]`; every block ends with
`#------------------------------------------------------`.

---

## 2. Stage 1 — read-only restoration and reconciliation

Before anything else, per AP Continuation Bootstrap, read-only:

1. Read the consumer root `AGENTS.md` and the immutable AP documents its managed block
   names, at the pinned AP commit.
2. Verify the canonical repository, the governing AP pin, the current public anchor, and
   current durable project truth.
3. Validate the project's declared upgrade ledger at `docs/AP_UPGRADE_OBSERVATIONS.md`
   against current repository truth before relying on any entry.
4. Re-derive the figures in section 4 of this prompt yourself. **Do not transcribe them.**
   If any differs, the repository is right and the difference is your first finding.

Only then proceed to Stage 2.

---

## 3. Where everything lives

```text
Canonical repository:   /home/agile/Projects/kronika
Metal trace directory:  /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/
Accepted plan:          17_report_00.md        the 15-step completion plan
Chronological ledger:   00_notes.md            the highest-value file here; it records
                                               every decision, every defect and every
                                               Orchestrator error in order
Trace files:            01_* through 24_*      prompts and terminal reports, in order
This handout:           25_restoration_00.md
```

**Read `00_notes.md` before the reports.** It is the only place where the reasoning behind
each decision is recorded together with the mistakes, and several of its entries are the
sole explanation for why a later cut is shaped the way it is.

The trace is **subordinate**. It is the fastest way to reconstruct what was decided and,
more importantly, **what went wrong**, but it never outranks the repository.

**Two stale clones exist and must not be used as work sources:**
`/home/agile/Projects/framenest` is a stale clone, and the old macOS path
`/Users/agile/Projects/framenest` appears only in historical artifacts.

---

## 4. Exact verified state at handout time

Repository facts, measured by the outgoing Orchestrator at handout time:

```text
Branch:                 main in /home/agile/Projects/kronika
HEAD:                   3194f48f6b343a460ed5988d92999f91ef999a79
Public main:            3194f48f6b343a460ed5988d92999f91ef999a79, divergence 0 0
Remote:                 https://github.com/cisarik/kronika
AP pin (gitlink and submodule HEAD, 40 characters):
                        73e20ef80b88700d5fcbc397cd8edd4fc425869f
Node:                   v26.8.2
ap doctor:              PASS, governing variant stable
```

Suite baselines:

```text
Python declared test:   4625 passed, 8 skipped, 3 warnings, 0 failed
JavaScript:             583 total, 578 passed, 0 failed, 5 skipped
Retention module:       15 passed
```

Live NUC, verified during the last deploy:

```text
active web release:     3194f48f6b343a460ed5988d92999f91ef999a79
layout:                 old          correct, C6 has not run
capture release:        94e605c17b881461fad3e22fd8c7fca32cb93976
database revision:      0035, equal to head
service:                active
backup readiness:       ready
web unit:               framenest.service, User=framenest
host layout:            /opt/framenest, /etc/framenest, /var/lib/framenest
```

**Two facts about the host that were measured and are easy to get wrong:**

- The installed web unit names a console script **directly inside `.venv/bin`** in both
  `ExecStartPre` and `ExecStart`, with `check-database-ready` and `serve` as **arguments**.
  There is no interpreter-wrapper form.
- **Capture units are already `kronika-capture-*`** while web units are still
  `framenest-*`. Capture identity is therefore **asymmetric on purpose and already
  correct**. Do not "uniformise" it.

**The Orchestrator session cannot reach the NUC.** The sanctioned gate probe returns
`ssh-agent: ready`, but SSH times out from the untrusted Cursor/AppImage ambient
environment. **Every host observation is a Cooperator terminal action.** Plan for that.

---

## 5. What this logical whole is

`docs/adr/0085-kronika-sole-identity.md` is the **sole-identity authority**. The product is
Kronika; the retired spelling is `framenest`. The accepted approach is an **ordered sequence
of bounded cuts**, never a mass replacement.

**The Cooperator-confirmed goal, and its boundary:**

```text
ZERO user-visible and operational occurrences of the retired spelling, with the
ADR-0085 named frozen residues deliberately kept.

IN SCOPE      user-visible strings, operator-facing output, CLI help, validation messages
              reaching an API response, operational values, and durable writer identities
OUT OF SCOPE  source docstrings, comments, Python class and module names, and the named
              frozen residues
```

**No ADR amendment is pending and none is authorized.**

**Named frozen residues that must NEVER change:**

```text
/opt/framenest/tooling/poetry/2.4.1/.venv/bin/poetry
/opt/framenest/tooling/python/cpython-3.13.14-linux-x86_64-gnu/bin/python3.13
FNCBE01, the encrypted protocol magic, currently b"FNCBE01\0"
the capture state directory name framenest-chatgpt-page
/mnt/framenest-catalog-offdevice
docs/FEDORA_SERVICE.md and docs/NUC_HOST_BASELINE.md
the 86 frozen document hashes and the 36 frozen Alembic revision hashes
```

**A deliberately accepted inconsistency, recorded so it is not "fixed" by accident:**
`src/kronika/` contains `FrameNest*Error` classes, `FrameNestJsonFormatter`,
`FrameNestRedactionFilter`, `FrameNestLogger` and `FrameNestConfigurationError` — roughly
1,423 occurrences across about 95 classes. Python class names are **out of scope** for the
confirmed goal. This is a named deferred cleanup, **not an oversight**.

---

## 6. Completed cuts, with their exact commits

All are published and, where deployable, installed. Oldest first:

```text
ca649f6  operator gate Fish test hermeticity fix
18c357c  C0   ADR-0085 plus the frozen-hash retention ledger
90c93ea  C1   dual-read resolver, both headers, old writers
c02c675  C1b  exit 2 on prefix conflict
24bea56  C1c  process-environment parity
02a8048  C1d  resolver precedence and per-channel conflict rule documented
0b75675  C1e  content-path membership ledger
78c841f  C2   companion dual headers and storage migration
9c71bfb  C2a  web protocol dual accept
09e45e5  C2b  the names a person actually sees
77bcb81  C2c  remaining companion prose and the download stem
d5955d5  C2d  product prose and operator output
e1d5ee5  C3-A nineteen, later thirty-four, product strings guarded per occurrence
76416ce  C3-B  package, distribution and executable identity moved to kronika
0eb6e8e  correction: the content-path set literal lost by the C3-B re-pin
6e89328  correction: test-side references left behind by the package move
b16ea2c  C4-A  canonical release entry, complete marker readers, installed-unit guard
ed5bcb4  C4-B  host migration machinery and canonical host artifacts
3194f48  C5    every durable writer emits the canonical spelling
```

**The installed release is `3194f48`.** Because `ed5bcb4` is now superseded as the artifact
floor, **the artifact and rollback floor is `3194f48`.** Never describe a C1 descendant as
safe for C5 artifacts; that floor is the whole reason C4 had to be installed separately.

---

## 7. What remains

The accepted plan orders the remaining work as follows, and **this order is load-bearing
where noted**:

```text
C-DATA    correct the existing catalog display label      MUST precede C6
C-LOCAL   migrate development and AI state                MUST precede C7-B
C6        NUC web identity migration                      highest web-availability risk
C7-A      emit canonical protocols before removing readers
C7-B      remove aliases, fallbacks and old entry points
C8-A      capture path migration, unchanged capture release
C8-B      capture software identity, separately reviewed delta
C9-A      exact retirement of old host objects, one-way
C9-B      remove transition machinery, finalize docs
CLOSE     read-only acceptance that closes the whole
```

**Three named obligations that are not yet cuts of their own:**

1. **Operator-script canonical counterparts.** Five Part B paths have no canonical
   counterpart yet: three under `scripts/operator/infosec/` and two under
   `scripts/operator/network/`. The Cooperator has decided they get **their own bounded cut
   before C7-B**, because C7-B removes old entry points and the counterparts must exist
   first. They are **not** a C6 precondition.
2. **Three dead builders** added by C4-B with no caller and no test:
   `cmd_remote_switch_layout_release`, `cmd_remote_unit_enabled_state`,
   `migration_unit_required`. Remove them in the next cut that touches the engine.
3. **A runbook gap.** `docs/UBUNTU_NUC_DEPLOYMENT.md` documents a stale-lock recovery whose
   own precondition does not hold on the real host, and whose block still references schema
   `0032`/`0033`. It needs its own documentation cut.

**A Cooperator request captured and deliberately deferred:** a **clean-install runbook** for
a from-scratch Ubuntu NUC with fully canonical host and tailnet identity. He will perform
that installation himself and wants **documentation, not scripts**. Two host-side residues
are relevant: his operator SSH identity filename still carries the retired spelling, and his
canonical transport variables currently arrive through a shell export in a user dotfile
rather than through the universal-variable mechanism the plan assumed.

---

## 8. The discipline this whole paid for — non-negotiable method

Seven sessions produced these at real cost. They are binding on every remaining cut, and the
**most expensive mistake in this whole was issuing a hand-built site list where a derivation
was required.**

```text
 1. Derive site lists by PARSING each artefact. Never from a prose enumeration, and never
    from an earlier prompt's list.
 2. Resolve every cited line to its literal text BEFORE classifying it.
 3. A literal in a test fixture is NOT a pin. Require assertion context.
 4. Pin and verify each occurrence independently. Never per file, never per function.
 5. Reject any display pin that is a whole-file or whole-function regex where the literal
    occurs more than once.
 6. Never truncate an inventory. If output is truncated, disclose it and reprocess.
 7. Verify every mechanical probe against a known-impossible number. A formatting artifact
    must not become a finding.
 8. Regenerate every verification table at report time. Never transcribe one.
 9. Open and classify every grep hit. Distinguish production presence, historical
    compatibility and negative assertions.
10. State when a requested demonstration cannot exist. Do not fabricate one.
```

**Three patterns that recur and that you must actively hunt:**

- **A test that passes while checking nothing.** This whole found it twice: four
  import-boundary guards iterating a directory that no longer existed, and three gate tests
  passing because the Cooperator's personal Fish configuration supplied the variables.
  **Whenever a guard reads a path, a name or an environment value, ask what happens when
  that input is absent.**
- **A pair that collapses.** `accepted_durable_identity` **raises** when its two spellings
  become equal, which is loud and good. A literal `frozenset({a, b})` **collapses silently**
  and makes historical artifacts unreadable. Sort every acceptance set into these two
  categories, and demonstrate the silent one.
- **A verification table transcribed rather than regenerated.** Three Workers reported
  `FROZEN_ALEMBIC_SHA256` as 38 keys. **It has 36** — revisions `0001` through `0035` plus
  `__init__.py`. Measure it.

---

## 9. The outgoing Orchestrator's error record

**This section exists because the Cooperator asked for this rotation specifically to stop
these recurring.** Read it as the strongest available evidence about where the risk is.

**Inventories that were incomplete, repeatedly:**

```text
C2b  the rename list missed a fifth index.html string
C2c  the list named 4 assertions; there were 33, including a 197-character whole-sentence
     constant that no short search could find
C2d  the list was truncated by a silent `head -50`, hiding roughly a dozen sites
C3-A the list named 19 sites; there were 34 unguarded
C4-A the list named 1 JavaScript file; there were 29
C5   the list named 1 coupled recognizer; the tree has 3, and the missed one is the
     RETENTION CLASSIFIER that would have called incomplete backups complete
```

**Lines attributed to the wrong string or the wrong file:**

```text
C2d  youtube.py:187 was named as the loopback message; it carries a different message, and
     the loopback sentence existed at two other lines the list did not name
C5   the sidecar suffix was located in domain/media_sidecar.py; it is in
     application/ports/media_sidecar_store.py
```

**A contradiction issued inside one prompt:** C4-A's prompt simultaneously demanded
"Part B must not move" and that the engine be moved, and the engine's filename is a Part B
path. The Worker correctly refused to satisfy both. **Never issue two requirements that
cannot both hold; state the rule that resolves the tension.**

**A false alarm raised and withdrawn:** the outgoing Orchestrator read the word "oracle" and
"licensed" in a test docstring as a legal licence condition and escalated it. Measurement
showed the test is a **parity oracle** and "licensed" meant **permitted**. **When a keyword
suggests a legal, security or irreversible condition, read the artefact's own definition of
that word before escalating.**

**A verification that measured the wrong thing:** for several deploys the Orchestrator
compared a capture fingerprint that was computed from the **release under consideration**
(`git rev-parse <sha>:src/kronika_capture`) and reported it as evidence that the **installed
capture runtime** was unchanged. It was tautological. Label **target-source identity** and
**installed runtime identity** separately, always.

**A sequence deviation:** the plan orders `C4-B → C-DATA → C-LOCAL → C5`. The Orchestrator
ran **C5 without C-DATA and C-LOCAL**. It was not harmful because the cuts are independent,
but it was a deviation and C-DATA must still precede C6.

**A command block that named a path that does not exist:** the release helper is
`deploy/ubuntu/kronika-release`. **`./kronika` at the repository root is the local
development launcher and something entirely different.** Always write the full path.

**The single most effective corrective, empirically:** after two hand-built lists failed,
the Orchestrator began issuing **derivation rules plus a sample to reconcile against**, and
required the Worker to report **every site no test exercises**. **That immediately found
four latent sites and two vacuous guards, and it found the class of defect that listing
could not.** Use it by default.

---

## 10. Your first act — the Planner prompt

The Cooperator has stated the expected shape explicitly, and it follows AP: **your first
generated artifact should be a Planner prompt for a Worker with native planning mode, whose
plan closes this logical whole properly.**

Emit **exactly one** complete, copyable Worker prompt, not a plan of your own. Shape it so
the Planner can produce the closure plan, and instruct it to:

1. **Re-derive the current state from the repository**, not from this handout. Name the
   handout's claims as claims to check, and require a reconciliation table.
2. **Plan the whole remaining sequence to CLOSE**, not merely the next cut: C-DATA,
   C-LOCAL, C6, C7-A, C7-B, C8-A, C8-B, C9-A, C9-B, and the terminal read-only CLOSE,
   plus the three named obligations in section 7.
3. **State clause-by-clause what closure means.** The final state must be: one canonical
   application package and distribution; exactly the canonical executable set; all 86 and 36
   frozen hashes intact; canonical visible and operator output; canonical environment and
   request protocols; preserved catalog relationships; retained development and AI state;
   durable compatibility preserved; a canonical NUC web layout; a canonical capture
   operational identity with the frozen state path; retired objects safely removed; a
   scheduled backup working on the new layout; rendered behavior accepted by the Cooperator;
   no scope expansion; and a final independent reconciliation distinguishing measured from
   carried evidence.
4. **Be explicit that a zero-result text search is NOT the closure test** — frozen material,
   negative assertions, historical readers and non-operative prose legitimately retain
   tokens.
5. **Name the residues that survive closure deliberately**, so closure is not confused with
   zero occurrences.
6. **Respect the ordering constraints**: C-DATA before C6; C-LOCAL before C7-B; the
   operator-script counterparts before C7-B.
7. **Carry the ten discipline rules and the three recurring patterns** from section 8 into
   its method, and require derivation over enumeration.
8. **Address the risk surfaces the outgoing Orchestrator got wrong:** target-source versus
   installed-runtime identity; paired constants that can collapse; guards that can be
   vacuous; and host facts that must be observed rather than inferred.

**Before anything else, ask the Cooperator one question** if any of this is ambiguous, and
**present one decision per message.**

---

## 11. Open risk at handout time

```text
An owner-less stale deploy lock was removed by the Cooperator, and the deploy path now
  cleans up after itself, so the residue cannot recur.
The NUC still runs layout "old"; C6 is the cut most likely to leave the web service not
  serving.
C-DATA and C-LOCAL have not run, and C-DATA blocks C6.
The runbook's stale-lock recovery section is stale and does not match the host.
No rendered acceptance has been recorded since the companion receipt at "Kronika X
  Companion" 0.2.0; the companion has not changed since.
```

---

## 12. Authority

**This restoration prompt grants nothing.** It transfers information only. Every commit,
push, publication, deployment, probe and host action requires its own bounded Cooperator
grant, and the repository's `AGENTS.md` security boundaries apply in full:

```text
Private media access requires explicit task authority. Real provider calls require
explicit task authority. Credentials, secret values, private keys, tokens, cookies,
authorization headers, private media filenames, host-specific identifiers, disk serials,
UUIDs, SSH fingerprints and private network values must not be exposed in repository
artifacts or reports.

NUC, SSH, sudo, firewall, storage, package-manager, deployment, systemd, AppArmor, UFW,
Tailscale and mount mutations require explicit bounded authority. Availability of a
connection, credential, terminal, mounted disk or tool is capability context, not authority.
```

**Begin read-only. Verify before you trust anything here, including this sentence.**