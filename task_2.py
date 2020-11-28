"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from random import uniform


def merge(lft, rght=[]):
    lt = 0
    rt = 0
    res = []
    while lt < len(lft) and rt < len(rght):
        if lft[lt] <= rght[rt]:
            res.append(lft[lt])
            lt += 1
        else:
            res.append(rght[rt])
            rt += 1
    while lt < len(lft):
        res.append(lft[lt])
        lt += 1
    while rt < len(rght):
        res.append(rght[rt])
        rt += 1
    return res


def merge_sort(arr_inp):
    mid = len(arr_inp) //  2
    if len(arr_inp) <= 1:
        return arr_inp
    left = merge_sort(arr_inp[:mid])
    right = merge_sort(arr_inp[mid:])
    return merge(left, right)


arr = [uniform(0, 50) for _ in range(1000)]
print(arr)
print(merge_sort(arr))
