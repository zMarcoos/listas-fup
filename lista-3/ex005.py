amount = int(input('Quantas vezes você quer que o programa seja lido: '))

maximum = 0
summation = 0

for _ in range(amount):
  number = int(input('Digite um número: '))

  summation += number

  if number > maximum:
    maximum = number

print(f'A somatória é {summation}')
print(f'O máximo é {maximum}')
