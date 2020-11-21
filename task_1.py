"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""

from collections import namedtuple, defaultdict


def proceeds_namedtuple(n):
    proc = namedtuple('Proc', 'name proc_year')
    proc_list = []
    sum_all = 0
    bigger = []
    smaller = []
    for i in range(n):
        comp_name = input('Введите название предприятия: ')
        sum_proc = sum([float(j) for j in (input('через пробел введите прибыль данного предприятия\n'
                                                 'за каждый квартал(Всего 4 квартала):').split(' '))])
        sum_all += sum_proc
        proc_list.append(proc(name=comp_name, proc_year=sum_proc))
        i += 1
    avg = sum_all / n
    print(f'Средняя годовая прибыль всех предприятий: {avg}')
    for k in proc_list:
        if k.proc_year >= avg:
            bigger.append(k.name)
        else:
            smaller.append(k.name)
    print('Предприятия, с прибылью выше среднего значения: ', *bigger)
    print()
    print('Предприятия, с прибылью ниже среднего значения: ', *smaller)


def proceeds_defaultdict(n):
    comp_dict = defaultdict()
    bigger = []
    smaller = []
    for i in range(n):
        comp_name = input("Введите название предприятия: ")
        proceed_sum = sum([float(j) for j in (input('через пробел введите прибыль данного предприятия\n'
                                                    'за каждый квартал(Всего 4 квартала):').split(' '))])
        comp_dict[comp_name] = proceed_sum
    avg = sum(comp_dict.values()) / n
    print(f"Средняя прибыль всех предприятий за год: {avg}")
    for k in comp_dict:
        if comp_dict[k] >= avg:
            bigger.append(k)
        else:
            smaller.append(k)
    print('Предприятия, с прибылью выше среднего значения: ', *bigger)
    print()
    print('Предприятия, с прибылью ниже среднего значения: ', *smaller)


num = int(input('Введите количество предприятия для расчета прибыли: '))
proceeds_namedtuple(num)
proceeds_defaultdict(num)
