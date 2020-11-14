"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

from uuid import uuid4
import hashlib


salt = uuid4().hex
cash = {}


def cash_url(url):
    if url in cash:
        print(f'Страница {url} уже сохранена в кеше')
    else:
        hashed = hashlib.sha256(url.encode() + salt.encode()).hexdigest()
        cash[url] = hashed
        print(cash)
url_inp = ''
while url_inp != '0':
    url_inp = input('Введите адрес(для выхода наберите 0): ')
    cash_url(url_inp)