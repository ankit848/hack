import requests
import random

# Function to generate random numbers
def generate_random_numbers():
    return ''.join(str(random.randint(0, 9)) for _ in range(3))

# Function to submit form data
def submit_form(name, email, password):
    url = 'http://hacking122.rf.gd/login.php'
    data = {
        'name': name,
        'email': email,
        'password': password,
    }
    headers = {
         "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; CLT-L29 Build/HUAWEICLT-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]",
    }
    response = requests.post(url, data=data, headers=headers)
    print(email)
    print(name)
    print(password)
    print(response.url)
    if response.url == 'http://hacking122.rf.gd/backened.php':
        print("Form submitted successfully.")
    else:
        print("Form submission failed.")

# Main function
def main():
    password = 'ankit'
    for _ in range(3):  # Loop 3 times
        name = 'krishna'
        email = f'dinesh{generate_random_numbers()}p{generate_random_numbers()}@gmail.com'
            
        submit_form(name, email, password)

if __name__ == "__main__":
    main()
