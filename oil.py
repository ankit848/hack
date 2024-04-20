import requests
import random
from bs4 import BeautifulSoup

# Function to generate random numbers
def generate_random_numbers():
    return ''.join(str(random.randint(0, 9)) for _ in range(3))

# Function to hash the password
def hash_password(password):
    # Add your password hashing logic here
    return password

# Function to submit form
def submit_form(session, account, code, pwd, user_type):
    url = 'https://oli-bp.com/'
    hashed_pass = hash_password(pwd)  # Hash the password
    data = {
       'account': account,
       'code': code,
       'pwd': hashed_pass,
       'user_type': user_type,
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; CLT-L29 Build/HUAWEICLT-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]",
    }
    response = session.post(url, data=data, headers=headers)
    print(pwd)
    print(account)
    print(response.url)
    print(response.content)  # Print response content
    if 'https://api.oli-bp.com/api/user/register?lang=en' in response.url:
        print("Form submitted successfully.")
    else:
        print("Form submission failed.")

def main():
    code = '517651'
    pwd = 'Hacker123@'
    user_type = 1
    for _ in range(5):  # Loop 5 times
        account = f'hackers{generate_random_numbers()}p{generate_random_numbers()}@gmail.com'
        with requests.Session() as session:
            submit_form(session, account, code, pwd, user_type)

if __name__ == "__main__":
    main()
