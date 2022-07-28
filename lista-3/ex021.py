x = int(input('x: '))
y = int(input('y: '))

coordinates = []

for index in range(1, 9):
  if y != index: 
    coordinates.append((x, index))
    
  if x != index:
    coordinates.append((index, y))

print(f'Possíveis combinações: {coordinates}')
