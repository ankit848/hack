import requests
import random
from bs4 import BeautifulSoup

# Function to generate random numbers
def generate_random_numbers():
    return ''.join(str(random.randint(0, 9)) for _ in range(3))

# Function to get token from server
def get_token():
    url = 'https://loyality-one.site/user/register'
    headers = {
 "User-Agent": "Mozilla/5.0 (Linux; Android 10; CLT-L29 Build/HUAWEICLT-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]",
    }
    try:
        with requests.Session() as session:
            response = session.get(url, headers=headers)
            response.raise_for_status()  # Raise an exception for non-2xx status codes
            soup = BeautifulSoup(response.content, 'html.parser')
            token = soup.find('input', {'name': '_token'}).get('value')
            return token
        
    except requests.exceptions.RequestException as e:
        print(f"Failed to get token: {e}")
        return None

_token = get_token()
if _token:
    print("Token obtained successfully:", _token)
else:
    print("Failed to obtain token.")

def submit_form(_token,area_code, username, email, password, password_confirmation):

  url = 'https://loyality-one.site/user/register'
    data = {
        '_token': _token,
        'username': mobile,
        'email': email,
        'password': password,
        'password_confirmation': password_confirmation,
        'country': country,
        'area_code': mobile_code
    }
    headers = {
           "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*",
        "Host":"loyality-one.site",
        "Referer":"https://loyality-one.site/user/login",
        "Sec-Fetch-User":"1",
        "Upgrade-Insecure-Requests":"1",
        "Set-Cookie":"XSRF-TOKEN=eyJpdiI6IllQaVNnYXdzQ09OalIxQzhGMlI0eWc9PSIsInZhbHVlIjoicnpBYzlLeXVjeldMYjIyMmdDajdkVzR1NG1rTHRYaWhGdHdFTDlwTkFMMnZsYzUydkw4VEFIdm5USkZKVDVxWlNTVWFmSzNoUTZMNllOdnc2VFVOYXNWWVBXMVhJZDg0KzZwdFRIZWVWZ3VJeUs2THFTYjI0aXR6RXpqbTFDa2IiLCJtYWMiOiJhZDliNGU4MmM4YzgzMmViOGIzMjRjMjkxNmUwZTkwYWFjNDg4NzYwZDNlNjM2MjMzYTczNTY2MjgyMmU3N2I5IiwidGFnIjoiIn0%3D; expires=Sat, 20 Apr 2024 04:48:24 GMT; Max-Age=7200; path=/; samesite=lax; secure",
        "Set-Cookie":"hyiplab_session=eyJpdiI6InhGZzBHc3dha3BNcWlVMlF3ZlJLOWc9PSIsInZhbHVlIjoiS0VNVC9IS3dLVDRsdmlhaUNncWJTbUsxNmZmNEZNaHowK2wzdmllRVhId3RFbDR0WUJ1dVZtU1JYM1dhUFUzelo3WHVMU0lnOU1mWUQxOE1ackppcjFvR2NBb2RnVGtuSHdoT0c5Sy9qYktCT1JEZlljUGoxUFNrMGxSa3V2aXAiLCJtYWMiOiI1ZDY0YzViMDdjMWU1NTE3Y2I4MmYwYTM5NTVjMzVjMzAxMWQxMzI2YWZkYzhlYTU3NjFkOTUxOTcwZTNhOGZlIiwidGFnIjoiIn0%3D; expires=Sat, 20 Apr 2024 04:48:24 GMT; Max-Age=7200; path=/; httponly; samesite=lax; secure",
        "Cookie":"MicrosoftApplicationsTelemetryDeviceId=58f4586a-8ed6-4cc7-8e4c-4044676e6428; MicrosoftApplicationsTelemetryFirstLaunchTime=2024-04-20T02:44:43.485Z; MicrosoftApplicationsTelemetryDeviceId=58f4586a-8ed6-4cc7-8e4c-4044676e6428; MicrosoftApplicationsTelemetryFirstLaunchTime=2024-04-20T02:44:43.485Z; XSRF-TOKEN=eyJpdiI6ImFZaVcrN25YNnhnMm5HbERna3NzR2c9PSIsInZhbHVlIjoiSHM3cExjdE1rcFp1ekpsWVh2T3RyVDF3emhGUDZ1ZDdlRzhydTJFNjl3NWlTWisvL1JSOWNoU2FUMkZyNTIvc3VBQzJjV1ZJQVJ2T05zTGlQWCtvNmdXTkY0eUR0N1hZdmUydVFFM0RZMm1PMVJoVExSSE1oRXZFMkJYZXhlRGEiLCJtYWMiOiI5YThiMTUwZjI2ODk1MTkzMGRhMzljOGRhMTgxZTYzYjliNTNjMDJlMThlYmMzNmYyYjk0NTFhODI4ZjE2YTE1IiwidGFnIjoiIn0%3D; hyiplab_session=eyJpdiI6ImxOUFl2RWg1U0hBa0FQMXBMNzFjNmc9PSIsInZhbHVlIjoicTRKb3J0U2tMZEg2TUFmYzZVNWFveERIMXFUSUxQN2Z1cGZjNHl3STFMT1NMRjRNU1lIem85OVc1b0VLU25lUEFtWVYzV09uZzVJczhMQ0VtTXNTQ2RnK20yU2hXa2duNE5pR290ZktlMEYwRVhQNHpQNnRESVRia0MzNGdKc3kiLCJtYWMiOiI0Yjg3Y2VhMzk3MmExMWRhY2JmMGE3YmNlZDgwODgyN2RkZDgzMjZjNDZkZTI2NDAxMzFhMDNjMDdkNmFjZjgyIiwidGFnIjoiIn0%3D",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; CLT-L29 Build/HUAWEICLT-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]",
   }
    try:
        response = requests.post(url, data=data, headers=headers)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        print("Form submitted successfully.")
        print("Submitted Data:")
        print(f"Username: {mobile}")
        print(f"Email: {email}")
        print(f"Mobile Code: {mobile_code}")
        print(f"Password: {password}")
        print(f"Password Confirmation: {password_confirmation}")
        print(f"Response URL: {response.url}")
    except requests.exceptions.RequestException as e:
        print(f"Form submission failed: {e}")

# Main function
def main():
    password = 'hacker@12345'
    password_confirmation = 'hacker@12345'
    mobile_code = '+977'

    for _ in range(2):  # Loop 2 times
        mobile_base = '9800005678'
        mobile = int(mobile_base) + random.randint(1000, 9999)  # Add a random 4-digit number to mobile_base
        username = f'hacker{generate_random_numbers()}'
        email = f'{username}p{generate_random_numbers()}@gmail.com'
        
        submit_form(_token,area_code, username, email, password, password_confirmation)

if __name__ == "__main__":
    main()
    

