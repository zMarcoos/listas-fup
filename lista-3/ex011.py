number = int(input("Digite um número (maior): "))
otherNumber = int(input("Digite outro número (menor): "))

while otherNumber:
  number, otherNumber = otherNumber, number % otherNumber

print(f'O MDC é {number}')