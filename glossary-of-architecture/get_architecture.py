from bs4 import BeautifulSoup
import json
import urllib2
import string

BASE_URL = "https://en.wikipedia.org/wiki/Glossary_of_architecture"
filename = "words.json"
entries = {}

res = urllib2.urlopen(BASE_URL)
html = res.read()
soup = BeautifulSoup(html, "lxml")
sections = soup.select("dl")

for s in sections:
    dt = s.select("dt")
    dd = s.select("dd")
    
    if len(dt) == len(dd):
        for i in range(len(dt)):
            word = dt[i].text
            definition = dd[i].text
            if len(dd) < 140:
                entries[word] = definition

    
with open(filename, 'a') as f:
    json.dump(entries, f)
