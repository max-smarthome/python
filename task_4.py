"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

import timeit

from collections import OrderedDict as ord

dict_inp = {str(i): i for i in range(1000)}

dict_ordered = ord(dict_inp)


def fill_dict(n):
    dct = dict()
    for i in range(n):
        dct[str(i)] = i


def fill_ordered_dict(n):
    dct = ord()
    for i in range(n):
        dct[str(i)] = i


def take_from_dict(inp_dct):
    for key, value in inp_dct.items():
        k = key
        v = value


def sort_dict(inp_dict):
    return sorted(inp_dict.items(), key=lambda x: x[1])


def get_dict(inp_dict):
    for i in range(100):
        inp_dict.get(str(i))


name_list = ['take_from_dict', 'sort_dict', 'get_dict']


print(f"fill_dict - {timeit.timeit(stmt='fill_dict(1000)', setup='from __main__ import fill_dict', number=1000)}")
print(f"fill__ordered_dict - {timeit.timeit(stmt='fill_ordered_dict(1000)', setup='from __main__ import fill_ordered_dict', number=1000)}")
for i in name_list:
    print(f"{i}_ordered - {timeit.timeit(stmt=i + f'(dict_ordered), ', setup=f'from __main__ import {i}, dict_ordered', number=1000)}")
    print(f"{i} - {timeit.timeit(stmt=i + f'(dict_inp)', setup=f'from __main__ import {i}, dict_inp', number=1000)}")


'''Почти для всех операций OrderedDict медленнее обычного словаря, однако несущественно.
 Скорее всего упорядоченный словарь был полезен до питона 3.5, когда обычный словарь был неупорядоченным.
 Сейчас смысла в его применении особого нет 
fill_dict - 0.22187289999999993
fill__ordered_dict - 0.2745048
take_from_dict_ordered - 0.06224070000000004
take_from_dict - 0.03351550000000003
sort_dict_ordered - 0.10715779999999997
sort_dict - 0.07962730000000007
get_dict_ordered - 0.0222313999999999
get_dict - 0.021088599999999902'''