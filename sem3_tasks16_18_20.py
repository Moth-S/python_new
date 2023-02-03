# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
#  Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
#   В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# пример
# 5
# 1 2 3 4 5
# 3
# -> 1

# from random import randint

# length_list = int(input('Length list: '))
# lst = []

# for i in range(length_list):
#     lst.append(randint(1, 10))

# print(lst)

# desired_value = int(input('value search: '))
# print(f"-> {lst.count(desired_value)}")

# _____________________________________________________________________________________________

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# пример
# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint

length_list = int(input('Length list: '))
lst = []
difference = 11

for i in range(length_list):
    lst.append(randint(1, 10))

print(lst)

num = int(input('number: '))

for j in lst:
    if abs(j-num) < difference:
        difference = abs(j-num)
        near_num = j

print(near_num)


