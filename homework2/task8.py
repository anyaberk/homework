# todo: Проверить истинность высказывания: "Данное четырехзначное число читается одинаково слева направо и справа налево".
a = int(input('Введите четырехзначное число: '))
str_a = str(a)
a_obr = str_a[3:4] + str_a[2:3] + str_a[1:2] + str_a[0:1]
print(f'Данное четырехзначное число читается одинаково слева направо и справа налево : {str_a == a_obr}')