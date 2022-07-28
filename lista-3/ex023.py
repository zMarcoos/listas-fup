amount = int(input ("Quantidade de pontos: "))
xmin = xmax = ymin = ymax = None

for index in range(1, amount + 1):
  x = int(input("x: "))
  y = int(input("y: "))

  if xmin is None or x < xmin:
    xmin = x
  if xmax is None or x > xmax:
    xmax = x
  if ymin is None or y < ymin:
    ymin = y
  if ymax is None or y > ymax:
    ymax = y

print(f'Mínimo: {xmin}, {ymin}')
print(f'Máximo: {xmax}, {ymax}')