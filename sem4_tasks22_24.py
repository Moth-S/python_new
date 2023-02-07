# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n = int(input('Length first list: '))
m = int(input('Length second list: '))
lst1, lst2 = [], []

strng1=input('input elements of 1st list (through a space): ').split()
for i in strng1:
    lst1.append(i)

strng2=input('input elements of 2nd list (through a space): ').split()
for j in strng2:
    lst2.append(j)

print(set(lst1) & set(lst2))
