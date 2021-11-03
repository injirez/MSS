import re

TEST = []
sortTest = {}
marks = []

# Считываеи файл и записываем в массив
with open('src/TEST.txt') as f:
    for line in f:
        TEST.append(line.replace('\n', ''))

# Удаляем имена и считаем кол-во плюсов
for elem in TEST:
    mark = re.sub('[а-яА-Я]', '', elem)
    plusNum = mark.count('+')
    # Добавляем оценки в массив
    marks.append(plusNum)

# Делаем из массивов словарь
zipIterator = zip(TEST, marks)
resDict = dict(zipIterator)
# Сортируем словарь по значениям
resDict = dict(sorted(resDict.items(), key=lambda item: item[1], reverse=True))

# Выводим значения
for key, value in resDict.items():
    print(key.replace('+', '').replace('-', ''))

