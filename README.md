# URLRedirectionChecker

## Overview

URLRedirectionChecker is a modular Python toolkit designed to analyze URL redirection chains, check HTTP status codes, validate content types, and assess URLs for potential risks (e.g., being on a blocklist or whitelist). The project progresses through several stages, starting from simple status code checks to advanced redirection tracing with content validation.

This is particularly useful for security analysts, penetration testers, or developers who want to understand how URLs behave and whether they redirect to unsafe or unexpected destinations.

## Project Structure

```bash
URLRedirectionChecker-main/
│
├── CheckingHTTPStatus/
│   ├── http_status_descriptors_req.py     # Using requests library
│   ├── http_status_descriptors_http.py    # Using http.client
│   └── http_status_descriptors_UL.py      # Using urllib3
│
├── ConnectingToTheURLs/
│   ├── connect_to_URL_req.py              # Basic connectivity using requests
│   ├── connect_to_URL_http.py             # Basic connectivity using http.client
│   └── connect_to_URL_UL.py               # Basic connectivity using urllib3
│
├── TracingURLs/
│   ├── RawURLRedirecter_req.py            # Traces redirects using requests
│   ├── RawURLRedirecter_http.py           # Traces redirects using http.client
│   └── RawURLRedirecter_UL.py             # Traces redirects using urllib3
│
├── TracingURLsWithContentValidation/
│   ├── URLRedirecter_req.py               # Redirect tracing + content validation (requests)
│   ├── URLRedirecter_http.py              # Redirect tracing + content validation (http.client)
│   └── URLRedirecter_UL.py                # Redirect tracing + content validation (urllib3)
│
└── URLRedirectionChecker/
    └── URLRedirectionChecker.py           # Final, consolidated script
```

# URLRedirectionChecker (Partial README)

This `README.md` provides information based on the text snippet provided. A full `README.md` would typically include an overview and project structure.

## Features

✅ Progressive development:
* Start with just checking HTTP status codes
* Move on to basic connectivity
* Implement redirection tracking
* Add content-type validation
* End with a complete consolidated checker

🌐 Multiple libraries used:
* requests
* http.client
* urllib3

🔁 Redirection support:
* Tracks multiple redirects up to a configurable limit
* Displays intermediate and final destination URLs

⚠️ Content validation:
* Detects non-HTML content in the redirection chain
* Stops analysis if suspicious content-type is encountered

🔒 Blocklist/Whitelist support (planned):
* Integration with blocklist aggregators or local caches (dictionary-based)
* Intended to flag malicious or trusted domains

## Usage

To use the final tool:

```bash
cd URLRedirectionChecker/URLRedirectionChecker
python URLRedirectionChecker.py
```
