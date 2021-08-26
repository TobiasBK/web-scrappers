# https://www.youtube.com/watch?v=zo7yzIVpIJo&t=188s
from bs4 import BeautifulSoup
import requests

requests = requests.get('https://bbc.com/news')
html = requests.content

soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())