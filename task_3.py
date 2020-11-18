"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import timeit
import cProfile
from random import randint


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


n_inp = int(input('Введите число: '))
n_6 = randint(100000, 1000000)
n_7 = randint(1000000, 10000000)
n_8 = randint(10000000, 100000000)


# сделаем профилировку через timeit
# напишем фукнцию для профилировки через timeit
def print_time(func):
    print(f'Время на введенном числе {n_inp} ', timeit.timeit(f"{func}(n_inp)",
                                                              setup=f"from __main__ import {func}, n_inp",
                                                              number=10000))
    print('Время на числе 6 знаков ', timeit.timeit(f"{func}(n_6)",
                                                    setup=f"from __main__ import {func}, n_6",
                                                    number=10000))
    print('Время на числе 7 знаков ', timeit.timeit(f"{func}(n_7)",
                                                    setup=f"from __main__ import {func}, n_7",
                                                    number=10000))
    print('Время на числе 8 знаков ', timeit.timeit(f"{func}(n_8)",
                                                    setup=f"from __main__ import {func}, n_8",
                                                    number=10000))


print('Решение через рекурсию')
print_time("revers")

print('Решение через цикл')
print_time("revers_2")

print('Решение через срез')
print_time("revers_3")

'''Решение через рекурсию
Время на введенном числе 6758930384  0.02907999999999955
Время на числе 6 знаков  0.016560600000000036
Время на числе 7 знаков  0.019407099999999566
Время на числе 8 знаков  0.02142759999999999
Решение через цикл
Время на введенном числе 6758930384  0.020650200000000396
Время на числе 6 знаков  0.012646499999999783
Время на числе 7 знаков  0.014613100000000045
Время на числе 8 знаков  0.016609400000000107
Решение через срез
Время на введенном числе 6758930384  0.0032054999999999723
Время на числе 6 знаков  0.003042500000000281
Время на числе 7 знаков  0.0030447000000002333
Время на числе 8 знаков  0.0030663999999998026'''


# можно сделать профилировку всех функций разом
def main(n_inp):
    revers(n_inp)
    revers_2(n_inp)
    revers_3(n_inp)


cProfile.run("main(6758930384)")

# или по отдельности
cProfile.run("revers(6758930384)")
cProfile.run("revers_2(6758930384)")
cProfile.run("revers_3(6758930384)")

'''Видно, что решение с рекурсией наиболее медленное, так как функция вызывает саму себя, 
кроме того имеет внутри арифметические операции. 
Цикл находится на втром месте по скорости, так как использует арифметические операции.
Срез же является самым быстрым'''
