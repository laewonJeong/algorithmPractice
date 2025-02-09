import sys
import re

input = sys.stdin.readline
html = input()

divs = re.findall('<div title="(.*?)">(.*?)</div>', html)

for title, paragraph in divs:
    print(f'title : {title}')
    sentence = re.findall('<p>(.*?)</p>', paragraph)
    for s in sentence:
        s = re.sub('(<.*?>)', '', s)
        s = re.sub('\s+', ' ', s)
        print(s)