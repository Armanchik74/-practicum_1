"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: Задание 55.py
Автор: 2020 © А.С. Манукян, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 19/12/2020
Дата последней модификации: 19/12/2020
Описание: Решение задачи № 55
#версия Python:3.9
"""
Заданы M строк слов, которые вводятся с клавиатуры (в каждой строке – одно слово). Вводится слог (последовательность букв). Удалить данный слог из каждой строки.
""
import re
M = 3
list_strings = []

for i in range(0, M):
    print("Введите строку:", end=' ')
    list_strings.append(input())
print("Введите слог:", end=' ')
syllable = input()

for string in list_strings:
    string = re.sub(syllable, '', string)
    print(string)
