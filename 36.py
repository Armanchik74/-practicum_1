"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: Задание 36.py
Автор: 2020 © А.С. Манукян, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 17/12/2020
Дата последней модификации: 17/12/2020
Описание: Решение задачи № 36
#версия Python:3.9
"""
Дан одномерный массив числовых значений, насчитывающий N элементов. Вставить группу из M новых элементов, начиная с позиции K.
""
import array
import random

N = int(input("Введите количество элементов массива "))
M = int(input("Количесвто элементов в группе"))
K = int(input("Позиция K"))
A = [random.randint(0, 100) for i in range(0, N)]
B = [random.randint(0, 100) for b in range(0, M)]

print(A)
print(B)

A.insert(K, B)
print(A)
