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
    print("\033[1m\033[91m              hdg\033[0m")
    print("\n\n")

def send_request(url, proxy):
    global success_counter
    
    try:
        # Initialize UserAgent object
        ua = UserAgent()
        
        # Generate a random user agent
        user_agent = ua.random
        
        # Set the User-Agent header
        headers = {"User-Agent": user_agent}
        
        # Send GET request with the specified User-Agent and proxy
        response = requests.get(url, headers=headers, proxies=proxy, timeout=5)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            with counter_lock:
                success_counter += 1
            print(f"\033[1;35m{success_counter} => Request to \033[1;37m{url} \033[1;34m with \033[1;33mUser-Agent \033[1;37m{user_agent} \033[0;32msuccessful\033[0m")
            # Process response data if needed
        else:
            print(f"Request to \033[0;31m{url} with User-Agent {user_agent} \033[0;31mfailed with status code: {response.status_code}\033[0m")
            
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
        
        # List of proxies
        proxies = [
            "5.53.200.33:3128",
            "155.61.23.119:3128",
            "167.175.50.84:80",
            "165.225.52.25:80",
            "19.26.163.145:8081",
            "245.135.58.63:3128",
            "180.32.120.63:80",
            "160.105.47.210:8081",
            "246.153.175.188:3128",
            "87.9.119.10:8081",
            "241.7.104.160:8080",
            "58.206.223.144:80",
            "255.50.209.54:8080",
            "179.37.162.18:8080",
            "17.205.233.89:8081",
            "82.235.43.117:8080",
            "175.173.189.65:8081",
            "246.76.204.52:80"
        ]
        
        # Token bucket algorithm
        token_bucket = [time.time()] * max_workers
        
        # Create a ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit requests
            for _ in range(num_requests):
                # Wait for a token to be available in the token bucket
                while True:
                    current_time = time.time()
                    if current_time - token_bucket[0] >= 2:  # Limiting to 2 seconds
                        token_bucket.pop(0)
                        token_bucket.append(current_time)
                        break
                    time.sleep(0.1)
                
                # Choose a random proxy from the list
                proxy = {"https": random.choice(proxies)}
                executor.submit(send_request, url, proxy)
        
        # Print the total number of successful requests
        print(f"\033[0;33mTotal successful requests: {success_counter}\033[0m")
    
    except ValueError:
        print("Invalid input. Please enter a valid integer for number of requests and workers.")

if __name__ == "__main__":
    main()
