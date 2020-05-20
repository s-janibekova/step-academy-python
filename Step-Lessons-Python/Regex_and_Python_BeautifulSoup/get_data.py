import requests
from bs4 import BeautifulSoup


page = requests.get("http://google.com")
soup = BeautifulSoup(page.content, 'html.parser')

print(soup)