number = int(input('Digite um número: '))

summation = 0
for index in range(number, 0, -1):
  if index % 2 == 0 or index == number: continue

  summation += index

print(f'A soma dos números ímpares anteriores é {summation}')