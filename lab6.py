# Инициализируем переменные
mas = [[6, 5, 4, 3, 2, 1],
       [6, 5, 4, 3, 2, 1],
       [6, 5, 4, 3, 2, 1],
       [6, 5, 4, 3, 2, 1],
       [6, 5, 4, 3, 2, 1]]
sum = []
keys = []
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0
sum6 = 0

# Считаем суммы
for i in range(5):
       sum1 += mas[i][0]
       sum2 += mas[i][1]
       sum3 += mas[i][2]
       sum4 += mas[i][3]
       sum5 += mas[i][4]
       sum6 += mas[i][5]

# Добаляем суммы в массив
sum.append(sum1)
sum.append(sum2)
sum.append(sum3)
sum.append(sum4)
sum.append(sum5)
sum.append(sum6)

# Делаем словарь из массива и индексов
zipIterator = zip([i for i in range(6)], sum)
sortSum = dict(zipIterator)

# Сортируем словарь по значениям
sortSum = dict(sorted(sortSum.items(), key=lambda item: item[1]))

# Меняем элементы местами
for i in range(6):
       a = int(sortSum[len(sortSum) - i - 1] / 5)
       mas[0][i], mas[1][i], mas[2][i], mas[3][i], mas[4][i] = a, a, a, a, a
