number = int(input("Digite um número: "))

factorial = number
for index in range(number - 1, 1, -1):
  factorial *= index

print(f'O fatorial é {factorial}')