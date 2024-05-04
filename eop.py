import requests
import random

# Function to generate random numbers
def generate_random_numbers():
    return ''.join(str(random.randint(0, 9)) for _ in range(3))

# Function to submit form data
def submit_form(emtoken, user_email, user_pass, user_conpass, terms_check, user_ref):
      url = 'https://earnzop.com/register/'
  
    data = {
        'emtoken': emtoken,
        'user_name': user_name,
        'user_email': user_email,
        'user_pass': user_pass,
        'user_conpass': user_conpass,
        'terms_check': term_check,
        'user_ref': user_ref
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; CLT-L29 Build/HUAWEICLT-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]",
    }
    response = requests.post(url, data=data, headers=headers)
    print(user_name)
    print(response.url)
    if 'https://earnzop.com/dashboard/' in response.url:
        print("Form submitted successfully.")
    else:
        print("Form submission failed.")

# Main function
def main():
        for _ in range(2):
            emtoken = 'e5b431e58da1f00b8fe8b04c60f73f1d7a36d28d61b1d8c974ebcb50d56ac02d'
            user_pass = 'hacker@1234a55'
            user_conpass = 'hacker@1234a55'
            terms_check = 'on'  # Define area_code within the main function
            user_ref = 'AB1BB'
            submit_form(emtoken, user_email, user_pass, user_conpass, terms_check, user_ref)
            if __name__ == "__main__":
                main()
