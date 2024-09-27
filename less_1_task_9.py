"""Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)."""

a = float(input('Введите число a: '))
b = float(input('Введите число b: '))
c = float(input('Введите число c: '))

if a > b and b > c or a < b and b < c:
    print('Среднее число b')
elif b > a and a > c or b < a and a < c:
    print('Среднее чило a')
else:
    print('Среднее число c')
