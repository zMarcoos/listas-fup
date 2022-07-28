
ax = float(input('Digite o ponto ax: '))
ay = float(input('Digite o ponto ay: '))
bx = float(input('Digite o ponto bx: '))
by = float(input('Digite o ponto by: '))

x = bx - ax
y = by - ay

print(f'A distância entre ({ax}, {ay}) e ({bx}, {by}) é: {(y ** 2 + x ** 2) ** 0.5}')