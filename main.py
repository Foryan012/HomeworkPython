x = int(input('Введите сумму вклада: '))
p = float(input('Введите процентную ставку: '))
y = int(input('Введите желаемую сумму: '))
b = x + p + y
print(round(b, 0))
year = 0
while x < y:
    x = x + ( x * p / 100)
    x = int(x)
    year += 1
print('Через', year, 'лет сумма достигнет', y)
