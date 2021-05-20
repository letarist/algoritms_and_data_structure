"""В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный
 и максимальный элементы в сумму не включать."""

import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив:   {array}')
id_min = 0
id_max = 0
summary = 0
for i in range(len(array)):
    if array[i] < array[id_min]:
        id_min = i
    elif array[i] > array[id_max]:
        id_max = i
if id_max < id_min:  # условие если максимальное число стоит левее чем минимальное
    id_max, id_min = id_min, id_max
for i in range(id_min + 1, id_max):  # id_min + 1  -для того, чтобы число под этим индексом не включалось в диапазон
    summary += array[i]
print(summary)
