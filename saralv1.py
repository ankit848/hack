import requests
import random
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# Function to generate random numbers
def generate_random_numbers():
    return ''.join(str(random.randint(0, 9)) for _ in range(3))

# Function to visit the invite URL
def visit_invite_url(session, headers, referred_code):
    url = f'https://saralshikshya.com.np/invite/{referred_code}'
    try:
        response = session.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        print("Accepted.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to visit invite URL: {e}")

# Function to get token and payloads from server
def get_token_and_payloads(session, headers):
    url = 'https://saralshikshya.com.np/register'
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
def submit_form(_token, session, _method, name, email, password, password_confirmation, referred_code, payloads, headers):
    url = 'https://saralshikshya.com.np/register'
    data = {
        '_token': _token,
        '_method': _method,
        'name': name,
        'email': email,
        'password': password,
        'referred_code': referred_code,
        'confirm_password': password_confirmation,
    }
    try:
        response = session.post(url, data=data, headers=headers)
        if 'https://saralshikshya.com.np/myprofile' in response.url:
            print("Form submitted successfully.")
            print("Email:", email)
        else:
            print("Form submission failed.")
    except Exception as e:
        print("An error occurred:", e)

def main():
    ua = UserAgent()
    
    # Generate 1000 random user agents
    user_agents = [ua.random for _ in range(1000)]
    
    with requests.Session() as session:
        headers = {"User-Agent": random.choice(user_agents)}
        referred_code = '655893'
        
        # Visit invite URL first
        visit_invite_url(session, headers, referred_code)
        
        # Get token and payloads after visiting invite URL
        _token, payloads = get_token_and_payloads(session, headers)
        
        # Proceed with form submission if token and payloads are obtained
        if _token and payloads:
            for _ in range(100000):  # Loop 5 times for testing, you can increase this number
                email = f'ramdevaryal{generate_random_numbers()}@gmail.com'
                submit_form(_token, session, 'post', 'Ramdev Aryal', email, 'ramdev@123450', 'ramdev@123450', referred_code, payloads, headers)

if __name__ == "__main__":
    main()
