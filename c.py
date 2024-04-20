import requests
import random
from bs4 import BeautifulSoup

# Function to generate random numbers
def generate_random_numbers():
    return ''.join(str(random.randint(0, 9)) for _ in range(3))

# Function to get token from server
import requests
from bs4 import BeautifulSoup

def get_token():
    url = 'https://loyality-one.site/user/register'
    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*",
        "Host":"loyality-one.site",
        "Referer":"https://loyality-one.site/user/login",
        "Sec-Fetch-User":"1",
        "Upgrade-Insecure-Requests":"1",
       "User-Agent": "Mozilla/5.0 (Linux; Android 10; CLT-L29 Build/HUAWEICLT-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]",
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        soup = BeautifulSoup(response.content, 'html.parser')
        token = soup.find('input', {'name': '_token'})
        if token:
            print("Token obtained:", token['value'])
            return token['value']
        else:
            print("Token element not found.")
            return None
    except requests.exceptions.RequestException as e:
        print("Error fetching token:", e)
        return None

get_token()


# Function to submit form data
def submit_form(token, username, email, password, password_confirmation, area_code):
    url = 'https://loyality-one.site/user/register'
    data = {
        '_token': token,
        'username': username,
        'email': email,
        'password': password,
        'password_confirmation': password_confirmation,
        'area_code': area_code
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*",
        "Host":"loyality-one.site",
        "Referer":"https://loyality-one.site/user/login",
        "Sec-Fetch-User":"1",
        "Upgrade-Insecure-Requests":"1",
      "User-Agent": "Mozilla/5.0 (Linux; Android 10; CLT-L29 Build/HUAWEICLT-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]"
    }
    
    try:
        response = requests.post(url, data=data, headers=headers)
        response.raise_for_status()
        print("Form submitted successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Failed to submit form: {e}")

# Getting the token
token = get_token()
if token:
    # You can then use this token to submit the form
    submit_form(token, username, email, password, password_confirmation, area_code)


def main():
    password = 'hacker@12345'
    password_confirmation = 'hacker@12345'
    mobile_code = '+977'
    user = 'raamamm'
  
    
    for _ in range(2):  # Loop 2 times
        mobile_base = '9800005678'
        username = int(mobile_base) + random.randint(1000, 9999)  # Add a random 4-digit number to mobile_base
        email = f'{user}p{generate_random_numbers()}@gmail.com'
        
        # Assuming areacode is a parameter, it needs to be passed in
        submit_form(token, username, email, password, password_confirmation, area_code)

if __name__ == "__main__":
    main()
