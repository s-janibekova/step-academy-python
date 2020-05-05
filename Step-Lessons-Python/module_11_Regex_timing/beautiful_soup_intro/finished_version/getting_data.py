import requests
from bs4 import BeautifulSoup


page = requests.get('http://www.google.com')
soup = BeautifulSoup(page.content, 'html.parser')


print(soup)