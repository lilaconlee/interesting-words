from bs4 import BeautifulSoup
import json
import urllib2

BASE_URL = "http://users.tinyonline.co.uk/gswithenbank/unuwords.htm"
filename = "words.json"
entries = {}

res = urllib2.urlopen(BASE_URL)
html = res.read()
soup = BeautifulSoup(html, "lxml")
trs = soup.select('table')[0].select('tr')

for tr in trs:
    if len(tr) == 2:
        e = tr.select('td')
        word = e[0].text
        definition = e[1].text
        entries[word] = definition

with open(filename, 'a') as f:
    json.dump(entries, f)
