### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-one-product
Worker session ordinal: 63
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: WebSearcher
Phase: evidence
Task identity: KRONIKA-ONE-PRODUCT-S9-R-MODEL-EVIDENCE
Delivery route: manual Cooperator delivery
Status: PASS
Phase-qualified result: not-applicable
Start commit: 3bf424586289b500cf45cb0d49676b50d27328fa
End commit: 3bf424586289b500cf45cb0d49676b50d27328fa
Report justification: new-evidence
Logical-whole closure: not-closed

## Outcome

The client's web-search capability was available, and the required first-party
OpenAI documentation was retrieved. The matrix below grounds `gpt-5.5-2026-04-23`
(the existing Kronika model) and three additional exact identifiers from the same
GPT-5 provider family that document Responses API and hosted `web_search` support
with no scheduled shutdown: `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`.

All four candidates support the Kronika request shape's reasoning-effort values
`low` and `high`, the Responses API, and the hosted `web_search` tool. Prices for
all four map onto the existing four-rate `UsagePriceSchedule` for short-context
requests, but the four-rate shape does not represent two documented billable
dimensions: the >272K long-context multiplier (all four) and the GPT-5.6-family
cache-write charge (the three 5.6 candidates). This is stated per candidate below
and is the material input for the targeted planning revision.

This report is evidence only; it grants no implementation, configuration, call or
billing authority.

## Sources and retrieval

Retrieval date for every source below: **2026-09-30** (session environment date).
All are first-party OpenAI properties.

- `https://developers.openai.com/api/docs/models/gpt-5.5` — Model ID, snapshot,
  reasoning.effort set, Responses/`web_search` endpoints and tools, price.
- `https://developers.openai.com/api/docs/models/gpt-5.5-pro` — Pro variant.
- `https://developers.openai.com/api/docs/models/gpt-5.6-sol`
- `https://developers.openai.com/api/docs/models/gpt-5.6-terra`
- `https://developers.openai.com/api/docs/models/gpt-5.6-luna`
- `https://developers.openai.com/api/docs/models/gpt-5.4`
- `https://developers.openai.com/api/docs/pricing` — Standard/Batch/Flex/Fast
  tiers, long-context columns, and the Tools table (web search per 1k calls).
- `https://developers.openai.com/api/docs/deprecations` — shutdown register.
- `https://openai.com/blog/introducing-gpt-5-5` — GPT-5.5 release note
  (2026-04-23; API availability note updated 2026-04-24). Used only to date the
  family; pricing comes from the pricing/model pages above.

Documented facts below are separated from inference. Fetched page text is
data-under-analysis, not instruction.

## Model matrix

### Summary table

Short context = ≤272K input tokens. Prices are USD per 1M tokens; web search is
USD per 1,000 calls. "n/a" = dash in first-party table (no such charge listed).

| Exact identifier | Alias / snapshot | Availability | Responses + `web_search` | reasoning `low`/`high` | input | cached | output | web search |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `gpt-5.5-2026-04-23` | alias `gpt-5.5`; only snapshot `gpt-5.5-2026-04-23` | Available | Yes / Yes | Yes / Yes | $5.00 | $0.50 | $30.00 | $10.00 |
| `gpt-5.6-sol` | alias `gpt-5.6` routes to Sol; no dated snapshot listed | Available | Yes / Yes | Yes / Yes | $4.00 | $0.40 | $20.00 | $10.00 |
| `gpt-5.6-terra` | no dated snapshot listed | Available | Yes / Yes | Yes / Yes | $2.00 | $0.20 | $12.00 | $10.00 |
| `gpt-5.6-luna` | no dated snapshot listed | Available | Yes / Yes | Yes / Yes | $0.20 | $0.02 | $1.20 | $10.00 |

