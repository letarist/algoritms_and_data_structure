"""Нахождение простых чисел по индексу БЕЗ использования решета Эратосфена"""
import timeit
import cProfile

SIZE = 1000


def not_eratosfen(easy_num):
    easy_list = []
    result = []
    for k in range(2, SIZE):
        easy_list.append(True)
        for i in range(2, k):
            if k % i == 0:
                easy_list[k - 2] = False
                break
    for idx in range(len(easy_list)):
        if easy_list[idx] is True:
            result.append(idx + 2)
    return result[easy_num]


print(timeit.timeit('not_eratosfen(1)', number=1000, globals=globals()))  # 3.5435272999999996
print(timeit.timeit('not_eratosfen(5)', number=1000, globals=globals()))  # 3.4719605
print(timeit.timeit('not_eratosfen(10)', number=1000, globals=globals()))  # 3.5077871
print(timeit.timeit('not_eratosfen(15)', number=1000, globals=globals()))  # 3.3614128
print(timeit.timeit('not_eratosfen(20)', number=1000, globals=globals()))  # 3.161237800000002
print(timeit.timeit('not_eratosfen(25)', number=1000, globals=globals()))  # 3.564655000000002
print(timeit.timeit('not_eratosfen(30)', number=1000, globals=globals()))  # 3.3112081000000018
print(timeit.timeit('not_eratosfen(35)', number=1000, globals=globals()))  # 3.0886020999999992
print(timeit.timeit('not_eratosfen(40)', number=1000, globals=globals()))  # 3.269105800000002
print(timeit.timeit('not_eratosfen(45)', number=1000, globals=globals()))  # 3.3094701999999963
print(timeit.timeit('not_eratosfen(100)', number=1000, globals=globals()))  # 3.174583300000002

cProfile.run('not_eratosfen(100)')

# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#      1    0.003    0.003    0.003    0.003 less_4_task 2.2.py:5(not_eratosfen)
#      1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#   1166    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Без использования решета Эратосфена
# ВЫВОД. Какое бы по индексу число мы не искали, время выполнения приблизительно одно и то же. Эта функция с константной
# асимптотикой. На время выполнения этой функции влияет константа SIZE, но при этом время нахождения числа по индексу
# так же примерно одинаковое. Этот алгоритм работает медленнее чем решето Эратосфена примерно в на треть.
