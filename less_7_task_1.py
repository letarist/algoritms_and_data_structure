"""Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
[-100; 100). Выведите на экран исходный и отсортированный массивы."""

from random import randint


def bubble_sort(array):
    for _ in range(len(array) - 1):
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
    return array


SIZE = 10
data = [randint(-100, 100) for _ in range(SIZE)]
print(f'ИСХОДНЫЙ МАССИВ : {data}')
print(f'ОТСОРТИРОВАННЫЙ МАССИВ: {bubble_sort(data)}')

#  алгоритм улучшен заменой цикла while на цикл for, так как он быстрее выполняется
