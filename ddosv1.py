import requests
import random
import os
import threading
from concurrent.futures import ThreadPoolExecutor
from fake_useragent import UserAgent

# Global counter to keep track of successful requests
success_counter = 0
counter_lock = threading.Lock()

def show():
    os.system('clear')  # Clear the terminal screen
    print("\033[1m\033[91m                 Load Testing with Proxies\033[0m")
    print("\n\n")

def fetch_proxies():
    proxy_list_url = "https://www.sslproxies.org/"  # Public proxy list URL
    response = requests.get(proxy_list_url)
    proxies = []
    if response.status_code == 200:
        # Parse the proxy list page to extract proxy IPs and ports
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find(id='proxylisttable')
        for row in table.tbody.find_all('tr'):
            tds = row.find_all('td')
            ip = tds[0].text
            port = tds[1].text
            proxies.append(f"http://{ip}:{port}")
    return proxies

def validate_proxy(proxy):
    try:
        response = requests.get("http://www.google.com", proxies={"http": proxy, "https": proxy}, timeout=5)
        if response.status_code == 200:
            return True
    except:
        return False
    return False

def send_request(url, proxy):
    global success_counter
    
    try:
        # Initialize UserAgent object
        ua = UserAgent()
        
        # Generate a random User-Agent
        user_agent = ua.random
        
        # Set the User-Agent header
        headers = {"User-Agent": user_agent}
        
        # Send GET request with the specified User-Agent and proxy
        response = requests.get(url, headers=headers, proxies={"http": proxy, "https": proxy})
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            with counter_lock:
                success_counter += 1
            print(f"\033[1;35m{success_counter} => Request to \033[1;37m{url} \033[1;34m with \033[1;33mUser-Agent \033[1;37m{user_agent} \033[0;32msuccessful using proxy {proxy}\033[0m")
        else:
            print(f"Request to \033[0;31m{url} with User-Agent {user_agent} \033[0;31mfailed with status code: {response.status_code} using proxy {proxy}\033[0m")
            
    except requests.exceptions.RequestException as e:
        print(f"\033[0mAn error occurred while sending request to \033[0;31m{url}\033[0m using proxy {proxy}: {e}")

def main():
    show()
    try:
        # Define the URL
        url = input("\033[96mEnter target URL: ")
        
        # Number of times to send the request
        num_requests = int(input("\033[97mEnter number of requests: "))
        
        # Maximum number of workers
        max_workers = int(input("\033[94mEnter number of workers: "))
        
        # Fetch and validate proxies
        proxies = fetch_proxies()
        valid_proxies = [proxy for proxy in proxies if validate_proxy(proxy)]
        
        if not valid_proxies:
            print("No valid proxies found. Please try again later.")
            return
        
        # Create a ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit requests
            for _ in range(num_requests):
                proxy = random.choice(valid_proxies)
                executor.submit(send_request, url, proxy)
        
        # Print the total number of successful requests
        print(f"\033[0;33mTotal successful requests: {success_counter}\033[0m")
    
    except ValueError:
        print("Invalid input. Please enter a valid integer for number of requests and workers.")

if __name__ == "__main__":
    main()
