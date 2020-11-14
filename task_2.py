"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""
from uuid import uuid4
import hashlib
#создаем соль
salt = uuid4().hex #45d6a6854d4a4abfa3f0ccd98e095ab1
print(type(salt))

def passw_hash(password):
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest()

def passw_check(passw_hashed, input_passw):
    return passw_hashed == hashlib.sha256(salt.encode() + input_passw.encode()).hexdigest()


def login_system():
    hashed_obj = passw_hash(input('Введите пароль: '))
    print(f'В базе данных хранится строка: {hashed_obj}')
    if passw_check(hashed_obj, input(f'Введите пароль еще раз для проверки: ')):
        print('Вы ввели правильный пароль')
    else:
        print('Пароли не совпадают')
        # как вариант можно воспользоваться знаниями прошлого урока и применить рекурсию до момента совпдаения паролей,
        #выглядит как иммитация ввода пароля при регистрации
        #login_system()

login_system()




