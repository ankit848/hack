import requests
import random

# Function to generate random numbers
def generate_random_numbers():
    return ''.join(str(random.randint(0, 9)) for _ in range(3))

# Function to submit form data
def submit_form(usponsor, uname, umobile, uemail, upass, uconpass):
    url = 'https://moneypluslife.info/panel/RegisterProcess'
    data = {
        'usponsor': usponsor,
        'uname': uname,
        'umobile': umobile,
        'uemail': uemail,
        'upass': upass,
        'uconpass': uconpass
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("Form submitted successfully.")
    else:
        print("Form submission failed.")

# Main function
def main():
    usponsor = 'MPL2298238'
    upass = '1234567890'
    uconpass = '1234567890'

    for _ in range(3):
        uname = 'Radhey Radhey'
        umobile = '9812345678' + '/' + generate_random_numbers()
        random_numbers = generate_random_numbers()
        uemail = f'dinesh{random_numbers}p{generate_random_numbers()}@gmail.com'
        
        submit_form(usponsor, uname, umobile, uemail, upass, uconpass)

if __name__ == "__main__":
    main()
