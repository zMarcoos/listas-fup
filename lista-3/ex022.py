height = int(input('Altura: '))
blocks = 0

for index in range(1, height + 1):
  blocks += index ** 2

print(f'Total de blocos: {blocks}')