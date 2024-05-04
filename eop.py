import requests
import random
from bs4 import BeautifulSoup

# Function to generate random numbers
def generate_random_numbers():
    return ''.join(str(random.randint(0, 9)) for _ in range(3))

# Function to submit form data
def submit_form(url, user_email, user_name, user_pass, user_conpass, terms_check, user_ref):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    emtoken = soup.find('input', {'name': 'emtoken'}).get('value')

    data = {
        'emtoken': emtoken,
        'user_name': user_name,  # Generate a random username
        'user_email': user_email,
        'user_pass': user_pass,
        'user_conpass': user_conpass,
        'terms_check': terms_check,
        'user_ref': user_ref
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; CLT-L29 Build/HUAWEICLT-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]",
    }
    response = requests.post(url, data=data, headers=headers)
    print(data['user_name'])
    print("Response Content:", response.content.decode("utf-8"))
    print(response.url)
    if 'https://earnzop.com/dashboard/' in response.url:
        print("Form submitted successfully.")
    else:
        print("Form submission failed.")

# Main function
def main():
    for _ in range(2):
        url = 'https://earnzop.com/em-apc/u/R92t3R'
        user_pass = 'hacker@1234a55'
        user_conpass = 'hacker@1234a55'
        terms_check = 'on'  # Define terms_check within the main function
        user_ref = 'AB1BB'
        user_name = f'hackings12{generate_random_numbers()}'
        user_email = f'dinesh{generate_random_numbers()}p{generate_random_numbers()}@gmail.com'
        submit_form(url, user_email, user_name, user_pass, user_conpass, terms_check, user_ref)

# Execute main function if the script is run directly
if __name__ == "__main__":
    main()
