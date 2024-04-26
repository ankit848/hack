import http.cookiejar
import os

def get_chrome_cookies():
    # Path to Chrome's cookie file
    cookie_file_path = os.path.expanduser("~/.config/google-chrome/Default/Cookies")

    # Create a MozillaCookieJar object
    cookie_jar = http.cookiejar.MozillaCookieJar()

    # Load cookies from the Chrome cookie file
    cookie_jar.load(cookie_file_path, ignore_discard=True, ignore_expires=True)

    # Return the cookies
    return cookie_jar

# Example usage
chrome_cookies = get_chrome_cookies()
for cookie in chrome_cookies:
    print(cookie)
