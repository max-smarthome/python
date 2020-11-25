"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-5 ваших разных скриптов!.
Сделать их разные реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

from memory_profiler import profile


# Наивный алгоритм
@profile
def simple(i):
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


# Решето Эратосфена1
@profile
def eratosfen(i, l=1000000):
    n = 2
    numbers = [x for x in range(l)]
    numbers[1] = 0
    while n < l:
        if numbers[n] != 0:
            j = n * 2
            while j < l:
                numbers[j] = 0
                j += n
        n += 1
    return [k for k in numbers if k != 0][i - 1]


num = int(input('Введите номер простого числа: '))
simple(num)
eratosfen(num)

'''Python 3.8 64 разрядная ОС
Сравниваются два алгоритма нахождения i-ого простого числа. В наивном алгоритме память почти не загружена,
а вот в решете Эратосфена используется достаточно большой объем памяти, 
при том она не очищается по окончании выполнения функции. Это вызвано тем, что в решете Эратосфена создается список,
который потом не очищается, а ссылка на него остается. Прирост памяти при создании списка около 40 MiB 

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    27     86.7 MiB     86.7 MiB           1   @profile
    28                                         def simple(i):
    29
    30     86.7 MiB      0.0 MiB           1       count = 1
    31     86.7 MiB      0.0 MiB           1       n = 2
    32     86.7 MiB   -222.8 MiB        7918       while count <= i:
    33     86.7 MiB   -222.8 MiB        7918           t = 1
    34     86.7 MiB   -222.8 MiB        7918           is_simple = True
    35     86.7 MiB -157804.1 MiB     3721545           while t <= n:
    36     86.7 MiB -157778.7 MiB     3720545               if n % t == 0 and t != 1 and t != n:
    37     86.7 MiB   -197.4 MiB        6918                   is_simple = False
    38     86.7 MiB   -197.4 MiB        6918                   break
    39     86.7 MiB -157581.3 MiB     3713627               t += 1
    40     86.7 MiB   -222.8 MiB        7918           if is_simple:
    41     86.7 MiB    -25.4 MiB        1000               if count == i:
    42     86.6 MiB     -0.1 MiB           1                   break
    43     86.7 MiB    -25.3 MiB         999               count += 1
    44     86.7 MiB   -222.8 MiB        7917           n += 1
    45     86.6 MiB      0.0 MiB           1       return n


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    49     86.6 MiB     86.6 MiB           1   @profile
    50                                         def eratosfen(i, l=1000000):
    51     86.6 MiB      0.0 MiB           1       n = 2
    52    125.2 MiB  -9055.4 MiB     1000003       numbers = [x for x in range(l)]
    53    125.2 MiB      0.0 MiB           1       numbers[1] = 0
    54    125.2 MiB      0.0 MiB      999999       while n < l:
    55    125.2 MiB      0.0 MiB      999998           if numbers[n] != 0:
    56    125.2 MiB      0.0 MiB       78498               j = n * 2
    57    125.2 MiB      0.0 MiB     2853706               while j < l:
    58    125.2 MiB      0.0 MiB     2775208                   numbers[j] = 0
    59    125.2 MiB      0.0 MiB     2775208                   j += n
    60    125.2 MiB      0.0 MiB      999998           n += 1
    61    126.3 MiB      1.1 MiB     1000003       return [k for k in numbers if k != 0][i - 1]

'''