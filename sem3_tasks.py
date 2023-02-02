# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

length_list = int(input('Length list: '))
lst = []
summa = 0

for i in range(length_list):
    lst.append(randint(1,10))

for j in range(len(lst)):
    if j % 2 == 1:
        summa += lst[j]

print(f"{lst} -> answer {summa}")




