number = int(input("Digite um número: "))
summation = 2

for index in range(2, number + 1):
  summation += (1 / index)

print(f'Soma: {summation:.2f}')