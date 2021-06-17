"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: Задание 100.py
Автор: 2021 © А.С. Манукян, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 12/05/2021
Дата последней модификации: 12/05/2021
Связанные файлы/пакеты: numpy, random
Описание: Решение задачи №100
#версия Python: 3.9
"""
k = int(input('Введите количество классов: '))
name = [] #Название класа
my_class = {} 
 
for i in range(k):
  n = input('Введите название класса:')
  name.append(n)
  count_of_class_man = int(input('Введите кол-во мальчиков'))
  count_of_class_girl = int(input('Введите кол-во девочек'))
