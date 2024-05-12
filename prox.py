import requests

# Define the proxy
proxy = {
    'http': 'http://82.235.43.117:8080',
    'https': 'http://82.235.43.117:8080'
}

# URL to test the proxy
url = 'https://httpbin.org/ip'

try:
    # Send a request through the proxy
    response = requests.get(url, proxies=proxy)
    
    # Check if the request was successful
    if response.status_code == 200:
        print("Proxy connection successful!")
        print("Your IP Address:", response.json()['origin'])
    else:
        print("Failed to connect to the proxy:", response.status_code)
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
