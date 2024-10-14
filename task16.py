# todo: База данных пользователя.
# Задан массив объектов пользователя


users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

# Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
# ,первой букве логина, и заданной группе.

#Сперва вводится тип сортировки:

a = int(input('''Тип сортировки:
1. По возрасту
2. По первой букве
3. По группе
=>  '''))



#Затем сообщение для ввода
k = input('Ввидите критерии поиска:')

match a:
    case 1:
        for i in users:
            if i['age'] > int(k):
                print (i)
    case 2:
        for i in users:
            if i['login'] > k:
                print(i)
    case 3:
        for i in users:
            if i['group'] > k:
                print(i)

#Пользователь: 'Piter' возраст 23 года , группа  "admin"
#Пользователь: 'Dasha' возраст 30 лет , группа  "master"




