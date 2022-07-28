number = int(input("Digite um número: "))

print('-' * 16)

for index in range(1, number + 1):
  print('*' * index)

print('-' * 16)

for index in range(number, 0, -1):
  print('*' * index)

print('-' * 16)

for index in range(number, 0, -1):
  print(' ' * (number - index) + '*')  

print('-' * 16)

for index in range(1, number + 1):
  print(' ' * (number - index) + '*')

print('-' * 16)

for index in range(number, 0, -1):
  print(' ' * (number - index) + '*' * index)

print('-' * 16)

for index in range(0, number + 1):
  print(' ' * (number - index) + '*' * index)

print('-' * 16)

for index in range(0, number):
  print(' ' * index + '* ' * number)

print('-' * 16)

for index in range(number, 0, -1):
  print(' ' * (number - index) + '* ' * index)

print('-' * 16)

for index in range(number, 0, -1):
  print((number - index) * ' ', end='')

  for jndex in range(index):
    print('* ', end='') if jndex == 0 or jndex + 1 == index else print('  ', end='')
  print() 

print('-' * 16)