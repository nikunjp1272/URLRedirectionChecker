# URLRedirectionChecker

---

## Overview

**URLRedirectionChecker** is a modular Python toolkit designed to analyze URL redirection chains, check HTTP status codes, validate content types, and assess URLs for potential risks (e.g., being on a blocklist or whitelist). The project progresses through several stages, starting with simple status code checks and advancing to advanced redirection tracing with content validation.

This tool is handy for security analysts, penetration testers, or developers who want to understand how URLs behave and whether they redirect to unsafe or unexpected destinations, all within the safety of an isolated Docker container.

---

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
├── URLRedirectionChecker/
│   └── URLRedirectionChecker.py           # Final, consolidated script (now Dockerized)
│
├── DockerIntegration/
    └── Dockerfile                             # Instructions to build the Docker image
    └── requirements.txt                       # Python dependencies for the Docker image

```

---

## Features

* ✅ **Progressive development:**
    * Start with just checking HTTP status codes
    * Move on to basic connectivity
    * Implement redirection tracking
    * Add content-type validation
    * End with a complete consolidated checker
* 🌐 **Multiple libraries used:**
    * `requests`
    * `http.client`
    * `urllib3`
* 🔁 **Redirection support:**
    * Tracks multiple redirects up to a configurable limit
    * Displays intermediate and final destination URLs
* ⚠️ **Content validation:**
    * Detects non-HTML content in the redirection chain
    * Stops analysis if suspicious content-type is encountered
* 🔒 **Enhanced Safety with Docker:**
    * All URL checks run within an isolated container, protecting your host system.
    * **Automatic Shutdown for Malicious URLs:** If a URL is identified as malicious (based on the defined `MALICIOUS_DOMAINS`), the container will automatically terminate, preventing further execution and alerting the user.
---

## Usage

You can use URLRedirectionChecker either by running the Python script directly (for development or specific testing) or by using the **recommended Dockerized version** for enhanced safety and ease of use.

### Using the Docker Image (Recommended for Safety)

The Docker image encapsulates the `URLRedirectionChecker.py` script and its dependencies, providing an isolated environment for checking URLs. This is crucial as it prevents potentially malicious URLs from directly affecting your local system.

1.  **Install Docker:**
    If you don't have Docker installed, follow the official Docker installation guide for your operating system: [Get Docker](https://docs.docker.com/get-docker/)

2.  **Pull the Docker Image:**
    Pull the latest version of the `URLRedirectionChecker` image from Docker Hub:

    ```bash
    docker pull [your_dockerhub_username]/url-redirect-checker:latest
    ```
    *(Replace `[your_dockerhub_username]` with your actual Docker Hub username)*
