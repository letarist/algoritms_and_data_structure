"""Определить, какое число в массиве встречается чаще всего."""

import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив: {array}')

digit = array[0]
max_count = 1
for i in range(len(array) - 1):
    count = 1  # для каждого встречающегося элемента списка обновляем счетчик
    for k in range(i + 1, len(array)):
        if array[i] == array[k]:
            count += 1
        if max_count < count:
            max_count = count
            digit = array[i]
if max_count <= 1:
    print(f'Все элементы в единственном числе')
else:
    print(f'{digit} встречается в исходном массиве {max_count} раз')
