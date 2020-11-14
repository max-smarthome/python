"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""

import hashlib


input_str = input('Введите строку ')

lst = []
for i in range(0, len(input_str) + 1):
    for j in range(i + 1, len(input_str) + 1):
        lst.append(hashlib.sha1(input_str[i:j].encode()).hexdigest())

lst.remove(hashlib.sha1(input_str.encode()).hexdigest())

print(f'Всего подстрок: {len(set(lst))}')
