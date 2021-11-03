# Инициализируем входную строку
inputStr = 'A       B 16'
# Разбиваем строку на массив и присваеваем значения
nums = inputStr.split()
num1 = nums[0]
num2 = nums[1]
system = int(nums[2])

# Переводим числа в десятичную систему счисления и считаем сумму
def sum(first, second, system):
    first = int(first, system)
    second = int(second, system)

    return first + second

# Выводим результат
print(sum(num1, num2, system))