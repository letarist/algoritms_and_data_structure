"""Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
 [0; 50). Выведите на экран исходный и отсортированный массивы."""

from random import randint


def merge_sort(array):
    if len(array) < 2:
        return array
    left = merge_sort(array[:len(array) // 2])
    right = merge_sort(array[len(array) // 2:])
    st = i = j = 0
    if i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[st] = left[i]
            i += 1
        elif right[j] < left[i]:
            array[st] = right[j]
            j += 1
        st += 1

    while i < len(left):
        array[st] = left[i]
        i += 1
        st += 1
    while j < len(right):
        array[st] = right[j]
        j += 1
        st += 1
    return array


SIZE = 10
data = [randint(0, 50) for _ in range(SIZE)]
print(f'ИСХОДНЫЙ МАССИВ : {data}')
print(f'ОТСОРТИРОВАННЫЙ МАССИВ: {merge_sort(data)}')
