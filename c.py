import requests
import random

# Function to generate random numbers
def generate_random_numbers():
    return ''.join(str(random.randint(0, 9)) for _ in range(3))

# Function to submit form data
def submit_form(_token, firstname, lastname, username, email, country, mobile_code, country_code, mobile, password, password_confirmation):
    url = 'https://10.alabbd.xyz/user/register'
    data = {
        '_token': _token,
        'firstname': firstname,
        'lastname': lastname,
        'username': username,
        'email': email,
        'mobile': mobile,
        'password': password,
        'password_confirmation': password_confirmation,
        'country': country,
        'mobile_code': mobile_code,
        'country_code': country_code
    }
    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*",
        "Origin": "https://10.alabbd.xyz/",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; CLT-L29 Build/HUAWEICLT-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]",
    }
    try:
        response = requests.post(url, data=data, headers=headers)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        print("Form submitted successfully.")
        print("Submitted Data:")
        print(f"First Name: {firstname}")
        print(f"Last Name: {lastname}")
        print(f"Username: {username}")
        print(f"Email: {email}")
        print(f"Mobile: {mobile}")
        print(f"Country: {country}")
        print(f"Mobile Code: {mobile_code}")
        print(f"Country Code: {country_code}")
        print(f"Password: {password}")
        print(f"Password Confirmation: {password_confirmation}")
        print(f"Response URL: {response.url}")
    except requests.exceptions.RequestException as e:
        print(f"Form submission failed: {e}")

# Main function
def main():
    _token = '41BkbD5fRpSyV5EPMu9I6m1C0w4l8gvw4wkBQ7Ej'
    firstname = 'Hacker'
    lastname = 'King'
    password = 'hacker@12345'
    password_confirmation = 'hacker@12345'
    country = 'Nepal'
    mobile_code = '977'
    country_code = 'NP'

    for _ in range(2):  # Loop 2 times
        mobile_base = '9800005678'
        mobile = int(mobile_base) + random.randint(1000, 9999)  # Add a random 4-digit number to mobile_base
        username = f'hacker{generate_random_numbers()}'
        email = f'{username}p{generate_random_numbers()}@gmail.com'
            
        submit_form(_token, firstname, lastname, username, email, country, mobile_code, country_code, mobile, password, password_confirmation)

if __name__ == "__main__":
    main()
