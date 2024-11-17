
#todo: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы.

# Пример:
mass = [1,2,17,54,30,89,2,1,6,2]

from random import randint as ri
n=int(input('Введите размер массива: '))
mass=[None]*n
for i in range(n):
    mass[i]=ri(0,10)
print(mass)

min_distance = n
min_indices = [None]*2

for i in range(len(mass)):
    for j in range(i + 1, len(mass)):
        if mass[i] == mass[j]:
            distance = j - i
            if distance < min_distance:
                min_distance = distance
                min_indices = [i, j]

if min_indices[0] != None:
    print(f"Минимальное расстояние: {min_distance}, Индексы: {min_indices}")
else:
    print('Одинаковых чисел в массиве нет')

# Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
# Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
# Для числа 17 нет минимального растояния т.к элемент в массиве один.
