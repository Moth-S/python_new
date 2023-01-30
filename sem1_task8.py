# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('horizontal quantity: '))
m = int(input('vertical quantity: '))
k=int(input('How many slices need to be broken off? '))

if k%n==0 or k%m==0:
    print('yes')
else:
    print('no')