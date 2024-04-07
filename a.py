import requests
session = requests.Session()
id = "MPL2298238"
pas = "9807298843"
url = 'https://moneypluslife.info/panel/Authentic'
data = {
    "u1": id,
    "p1": pas,
    "1d2es5e8s": "",  # Make sure this empty string is intentional
}
headers = {
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "*/*",
    "Origin": "https://moneyplus.info",
    "Referer": "https://moneypluslife.info/panel/login",  # Corrected referer URL
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; CLT-L29 Build/HUAWEICLT-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]",
}

try:
    response = session.post(url, data=data, headers=headers)
    print(response)
    """
    response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
    try:
        json_response = response.json()
        print(json_response)
    except json.JSONDecodeError as e:
        print("Failed to decode JSON response:", e)
        print("Response content:", response.content.decode())
           """
except requests.RequestException as e:
    print("An error occurred:", e)
 
