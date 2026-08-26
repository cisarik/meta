External Research Report: Free-Tier LLM Providers for playable-free-rivals

Research date: 26 August 2026. I applied the hard gate conservatively: a provider qualifies only when I could establish a recurring/no-cost API path plus server-side custom tool calling. One-time signup credits do not qualify.

1. Verdict table
Provider	Qualifies	Tool calling	OpenAI-compatible	Free limit, Aug 2026	Signup friction	Recommended free model(s)	Grounding
Groq	Y	Yes, including required	Yes	GPT-OSS/Qwen: 30 RPM, 1,000 RPD, 8K TPM, 200K TPD	Low, account + key	openai/gpt-oss-20b, qwen/qwen3.6-27b, openai/gpt-oss-120b	[VERIFIED]
Cloudflare Workers AI	Y	Yes, including required	Yes /v1/chat/completions	10,000 Neurons/day; resets 00:00 UTC	Low-medium, account ID + token	@cf/zai-org/glm-4.7-flash; @cf/nvidia/nemotron-3-120b-a12b	[VERIFIED]
Google AI Studio / Gemini	Y	Yes	Yes	Free input/output on selected models; RPM/TPM/RPD are model/project/account dependent and shown in AI Studio	Low, Google account + key	gemini-3.7-flash; gemini-3.5-flash-lite	[VERIFIED]
Mistral La Plateforme	Y	Yes, required/specific tool	Effectively Yes	Free Mode has included monthly API usage; exact current quota not publicly fixed	Low, Free Mode, no CC documented	mistral-small-latest / mistral-small-2603	[VERIFIED]
IBM watsonx.ai Runtime Lite	Y	Yes	Partial / near-compatible	300,000 tokens/month, published Lite allowance; IBM also documents inference request limits	Medium-high, Cloud service + project + IAM	ibm/granite-4-h-small	[VERIFIED]
OpenRouter :free	Y	Yes when selected model supports tools	Yes	Pure-free account: 50 requests/day total, 20 RPM; failed requests count	Very low	openrouter/free or currently tool-capable :free model	[VERIFIED]
Hugging Face Inference Providers	Y*	Yes, model/provider dependent	Yes	Free users receive $0.10 recurring monthly inference credit	Low	Select live route advertising tool support	[VERIFIED]
Aion Labs	N*	Model capability likely, direct API contract not verified	Yes	15 RPM, 20K TPM, 20K tokens/day	Low, no card	aion-labs/aion-3.0 candidate	[VERIFIED free/API], [LIKELY tools]
SambaNova Cloud	N	Yes	Yes	Current plan requires purchased credits after one-time signup credit	Medium	n/a	[VERIFIED]
Cerebras Inference	N	Yes	Yes	Current offering is $5 Free Trial, not recurring	Low	n/a	[VERIFIED]
Cohere	N	Yes	Compatible path exists	Evaluation key: 1,000 calls/mo, 20 RPM, but trial/evaluation use rather than public production service	Low	n/a	[VERIFIED]
Together AI	N	Yes	Yes	No free trial since June 2026; minimum $5 credit purchase	Low	n/a	[VERIFIED]
Fireworks AI	N	Yes	Yes	$1 one-time free credit, then prepaid	Low	n/a	[VERIFIED]
xAI	N	Yes	Yes	Prepaid/invoiced billing; no recurring free API allowance found	Low-medium	n/a	[VERIFIED]
Perplexity API	N	Not material	OpenAI-like	Must add payment method and purchase API credits	Medium	n/a	[VERIFIED]
NVIDIA hosted NIM Catalog	N*	Yes	Yes	Free hosted endpoints are positioned for prototyping; model/traffic-dependent limits, no durable recurring production quota documented	Low	existing integration	[VERIFIED]
GitHub Models	N	n/a	n/a	Service retired July 30, 2026	n/a	n/a	[VERIFIED]

Y* for Hugging Face means it passes literally, but its $0.10/month pool is microscopic. N* denotes an interesting near-miss rather than a technically incapable service.

