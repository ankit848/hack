import browser_cookie3

# Get cookies from Chrome
chrome_cookies = browser_cookie3.chrome()

# Print the cookies
print("Cookies from Chrome:")
for cookie in chrome_cookies:
    print(cookie.name, ":", cookie.value)
