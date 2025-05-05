import http.client
from urllib.parse import urlparse
from http import HTTPStatus

def check_status_http_client(url):
    try:
        parsed_url = urlparse(url.strip())

        # Ensure the URL has a scheme and netloc
        if not parsed_url.scheme or not parsed_url.netloc:
            print(f"Invalid URL: {url}")
            return

        conn = http.client.HTTPSConnection(parsed_url.netloc) if parsed_url.scheme == 'https' else http.client.HTTPConnection(parsed_url.netloc)
        conn.request("GET", parsed_url.path or '/')
        response = conn.getresponse()

        status_code = response.status
        description = HTTPStatus(status_code).phrase if status_code in HTTPStatus._value2member_map_ else f"Status code {status_code} - Not in the dictionary"

        print(f"\nURL: {url}")
        print(f"Status code: {status_code} - {description}")

        if 300 <= status_code < 400:
            location = response.getheader('Location')
            print(f"Redirected to: {location}")

        conn.close()
    except Exception as e:
        print(f"\nURL: {url}")
        print(f"Error: {e}")

# Accept multiple URLs from user input
user_input = input("Enter URLs separated by commas: ")
urls = user_input.split(',')

# Check each URL
for url in urls:
    if url.strip():
        check_status_http_client(url)