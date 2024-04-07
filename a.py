import requests
import uuid
import random
import os
import time
import json
import string

proxy_url = 'https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt'

try:
    response = requests.get(proxy_url)
    if response.status_code == 200:
        proxies_list = response.text.strip().split('\n')
        random_proxy = random.choice(proxies_list)  # Select a random proxy from the list
    else:
        print("Failed to fetch proxies from the provided URL.")

    uid = "shresthaankit444@gmail.com"
    ps = "rakesh12@"

    def one():
        ua = 'Dalvik/2.1.0 (Linux; U; Android 11; SM-G986U Build/RP1A.200720.012) [FBAN/Orca-Android;FBAV/316.4.0.15.120;FBPN/com.facebook.orca;FBLC/en_US;FBBV/297403762;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBDV/SM-G986U;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2201};FB_FW/1;]'
        return ua

    session = requests.Session()
    session.proxies = {'http': f'http://{random_proxy}', 'https': f'https://{random_proxy}'}

    data = {
        "adid": str(''.join(random.choices(string.hexdigits, k=16))),
        "format": "json",
        "device_id": str(uuid.uuid4()),
        "email": uid,
        "password": ps,
        "generate_analytics_claims": "1",
        "credentials_type": "password",
        "source": "login",
        "error_detail_type": "button_with_disabled",
        "enroll_misauth": "false",
        "generate_session_cookies": "1",
        "generate_machine_id": "1",
        "fb_api_req_friendly_name": "authenticate",
    }
    headers = {
        "Accept-Encoding": "gzip, deflate",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "User-Agent": one(),
        "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
        "X-FB-Friendly-Name": "authenticate",
        "X-FB-Connection-Type": "unknown",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-FB-HTTP-Engine": "Liger",
        "Content-Length": "329",
    }
    url = 'https://b-graph.facebook.com/auth/login'
    po = session.post(url, data=data, headers=headers).json()
    print(po)

except requests.RequestException as e:
    print("An error occurred:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
