maximum = 0

for _ in range(10):
  number = int(input('Digite um número: '))

  if number > maximum:
    maximum = number

print(f'O máximo é {maximum}')