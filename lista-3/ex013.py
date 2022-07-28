first_value = int(input("Digite o valor inicial: "))
ratio = int(input("Digite o valor da razão: "))
amount = int(input("Digite o número de termos: "))

for index in range(first_value, first_value + ratio * amount, ratio):
  print(index, end=" ")
