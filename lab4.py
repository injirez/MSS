import re

TEST = []
sortTest = {}
marks = []

with open('src/TEST.txt') as f:
    for line in f:
        TEST.append(line.replace('\n', ''))

for elem in TEST:
    mark = re.sub('[а-яА-Я]', '', elem)
    plusNum = mark.count('+')
    marks.append(plusNum)

zipIterator = zip(TEST, marks)
resDict = dict(zipIterator)
resDict = dict(sorted(resDict.items(), key=lambda item: item[1], reverse=True))

for key, value in resDict.items():
    print(key.replace('+', '').replace('-', ''))

