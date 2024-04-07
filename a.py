import requests
import uuid
import random
import os
import time
import json
import string  # Add import for string module

session = requests.Session()
uid = "shresthaankit444@gmail.com"
ps = "rakesh12@"

def one():
    ua = 'Mozilla/5.0 (Linux; Android 12; 22011119UY Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]'
    return ua

try:
    fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'
    fbbv = str(random.randint(111111111, 999999999))
    android_version = '12'  # Assuming these values, you should replace them with actual values.
    model = 'YourModel'
    build = 'YourBuild'
    fblc = 'YourFblc'
    fbcr = 'YourFbcr'
    fbmf = 'YourFbmf'
    fbbd = 'YourFbbd'
    fbdv = 'YourFbdv'
    fbsv = 'YourFbsv'
    fbca = 'YourFbca'
    fbdm = 'YourFbdm'

    data = {
        "adid": str(''.join(random.choices(string.hexdigits, k=16))),  # Fix typo here, it should be `choices` instead of `choices`.
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
        "User-Agent": one(),  # Fix function call, it should be `one()` instead of `ONE()`.
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
    """
    if 'sessiony' in po:
        print("Success")
    else:
        print('Error')
        """
except requests.exceptions.ConnectionError:
    time.sleep(20)
except Exception as e:
    pass

