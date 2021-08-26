# hackerNews scrapper for django
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Creates a header
# headers = {'User-agent': 'Mozilla/5.0'}

hn_r = requests.get("https://news.ycombinator.com/")
hn_soup = BeautifulSoup(hn_r.content, 'html5lib')
hn_headings = hn_soup.findAll("td", {"class": "title"})
hn_news = []

for hnh in hn_headings:
    hn_news.append(hnh.text)

#django function
def index(req):
    return render(req, 'core/index.html', {'hn_news': hn_news})

