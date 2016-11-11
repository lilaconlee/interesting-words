from bs4 import BeautifulSoup
import json
import urllib2
import string

BASE_URL = "https://en.oxforddictionaries.com/explore/weird-and-wonderful-words"
filename = "words.json"
entries = {}

res = urllib2.urlopen(BASE_URL)
html = res.read()
soup = BeautifulSoup(html, "lxml")
table = soup.select("table")[0].select('tr')
for tr in table:
    e = tr.select('td')
    word = e[0].text.strip()
    definition = e[1].text.strip()
    entries[word] = definition

with open(filename, 'a') as f:
    json.dump(entries, f)
