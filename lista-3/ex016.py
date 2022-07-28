number = int(input("Digite um número: "))
sequential = 1

for index in range(1, number + 1):
  for _ in range(1, index + 1):
    print(sequential, end=' ')
    sequential += 1
  print()