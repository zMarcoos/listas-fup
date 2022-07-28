ax = int(input('ax: '))
ay = int(input('ay: '))
bx = int(input('bx: '))
by = int(input('by: '))
xmin = int(input('xmin (caixa): '))
ymin = int(input('ymin (caixa): '))
xmax = int(input('xmax (caixa): '))
ymax = int(input('ymax (caixa): '))

collided = False

while ax < xmax:
  if xmax > ax > xmin and ymax > ay > ymin:
    collided = True
    break
  
  ax = ax + bx
  ay = ay + by
  
print('A reta cruza a caixa') if collided else print('A reta não cruza a caixa')
