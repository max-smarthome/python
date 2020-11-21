"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""
from collections import deque
import timeit

lst = [i for i in range(1000)]
dq = deque()
dq.extend(lst)
lst_ex = [i for i in range(1000)]


def list_append(n):
    for i in range(n):
        lst.append(i)


def deque_append(n):
    for i in range(n):
        dq.append(i)


def list_appendleft(n):
    for i in range(n):
        lst.insert(0, i)


def deque_appendleft(n):
    for i in range(n):
        dq.appendleft(i)


def list_extend(n):
    lst.extend(lst_ex)


def deque_extend(n):
    dq.extend(lst_ex)


def list_insert(n):
    for i in range(n):
        lst.insert(i, 1)


def deque_insert(n):
    dq.rotate(100)
    for i in range(n):
        dq.appendleft(n)
    dq.rotate(100)


def list_reverse(n):
    lst.reverse()


def deque_reverse(n):
    dq.reverse()


name_list = ['list_append', 'deque_append', 'list_appendleft', 'deque_appendleft', 'list_extend', 'deque_extend',
             'list_insert', 'deque_insert', 'list_reverse', 'deque_reverse']


for i in name_list:
    print(f"{i} - {timeit.timeit(stmt=i + f'(10)', setup=f'from __main__ import {i}', number=1000)}")


'''Из тайминга видно, что deque выполняет большинство процедур быстрее, чем list. 
При  этом append имеет примерно схожие показатели в обоих реализациях, а вот на extend list показывает себя лучше.
Даже вставка в произвольное место в списке выполняется медленнне, чем очередь. Это обусловлено тем, что appendleft 
выполняется быстрее insert 
list_append - 0.0008791999999999689
deque_append - 0.0008548999999999918
list_appendleft - 0.05644900000000008
deque_appendleft - 0.0009142000000000872
list_extend - 0.012412899999999949
deque_extend - 0.006445499999999993
list_insert - 9.0099111
deque_insert - 0.001719800000000049
list_reverse - 0.6864073000000008
deque_reverse - 1.6601675
'''