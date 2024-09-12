"""Сформировать из введенного числа обратное по порядку входящих в него цифр
 и вывести на экран. Например, если введено число 3486, надо вывести 6843.

https://docs.google.com/spreadsheets/d/1KUoWlvZoZagmuiD9H4WCgQukaWiogXR44_xNdmMF-sE/edit?usp=sharing
ССЫЛКА НА GOOGLE ТАБЛИЦУ С ГРАФИКАМИ"""

import cProfile
import timeit


def digit_reverse(digit, res=0):
    if digit == 0:
        return res
    if digit < 10:
        return digit_reverse(digit // 10, res + (digit % 10))
    else:
        return digit_reverse(digit // 10, (res + (digit % 10)) * 10)


print(timeit.timeit('digit_reverse(11)', number=1000, globals=globals()))  # 0.0003049999999999997
print(timeit.timeit('digit_reverse(121)', number=1000, globals=globals()))  # 0.0004352999999999996
print(timeit.timeit('digit_reverse(1221)', number=1000, globals=globals()))  # 0.0006031000000000005
print(timeit.timeit('digit_reverse(12321)', number=1000, globals=globals()))  # 0.0007974000000000002
print(timeit.timeit('digit_reverse(123321)', number=1000, globals=globals()))  # 0.0007974000000000002
print(timeit.timeit('digit_reverse(12345674312345342123)', number=1000, globals=globals()))  # 0.003927299999999998
print(timeit.timeit('digit_reverse(12345674312349706986742123)', number=1000,
                    globals=globals()))  # 0.005365599999999998
print(timeit.timeit('digit_reverse(12345674312349706986743536634634466442123)', number=1000,
                    globals=globals()))  # 0.0091357
print(timeit.timeit('digit_reverse(12345674312349706986734453454353453453453455345343542123)', number=1000,
                    globals=globals()))  # 0.012777400000000001
print(timeit.timeit('digit_reverse(12345674312349706986734453454353453453453455345343542123565645656456644565656656)'
                    , number=1000, globals=globals()))  # 0.0190639
cProfile.run(
    'digit_reverse(1231243547687978890785674323293523952368562836582357836257325723568787253787235563878287542354364565'
    '645635342423424345645645646423423425367987980890667979797898797897979756757586970808908908908908989090004242342344'
    '234234324242342424234242342467678679789898908876856745456464534523423424235345687978890890890890898979798797056464'
    '456457567563452345345345645645654756756757453432453453453464565756756756753464575686778898098908908908909524312441'
    '4364567686787856745342453454565676789789898990890099090900867965634242435457678679798897897970909999909086767668'
    '2342354646575645234236567889879896786756456345465668767789789789789678567564534534534534534545656756767867886786)')

#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#    667/1    0.002    0.000    0.002    0.002 less_4_task_1.1.py:7(digit_reverse)
#        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# В данном решении задачи использовался рекурсивный алгоритм
# Оценка задачи со стороны асимптотики: асимптотика линейная
