#todo: Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу.

from random import randint as ri

arr = [0,1,2,3,4,5,6,7,8,9 ]

for i in range (10):
    arr[i] = ri(0,9999)

print(arr)

for i in range (10):
    arr[i] += 1

print(arr)