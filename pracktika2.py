# Priklad 1

name = ''
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
print()

# Priklad 2

name = None # спочатку ми не знаємо імені користувача # нескінчений цикл
while True:
    print('Меню:')
    print('1.Ввести ім‘я')
    print('2.Вивести привітання')
    print('3.Вийти')
    response = input('Виберіть пункт: ')
    print()
    if response == '1':
        name = input('Введіть ваше ім‘я: ')
    elif response =='2':
        if name: #вітаємося з користувачем, якщо ім'я вже введено
            print('Привіт, ', name, '!', sep='')
        else:
            print('Я не знаю вашого імені.')
    elif response == '3': # оператор break завершує виконання циклу
            break #якщо користувач вибрав 3, то виходимо з циклу
    else:
        print('Неправильне введення.')
        print()

# Task

from math import *
Input = input("T input:")
t = float(Input)
deltaT = 0.1
while True:
    if (t >= 0 and t <= 6.5):
        z = (2.3 * t + 8)/(2*cos(t)+1)
        t += deltaT
        print(z)
    else:
        break
