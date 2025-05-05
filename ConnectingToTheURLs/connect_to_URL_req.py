import requests

def check_status_requests(url):
    try:
        response = requests.get(url.strip(), timeout=10)
        return response.status_code
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Accept multiple URLs from user input
user_input = input("Enter URLs separated by commas: ")

# Split and loop through the URLs
urls = user_input.split(',')

for url in urls:
    url = url.strip()
    if not url:
        continue
    status_code = check_status_requests(url)
    print(f"Status code for {url}: {status_code}")