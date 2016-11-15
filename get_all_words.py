import json

filename = "words.json"
dirs = [
        "glossary-of-architecture",
        "oxford-dictionaries",
        "personal-stash",
        "phrontistery",
        "scorpio-tales",
        ]
entries = {}

for dir in dirs:
    with open(dir + "/" + filename) as f:
        words = json.load(f)
        entries.update(words)

with open(filename, 'w') as f:
    json.dump(entries, f)
