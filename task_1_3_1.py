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
    def __init__(self, tasks):
        self.elems_tasks = tasks
        self.elems_revision = []
        self.elems_decided = []

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
    task = TasksQueueClass(['task' + str(i) for i in range(100000)])
    task2 = task
    print(f'размер объекта класса: {asizeof.asizeof((task))}')
    task.pop_out_task()
    task.push_in_revision()
    del task
    del task2



my_func()

'''Python 3.8 OS 64
Здесь профилируется функция операций с классом. Как видно из таблицы основная память выделяется при создании массива.
При этом память освобождается только при удалении второй переменной task
  размер объекта класса: 7216912

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    70     99.8 MiB     99.8 MiB           1   @profile
    71                                         def my_func():
    72    107.4 MiB  -2205.1 MiB      100003       task = TasksQueueClass(['task' + str(i) for i in range(100000)])
    73    107.4 MiB      0.0 MiB           1       task2 = task
    74    107.1 MiB     -0.3 MiB           1       print(f'размер объекта класса: {asizeof.asizeof((task))}')
    75    107.1 MiB      0.0 MiB           1       task.pop_out_task()
    76    107.1 MiB      0.0 MiB           1       task.push_in_revision()
    77    107.1 MiB      0.0 MiB           1       del task
    78    101.1 MiB     -6.0 MiB           1       del task2
'''