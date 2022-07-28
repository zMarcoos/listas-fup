base = float(input('Salário base: '))
dependents = float(input('Número de dependentes: '))

total = base + 120 * dependents

if 1000 <= total <= 2500:
  total *= 0.9
else:
  total *= 0.8

if total <= 1750:
  total += 500
else:
  total += 250

print(f'O salário a receber do funcionário é: R${total:.2f}')