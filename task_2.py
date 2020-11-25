"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, библиотеки) для оптимизации памяти и
доказать! (наглядно, кодом) их эффективность (на примере профилировщика)
"""
import gc
from  random import randint
from  memory_profiler import profile


def create_cycle(n):
    lst = [randint(1, 10) for i in range(n)]
    lst.append(lst)


@profile
def main_2(n):
    print("Создадим мусор")
    for i in range(8):
        create_cycle(n)


@profile
def main(n):
    print("Создадим мусор")
    for i in range(8):
        create_cycle(n)
    n = gc.collect()
    print("Количество собранного мусора:", n)


main_2(100000)
main(100000)


'''Python 3.8 OS 64
gc - сборщик муссора. gc.collect() - принудительно собирает мусор по событию.
Как видно из профилирования двух функций, во втором случае происходит принудительное удаление
мусора и освобождение памяти. 

Создадим мусор
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    16     98.8 MiB     98.8 MiB           1   @profile
    17                                         def main_2(n):
    18     98.8 MiB      0.0 MiB           1       print("Создадим мусор")
    19    105.3 MiB      0.0 MiB           9       for i in range(8):
    20    105.3 MiB      6.5 MiB           8           create_cycle(n)


Создадим мусор
Количество собранного мусора: 25
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    23    105.3 MiB    105.3 MiB           1   @profile
    24                                         def main(n):
    25    105.3 MiB      0.0 MiB           1       print("Создадим мусор")
    26    112.2 MiB      0.0 MiB           9       for i in range(8):
    27    112.2 MiB      6.8 MiB           8           create_cycle(n)
    28     98.8 MiB    -13.4 MiB           1       n = gc.collect()
    29     98.8 MiB      0.0 MiB           1       print("Количество собранного мусора:", n)'''