2. Qualifying provider cards
Groq

Best clean drop-in. [VERIFIED] Groq's Free Plan currently gives openai/gpt-oss-20b, openai/gpt-oss-120b, and qwen/qwen3.6-27b 30 RPM, 1,000 RPD, 8,000 TPM, 200,000 TPD. Limits are organization-level and responses expose retry-after plus remaining-request/token headers.

All current hosted models support tool use, although groq/compound specifically does not support local application tools. GPT-OSS and Qwen do. Groq supports normal structured tool_calls, forced tool use, streaming, and an OpenAI-style endpoint.

For Libre Tiles, start with openai/gpt-oss-20b. The important constraint is probably 8K TPM / 200K TPD, rather than its generous request counter.

Groq Free Plan rate limits

Cloudflare Workers AI

Probably the best additional capacity pool. [VERIFIED] Workers Free includes 10,000 Neurons every day, with no paid plan required; allowance resets at midnight UTC.

It now has a genuine OpenAI-compatible /v1/chat/completions endpoint. @cf/zai-org/glm-4.7-flash explicitly supports function calling, multi-turn tools, tool_choice: "required", parallel tool calls and streaming. Crucially, it remains available on Workers Free after Cloudflare moved several expensive frontier models behind billing in July.

For Scrabble I would use GLM-4.7-Flash first, rather than burn free Neurons on Nemotron 120B.

Workers AI pricing

Google AI Studio / Gemini

Very compelling capacity source. [VERIFIED] gemini-3.7-flash currently has free-of-charge input and output tokens on the Free Tier and is GA. Google provides an OpenAI compatibility endpoint requiring essentially a base-URL, key and model change.

The catch is quota predictability: free API limits vary by model/project/account and the authoritative live values are shown in AI Studio rather than as one stable public table. Limits are project-level, so creating more API keys is not a legitimate quota multiplier.

There are also recent user reports of surprising free-tier RESOURCE_EXHAUSTED failures. Treat that operational observation as [LIKELY], not as Google's stated SLA.

Mistral La Plateforme

Excellent adapter fit, less excellent capacity transparency. [VERIFIED] New accounts can operate in Free Mode, API access is enabled without a credit card, and included monthly usage is subject to limits visible in the account Limits page. Mistral does not currently publish one universal numeric free quota that I would safely bake into Libre Tiles.

The Chat API supports normal JSON functions plus tool_choice values including required and forcing a named function. mistral-small-2603 / mistral-small-latest is the obvious candidate: Mistral Small 4 has 119B total parameters, 6.5B active, and explicitly supports Function Calling.

IBM watsonx.ai Runtime Lite

The sleeper candidate. [VERIFIED] IBM currently offers a genuine Free Lite runtime allocation of 300,000 input+output tokens per month. The Lite service can be deleted after 30 days of inactivity, a worthwhile operational gotcha.

watsonx exposes server-side chat APIs, SSE streaming, JSON tools, structured tool calls and explicit named tool_choice. The wire format is very close to OpenAI Chat Completions, but IAM authentication, project_id and IBM API versioning make this less plug-and-play than Groq.

ibm/granite-4-h-small is the model I would test first.

OpenRouter

Already useful, but it explains your evening pain. [VERIFIED] A pure free account has 50 free-model requests/day total and 20 RPM. Spending at least $10 historically raises the free-model daily allowance to 1,000, but that would violate this project's pure-free premise. Failed requests also count.

openrouter/free can dynamically select a zero-cost model satisfying requested capabilities such as tools, but rotating among :free models does not manufacture additional account-level daily quota.

Hugging Face Inference Providers

Qualifies technically, not strategically. [VERIFIED] Free HF accounts currently receive $0.10 of recurring monthly inference credits. Routed inference can be accessed through HF's OpenAI-compatible router, with tool support depending on the chosen model/provider route.

I would integrate it only if essentially free to add to your adapter abstraction. Ten cents per month is a puddle, not a reservoir.

