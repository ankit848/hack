import requests
from concurrent.futures import ThreadPoolExecutor

# Function to send HTTP request
def send_request(url):
    try:
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print(f"Request to {url} successful")
            # Process response data if needed
        else:
            print(f"Request to {url} failed with status code: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while sending request to {url}: {e}")

def main():
    # Define the URL
    url = 'https://clickerra.xyz'
    
    # Number of times to send the request
    num_requests = 200
    
    # Maximum number of workers
    max_workers = 20
    
    # Create a ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit requests
        for _ in range(num_requests):
            executor.submit(send_request, url)

if __name__ == "__main__":
    main()
