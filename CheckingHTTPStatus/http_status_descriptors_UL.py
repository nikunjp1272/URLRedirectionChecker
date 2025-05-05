import urllib3
from http import HTTPStatus

def check_status_urllib3(url):
    http = urllib3.PoolManager()
    
    try:
        response = http.request('GET', url.strip(), redirect=False, timeout=urllib3.util.Timeout(connect=5.0, read=20.0))
        
        status_code = response.status
        description = HTTPStatus(status_code).phrase if status_code in HTTPStatus._value2member_map_ else f"Status code {status_code} - Not in the dictionary"

        print(f"\nURL: {url}")
        print(f"Status code: {status_code} - {description}")

        if 300 <= status_code < 400:
            location = response.headers.get('Location')
            print(f"Redirected to: {location}")
    except urllib3.exceptions.HTTPError as e:
        print(f"\nURL: {url}")
        print(f"Error: {e}")
    except Exception as e:
        print(f"\nURL: {url}")
        print(f"Unexpected error: {e}")

# Accept multiple URLs from user input
user_input = input("Enter URLs separated by commas: ")
urls = user_input.split(',')

for url in urls:
    if url.strip():
        check_status_urllib3(url)