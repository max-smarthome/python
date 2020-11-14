"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список программно, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
def time_decor(func):
    import time

    def time_func(*args, **kwargs):
        start = time.time()
        res = func(*args)
        end = time.time()
        print(f'Время выполнения {end - start}')
        return res
    return time_func

@time_decor
def list_fill(n):
    lst = list()
    for i in range(n):
        lst.append(i)
    return lst

@time_decor
def list_oper(lst):
    for i in range(len(lst) - 1):
        lst.index(i)


@time_decor
def dict_fill(n):
    dct = dict()
    for i in range(n):
       dct[i] = i
    return dct

@time_decor
def dict_oper(dct):
    for i in range(len(dct) - 1):
        dct.get(i)


list_save = list_fill(100000)
dict_save = dict_fill(100000)
list_oper(list_save)
dict_oper(dict_save)

#словарь заполняется дольше так как требуется хешировать каждый объект, однако со словарем быстрее работать, так как есть функция get