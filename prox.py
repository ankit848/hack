import requests

# Define the proxy
proxy = {
    'http': 'socks4://202.40.177.94:5678',
    'http': 'http://102.38.31.8:9999',
    'http': 'http://41.159.154.43:3128'
}

# URL to test the proxy
url = 'https://httpbin.org/ip'

try:
    # Send a request through the proxy with a timeout of 3 seconds
    response = requests.get(url, proxies=proxy, timeout=3)
    
    # Check if the request was successful
    if response.status_code == 200:
        print("Proxy connection successful!")
        print("Your IP Address:", response.json()['origin'])
    else:
        print("Failed to connect to the proxy:", response.status_code)
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
