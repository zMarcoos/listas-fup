number = int(input('Digite um número de 4 digitos: '))

print(f'{number // 1000}\n{number % 1000 // 100}\n{number % 100 // 10}\n{number % 10}')