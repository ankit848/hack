import requests
session = requests.Session()
id = "MPL2298238"
pas = "980720098843"
url = 'https://moneypluslife.info/panel/Login'
data = {
    "u1": id,
    "p1": pas
}
headers = {
    "Accept-Encoding": "gzip, deflate",
    "Accept": "*/*",
     "path":"/panel/Authentic",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; CLT-L29 Build/HUAWEICLT-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]"
}

response = requests.post(url, data=data, headers=headers)
print(response)
if 'session_key' in response:
    print('Logged in successfully.')
else:
    print("Login failed.")

