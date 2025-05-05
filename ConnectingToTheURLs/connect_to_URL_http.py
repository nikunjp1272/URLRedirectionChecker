import http.client
from urllib.parse import urlparse

def check_status_http_client(url):
    try:
        parsed_url = urlparse(url.strip())
        if not parsed_url.scheme:
            print(f"Invalid URL (missing scheme): {url}")
            return None

        conn = http.client.HTTPSConnection(parsed_url.netloc, timeout=10) if parsed_url.scheme == 'https' \
               else http.client.HTTPConnection(parsed_url.netloc, timeout=10)
        
        conn.request("GET", parsed_url.path or '/')
        response = conn.getresponse()
        status = response.status
        conn.close()
        return status

    except Exception as e:
        print(f"Error checking URL '{url}': {e}")
        return None

# Accept multiple URLs from user input
user_input = input("Enter URLs separated by commas: ")

# Split and loop through the URLs
urls = user_input.split(',')

for url in urls:
    url = url.strip()
    if not url:
        continue
    status_code = check_status_http_client(url)
    if status_code is not None:
        print(f"Status code for {url}: {status_code}")
