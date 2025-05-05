import http.client
from urllib.parse import urlparse
from http import HTTPStatus

# Whitelist of safe content types
ALLOWED_CONTENT_TYPES = ['text/html', 'application/json', 'text/plain', 'application/xml']

# Custom headers to simulate a browser request
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://www.google.com",
    "Connection": "keep-alive"
}

def check_status_http_client(url, max_redirects=10, timeout=20):
    redirects = 0
    print(f"\nChecking: {url}")

    while redirects < max_redirects:
        parsed_url = urlparse(url)
        conn = http.client.HTTPSConnection(parsed_url.netloc, timeout=timeout) if parsed_url.scheme == 'https' else http.client.HTTPConnection(parsed_url.netloc, timeout=timeout)
        
        try:
            conn.request("GET", parsed_url.path or '/', headers=HEADERS)
            response = conn.getresponse()

            status_code = response.status
            headers = response.getheaders()
            content_type = dict(headers).get('Content-Type', '').split(';')[0]
            description = HTTPStatus(status_code).phrase if status_code in HTTPStatus._value2member_map_ else f"Status code {status_code} - Not in the dictionary"
            
            print(f"Status code: {status_code} - {description}")

            # Check for content-type validation
            if content_type not in ALLOWED_CONTENT_TYPES:
                print(f"Content-Type '{content_type}' is not allowed.")
                break

            # Check for redirection
            if 300 <= status_code < 400:
                url = dict(headers).get('Location')
                print(f"Redirected to: {url}")
                redirects += 1
            else:
                break
        except Exception as e:
            print(f"Error: {e}")
            break
        finally:
            conn.close()

    if redirects == max_redirects:
        print("Max redirects reached.")

# Handle multiple URLs from user input
def check_multiple_urls():
    user_input = input("Enter URLs separated by commas: ")
    urls = user_input.split(',')
    
    for url in urls:
        url = url.strip()
        if url:
            check_status_http_client(url)

# Example usage
check_multiple_urls()