3. TOP-5 new integrations for Libre Tiles
Rank	Provider	Why	Estimated adapter effort
1	Groq	Near-drop-in OpenAI API, excellent tool semantics, precise free limits, good ≥20B choices	1-3 hours
2	Cloudflare Workers AI	10K Neurons/day, independent capacity pool, free tool-capable GLM, OpenAI endpoint	2-4 hours
3	Google Gemini	Strongest model quality/capacity candidate; OpenAI shim makes migration easy	2-4 hours
4	Mistral	No-card Free Mode, native tools and forced calls, familiar Chat Completions shape	2-4 hours
5	IBM watsonx.ai Lite	300K recurring tokens/month and independent infrastructure	0.5-1 day

I would implement them in roughly that order. Groq + Cloudflare + Gemini are the real prize: three independent failure domains without a major architectural rewrite.

4. Rate-limit survival tactics
Provider-level fallback, not key multiplication. [VERIFIED principle] Use an ordered chain such as Groq -> Cloudflare -> Gemini -> Mistral -> IBM -> OpenRouter. One provider's 429 should immediately expose another provider's legitimate quota.
Respect quota telemetry. Parse Retry-After and provider rate-limit headers where offered, especially Groq. Use jittered retry only when waiting is short; otherwise fail over.
Make validate_move cheap. The first model turn need only produce compact placement arguments. Do not spend ~700 output tokens before validation if a 50-token tool call is sufficient. Token-metered free tiers stretch dramatically when reasoning prose is separated from move selection.
Capability-test every model before enabling it. Test tool_choice:"required", exact schema arguments, streamed tool-call reconstruction, tool-result continuation and malformed-call handling. Automatically quarantine a model that starts answering in prose rather than calling validate_move.
Per-model rotation: [SPECULATIVE]. Only assume separate capacity when the provider explicitly documents per-model quotas. Do not assume extra API keys/projects create extra quota. OpenRouter's free daily quota is account-wide; Cloudflare's Neuron pool is aggregate.
Move synthetic evaluation and health checks away from play sessions. [SPECULATIVE]. This preserves burst quota. Do not assume providers grant more quota merely because traffic is off-peak.
5. Important disqualifiers

Cerebras is technically almost perfect, including tool calling and excellent free-labelled rate-limit tables, but its current pricing describes the acquisition path as a $5 Free Trial followed by paid Developer access. Therefore N.

SambaNova has contradictory documentation: its rate-limit page still describes a Free Tier, but the current Plans page says users must add payment and purchase credits to make initial requests; SambaNova staff also describe the signup $5 as one-time. I would not architect against the older quota wording.

Cohere gives useful evaluation quotas, but explicitly treats those keys as evaluation/trial rather than the route for serving a public production application. Together abolished its free trial in June 2026. Fireworks supplies only $1 initial credit. xAI and Perplexity require funded billing/credits.

GitHub Models can be deleted from future research lists: GitHub retired the Models playground, catalog and inference API on July 30, 2026.

Aion Labs is the one I would keep on a watchlist. Its own docs verify a genuinely free no-card tier at 15 RPM / 20K TPM / 20K tokens/day and an OpenAI-compatible API. Third parties show Aion models performing tool calls, but I could not verify custom tools/tool_choice in Aion's own API documentation during this research. Under your strict grounding contract, that means not qualified yet, rather than optimistic inclusion.

Bottom line

The adapter-expansion logical whole has a strong basis: add Groq, Cloudflare Workers AI, Gemini, Mistral, then IBM watsonx.ai Lite. That transforms the current two-lane setup into several independent quota pools while keeping four of the five additions very close to your existing OpenAI Chat Completions abstraction.

The biggest discovery is Cloudflare Workers AI: 10,000 free Neurons/day plus a proper OpenAI endpoint and a currently free GLM-4.7-Flash with explicit tool_choice:"required" makes it unusually well matched to a strict validate_move Scrabble loop.

These tiers are unusually volatile in 2026, so a periodic re-check could catch quota cuts or a newly qualifying Aion/SambaNova-style entrant.