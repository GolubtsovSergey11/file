import json

with open('newsafr.json') as f:
    date = json.load(f)
    words_count = {}
    for items in date['rss']['channel']['items']:
        for word in items['description'].split():
            if len(word) > 5:
                words_count[word.lower()] = words_count.get(word.lower(), 0) + 1

    top = []
    for key, value in words_count.items():
        top.append((value, key))
        #print(top)
    top.sort(reverse=True)
    i = 1
    for item in top[0:10]:
        print(f'{i}. Слово "{item[1]}" встречается {item[0]} раз.')
        i += 1
