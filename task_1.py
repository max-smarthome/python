"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""
def calc():
    symbol = input("Введите операцию (+, -, *, / или 0 для выхода): ")

    if symbol in '0+-*/':
        if symbol == '0':
            return 'Досвидание'
        num1_str = input('Введите первое число: ')
        if not num1_str.isdigit():
            print("Вы ввели не число. Попробуйте еще")
            return calc()
        num1 = int(num1_str)
        num2_str = input('Введите второе число: ')
        if not num2_str.isdigit():
            print("Вы ввели не число. Попробуйте еще")
            return calc()
        num2 = int(num2_str)
        if symbol == '+':
            print(f'Результат {num1 + num2}')
            return calc()
        if symbol == '-':
            print(f'Результат {num1 - num2}')
            return calc()
        if symbol == '*':
            print(f'Результат {num1 * num2}')
            return calc()
        if symbol == '/':
            if num2 != 0:
                print(f'Результат {num1 / num2}')
                return calc()
            else:
                print('делить на 0 нельзя')
                return calc()
    else:
        print('Вы ввели неверный символ')
        return calc()

print(calc())