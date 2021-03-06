"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: Задание 17.py
Автор: 2020 © А.С. Манукян, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 12/12/2020
Дата последней модификации: 12/12/2020
Описание: Решение задачи № 17
#версия Python:3.9
"""
Имеются две ёмкости: кубическая с ребром A, цилиндрическая с высотой H и радиусом основания R. Определить, поместится ли жидкость объёма M в первую ёмкость, во вторую, в обе.
""
import math
A = int(input("Ребро кубической ёмкости:"))
H = int(input("Высота цилиндрической ёмкости:"))
R = int(input("Радиус основания цилиндрической ёмкости:"))
M = int(input("Введите объем жидкости:"))
SK = A ** 3
print(SK, "Объём куба")
SC = math.pi * R ** 2 * H
print(SC, "Объём цилиндра")
if M < SC and M < SK:
    print("Жидкость поместится в оба сосуда")
if M < SC:
    print("Жидкость поместится в цилиндр")
if M < SK:
    print("Жидкость поместится в куб")
