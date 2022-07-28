first_number = float(input("Digite um número: "))
second_number = float(input("Digite outro número: "))

if first_number == second_number:
  print("Os valores são iguais")
else:
  print(f"{first_number} é maior que {second_number}") if first_number > second_number else print(f"{second_number} é maior que {first_number}")