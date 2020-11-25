"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from memory_profiler import profile


@profile
def sum_row(n, su=0, curr_num=1):
    return su if n == 0 else sum_row(n - 1, su + curr_num, curr_num / -2)


@profile
def my_func(num):
    def sum_row(n, su=0, curr_num=1):
        return su if n == 0 else sum_row(n - 1, su + curr_num, curr_num / -2)

    print(sum_row(num))


#sum_row(1000)
my_func(1000)

'''При вызове функции sum_row profile выдает таблицу на каждый ее рекурсивный вызов:
Filename: C:/Users/mkharitonov/Desktop/Обучение/урок6/task_3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    11     87.4 MiB     87.4 MiB          99   @profile
    12                                         def sum_row(n, su=0, curr_num=1):
    13     87.4 MiB      0.1 MiB          99       return su if n == 0 else sum_row(n - 1, su + curr_num, curr_num / -2)


Filename: C:/Users/mkharitonov/Desktop/Обучение/урок6/task_3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    11     87.4 MiB     87.4 MiB         100   @profile
    12                                         def sum_row(n, su=0, curr_num=1):
    13     87.4 MiB      0.1 MiB         100       return su if n == 0 else sum_row(n - 1, su + curr_num, curr_num / -2)


Мы можем увидеть сколько функция потребляет на каждом шаге, но не можем увидеть сколько функция потребляет суммарно
Чтобы это обойти можно сделать обертку. В данном случае оберткой является функция my_func
Итогом получаем следующую таблицу, где представлено общее значения памяти для функции

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    16     86.8 MiB     86.8 MiB           1   @profile
    17                                         def my_func(num):
    18     88.6 MiB      1.8 MiB        1002       def sum_row(n, su=0, curr_num=1):
    19     88.6 MiB      0.0 MiB        1001           return su if n == 0 else sum_row(n - 1, su + curr_num, curr_num / -2)
    20                                         
    21     88.6 MiB      0.0 MiB           1       print(sum_row(num))
'''
