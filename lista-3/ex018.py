number = int(input("Digite um número: "))

total = 0
denominator = 1

for index in range(1, number + 1):
  if index % 2 == 0:
    total -= (4 / denominator)
  else:
    total += (4 / denominator)
  denominator += 2

print(f'Total: {total}')