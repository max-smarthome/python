"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""

import timeit
from random import randint
from functools import lru_cache

n_6 = randint(100000, 1000000)
n_7 = randint(1000000, 10000000)
n_8 = randint(10000000, 100000000)


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


print('Решение без мемоизации')
print('Время на числе 6 знаках ', timeit.timeit("recursive_reverse(n_6)",
                                                setup="from __main__ import recursive_reverse, n_6",
                                                number=10000))
print('Время на числе 7 знаках ', timeit.timeit("recursive_reverse(n_7)",
                                                setup="from __main__ import recursive_reverse, n_7",
                                                number=10000))
print('Время на числе 8 знаках ', timeit.timeit("recursive_reverse(n_8)",
                                                setup="from __main__ import recursive_reverse, n_8",
                                                number=10000))

'''Решение без мемоизации
Время на числе 6 знаках  0.02270289999999997
Время на числе 7 знаках  0.026075799999999982
Время на числе 8 знаках  0.02922659999999999'''


# декоратор для мемоизации.
# Можно обойтись без декоратора, а сохранять данные в словарь внутри функции,
# но с декоратором выглядит красивее и практичнее
def memo(func):
    memo_cash = {}

    def decorator(*args):
        if args not in memo_cash:
            memo_cash[args] = func(*args)
        return memo_cash[args]

    return decorator


# с помощью мемоизации написанной вручную
@memo
def recurs_reverse_memo(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


print('Решение с собственной мемоизацией')
print('Время на числе 6 знаках ', timeit.timeit("recurs_reverse_memo(n_6)",
                                                setup="from __main__ import recurs_reverse_memo, n_6",
                                                number=10000))
print('Время на числе 7 знаках ', timeit.timeit("recurs_reverse_memo(n_7)",
                                                setup="from __main__ import recurs_reverse_memo, n_7",
                                                number=10000))
print('Время на числе 8 знаках ', timeit.timeit("recurs_reverse_memo(n_8)",
                                                setup="from __main__ import recurs_reverse_memo, n_8",
                                                number=10000))
'''Решение с собственной мемоизацией
Время на числе 6 знаках  0.0019295000000000284
Время на числе 7 знаках  0.0019135000000000124
Время на числе 8 знаках  0.0019304999999999461'''


# для сранения скорости встроенных и написанных функций
# можно взять встроенный мемоизатор из пакета functools

@lru_cache()
def recurs_reverse_memo_auto(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


print('Решение с встроенной мемоизацией')
print('Время на числе 6 знаках ', timeit.timeit("recurs_reverse_memo_auto(n_6)",
                                                setup="from __main__ import recurs_reverse_memo_auto, n_6",
                                                number=10000))
print('Время на числе 7 знаках ', timeit.timeit("recurs_reverse_memo_auto(n_7)",
                                                setup="from __main__ import recurs_reverse_memo_auto, n_7",
                                                number=10000))
print('Время на числе 8 знаках ', timeit.timeit("recurs_reverse_memo_auto(n_8)",
                                                setup="from __main__ import recurs_reverse_memo_auto, n_8",
                                                number=10000))

'''Решение с встроенной мемоизацией
Время на числе 6 знаках  0.0006384999999999863
Время на числе 7 знаках  0.000657899999999989
Время на числе 8 знаках  0.0005782999999999205'''

'''как видно из примеров решение с мемоизацией значительно уменьшает время выполнения функции. 
Это вызвано тем, что при решении без мемоизации, функции вызываются повторно, 
а с мемоизацией значения сохраняютс в кэш. При этом, если использовать встроенную мемоизацию из встроенного модуля 
functools, то решение повышается еще значительнее. Это вывзвано тем, что встроенные фукнции всегда работают быстрее'''
