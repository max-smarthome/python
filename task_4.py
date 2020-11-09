"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Ряд строить программно - в самой же рекурсивной ф-ции
или даже обойтисть без создания ряда

Элемент в 2 раза меньше предыд и имеет противопол знак
"""
def sum_row(n, su = 0, curr_num = 1):
    return su if n == 0 else sum_row(n-1, su + curr_num, curr_num/-2)
try:
    inp = int(input('Введите число: '))
    print(f'Количество элементов - {inp} сумма - {sum_row(inp)}')
except ValueError:
    print('Вы ввели не число')
