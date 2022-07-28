product = input('Produto: ')
first_weight = float(input('Massa da versão 1 (g): '))
first_price = float(input('Preço da versão 1 (R$): '))
second_weight = float(input('Massa da versão 2 (g): '))
second_price = float(input('Preço da versão 2 (R$): '))

if first_weight / first_price > second_weight / second_price:
  print(f'{product} de {first_weight}g por R${first_price:.2f} é mais vantajoso')
else:
  print(f'{product} de {second_weight}g por R${second_price:.2f} é mais vantajoso')