"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: Задание 20.py
Автор: 2020 © А.С. Манукян, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 12/12/2020
Дата последней модификации: 12/12/2020
Описание: Решение задачи № 20
#версия Python:3.9
"""
Дано число X. Определить, принадлежит ли это число заданному промежутку [a,b].
""
import math
x = int(input("Введите число для проверки:"))
a = int(input("Укажите начало промежутка:"))
b = int(input("Укажите конец промежутка:"))

if math.fabs(a) <= math.fabs(x) <= math.fabs(b):
    print("Число ",x, " Принадлежит множеству [",a,",",b,"]")
else:
    print("Число ",x, " не принадлежит множеству [",a,",",b,"]")
