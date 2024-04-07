import requests

def login_to_moneypluslife(id, password):
    # Define the form data
    form_data = {
        'u1': id,
        'p1': password
    }

    # Define the URL for form submission
    login_url = 'https://moneypluslife.info/panel/Login'

    # Create a session
    with requests.Session() as session:
        # Send POST request to login
        response = session.post(login_url, data=form_data)

        # Check if the session cookie is set
        if 'session' in session.cookies:
            print("Login Successful!")
            # Print the response content
            print("Response content:", response.content)
        else:
            print("Login Unsuccessful!")

if __name__ == "__main__":
    # Replace 'your_id' and 'your_password' with the actual credentials
    id = 'MPL2298238'
    password = '9807298843'
    login_to_moneypluslife(id, password)
