number = int(input('Digite um número: '))

for index in range(1, number + 1):
  if number % index == 0:
    print(index, end=' ')
    
    if index == number // 2: break

print(number)
