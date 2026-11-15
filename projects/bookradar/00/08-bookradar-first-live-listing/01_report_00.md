# BookRadar MVP: agent, administration, and periodic monitoring

## Goal

A local application where you configure NVIDIA NIM and Brave Search, add a book, and the agent searches for offers across the web, retrieves their availability, and repeats the check every **12 hours**. New findings and changes appear in the application.

This goal replaces the original task of reading a single Martinus page. Under AP, it becomes a new logical whole, `bookradar-local-agent-mvp`; the original plan will not be presented as a completed plan for the broader MVP.

## Interface and settings

Three main screens in Slovak:

- **Watched books:** title, optional author and ISBN, target language, monitoring toggle, interval, and a “Search now” button.
- **Book detail:** offers grouped by retailer, price and currency, edition language, seller-reported availability, check time, link, and supporting excerpt. Also show run history and errors.
- **Settings:** NVIDIA API key, model identifier, optional temperature, output token limit, timeout, Brave API key, check interval, and fixed usage limits.

The NVIDIA integration will use `https://integrate.api.nvidia.com/v1/chat/completions`; the model will be configurable without code changes. A “Test connection” button will also check whether structured output is usable. ([NVIDIA API](https://docs.api.nvidia.com/nim/reference/llm-apis))

Keys are stored in macOS Keychain. The interface shows only whether they are configured and allows them to be replaced or deleted.

## Search and offer processing

The flow of a single run:

1. The model prepares at most two search queries based on the requested book.
2. Brave Search returns candidate links. The application removes duplicate URLs and processes at most five offers from different retailers. It uses the documented Web Search API. ([Brave Search](https://api-dashboard.search.brave.com/documentation/services/web-search))
3. The application fetches the pages themselves and separates structured product data from text. Search snippets are used only to discover offers.
4. The model extracts data and supporting quotations. The application validates the format and checks that quotations occur in the fetched content; unsupported data remains unknown.
5. Results are stored through the existing research v1 contract and importer. The agent does not automatically grant human approval.

Availability will clearly distinguish “Seller reports in stock,” “Reserved,” “Seller reports unavailable,” “Unknown,” and, separately, “Check failed.” Every value carries a time and source. Neither the page language nor a matching title confirms a Slovak edition.

Fetching will be sequential: public HTTPS, TLS verification, blocking internal addresses even after redirects, at most three redirects within the same host or its `www` variant, a 20-second timeout, and a 2 MiB limit per page. No automatic retries. A dynamic or blocked page produces a truthful incomplete result.

## Technical implementation and service

- Add an application crate, `bookradar-app`: Axum/Tokio for the web interface and scheduler, reqwest for HTTP, and scraper for HTML. Lock dependencies in `Cargo.lock`.
- Preserve the existing domain rules, research v1, both current database formats, and the original CLI. A new SQLite database will contain only settings, watched books, runs, references to findings, and notifications.
- Use internal interfaces for the model, search, page fetching, time, and key storage so the entire flow can be tested without internet access.
- A single worker process executes at most one run at a time. Manual and scheduled requests for the same book are coalesced. An interrupted import resumes from the identical saved data.
- A macOS LaunchAgent starts the application at login and restarts it after a crash. The web interface is available only on `127.0.0.1`; closing the browser does not stop monitoring. ([Apple](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html))
- After the computer wakes, perform one catch-up check for each overdue book. Checks do not run while the computer is shut down or asleep.

Default caps: **200 Brave requests and 1,000 NIM calls per month**, configurable in administration. Connection tests and failed attempts also count. Once a cap is reached, the affected runs pause; there is no automatic provider switch or limit increase. These caps limit the number of calls; the account plan determines their cost.

## Delivery order and verification

1. Administration with key storage and a working connection test for both APIs.
2. The complete manual flow: add a book → search → fetch offers → display results.
3. Persistent monitoring, a 12-hour interval, history, and notifications without repeating the same finding.
4. Installation, status inspection, and uninstallation of the macOS service; uninstallation preserves user data.

Automated tests will cover the complete flow using API test doubles, malformed model responses, unsupported claims, a Czech edition, unknown availability, blocked pages, API limits, URL security, restart recovery, and repeated import. The existing 113 tests remain intact; CI will not call live services.

Practical acceptance will verify real NVIDIA and Brave calls, processing offers from at least two retailers, displaying evidence, and an automatic run with the browser closed. This is followed by an independent review of the UI, keys, and the boundary between seller claims and verified availability.
