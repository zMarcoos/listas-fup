maximum = 0
summation = 0

while True:
  number = int(input('Digite um número: '))
  if number < 0:
    break

  summation += number

  if number > maximum:
    maximum = number

print(f'A somatória é {summation}')
print(f'O máximo é {maximum}')
