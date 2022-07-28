ax = int(input('ax: '))
ay = int(input('ay: '))
bx = int(input('bx: '))
by = int(input('by: '))
amount = int(input('Quantidade : '))

coordinates = [(ax, ay), (bx, by)]

for _ in range(1, amount + 1):
  ax = ax + bx
  ay = ay + by

  coordinates.append((ax, ay))

print(f'Pontos: {coordinates}')