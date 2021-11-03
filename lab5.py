# Массив для записи содержимого файла
lines = []

# Считываеи файл и записываем в массив
with open('src/LIST01.txt') as f:
    for line in f:
        lines.append(line.replace('\n', ''))

# Отрываем файл для записи
f = open('src/LIST02.txt', 'w')

# Редактируем строки
for line in lines:
    line = ' '.join(line.split())
    line = line[0].upper() + line[1:]
    if line[-1] != '.':
        line += '.'

    # Записываем в файл
    f.write(line + '\n')

