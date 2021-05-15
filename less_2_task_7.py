n = int(input('Введите количество членов прогрессии: '))
i = 0
summary = 0
while i < n:
    i += 1
    summary += i
if summary != n * (n + 1) / 2:
    print(f'Опровергнуто: {summary} не равно {int(n * (n + 1) / 2)}')
else:
    print(f'Доказано: {summary} равно {int(n * (n + 1) / 2)}')
