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
Здесь профилируется функция операций с классом. Как видно из таблицы основная память выделяется при создании массива.
При этом память освобождается только при удалении второй переменной task
  размер объекта класса: 2094392
Filename: C:/Users/mkharitonov/Desktop/Обучение/урок6/task_1_3_1.py
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    70     99.5 MiB     99.5 MiB           1   @profile
    71                                         def my_func():
    72    101.5 MiB      1.3 MiB       20006       task = TasksQueueClass(['task' + str(i) for i in range(10000)], ['rev' + str(i) for i in range(10000)],
    73    101.5 MiB      0.7 MiB       10003                              ['decid' + str(i) for i in range(10000)])
    74    101.5 MiB      0.0 MiB           1       task2 = task
    75    102.9 MiB      1.4 MiB           1       print(f'размер объекта класса: {asizeof.asizeof((task))}')
    76    102.9 MiB      0.0 MiB           1       task.pop_out_task()
    77    102.9 MiB      0.0 MiB           1       del task
    78    100.4 MiB     -2.6 MiB           1       del task2

'''