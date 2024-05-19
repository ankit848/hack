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
    url = 'https://datebtc.com/#/reg?code=BQA8O'
    try:
        response = session.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        print("Visited refer URL.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to visit refer URL: {e}")

# Function to submit form
def submit_form(session, headers, phone, username, password, promotion, email, country, st, sk):
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
        if response_url == 'https://datebtc.com/#/':
            print("Form submitted successfully.")
            print("Username:", username)
            print("Email:", email)
        else:
            print("Form submission failed. Response URL did not match expected URL.")
    except Exception as e:
        print("An error occurred:", e)

def main():
    ua = UserAgent()
    
    # Generate 1000 random user agents
    user_agents = [ua.random for _ in range(1000)]
    
    # List of names
    names = ["Ram Yadav", "Krishna Kandel", "Jilab Paudel", "Emily Brown", "Shanta Aryal", "Monika Gurung", "Robert Taylor", "Olivia Martinez", "James Anderson", "Emma Thomas", "Magar gurue", "Seeya Mahato", "Matthew Clark", "Prital Thanet", "Daniel Lewis", "Chloe Hall", "Christopher Hill", "Mia Allen", "Joseph Scott", "Ella Green"]
    
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
            promotion = 'BQA8O'
            country = '尼泊尔'
            st = generate_st()
            sk = generate_sk()
            
            submit_form(session, headers, phone, username, password, promotion, email, country, st, sk)

if __name__ == "__main__":
    main()
