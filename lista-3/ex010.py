number = int(input("Digite um número (maior): "))
otherNumber = int(input("Digite outro número (menor): "))

greater = number
mmc = 1

while True:
  if greater % number == 0 and greater % otherNumber == 0:
    mmc = greater
    break

  greater += 1

print(mmc)