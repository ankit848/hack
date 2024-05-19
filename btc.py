import requests
import random
import time
import hashlib
from fake_useragent import UserAgent

# Function to generate random numbers
def generate_random_numbers():
    return ''.join(str(random.randint(0, 9)) for _ in range(8))

# Function to generate random usernames
def generate_random_username():
    username = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(8))
    return username

# Function to generate random st
def generate_st():
    return str(int(time.time() * 1000))

# Function to generate random sk (placeholder, replace with actual logic if known)
def generate_sk():
    # The logic for generating sk should be implemented if known.
    # For this example, we are using a random hex string.
    return hashlib.md5(str(random.random()).encode()).hexdigest().upper()

# Function to visit the refer URL
def visit_refer_url(session, headers):
    url = 'https://datebtc.com/#/reg?code=C5XGM'
    try:
        response = session.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        print("Visited refer URL.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to visit refer URL: {e}")

# Function to submit form
def submit_form(session, headers, phone, username, password, promotion, email, country, st, sk):
    # First OPTIONS request
    options_url = 'https://api.datebtc.com/uc/register/phoneEmail'
    options_headers = {
        'Access-Control-Request-Method': 'POST',
        'Access-Control-Request-Headers': 'lang,x-auth-token'
    }
    try:
        session.options(options_url, headers=options_headers)
        print("First OPTIONS request sent.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send first OPTIONS request: {e}")

    # Actual POST request
    url = 'https://api.datebtc.com/uc/register/phoneEmail'
    data = {
        'phone': phone,
        'username': username,
        'password': password,
        'promotion': promotion,
        'email': email,
        'country': country,
        'superPartner': '',
        'ticket': '',
        'randStr': '',
        'st': st,
        'sk': sk,
    }
    try:
        response = session.post(url, data=data, headers=headers)
        response_url = response.url
        response_content = response.content.decode('utf-8')
        print(f"Response URL: {response_url}")
        print(f"Response Content: {response_content}")
        if response.status_code == 200 and 'some_success_indicator' in response_content:
            print("Form submitted successfully.")
            print("Username:", username)
            print("Email:", email)
        else:
            print("Form submission failed.")
            print("Response Status Code:", response.status_code)
            print("Response Content:", response_content)
    except requests.exceptions.RequestException as e:
        print(f"Form submission failed with exception: {e}")

    # Second OPTIONS request
    options_url = 'https://api.datebtc.com/uc/withdrawcode/messages'
    options_headers = {
        'Access-Control-Request-Method': 'GET',
        'Access-Control-Request-Headers': 'content-type,lang,sk,st,x-auth-token'
    }
    try:
        session.options(options_url, headers=options_headers)
        print("Second OPTIONS request sent.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send second OPTIONS request: {e}")

def main():
    ua = UserAgent()

    # Generate 1000 random user agents
    user_agents = [ua.random for _ in range(1000)]

    # List of names
    names = ["Ram Yadav", "Krishna Kandel", "Jilab Paudel", "Emily Brown", "Shanta Aryal", "Monika Gurung", "Robert Taylor", "Olivia Martinez", "James Anderson", "Emma Thomas", "Magar Gurue", "Seeya Mahato", "Matthew Clark", "Prital Thanet", "Daniel Lewis", "Chloe Hall", "Christopher Hill", "Mia Allen", "Joseph Scott", "Ella Green"]

    with requests.Session() as session:
        headers = {"User-Agent": random.choice(user_agents)}

        # Visit refer URL first
        visit_refer_url(session, headers)

        # Proceed with form submission
        for _ in range(2):  # Loop 2 times for testing, you can increase this number
            name = random.choice(names)
            username = generate_random_username()
            phone = generate_random_numbers()
            email = f'{username}@gmail.com'
            password = 'asasas'
            promotion = 'C5XGM'
            country = '尼泊尔'
            st = generate_st()
            sk = generate_sk()

            submit_form(session, headers, phone, username, password, promotion, email, country, st, sk)

if __name__ == "__main__":
    main()
