import requests
from bs4 import BeautifulSoup

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

token = get_token()
if token:
    print("Token obtained successfully:", token)
else:
    print("Failed to obtain token.")
