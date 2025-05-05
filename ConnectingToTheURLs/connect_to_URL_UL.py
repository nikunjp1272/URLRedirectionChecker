import urllib3

def check_status_urllib3(url):
    http = urllib3.PoolManager()
    try:
        response = http.request('GET', url.strip(), timeout=urllib3.util.Timeout(connect=5.0, read=10.0))
        return response.status
    except urllib3.exceptions.HTTPError as e:
        return f"Error: {e}"

# Accept multiple URLs from user input
user_input = input("Enter URLs separated by commas: ")

# Split and loop through the URLs
urls = user_input.split(',')

for url in urls:
    url = url.strip()
    if not url:
        continue
    status_code = check_status_urllib3(url)
    print(f"Status code for {url}: {status_code}")