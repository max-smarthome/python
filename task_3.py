"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""
from random import randint
from numpy import median
from timeit import timeit


def heap_form(arr, n, i):
    root = i  # Initialize largest as root
    lt = 2 * i + 1  # left = 2*i + 1
    rt = 2 * i + 2  # right = 2*i + 2
    if lt < n and arr[root] < arr[lt]:
        root = lt
    if rt < n and arr[root] < arr[rt]:
        root = rt
    if root != i:
        arr[i], arr[root] = arr[root], arr[i]  # свап
        heap_form(arr, n, root)


def heap_sort(arr_in):
    n = len(arr_in)
    # Строим кучу
    for i in range(n-1, -1, -1):
        heap_form(arr_in, n, i)
    # Извлекаем элементы из кучи
    for i in range(n-1, -1 , -1):
        arr_in[i], arr_in[0] = arr_in[0], arr_in[i] # свап
        heap_form(arr_in, i, 0)


def med(arr_inp, m):
    heap_sort(arr_input)
    return arr_input[m]


def median_no_sort(arr_inp):
    left = []
    right = []
    for i in range(len(arr_inp)):
        for j in range(len(arr_inp)):
            if i == j:
                continue
            if arr_input[i] < arr_inp[j]:
                right.append(arr_inp[j])
            if arr_input[i] > arr_inp[j]:
                left.append(arr_inp[j])
            if arr_inp[i] == arr_inp[j] and i > j:
                left.append(arr_inp[j])
            if arr_inp[i] == arr_inp[j] and i < j:
                right.append(arr_inp[j])
        if len(left) == len(right):
            return arr_input[i]
        left.clear()
        right.clear()


m = int(input('Введите m '))
arr_input = [randint(1, 100) for _ in range(2*m + 1)]

print(f'Медиана из numpy равна: {median(arr_input[:])}')
print(f'Медиана равна: {med(arr_input[:], m)}')
print(f'Медиана без сортировка равна: {median_no_sort(arr_input[:])}')

print('Время через сортировку: ' + str(timeit("med(arr_input[:], m)", setup = "from __main__ import med, arr_input, m",
             number=10)))
print('Время без сортировки: '+ str(timeit("median_no_sort(arr_input[:])", setup = "from __main__ import median_no_sort, arr_input",
             number=10)))

'''
Были предложен два алгоритма нахождения медианы. В первом случае использовалась сортировка кучей, 
после чего была выбарна медиана, как центр массива. 
Во втором случае осуществлялся проход по всему массиву и находился элемент, 
когда слева и спарва одинаковое число элементов.
Как видно ниже, на малленьких массивах время лучше у алгоритма без сортировки,
с ростом массива лучше результаты показывает алгоритм с сортировкой.

Введите m 10
Медиана из numpy равна: 39.0
Медиана равна: 39
Медиана без сортировка равна: 39
Время через сортировку: 0.0011197000000002788
Время без сортировки: 0.000767900000000043535

Введите m 100
Медиана из numpy равна: 51.0
Медиана равна: 51
Медиана без сортировка равна: 51
Время через сортировку: 0.007497400000000098
Время без сортировки: 0.07363979999999959


Введите m 1000
Медиана из numpy равна: 50.0
Медиана равна: 50
Медиана без сортировка равна: 50
Время через сортировку: 0.10087050000000009
Время без сортировки: 6.668773600000001
'''