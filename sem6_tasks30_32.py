# Задача 30: Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# first_number = int(input('first number: '))
# diff = int(input('difference: '))
# amount = int(input('amount of numbers: '))
# lst = []

# while amount > 0:
#     lst.append(first_number+(amount-1)*diff)
#     amount -= 1
# print(sorted(lst))

# _____________________________________________________________________________________

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и
# не больше заданного максимума)

from random import randint

start_range = int(input("range start value: "))
end_range = int(input("range end value: "))
n = int(input('Length list: '))
lst = []

for i in range(n):
    lst.append(randint(1, 100))

print(lst)

for j in range(len(lst)):
    if start_range <= lst[j] <= end_range:
        print(j, end=' ')
