import json

filename = "words.json"
dirs = ["oxford-dictionaries", "phrontistery", "scorpio-tales"]
entries = {}

for dir in dirs:
    with open(dir + "/" + filename) as f:
        words = json.load(f)
        entries.update(words)

with open(filename, 'a') as f:
    json.dump(entries, f)
