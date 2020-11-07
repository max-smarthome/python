"""
Задание 5.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""

class StacksPlateClass:
    def __init__(self, max_size):
        self.elems = [[]]
        self.stack_max = max_size

    def last_isempty_stack(self):
        return self.elems[-1] == []

    def isempty_stack(self):
        return self.elems == [[]]

    def stack_size(self):
        size = 0
        for i in self.elems:
            size += len(i)
        return size

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if len(self.elems[-1]) < self.stack_max:
            self.elems[-1].append(el)
        else:
            self.elems.append([])
            self.elems[-1].append(el)


    def pop_out(self):
        val = self.elems[-1].pop()
        if self.last_isempty_stack():
            self.elems.pop()
        return val

    def get_val(self):
        return self.elems[- 1][-1]

    def number_stacks(self):
        return len(self.elems)

if __name__ == '__main__':

    stack = StacksPlateClass(5)

    stack.push_in(1)
    stack.push_in(2)
    stack.push_in(3)
    stack.push_in(4)
    stack.push_in(5)
    stack.push_in(21)
    stack.push_in(22)
    stack.push_in(23)
    stack.push_in(24)
    stack.push_in(25)
    stack.push_in(31)
    print(stack.stack_size())
    print(stack.last_isempty_stack())
    print(stack.isempty_stack())
    print(stack.number_stacks())
    print(stack.pop_out())
    print(stack.get_val())
    print(stack.number_stacks())