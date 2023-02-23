# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и
# выводить на печать построчно последние строки в количестве lines
# (на всякий случай проверим, что задано положительное целое число).
# Протестируем функцию на файле «article.txt» со следующим содержимым:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

# with open('file.txt', 'r', encoding='utf-8') as file:
#     f = file.read().splitlines()
#     num_end_words = int(input(f'Number of last rows (from 1 to {len(f)}): '))

#     for elem in range(num_end_words*(-1), 0):
#         print(f[elem])

# ____________________________________________________________________________________________________

# Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

# Требуется реализовать функцию longest_words(file), которая выводит слово,
# имеющее максимальную длину (или список слов, если таковых несколько).

# with open('article.txt', 'r', encoding='utf-8') as file:
#     text = file.read().split()
#     max_word = 0

#     [max_word := len(word) for word in text if len(word) > max_word]
#     [print(word) for word in text if len(word) == max_word]

# ____________________________________________________________________________________________________

# ДОП ЗАДАЧА.
# Классическая задача про бассейн, который заполняется через 3 трубы, слишком проста.
# У нас труб будет больше.

# Бассейн можно заполнить из N труб. В файле pipes.txt записаны времена заполнения всего бассейна
# только одной данной работающей трубой (в часах). Затем после пустой строки перечислены трубы,
# которые будут заполнять бассейн. Сколько минут на это потребуется?

# Номер трубы соответствует номеру строки, в которой записана ее производительность.

# Результат запишите в файл time.txt

# Пример
# Ввод

# 1
# 2
# 3
# (пустая строка)
# 1 2 3

# Вывод
# 32.72727272727273
from random import randint

with open('pipes.txt', 'w', encoding='utf-8') as pipes:
    k = 0
    for i in range(int(input('number of pipes: '))):
        pipes.write(str(randint(1, 10))+'\n')
        k += 1

    pipes.write('\n')

    pipes.write(input(f'enter the numbers pipes (from 1 to {k} ) through a space: '))

with open('pipes.txt', 'r', encoding='utf-8') as pipes:
    data=pipes.read().splitlines()

    hour=0
    for pipe in data[-1].split():
        hour+=1/int(data[int(pipe)-1])

    with open('time.txt', 'w', encoding='utf-8') as time:
        time.write(str(60/hour))
