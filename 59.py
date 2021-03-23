"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: Задание 59.py
Автор: 2020 © А.С. Манукян, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 19/12/2020
Дата последней модификации: 19/12/2020
Описание: Решение задачи № 59
#версия Python:3.9
"""
Заданы M строк, которые вводятся с клавиатуры. Подсчитать количество пробелов в каждой из строк.
""
import re
M = 3

list_strings = []
for i in range(0, M):
    print("Введите строку:", end=' ')
    list_strings.append(input())

for string in list_strings:
    count_spaces = len(re.findall(r'\s', string))
    print("В строке \"%s\" %s пробелов" % (string, count_spaces))
