"""
ссылка на google disk с диаграммами
https://drive.google.com/file/d/1qAafGXGeI3CFmGHKgwYT0Wxpx5P7LfNJ/view?usp=sharing
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь."""
print('Введите целое трехзначное число: ')
digit = int(input())
a = digit % 10
b = digit % 100 // 10
c = digit // 100

print(f'Сумма цифр числа = {a + b + c}')
