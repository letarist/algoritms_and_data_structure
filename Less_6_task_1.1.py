"""Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к. именно в
этих позициях первого массива стоят четные числа"""

import random
import sys

SIZE = 100
MIN_ITEM = 1
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив: {array}')
array = tuple(array)
even_index_elem = []


def even_idx(array):
    for i in range(len(array)):
        if array[i] % 2 == 0:
            even_index_elem.append(i)
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


summary = memory(SIZE) + memory(MIN_ITEM) + memory(MAX_ITEM) + memory(array) + memory(even_index_elem)
print(summary)

# Суммарные затраты на выполнение этой программы составили 5512 байт

# Вес кортежа 840 б., списка 920 б.. Вывод: кортежи использовать в плане памяти выгоднее
