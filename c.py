import requests
import random
from bs4 import BeautifulSoup

# Function to generate random numbers
def generate_random_numbers():
    return ''.join(str(random.randint(0, 9)) for _ in range(3))

# Function to get token from server
def get_token():
    url = 'https://loyality-one.site/user/register'
    headers = {
 "User-Agent": "Mozilla/5.0 (Linux; Android 10; CLT-L29 Build/HUAWEICLT-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]",
    }
    try:
        with requests.Session() as session:
            response = session.get(url, headers=headers)
            response.raise_for_status()  # Raise an exception for non-2xx status codes
            soup = BeautifulSoup(response.content, 'html.parser')
            token = soup.find('input', {'name': '_token'}).get('value')
            return token
        
    except requests.exceptions.RequestException as e:
        print(f"Failed to get token: {e}")
        return None

_token = get_token()
if _token:
    print("Token obtained successfully:", _token)
else:
    print("Failed to obtain token.")

def submit_form(_token, area_code, mobile, email, password, password_confirmation):
    url = 'https://loyality-one.site/user/register'
    data = {
        '_token': _token,
        'username': mobile,
        'email': email,
        'password': password,
        'password_confirmation': password_confirmation,
        'area_code': area_code,
    }
    try:
        response = requests.post(url, data=data)
        print(mobile)
        print(response.url)
        if 'https://loyality-one.site/user/dashboard' in response.url:
            print("Form submitted successfully.")
        else:
            print("Form submission failed.")
    except Exception as e:
        print("An error occurred:", e)

def main():
    password = 'hacker@12345'
    password_confirmation = 'hacker@12345'
    area_code = '+977'  # Define area_code within the main function

    for _ in range(3):  # Loop 2 times
        mobile_base = '9810005678'
        mobile = int(mobile_base) + random.randint(1000, 9999)  # Add a random 4-digit number to mobile_base
        username = f'hackers{generate_random_numbers()}'
        email = f'{username}p{generate_random_numbers()}@gmail.com'
        
        submit_form(_token, area_code, username, email, password, password_confirmation)

if __name__ == "__main__":
    main()

