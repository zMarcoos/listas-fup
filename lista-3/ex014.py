while True:
  option = input('1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Sair\nOpção: ')
  if option == '5':
    print('Operação finalizada.')
    break

  number = int(input("Digite um número: "))
  otherNumber = int(input("Digite outro número: "))

  if option == '1': print(number + otherNumber)
  elif option == '2': print(number - otherNumber)
  elif option == '3': print(number * otherNumber)
  elif option == '4': print(number / otherNumber)
  else: print('Opção inválida')
