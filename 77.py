"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 77.py
Автор: 2021 © А.С. Манукян, Челябинск
Лицензия использjвания: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 08/16/2021
Дата последней модификации: 08/16/2021
Описание: Решение задачи № 77
#версия Python:3.9
"""
 Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами. Просуммировать элементы каждой строки матрицы с соответствующими элементами L-й строки.
""
import random

N = 4
M = 5

L = 2


def get_row(column):
    col = []
    for i in range(0, column):
        col.append(random.randint(0, 9))

    return col


def get_matrix(row, column):
    matrix = []
    for i in range(0, row):
        matrix.append(get_row(column))

    return matrix


def print_matrix(matrix):
    i = 0
    while i < len(matrix):
        j = 0
        row = matrix[i]
        while j < len(row):
            column = row[j]
            print(column, end=' ')
            j += 1

        print()
        i += 1


A = get_matrix(N, M)
print("Исходная матрица:")
print_matrix(A)


l_row = A[L - 1].copy()

i = 0
while i < len(A):
    j = 0

    while j < len(A[i]):
        A[i][j] += l_row[j]
        j += 1

    i += 1

print("Моифицированная матрица:")
print_matrix(A)
