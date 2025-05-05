import urllib3
from http import HTTPStatus

def check_status_urllib3(url):
    http = urllib3.PoolManager()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://www.google.com",
        "Connection": "keep-alive"
    }

    redirect_limit = 10
    redirect_count = 0

    print(f"\nChecking: {url}")
    while redirect_count < redirect_limit:
        try:
            response = http.request('GET', url, headers=headers, redirect=False, timeout=10.0)
            status_code = response.status
            description = HTTPStatus(status_code).phrase if status_code in HTTPStatus._value2member_map_ else f"Status code {status_code} - Not in the dictionary"

            print(f"Status code: {status_code} - {description}")

            if 300 <= status_code < 400:
                next_url = response.headers.get('Location')
                print(f"Redirected to: {next_url}")
                if not next_url:
                    print("No Location header found for redirect.")
                    break
                url = next_url
                redirect_count += 1
                continue
            break
        except urllib3.exceptions.HTTPError as e:
            print(f"Error accessing {url}: {e}")
            break

    if redirect_count >= redirect_limit:
        print("Redirection limit reached.")

# Accept multiple URLs from user input
user_input = input("Enter URLs separated by commas: ")
urls = user_input.split(',')

for url in urls:
    check_status_urllib3(url.strip())