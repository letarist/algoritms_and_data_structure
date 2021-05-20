"""В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве. Примечание к
задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения."""

import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив: {array}')

i = 0
negative_index = 0
for i in range(len(array)):
    if array[i] < 0 and negative_index == 0:
        negative_index = i
    elif (array[i] < 0) and array[i] > array[negative_index]:
        negative_index = i
    i += 1
print(
    f'{array[negative_index]} является максимальным из отрицательных, и находится на {negative_index + 1} месте')
# так как индексация начинается с 0, для вычисления позиции к индексу прибавляется 1
