import urllib3
from http import HTTPStatus
import socket
import re
import certifi
from urllib.parse import urlparse

# A simple list of known malicious domains (for demonstration purposes)
MALICIOUS_DOMAINS = ['malicious.com', 'phishing.com', 'evilsite.com']

# Function to check if a domain is suspicious
def is_malicious_domain(domain):
    # Check against a hardcoded blacklist of domains (expand as needed)
    if any(malicious in domain for malicious in MALICIOUS_DOMAINS):
        return True
    return False

# Function to validate SSL certificates
import urllib3
import certifi
from urllib.parse import urlparse

def is_https_valid(url):
    try:
        parsed_url = urlparse(url)
        if parsed_url.scheme != 'https':
            return False  # Not HTTPS
        # Check for SSL validity using certifi
        with urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where()) as http:
            response = http.request('GET', url, timeout=10)
        return True
    except Exception as e:
        return False

# Function to check if a URL has any suspicious characteristics
def is_suspicious_url(url):
    # Check if URL contains suspicious patterns like random characters
    if re.search(r'[A-Za-z0-9]{16,}', url):  # long alphanumeric strings are common in phishing sites
        return True
    # Check for known bad domains or IP addresses
    domain = urlparse(url).netloc
    if is_malicious_domain(domain):
        return True
    return False

def check_status_urllib3(url, max_redirects=10, timeout=20):
    http = urllib3.PoolManager(timeout=urllib3.Timeout(connect=timeout, read=timeout))
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "close"
    }

    try:
        redirects = 0
        while redirects < max_redirects:
            response = http.request('GET', url, headers=headers, redirect=False)
            status_code = response.status
            description = HTTPStatus(status_code).phrase if status_code in HTTPStatus._value2member_map_ else f"Status code {status_code} - Not in the dictionary"
            content_type = response.headers.get('Content-Type')

            print(f"Checking URL: {url}")
            print(f"Status code: {status_code} - {description}")

            # Check for content-type validation
            if "text/html" not in (content_type or ''):
                print(f"Non-HTML content received: {content_type}. Stopping.")
                break

            # Check if the URL is suspicious (using the new function)
            if is_suspicious_url(url):
                print(f"Suspicious URL detected: {url}. Aborting.")
                break

            # Check for SSL/TLS validation
            if not is_https_valid(url):
                print(f"Invalid or missing SSL certificate for URL: {url}. Aborting.")
                break

            # Check for redirection
            if 300 <= status_code < 400:
                url = response.headers.get('Location')
                if url is None:
                    print("Location header is missing or invalid. Cannot proceed with redirection.")
                    break
                print(f"Redirected to: {url}")
                redirects += 1
            else:
                break

        if redirects >= max_redirects:
            print("Maximum redirection limit reached.")
    except urllib3.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

def check_multiple_urls():
    # Prompt the user for input
    user_input = input("Enter URLs separated by commas: ")
    urls = user_input.split(',')

    for url in urls:
        check_status_urllib3(url.strip())

# Call the function
check_multiple_urls()