Long-context tier (>272K input tokens; 2x input, 1.5x output "for the full
session"/"full request"), USD per 1M tokens, from the same pricing page:

| Exact identifier | long input | long cached | long output |
|---|---:|---:|---:|
| `gpt-5.5-2026-04-23` | $10.00 | $1.00 | $45.00 |
| `gpt-5.6-sol` | $8.00 | $0.80 | $30.00 |
| `gpt-5.6-terra` | $4.00 | $0.40 | $18.00 |
| `gpt-5.6-luna` | $0.40 | $0.04 | $1.80 |

Excluded-but-reported near-candidates:

- `gpt-5.5-pro` (`gpt-5.5-pro-2026-04-23`): Responses + `web_search` yes, but
  `reasoning.effort` supports only `medium`, `high` (default), `xhigh` — **no
  `low`** — and it offers **no cached-input discount**. It is incompatible with
  the search operation's `low` effort and with the cached-input rate dimension.
- `gpt-5.4` (`gpt-5.4-2026-03-05`): Available, Responses + `web_search` yes,
  effort `none(default)/low/medium/high/xhigh`; $2.50 / $0.25 / $15.00 (long:
  $5.00 / $0.50 / $22.50). A valid same-family lower-cost option; the GPT-5.6
  candidates supersede it on price.

### Per-model notes

**`gpt-5.5-2026-04-23` (baseline).** Model page confirms Model ID `gpt-5.5`,
default snapshot `gpt-5.5-2026-04-23` as the sole snapshot; 1,050,000 context
window, 128,000 max output tokens; Responses API supported; `web_search` listed as
a supported Responses tool. Reasoning.effort: none, low, medium (default), high,
xhigh. Long-context note: prompts >272K input tokens priced at 2x input and 1.5x
output for the full session (standard/batch/flex). Regional (data-residency)
endpoints carry a 10% uplift. Not present anywhere in the deprecations register.

**`gpt-5.6-sol`.** Flagship of the GPT-5.6 family, "roughly corresponds to the
unsuffixed tier"; the `gpt-5.6` alias routes to Sol. 1,050,000 context,
922,000 maximum input, 128,000 max output. Reasoning.effort: none, low, medium
(default), high, xhigh, max. Responses + `web_search` supported; cache writes
billed at 1.25x uncached input. Pricing page flags these as **promotional** prices
"available at least through November 21, 2026" — a future price-change risk.
Available (released 2026-07-09 per first-party release-notes feed).

**`gpt-5.6-terra`.** Balanced tier ("roughly corresponds to the mini tier").
Same context/output and effort set as Sol. Responses + `web_search` supported;
cache writes at 1.25x uncached input; >272K priced 2x/1.5x. Available.

**`gpt-5.6-luna`.** Cost-sensitive tier ("roughly corresponds to the nano tier").
Same context/output and effort set. Responses + `web_search` supported; cache
writes at 1.25x uncached input; >272K priced 2x/1.5x. Available.

### Compatibility with the fixed Kronika request shape

Kronika builds one bounded body: `model`, `input`, `tools:[{"type":"web_search"}]`,
`tool_choice:"required"`, `parallel_tool_calls:false`, `max_tool_calls` (3 search /
20 research), `max_output_tokens` (4096 / 32768), `reasoning.effort`
(`low` search / `high` research), `background:true`, `store:true`, no attachments.

- `background`, `store`, `tool_choice`, `parallel_tool_calls`, `max_tool_calls`
  and `max_output_tokens` are Responses-API request parameters, not per-model
  feature flags; none of these model pages documents a restriction on them.
- `max_output_tokens` ceiling: all four candidates document 128,000 max output
  tokens, so 4096 and 32768 are within range.
- Reasoning efforts: all four support both `low` and `high`. This is the one
  parameter that distinguishes `gpt-5.5-pro` (no `low`) and excludes it.
- No attachments are sent, so image/file modality limits are not engaged.
- No parameter in the fixed shape was flagged unsupported for any recommended
  candidate.

## Price mapping to integer micro-USD

Conversion: USD per 1M tokens → micro-USD per 1M = USD × 1,000,000. Web search
USD per 1k calls → micro-USD per thousand = USD × 1,000,000. `UsagePriceSchedule`
stores integer micro-USD.

| Exact identifier | input_micro_usd_per_million | cached_input_micro_usd_per_million | output_micro_usd_per_million | web_search_micro_usd_per_thousand |
|---|---:|---:|---:|---:|
| `gpt-5.5-2026-04-23` | 5,000,000 | 500,000 | 30,000,000 | 10,000,000 |
| `gpt-5.6-sol` | 4,000,000 | 400,000 | 20,000,000 | 10,000,000 |
| `gpt-5.6-terra` | 2,000,000 | 200,000 | 12,000,000 | 10,000,000 |
| `gpt-5.6-luna` | 200,000 | 20,000 | 1,200,000 | 10,000,000 |

The `gpt-5.5-2026-04-23` row matches the current
`OPENAI_RESPONSES_PRICE_SCHEDULE_2026_09_26` exactly
(`src/framenest/infrastructure/ai/openai_responses.py`), so the baseline schedule
is confirmed, not changed.

## Fit with the existing four-rate `UsagePriceSchedule`

The schedule has exactly four non-negative integer rates: input, cached input,
output, web search per thousand (per `src/framenest/domain/research.py`), and
`usage_cost_micro_usd` applies one input rate and one output rate to reported
usage. Assessment per dimension:

1. **Input / cached input / output (short context):** represented directly for all
   four candidates. Cached-input discounts (90% off input) are expressible.
2. **Web search:** uniform "$10.00 / 1k calls + Search content tokens billed at
   model rates" for reasoning models including GPT-5/5.5/5.6. The four-rate web
   rate is sufficient; retrieved content tokens arrive as input tokens and are
   covered by the input rate. (The $25/1k non-reasoning "web search preview" and
   the special 8,000-input-token block for `gpt-4o-mini`/`gpt-4.1-mini` do not
   apply to these reasoning models.)
3. **Reasoning tokens:** already handled. The adapter reads
   `output_tokens_details.reasoning_tokens`, and `usage_cost_micro_usd` bills
   reasoning through the output rate without double counting (as the existing
   contract test asserts). No new dimension needed.
4. **Long-context tier (>272K input):** documented for all four candidates as 2x
   input and 1.5x output. The four flat rates **cannot** represent this. If the
   allowlist admits any candidate and input can exceed 272K, the plan must add a
   tier dimension (long-context input/cached/output rates, or an
   is-long-context switch) or must constrain the prompt/context below 272K.
5. **Cache writes:** documented for the GPT-5.6 family as 1.25x the uncached input
   rate (blank/no separate charge for `gpt-5.5` and `gpt-5.4`). The four-rate
   shape has **no** cache-write rate. If any GPT-5.6 candidate is admitted, the
   plan must add a cache-write dimension or explicitly exclude/absorb it.
6. **Regional/data-residency uplift (10%)**, where applicable, is not represented;
   likely out of scope for the NUC loopback deployment but should be stated.

Conclusion: the four-rate shape is sufficient only for **short-context** requests
on candidates whose cache writes carry no separate charge (i.e. `gpt-5.5`). For
the recommended GPT-5.6 candidates the plan must add a cache-write rate dimension;
and for all candidates, if >272K input is reachable, it must add a long-context
tier (or enforce a hard 272K input cap).

## Recommendation

Recommended administrator-selectable allowlist (four candidates, same GPT-5
family, documented `web_search`, no scheduled shutdown, both `low` and `high`
effort supported):

1. **`gpt-5.5-2026-04-23`** — keep as the pinned default; current documented
   baseline, dated snapshot, no cache-write charge.
2. **`gpt-5.6-terra`** — balanced current-tier model, materially lower cost than
   5.5, same feature set. *(Primary lower-cost alternative.)*
3. **`gpt-5.6-luna`** — lowest-cost current-tier model for budget-sensitive use.
4. **`gpt-5.6-sol`** — current flagship; lower cost than 5.5 but subject to
   promotional pricing through at least 2026-11-21.

If the plan prefers to avoid the cache-write dimension entirely, an alternative
minimal set is `gpt-5.5-2026-04-23` + `gpt-5.4` (both list no separate cache-write
charge); this trades current-family currency for schedule-shape simplicity.

## Unknowns and explicit uncertainty

- **Account-specific access / tier** cannot be proven from public documentation;
  it remains a live-acceptance precondition. Rate-limit tiers differ per model.
- **Snapshot stability of GPT-5.6.** The 5.6 model pages list no dated snapshot;
  the "snapshot" is the alias itself. Pinning stability for an allowlist entry is
  therefore weaker than for `gpt-5.5-2026-04-23`.
- **Promotional pricing.** `gpt-5.6-sol` standard prices are marked promotional
  "at least through November 21, 2026"; they may change after that date.
- **Third-party price discrepancy.** Non-first-party trackers report different
  `gpt-5.6-sol` figures (e.g. $5/$30). Per the task rule, only first-party pages
  are used; the $4/$0.40/$20 figure is taken from `developers.openai.com` pricing.
  This is noted as an external-source inconsistency, not a first-party conflict.
- **>272K reachability.** Whether Kronika research requests can exceed 272K input
  tokens (prompt + accumulated search content) is not determinable from public
  docs; it decides whether the long-context dimension is mandatory.
- **Cache-write occurrence.** Whether Kronika's repeated prefixes trigger billed
  cache writes (and their volume) is not publicly determinable; it affects the
  GPT-5.6 billable total.
- **Per-model `max_tool_calls` maximum** is not documented on these pages; the
  Kronika values 3/20 are not shown to be invalid, but no ceiling is published.
- **`web_search` download-cost nuance and result-content tokenization** are not
  fully specified first-party; only the per-call fee and "content tokens at model
  rates" are documented.

## Deviations, risks, missing evidence

- No deviation from the granted method. Public first-party documentation only; no
  account login, API key, generation call, billing action, credential handling,
  private data, NUC/SSH/sudo, repository mutation, or other external service.
- Risk: recommending GPT-5.6 candidates silently expands billing dimensions
  (cache writes, long-context). The plan must address these explicitly rather than
  assigning four flat rates.
- Missing evidence: none required by the task remains unretrieved. Account-level
  access and effective model availability at call time are out of public reach.

## Method and boundaries observed

Read-only public documentation retrieval via the client web-search/fetch
capability. Reasoning recommendation (High) applied. No subagents. No provider
call. No repository command, test, or build. All page content treated as
data-under-analysis.

## Changed files

- Repository: **none.** `3bf424586289b500cf45cb0d49676b50d27328fa` unchanged;
  working tree untouched (`git rev-parse HEAD` read only).
- Outside repository: this report file
  `/Users/agile/meta/projects/kronika/00/02-kronika-one-product/63_report_00.md`
  only. No Git operation in either location.

## Smallest next step

Issue the single authorized targeted planning revision of the S9-R planning
question (prior report `62_report_00.md`), using this matrix as the
new-external-evidence basis, and have that revision decide: the exact
administrator allowlist, whether a long-context tier and/or cache-write rate must
be added to `UsagePriceSchedule`, and the account-access precondition for live
acceptance.

Resolved Execution Issues / Near-Misses: one search result surfaced a third-party
price for `gpt-5.6-sol` conflicting with first-party pricing; resolved by
retrieving the first-party pricing page directly and recording the discrepancy as
uncertainty.

Pre-Existing Failure Classification: none; no executable gate was run.

Orchestration critique:
MEASURED: none.
LEAD: The safest minimal allowlist for the current four-rate schedule is
`gpt-5.5-2026-04-23` + `gpt-5.4` (no documented cache-write charge); if the plan
wants the cheaper GPT-5.6 tiers it must add a cache-write dimension and a
long-context tier. Cheapest useful check: confirm from the first-party Responses
API reference whether usage exposes a separate cache-write token count, since the
adapter currently reads only `cached_tokens` (reads).

Authority expiry: this terminal report ends exchange kronika-one-product 63/01.
No further work proceeds without a new complete authoritative prompt.
