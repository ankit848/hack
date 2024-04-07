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

# Main function
def main():
    url = 'https://10.alabbd.xyz/'
    proxy_url = 'https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt'
    proxies = get_proxies(proxy_url)
    num_iterations = 100

    for i in range(num_iterations):
        for proxy in proxies:
            try:
                response = requests.get(url, proxies={'http': proxy})
                if response.status_code == 200:
                    print(f"Iteration {i+1}: Success: Visited {url} using proxy {proxy}")
                else:
                    print(f"Iteration {i+1}: Error: Unable to visit {url} using proxy {proxy}. Status Code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Iteration {i+1}: Error: {e}")
        time.sleep(0.01)  # Wait for 1 second before making the next request

if __name__ == "__main__":
    main()
