import requests
import random
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

# Function to generate random numbers
def generate_random_numbers():
    return ''.join(str(random.randint(0, 9)) for _ in range(3))

# Function to get token from server
def get_token():
    url = 'https://clickerra.xyz/user/register'
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; CLT-L29 Build/HUAWEICLT-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]",
    }
    try:
        with requests.Session() as session:
            response = session.get(url, headers=headers)
            response.raise_for_status()  # Raise an exception for non-2xx status codes
            soup = BeautifulSoup(response.content, 'html.parser')
            token = soup.find('input', {'name': '_token'}).get('value')
            return token, session  # Return both token and session
        
    except requests.exceptions.RequestException as e:
        print(f"Failed to get token: {e}")
        return None, None

def submit_form(_token, session, referBy, firstname, lastname, username, email, country, mobile_code, country_code, mobile, password, password_confirmation, agree):
    url = 'https://clickerra.xyz/user/register'
  
    data = {
        '_token': _token,
        'referBy': referBy,  # Fix: pass referBy to the data dictionary
        'firstname': firstname,
        'lastname': lastname,
        'username': username,
        'email': email,
        'password': password,
        'password_confirmation': password_confirmation,
        'country': country,
        'mobile_code': mobile_code,
        'country_code': country_code,
        'mobile': mobile,
        'agree': agree,
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; CLT-L29 Build/HUAWEICLT-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]",
    }

    try:
        response = session.post(url, data=data, headers=headers)
        if 'https://clickerra.xyz/user/dashboard' in response.url:
            print(f"Form submitted successfully for {mobile},{email},{username}.")
        else:
            print(f"Form submission failed for {mobile}.")
            print(response.url)
            print("Response content:", response.content)
    except Exception as e:
        print(f"An error occurred for {mobile}: {e}")

def main():
    referBy = 'Ram1223'
    password = 'hacker@123455'
    password_confirmation = 'hacker@123455'
    mobile_code = '977'  # Define area_code within the main function
    country_code = 'NP'
    agree = 'on'
    firstname = 'Fuck'
    lastname = 'Hacker'
    country = 'Nepal'  # Assuming this is the country name
    num_workers = 2 # Number of workers
    tokens_and_sessions = [get_token() for _ in range(num_workers)]  # Generate tokens and sessions for each worker

    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        for token, session in tokens_and_sessions:
            if token:
                print("Token obtained successfully:", token)
                for _ in range(1):  # Loop 3 times for each worker
                    mobile_base = '9700005678'
                    mobile = int(mobile_base) + random.randint(10, 99999)  # Add a random 4-digit number to mobile_base
                    username = f'hayackerss{generate_random_numbers()}'
                    email = f'{username}{generate_random_numbers()}@gmail.com'
                    
                    executor.submit(submit_form, token, session, referBy, firstname, lastname, username, email, country, mobile_code, country_code, mobile, password, password_confirmation, agree)
            else:
                print("Failed to obtain token for worker.")

if __name__ == "__main__":
    main()
