"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: Задание 90.py
Автор: 2021 © А.С. Манукян, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 12/05/2021
Дата последней модификации: 12/05/2021
Связанные файлы/пакеты: numpy, random
Описание: Решение задачи №90
#версия Python: 3.9
"""
p1 = [c for r in matrix[:L] for c in r[:K]]
p2 = [c for r in matrix[:L] for c in r[K+1:]]
p3 = [c for r in matrix[L+1:] for c in r[:K]]
p4 = [c for r in matrix[L+1:] for c in r[K+1:]]
