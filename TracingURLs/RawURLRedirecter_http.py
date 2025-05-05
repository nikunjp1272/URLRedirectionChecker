import http.client
from urllib.parse import urlparse
from http import HTTPStatus
import ssl

def check_status_http_client(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://www.google.com",
        "Connection": "close"
    }

    redirect_limit = 10
    redirect_count = 0

    print(f"\nChecking: {url}")
    while redirect_count < redirect_limit:
        parsed_url = urlparse(url)
        path = parsed_url.path or '/'
        if parsed_url.query:
            path += '?' + parsed_url.query

        conn = http.client.HTTPSConnection(parsed_url.netloc, timeout=20, context=ssl.create_default_context()) if parsed_url.scheme == 'https' else http.client.HTTPConnection(parsed_url.netloc, timeout=20)
        
        try:
            conn.request("GET", path, headers=headers)
            response = conn.getresponse()

            status_code = response.status
            description = HTTPStatus(status_code).phrase if status_code in HTTPStatus._value2member_map_ else f"Status code {status_code} - Not in the dictionary"

            print(f"Status code: {status_code} - {description}")

            if 300 <= status_code < 400:
                url = response.getheader('Location')
                print(f"Redirected to: {url}")
                redirect_count += 1
                conn.close()
                continue
            break
        except Exception as e:
            print(f"Error accessing {url}: {e}")
            break
        finally:
            conn.close()
    else:
        print("Redirection limit reached.")

# Accept multiple URLs from user input
user_input = input("Enter URLs separated by commas: ")
urls = user_input.split(',')

for url in urls:
    check_status_http_client(url.strip())