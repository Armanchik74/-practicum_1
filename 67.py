"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 67.py
Автор: 2021 © А.С. Манукян, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 29/01/2021
Дата последней модификации: 29/01/2021
Описание: Решение задачи № 67
#версия Python:3.9
"""
Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами. Найти наибольший элемент столбца матрицы A, для которого сумма абсолютных значений элементов максимальна.
""

import random
N = 4  # строк
M = 4  # столбцов

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

def listsum(list):
    sum = 0
    for element in list:
        sum += element

    return sum

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

tmp = list(zip(*A))

max_sum = 0
index_column_max_sum = 0

i = 0
while i < len(tmp):
    column = tmp[i]
    current_list_sum = listsum(column)
    if current_list_sum > max_sum:
        max_sum = current_list_sum
        index_column_max_sum = i

    i += 1

print("Матрица:")
print_matrix(A)
print("Cтолбец, для которого сумма абсолютных значений элементов максимальна:",
      index_column_max_sum)
print("Наибольший элемент этого столбца:", max(tmp[index_column_max_sum]))
