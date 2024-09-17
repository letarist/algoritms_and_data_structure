from collections import defaultdict

company = int(input('Сколько предприятий? '))
info_company = defaultdict(int)
average_profit = 0
for i in range(company):
    summary = 0
    name = input('Введите название компании: ')
    for k in range(1, 5):
        pr = float(input(f'введите прибыль за {k} квартал: '))
        summary += pr
    info_company[name] = summary

average_profit = sum(info_company.values()) / company
print(f'\nПредприятия, работающие с прибылью:')
for name, profit in info_company.items():
    if info_company[name] > average_profit:
        print(f'У компании {name} прибыль выше среднего, и заработала {info_company[name]}')
print('*' * 50)
print('\nПредприятия работающие с убытком: ')
for name, profit in info_company.items():
    if info_company[name] < average_profit:
        print(f'У компании {name} прибыль ниже среднего, и заработала {info_company[name]}')
