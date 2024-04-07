import requests
import time

# Function to get proxies from URL
def get_proxies(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            proxies = response.text.strip().split('\n')
            return proxies
        else:
            print(f"Failed to retrieve proxies from URL. Status Code: {response.status_code}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve proxies: {e}")
        return []

# Function to visit URL using proxy
def visit_url_with_proxy(url, proxy):
    try:
        response = requests.get(url, proxies={'http': proxy})
        if response.status_code == 200:
            print(f"Success: Visited {url} using proxy {proxy}")
        else:
            print(f"Error: Unable to visit {url} using proxy {proxy}. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Main function
def main():
    url = 'https://10.alabbd.xyz/'
    proxy_url = 'https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt'
    proxies = get_proxies(proxy_url)

    for proxy in proxies:
        visit_url_with_proxy(url, proxy)
        time.sleep(1)  # Wait for 1 second before visiting the next proxy

if __name__ == "__main__":
    main()
