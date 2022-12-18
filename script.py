per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input())
deposit = [int(money*per_cent['ТКБ']/100), int(money*per_cent['СКБ']/100), int(money*per_cent['ВТБ']/100), int(money*per_cent['СБЕР']/100)]
print(f'Максимальная сумма, которую вы можете заработать —  {max(deposit)}')
