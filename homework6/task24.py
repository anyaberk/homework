#todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.
#
# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!
input_ = "8 5 12 12 15 , 0 23 15 18 12 4 ! "
list_=[chr(96 + int(x)) if (x.isdigit()) and (int(x)>0) else x for x in  input_.split()]
print(list_)
list_ = filter(lambda x: not(x.isdigit() and int(x) <= 0), list_)
str = ''.join(list_)
print(str)


