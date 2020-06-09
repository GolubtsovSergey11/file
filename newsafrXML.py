import xml.etree.ElementTree as ET

parse = ET.XMLParser(encoding='utf-8')
tree = ET.parse('newsafr.xml', parse)
root = tree.getroot()

xml_items = root.findall('channel/item')
words_count = {}
for xml in xml_items:
    xmls = xml.find('description').text
    for word in xmls.split():
        if len(word) > 5:
            words_count[word.lower()] = words_count.get(word.lower(), 0) + 1

top = []
for key, value in words_count.items():
    top.append((value, key))
top.sort(reverse=True)
i = 0

for item in top[0:10]:
    i += 1
    print(f'{i}) Слово "{item[1].title()}" встречается {item[0]}')

