import requests
from http import HTTPStatus

def check_status_requests(url):
    try:
        response = requests.get(url.strip(), allow_redirects=False, timeout=20)

        status_code = response.status_code
        description = HTTPStatus(status_code).phrase if status_code in HTTPStatus._value2member_map_ else f"Status code {status_code} - Not in the dictionary"

        print(f"\nURL: {url}")
        print(f"Status code: {status_code} - {description}")

        if 300 <= status_code < 400:
            location = response.headers.get('Location')
            print(f"Redirected to: {location}")
    except requests.exceptions.RequestException as e:
        print(f"\nURL: {url}")
        print(f"Error: {e}")

# Accept multiple URLs from user input
user_input = input("Enter URLs separated by commas: ")
urls = user_input.split(',')

for url in urls:
    if url.strip():
        check_status_requests(url)