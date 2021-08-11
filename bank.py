per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

print('Введите сумму вклада:')
money = int(input())

print('У вас есть %d рублей' % (money))

deposit = []

for key in per_cent:

    percent = per_cent[key]
    deposit.append(money * percent / 100)

max_deposit = max(deposit)

print('Максимальная сумма, которую вы можете заработать — %d рублей' % (max_deposit))
