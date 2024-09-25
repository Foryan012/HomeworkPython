x = int(input('Введите сумму вклада: '))
p = int(input('Введите процентную ставку: '))
y = int(input('Введите желаемую сумму: '))
year = 0
while x < y:
    x = x + (x * p / 100)
    x = int(x)
    year += 1
print('Через', year, 'лет сумма достигнет', y)
