import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

'''
Supports:
https://www.pornhat.com/
'''

class Colors:
    header = '\033[95m'
    okblue = '\033[94m'
    okcyan = '\033[96m'
    okgreen = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    endc = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'


# Constants
base_url = 'https://www.pornhat.com/video/bunny-colby-and-quinton-james-s-big-cock-porn-by-adult-mobile/'
user_agent = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36"
default_domain = '{uri.scheme}://{uri.netloc}/'.format(uri=urlparse(base_url))
headers = {
    "Referer": default_domain,
    "User-Agent": user_agent
}

# Fetch page content
response = requests.get(base_url, headers=headers).text
soup = BeautifulSoup(response, 'html.parser')

# Extract video URL
video_url = soup.select_one('.video_720p', attrs={'label': '720p'})['src']

# Print results
print("\n" + "#" * 25 + "\n" + "#" * 25)
print(f"Captured URL: {Colors.okgreen}{video_url}{Colors.endc}")
print("#" * 25 + "\n" + "#" * 25)
print("\n")