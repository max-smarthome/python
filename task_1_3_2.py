"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-5 ваших разных скриптов!.
Сделать их разные реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from memory_profiler import profile
from pympler import asizeof


class TasksQueueClass:
    __slots__ =  ['elems_tasks', 'elems_revision', 'elems_decided']
    def __init__(self, tasks, rev, decid):
        self.elems_tasks = tasks
        self.elems_revision = rev
        self.elems_decided = decid

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
        self.elems_revision.insert(0, self.pop_out_task())

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


@profile
def my_func():
    task = TasksQueueClass(['task' + str(i) for i in range(10000)], ['rev' + str(i) for i in range(10000)],
                           ['decid' + str(i) for i in range(10000)])
    task2 = task
    print(f'размер объекта класса: {asizeof.asizeof((task))}')
    task.pop_out_task()
    del task
    del task2



my_func()

'''Python 3.8 OS 64

Если сравнить с примером без слотов, то память на объект класса выделяется чуть меньше, 
потому что мы избавились от словаря. Правда разница не существенная, 
так как переменные всего три и все они представляют из себя список.
размер объекта класса: 2094104
Filename: C:/Users/mkharitonov/Desktop/Обучение/урок6/task_1_3_2.py
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    71     99.4 MiB     99.4 MiB           1   @profile
    72                                         def my_func():
    73    101.6 MiB      1.4 MiB       20006       task = TasksQueueClass(['task' + str(i) for i in range(10000)], ['rev' + str(i) for i in range(10000)],
    74    101.6 MiB      0.7 MiB       10003                              ['decid' + str(i) for i in range(10000)])
    75    101.6 MiB      0.0 MiB           1       task2 = task
    76    103.1 MiB      1.5 MiB           1       print(f'размер объекта класса: {asizeof.asizeof((task))}')
    77    103.1 MiB      0.0 MiB           1       task.pop_out_task()
    78    103.1 MiB      0.0 MiB           1       del task
    79    100.7 MiB     -2.4 MiB           1       del task2

'''