# Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

num = int(input("enter a three-digit number: "))
print(num//100 + num % 100//10 + num % 10)
