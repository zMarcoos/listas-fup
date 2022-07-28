a = float(input('Digite um número: '))
b = float(input('Digite um número: '))
c = float(input('Digite um número: '))

largest = c

if a > b and a > c:
    largest = a
elif b > a and b > c:
    largest = b
else:
    largest = c

print(f'O maior é {largest}')