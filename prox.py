import requests

# Fetch the proxy list from the URL
proxies_url = "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt"
try:
    response = requests.get(proxies_url)
    if response.status_code == 200:
        # Extract proxies from the response
        proxies_list = response.text.strip().split('\n')

        # Iterate over each proxy
        for proxy in proxies_list:
            proxy = proxy.strip()  # Remove leading/trailing whitespaces
            if not proxy:
                continue  # Skip empty lines
            proxies = {
                'http': 'http://' + proxy,
                'https': 'https://' + proxy
            }

            # Make a request using the proxy
            try:
                response = requests.get('http://example.com', proxies=proxies, timeout=5)
                if response.status_code == 200:
                    print("Connected to proxy {} successfully!".format(proxy))
                else:
                    print("Failed to connect to proxy {}. Status code: {}".format(proxy, response.status_code))
            except requests.exceptions.RequestException as e:
                print("Error connecting to proxy {}: {}".format(proxy, e))
    else:
        print("Failed to fetch proxy list. Status code:", response.status_code)
except requests.exceptions.RequestException as e:
    print("Error fetching proxy list:", e)
