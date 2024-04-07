import requests
import random

# Function to generate random numbers
def generate_random_numbers():
    return ''.join(str(random.randint(0, 9)) for _ in range(3))

# Function to submit form data
def submit_form(usponsor, uname, umobile, uemail, upass, uconpass):
    url = 'https://moneypluslife.info/panel/RegisterProcess'  # Replace with the actual URL
    data = {
        'usponsor': usponsor,
        'uname': uname,
        'umobile': umobile,
        'uemail': uemail,
        'upass': upass,
        'uconpass': uconpass
    }
    with requests.Session() as session:
        response = session.post(url, data=data)
        # Check if the session is active
        if 'session' in session.cookies:
            print("Form submission successful.")
            # Get the redirected URL after successful form submission
            redirect_url = response.url
            # Assuming the user ID is present in the redirected URL
            user_id = redirect_url.split('/')[-1]
            print("User ID:", user_id)
        else:
            print("Form submission unsuccessful.")

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
