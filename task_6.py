"""
Задание 7.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".


Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""

class TasksQueueClass:
    def __init__(self):
        self.elems_tasks = []
        self.elems_revision=[]
        self.elems_decided=[]

    def is_empty_revision(self):
        return self.elems_revision == []

    def is_empty_tasks(self):
        return self.elems_tasks == []

    def tasks_queue_size(self):
         return len(self.elems_tasks)

    def revision_queue_size(self):
         return len(self.elems_revision)

    def decided_queue_size(self):
        return len(self.elems_decided)

    def push_in_task(self, el):
        self.elems_tasks.insert(0, el)

    def push_in_revision(self):
        self.elems_revision.insert(0,self.pop_out_task())

    def push_in_decided(self, el):
        self.elems_decided.append(el)

    def pop_out_revision(self):
        self.elems_revision.pop()

    def pop_out_task(self):
        return self.elems_tasks.pop()

    def get_val_task(self):
        return self.elems_tasks[-1]

    def get_val_revision(self):
        return self.elems_revision[-1]

if __name__ == '__main__':

    task = TasksQueueClass()

    task.push_in_task('Task1')
    task.push_in_task('Task2')
    task.push_in_task('task3')
    task.push_in_task('task4')
    task.push_in_task('task5')
    print(task.tasks_queue_size())
    print(task.push_in_revision())
    print(task.push_in_decided(task.pop_out_task()))
    print(task.get_val_revision())
    print(task.get_val_task())
    print(task.tasks_queue_size())
    print(task.revision_queue_size())
    print(task.decided_queue_size())