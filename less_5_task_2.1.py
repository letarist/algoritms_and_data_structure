from collections import deque

SHIFR = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
         'D': 13, 'E': 14, 'F': 15}
DESHIFR = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
           10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
result = deque()
transport = 0  # переменная переноса
a = input('Введите 1 число: ')
b = input('Введите 2 число: ')

if len(a) > len(b):
    a, b = deque(a), deque(b)
else:
    a, b = deque(b), deque(a)

while len(a) > 0:
    if len(b) > 0:
        test_result = SHIFR[a.pop()] + SHIFR[b.pop()] + transport  # Если на прошлой итерации переменная переноса
        # увеличилась, то ее прибавляем к результату последующей итерации
    else:
        test_result = SHIFR[a.pop()] + transport  # Вариант если 1 число окажется длиннее
    transport = 0  # после прибавления сразу же ее обнуляем
    if test_result < 16:
        result.appendleft(DESHIFR[test_result])
    else:
        result.appendleft(DESHIFR[test_result - 16])
        transport = 1  # Увеличиваем переменную переноса
if transport:
    result.appendleft(str(transport))
result = ''.join(result)
print(f'{result}')
