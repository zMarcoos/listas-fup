number = int(input('Digite um número de 3 digitos: '))

print(number % 10 * 100 + number // 10 % 10 * 10 + number // 100 % 10)