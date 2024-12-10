#todo: Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего выполнения
# Пример:
# render, 10,  12.05.2022 12:00
# show,    5,  12.05.2022 12:02
# render, 15,  12.05.2022 12:07
#
# Декоратор должен применяться для различных функций с переменным числом аргументов.
# Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.

import datetime


def count_calls(func):
    func_calls = {}

    def wrapper(*args, **kwargs):
        nonlocal func_calls
        func_name = func.__name__
        now = datetime.datetime.now()
        if func_name not in func_calls:
            func_calls[func_name] = {'count': 0, 'last_call': ''}
        func_calls[func_name]['count'] += 1
        func_calls[func_name]['last_call'] = now
        result = func(*args, **kwargs)
        return result
    wrapper.save_stats = lambda: save_stats(func_calls)
    return wrapper

def save_stats(func_calls):
    with open('debug.log', 'a') as f:
        for func_name, data in func_calls.items():
            f.write(f"{func_name}, {data['count']}, {data['last_call']}\n")


@count_calls
def render():
    print('render')


@count_calls
def show():
    print('show')


@count_calls
def process():
    print('process')



render()
process()
show()
show()
process()


render.save_stats()
show.save_stats()
process.save_stats()
