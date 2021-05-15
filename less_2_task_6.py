from random import randint

number_try = 0
comp_number = randint(0, 100)
while number_try < 10:
    user_number = int(input('Введите число: '))
    if comp_number < user_number:
        print('Загаданное число меньше вашего')
    elif comp_number > user_number:
        print('Загаданное число больше вашего')
    else:
        print('Вы угадали')
        break
    number_try += 1
