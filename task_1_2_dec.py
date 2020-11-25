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

from memory_profiler import memory_usage
from timeit import default_timer


def calc_t_mem(func):
    def mem_time(*args, **kwargs):
        start_t = default_timer()
        start_m = memory_usage()
        func(*args)
        end_t = default_timer()
        end_m = memory_usage()
        m_res = end_m[0] - start_m[0]
        t_res = end_t - start_t
        print(f'Время выполнения =  {t_res}, используемая память = {m_res}')
    return mem_time

# Наивный алгоритм
@calc_t_mem
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
@calc_t_mem
def eratosfen(i, l=10000):
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

'''
Здесь для оченки используется самописный декоратор. С его помощью можно понять, решето Эратосфена намного лучше вплане 
времени, однако намного хуже вплане использования памяти. Это вызвано тем, что решето использует список, который после 
своего создания не удаляется.
Время выполнения =  0.5505917999999994, используемая память = 0.0
Время выполнения =  0.11254429999999971, используемая память = 0.296875

'''


num = int(input('Введите номер простого числа: '))
simple(num)
eratosfen(num)
