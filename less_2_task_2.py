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
