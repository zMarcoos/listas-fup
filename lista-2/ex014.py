code = int(input('Digite o código do produto: '))
amount = int(input('Digite a quantidade do produto: '))

total = 0
unit = 0

if 1 <= code <= 10:
  unit = 10
  total = amount * unit
elif 11 <= code <= 20:
  unit = 15
  total = amount * unit
elif 21 <= code <= 30:
  unit = 20
  total = amount * unit
else:
  unit = 30
  total = amount * unit

print(f'Valor unitário: {unit}')
print(f'Valor total: {total}')

if total <= 250:
  total *= 0.95
elif 250 < total <= 500:
  total *= 0.9
else:
  total *= 0.85

print(f'Valor final: {total:.2f}')