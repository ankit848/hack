import requests

def login_to_moneypluslife(id, password):
    # Define the form data
    form_data = {
        'u1': id,
        'p1': password,
        '1d2es5e8s': ''  # Add the missing value for the form field
    }
    
    # Define the headers
    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*",
        "Origin": "https://moneyplus.info",
        "Referer": "https://moneypluslife.info/panel/login",  # Corrected referer URL
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; CLT-L29 Build/HUAWEICLT-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]",
    }

    # Define the URL for form submission
    login_url = 'https://moneypluslife.info/panel/Authentic'

    # Create a session
    with requests.Session() as session:
        # Send POST request to login
        response = session.post(login_url, data=form_data, headers=headers)

        # Check if the session cookie is set
        if 'PHPSESSID' in session.cookies:
            print("Login Successful!")
        else:
            print("Login Unsuccessful!")
            
if __name__ == "__main__":
    # Replace 'your_id' and 'your_password' with the actual credentials
    user = '9807298840'
    password = '9807298840'
    login_to_moneypluslife(id, password)
