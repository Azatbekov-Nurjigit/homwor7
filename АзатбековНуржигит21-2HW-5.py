envparse==0.2.0
MY_MONEY = 1000

from random import choice

lst = [i for i in range(1, 31)]
def stavka(lot, amount):
    win_lot = choice(lst)
    if lot == win_lot:
        print(f'Вы выиграли {amount*2}')
        return amount * 2
    print(f'Вы проиграли {amount} ')
    return -amount
if __name__ == 'main':
    print(lst)

import os
from envparse import env
env.read_envfile('settings.env')
money = int(os.getenv('MY_MONEY'))


gain = 0
lost = 0
total = 0


while True:
    commands = input('Введите слот и ставку или exit-almaz для выхода: ').split()
    if commands[0] == 'exit':
        print(f'Программа завершена!️‍\nОставшаяся сумма: {money} Денег потеряно: {lost} Денег заработано: {gain}\
         Разница: {total}')
        break
    if not 1 <= int(commands[0]) <= 30:
        print('Неправильный слот для ставки\nПодсказка: слот должен быть целым числом от 1 до 30')
        continue
    if int(commands[1]) > money or int(commands[1]) <= 0:
        print('Неправильная сумма для ставки\nПодсказка: сумма ставки должна быть целым положительным числом не больше \
        доступного числа денег\n'+f'Доступная сумма:{money}')
        continue

    result = stavka(int(commands[0]), int(commands[1]))
    if result < 0:
        lost += result
    else:
        gain += result
    total += result
    money += result
    if money == 0:
        print('Вы обонкротились.')
        break
















