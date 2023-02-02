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

from random import randint

lst, lst_sum_pairs = [], []
length_list = int(input("Length list: "))

for j in range(length_list):
    lst.append(randint(1, 10))

i = 0
while i < len(lst) // 2 + len(lst) % 2:
    lst_sum_pairs.append(lst[i] * lst[len(lst) - 1 - i])
    i += 1

print(f"{lst} => {lst_sum_pairs}")





