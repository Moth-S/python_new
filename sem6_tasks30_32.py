# Задача 30: Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_number = int(input('first number: '))
diff = int(input('difference: '))
amount = int(input('amount of numbers: '))
lst = []

while amount > 0:
    lst.append(first_number+(amount-1)*diff)
    amount -= 1
print(sorted(lst))
