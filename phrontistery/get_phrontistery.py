from bs4 import BeautifulSoup
import json
import os
import urllib
import urllib2
import string

BASE_URL = "http://www.phrontistery.info/"
filename = "words.json"
letters = string.ascii_lowercase
entries = {}

for l in letters:
    res = urllib2.urlopen(BASE_URL + l + ".html")
    html = res.read()
    soup = BeautifulSoup(html, "lxml")
    table = soup.select('table[class="words"]')[0].select('tr')
    for tr in table:
        e = tr.select('td')
        word = e[0].text.strip()
        definition = e[1].text.strip()
        entries[word] = definition

with open(filename, 'a') as f:
    json.dump(entries, f)
