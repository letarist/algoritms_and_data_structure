"""Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к. именно в
этих позициях первого массива стоят четные числа"""

import sys
import random

SIZE = 100
MAX_ELEM = 100
MIN_ELEM = -100

array = [random.randint(MIN_ELEM, MAX_ELEM) for _ in range(SIZE)]
print(f'Исходный массив: {array}')

even_index_elem = set()


def even_idx(array):
    for i in range(len(array)):
        if array[i] % 2 == 0:
            even_index_elem.add(i)
    return even_index_elem


print(f'Измененный массив: {even_idx(array)}')


def memory(x):
    print(f'{type(x)=} {sys.getsizeof(x)=} {x=}')
    res = sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                res += memory(key)
                res += memory(value)
        elif not isinstance(x, str):
            for item in x:
                res += memory(item)

    return res


summary = memory(SIZE) + memory(MIN_ELEM) + memory(MAX_ELEM) + memory(array) + memory(even_index_elem)
print(summary)

# Суммарные затраты на выполнение этой программы составили 7268 байт

# По затратам памяти самым тяжелым из представленных мной в этой PW является множество (2264 б.)
