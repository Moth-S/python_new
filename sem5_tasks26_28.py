# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# def exponentiate(a, b):
#     if b == 0:
#         return 1
#     elif b == 1:
#         return a
#     else:
#         return a*exponentiate(a, b-1)


# A = int(input('number: '))
# B = int(input('extent: '))
# print(exponentiate(A, B))

# _______________________________________________________________________________________________________

# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4

def summa_of_two_num(num1, num2):

    if num2 == 0:
        return a
    else:
        return summa_of_two_num(num1, num2-1)+1


a = int(input('number#1: '))
b = int(input('number#2: '))

print(summa_of_two_num(a, b))
