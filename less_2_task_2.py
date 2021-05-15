"""
ссылка на google disk: https://drive.google.com/file/d/1P-_T3PLPUCDOewP1PfYWAjEa2fZ8WE_T/view?usp=sharing
Посчитать четные и нечетные цифры введенного натурального числа.
 Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)."""
digit = int(input('Введите число: '))
ch = 0
nch = 0
while digit != 0:
    ost = digit % 10
    digit = digit // 10
    if ost % 2 == 0:
        ch += 1
    else:
        nch += 1
print(f'Четный - {ch}, нечетный - {nch}')
