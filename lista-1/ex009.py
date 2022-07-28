print('Equação: ax² + bx+ c = 0')

a = float(input('Digite o coeficiente a: '))
b = float(input('Digite o coeficiente b: '))
c = float(input('Digite o coeficiente c: '))

delta = b ** 2 - 4 * a * c
x1 = (-b + delta ** 0.5) / (2 * a)
x2 = (-b - delta ** 0.5) / (2 * a)

print(f'Delta = {delta}')
print(f'x\' = {x1}')
print(f'x\'\' = {x2}')