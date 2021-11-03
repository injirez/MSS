# Входная строка
inputStr = '7  14 231 187 256 -12'

# Разбиваем строку на массив
inputStr = inputStr.split()
# Присваеваем значение системе счисления
system = int(inputStr[0])
# Инициализируем строку результата
resStr = '{} '.format(system)

# Переводим числа в десятичную систему счисления и ловим неккоректные данные
for i in range(1, len(inputStr)):
    try:
        resStr += str(int(inputStr[i], system)) + ' '
    except:
        print(inputStr[i], '- is noit valid')

# Выводим результат
print(resStr)