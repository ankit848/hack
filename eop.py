import requests
import random
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

# Function to generate random numbers
def generate_random_numbers():
    return ''.join(str(random.randint(0, 9)) for _ in range(3))

# Function to get token from server
def get_token():
    url = 'https://earnzop.com/register/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; CLT-L29 Build/HUAWEICLT-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]",
    }
    try:
        with requests.Session() as session:
            response = session.get(url, headers=headers)
            response.raise_for_status()  # Raise an exception for non-2xx status codes
            soup = BeautifulSoup(response.content, 'html.parser')
            token = soup.find('input', {'name': 'emtoken'}).get('value')
            return token, session  # Return both token and session
        
    except requests.exceptions.RequestException as e:
        print(f"Failed to get token: {e}")
        return None, None

def submit_form(emtoken, session, user_email, user_pass, user_conpass, terms_check, user_ref):
    url = 'https://earnzop.com/register/'
  
    data = {
        'emtoken': emtoken,
        'user_name': user_name,
        'user_email': user_email,
        'user_pass': user_pass,
        'user_conpass': user_conpass,
        'terms_check': term_check,
        'user_ref': user_ref
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; CLT-L29 Build/HUAWEICLT-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]",
    }

    try:
        response = session.post(url, data=data, headers=headers)
        if 'https://earnzop.com/dashboard/' in response.url:
            print(f"Form submitted successfully for {user_name}.")
        else:
            print(f"Form submission failed for {user_name}.")
    except Exception as e:
        print(f"An error occurred for {user_name}: {e}")

def main():
    user_pass = 'hacker@1234a55'
    user_conpass = 'hacker@1234a55'
    terms_check = 'ON'  # Define area_code within the main function
    user_ref = 'AB1BB'
    num_workers = 2 # Number of workers
    tokens_and_sessions = [get_token() for _ in range(num_workers)]  # Generate tokens and sessions for each worker

    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        for emtoken, session in tokens_and_sessions:
            if emtoken:
                print("Token obtained successfully:", emtoken)
                for _ in range(1):  # Loop 3 times for each worker
                    user_name = f'hayackerss{generate_random_numbers()}'
                    user_email = f'{usernames}p{generate_random_numbers()}@gmail.com'
                    
                    executor.submit(submit_form, emtoken, session, user_email, user_pass, user_conpass, terms_check, user_ref)
            else:
                print("Failed to obtain token for worker.")

if __name__ == "__main__":
    main()
