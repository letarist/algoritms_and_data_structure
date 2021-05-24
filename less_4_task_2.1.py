"""Нахождение простых чисел по индексу с использованием решета Эратосфена"""
import timeit
import cProfile

SIZE = 10000


def func_eratosfen(easy_num):
    easy_list = []
    for i in range(SIZE):
        easy_list.append(i)
    easy_list[1] = 0
    m = 2
    while m < SIZE:
        if easy_list[m] != 0:
            j = m * 2
            while j < SIZE:
                easy_list[j] = 0
                j = j + m
        m += 1
    result = []
    for i in easy_list:
        if easy_list[i] != 0:
            result.append(easy_list[i])

    del easy_list
    return result[easy_num]


print(timeit.timeit('func_eratosfen(1)', number=1000, globals=globals()))  # 2.4520076
print(timeit.timeit('func_eratosfen(5)', number=1000, globals=globals()))  # 2.3854813000000004
print(timeit.timeit('func_eratosfen(10)', number=1000, globals=globals()))  # 2.4004250999999996
print(timeit.timeit('func_eratosfen(15)', number=1000, globals=globals()))  # 2.3666618
print(timeit.timeit('func_eratosfen(20)', number=1000, globals=globals()))  # 2.3408242999999995
print(timeit.timeit('func_eratosfen(25)', number=1000, globals=globals()))  # 2.376167200000001
print(timeit.timeit('func_eratosfen(30)', number=1000, globals=globals()))  # 2.4046144000000016
print(timeit.timeit('func_eratosfen(35)', number=1000, globals=globals()))  # 2.4242217000000004
print(timeit.timeit('func_eratosfen(40)', number=1000, globals=globals()))  # 2.4253715000000007
print(timeit.timeit('func_eratosfen(45)', number=1000, globals=globals()))  # 2.371909900000002
print(timeit.timeit('func_eratosfen(100)', number=1000, globals=globals()))  # 2.3403867

cProfile.run('func_eratosfen(100)')

# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#      1    0.003    0.003    0.004    0.004 er.py:5(func_eratosfen)
#      1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#  11229    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# С использованием решета Эратосфена
# ВЫВОД. Какое бы по индексу число мы не искали, время выполнения приблизительно одно и то же. Эта функция с константной
# асимптотикой. На время выполнения этой функции влияет константа SIZE, но при этом время нахождения числа по индексу
# так же примерно одинаковое
