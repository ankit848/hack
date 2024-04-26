import os
import sqlite3

def get_chrome_cookies():
    # Locate the Cookies file
    user_data_dir = os.path.expanduser("~/.config/google-chrome/Default")  # Update this path as per your system
    cookies_file = os.path.join(user_data_dir, "Cookies")

    # Connect to the SQLite database
    conn = sqlite3.connect(cookies_file)
    cursor = conn.cursor()

    # Query the cookies table
    cursor.execute("SELECT name, value FROM cookies")

    # Fetch all cookies
    cookies = cursor.fetchall()

    # Close the connection
    conn.close()

    return cookies

# Get and print Chrome cookies
chrome_cookies = get_chrome_cookies()
print("Cookies from Chrome:")
for cookie in chrome_cookies:
    print(cookie[0], ":", cookie[1])
