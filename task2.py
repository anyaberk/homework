# todo: Преобразуйте переменную age и foo в число
age = "23"
foo = "23abc"
age = int(age)
print (age, type(age))
# foo=int(foo)
# print (foo, type(foo))
#
# Преобразуйте переменную age в Boolean
age = "123abc"
age = bool(age)
print (age, type(age))
#
# Преобразуйте переменную flag в Boolean
flag = 1
flag = bool(flag )
print (flag , type(flag ))
#
# Преобразуйте значение в Boolean
str_one = "Privet"
str_two = ""
str_one = bool(str_one)
print (str_one , type(str_one))
str_two = bool(str_two)
print (str_two , type(str_two))
#
# Преобразуйте значение 0 и 1 в Boolean
print (f'0 = {bool(0)}')
print (f'1 = {bool(1)}')
#
# Преобразуйте False в строку
print(str(False))