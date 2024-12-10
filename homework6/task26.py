# #todo Задача 1. Чтение матрицы, load_matrix(filename)
# # Дан файл, содержащий таблицу целых чисел вида
# (в каждой строке через пробел записаны числа)
#
# 11 12 13 14 15 16
# 21 22 23 24 25 26
# 31 32 33 34 35 36
#
#
# Требуется написать функцию load_matrix(filename) которая загружает эту таблицу из файла.
# Если в каждой строке находится одинаковое количество чисел, функция возвращает список списков целых чисел.
# В противном случае возвращает False.
#
# Задачу следует решить с использованием списковых включений, циклы использовать НЕЛЬЗЯ!

filename = 'matrix.txt'

def load_matrix(filename):
    f = open(filename, 'r', encoding='utf-8')
    lines =f.readlines()
    l= len(lines[0].split())
    a = [False if len(li.split())!=l else True for li in lines]
    if all(a):
        matrix= [[int(i) for i in li.split()] for li in lines]
    else:
        matrix = False
    return matrix

file = 'matrix.txt'
print(load_matrix(file))
