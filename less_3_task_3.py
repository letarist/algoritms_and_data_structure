"""В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""

import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив:   {array}')
max_elem = 0
min_elem = 0
for i in range(len(array)):
    if array[i] > array[max_elem]:
        max_elem = i
    elif array[i] < array[min_elem]:
        min_elem = i
array[max_elem], array[min_elem] = array[min_elem], array[max_elem]
print(f'Измененный массив: {array}')
