"""
Задание 3.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""
from random import randint


list_capital = list(randint(1000000, 2100000) for i in range(10))
list_names = list(('comp'+ str(i))for i in list(randint(1, 10) for i in range(10)))

comp_dict =  dict(zip(list_names, list_capital))


#первый вариант O(n^2)
def sort_1(list_dict):
    list_dict = list(comp_dict.items())
    for i in range(len(list_dict)):
        index = i
        for j in range(i+1, len(list_dict)):
            if list_dict[index][1] < list_dict[j][1]:
                index = j
        list_dict[i], list_dict[index] = list_dict[index], list_dict[i]
    return list_dict[:3]


[print(i[0], '  ', i[1]) for i in sort_1(comp_dict)]

#второй вариант О(n)
def sort_2(list_dict):
    i = 0
    new_dict=list_dict.copy()
    output_dict={}
    while i < 3:
        list_1 = list(new_dict.items())
        max_comp = max(list_1, key = lambda x: x[1])
        del new_dict[max_comp[0]]
        output_dict[max_comp[0]] = max_comp[1]
        i += 1
    return output_dict
[print(i[0], ' ', i[1]) for i in sort_2(comp_dict).items()]

#Второй вариант лучше, его сложность легче