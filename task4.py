# todo: Заданы три числа в переменных x, y, z.
# Напечатать наибольшее из этих чисел.
# Пример:
# x = 10
# y = 15
# z = 2
# Ответ:
# Наибольшее число 15

# Пример:
# x = 77
# y = 9
# z = 130
# Ответ:
# Наибольшее число 130

x=int(input('х = '))
y=int(input('y = '))
z=int(input('z = '))

max_num = x
if y > max_num:
    max_num = y
if z > max_num:
    max_num =z
print (f'Наибольшее число {max_num}')
