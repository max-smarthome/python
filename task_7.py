"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
def func_proof(n, curr_step=1, sum_row=0, func_res=0 ):
    if curr_step == n + 1:
        if sum_row == func_res:
            return 'Формула верна'
        else:
            return 'Формула неверна'
    else:
        return func_proof(n, curr_step+1, sum_row + curr_step, n*(n+1)/2)
try:
    inp = int(input('Введите число: '))
    print(func_proof(inp))
except ValueError:
    print('Вы ввели не число')


