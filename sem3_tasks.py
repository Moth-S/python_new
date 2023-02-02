# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# from random import randint

# length_list = int(input('Length list: '))
# lst = []
# summa = 0

# for i in range(length_list):
#     lst.append(randint(1,10))

# for j in range(len(lst)):
#     if j % 2 == 1:
#         summa += lst[j]

# print(f"{lst} -> answer {summa}")

# ________________________________________________________________________________________________________________________

# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# from random import randint

# lst, lst_sum_pairs = [], []
# length_list = int(input("Length list: "))

# for j in range(length_list):
#     lst.append(randint(1, 10))

# i = 0
# while i < len(lst) // 2 + len(lst) % 2:
#     lst_sum_pairs.append(lst[i] * lst[len(lst) - 1 - i])
#     i += 1

# print(f"{lst} => {lst_sum_pairs}")

# ________________________________________________________________________________________________________________________

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform

float_lst = []

for i in range(6):
    float_lst.append(round(uniform(0, 20.5), 2))

max_remainder = 0
min_remainder = 0.999

for j in float_lst:

    if j - int(j) > max_remainder:
        max_remainder = j - int(j)

    if j - int(j) < min_remainder:
        min_remainder = j - int(j)

print(f"{float_lst} => {round(max_remainder-min_remainder,2)}")






