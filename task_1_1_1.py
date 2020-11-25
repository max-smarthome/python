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
from random import randint
import numpy as np
from pympler import asizeof

list_1 = list(randint(100, 1000) for i in range(1000000))
list_np = np.array(list_1)


# функция поиска нименьшего значения
@profile
def min_n(lst_inp):
    min_val = lst_inp[0]
    for i in lst_inp[1:]:
        if i < min_val:
            min_val = i
    return min_val


print(f'Список занимает {asizeof.asizeof(list_1)} памяти')
print(f'Массив numpy занимает {asizeof.asizeof(list_np)} памяти')

print(min_n(list_1))
print(min_n(list_np))

'''Python 3.8, 64 разрядная ОС
В описанном примере видно, что самое большое значение инкремента на цикле for. 
При этом значение инкремента видно только по значениям используемой памяти. 
Так же было добавлено профилирование функции при передачи массива созданного в numpy.
Видно, что кроме того, что массив в numpy занимает меньше памяти почти в 10 раз, он еще и не дает никакого прироста 
в используемой динамической памяти. Видимо, это вызвано тем, что в нем лучше организована "сборка мусора".

Для сравнения приложены таблицы еще одного запуска. Видно, что при разных запусках в условиях одной машины
динамическая память может выделяться по разному. 

На самом деле сильно улучшить эту функцию не выйдет, так как массив здесь используется внешний, 
а ссылка на переменную min_val удаляется после заверщения программы

Список занимает 34691760 памяти
Массив numpy занимает 4000112 памяти

Запуск 1

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    32    124.6 MiB    124.6 MiB           1   @profile
    33                                         def min_n(lst_inp):
    34    124.6 MiB      0.0 MiB           1       min_val = lst_inp[0]
    35    132.3 MiB      0.0 MiB     1000000       for i in lst_inp[1:]:
    36    132.3 MiB      0.0 MiB      999999           if i < min_val:
    37    132.2 MiB      0.0 MiB           7               min_val = i
    38                                         
    39    124.6 MiB     -7.6 MiB           1       return min_val


100

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    32    124.6 MiB    124.6 MiB           1   @profile
    33                                         def min_n(lst_inp):
    34    124.6 MiB      0.0 MiB           1       min_val = lst_inp[0]
    35    124.6 MiB -30258.7 MiB     1000000       for i in lst_inp[1:]:
    36    124.6 MiB -30258.6 MiB      999999           if i < min_val:
    37    124.6 MiB      0.0 MiB           7               min_val = i
    38                                         
    39    124.6 MiB     -0.1 MiB           1       return min_val


100
Запуск 2

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    33    124.2 MiB    124.2 MiB           1   @profile
    34                                         def min_n(lst_inp):
    35    124.2 MiB      0.0 MiB           1       min_val = lst_inp[0]
    36    131.9 MiB      0.0 MiB     1000000       for i in lst_inp[1:]:
    37    131.9 MiB      0.0 MiB      999999           if i < min_val:
    38    131.8 MiB      0.0 MiB           2               min_val = i
    39                                         
    40    124.2 MiB     -7.6 MiB           1       return min_val


100


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    33    124.2 MiB    124.2 MiB           1   @profile
    34                                         def min_n(lst_inp):
    35    124.2 MiB      0.0 MiB           1       min_val = lst_inp[0]
    36    124.2 MiB -37519.4 MiB     1000000       for i in lst_inp[1:]:
    37    124.2 MiB -37519.4 MiB      999999           if i < min_val:
    38    124.2 MiB      0.0 MiB           2               min_val = i
    39                                         
    40    124.2 MiB     -0.1 MiB           1       return min_val


100
'''
