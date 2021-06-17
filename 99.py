"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: Задание 99.py
Автор: 2021 © А.С. Манукян, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 12/05/2021
Дата последней модификации: 12/05/2021
Связанные файлы/пакеты: numpy, random
Описание: Решение задачи №99
#версия Python: 3.9
"""
students = [
    ('first', 20, 30, 50),
    ('second', 100, 0, 50),
    ('third', 10, 50, 60),
]
 
def avg3(a, b, c):
    return (a + b + c) / 3.0
 
def sort_by_avg(student):
    return -avg3(student[1], student[2], student[3])
 
print(sorted(students, key = sort_by_avg))
