def is_prime(number):
  for index in range(2, int(number ** 0.5) + 1):
    if number % index == 0:
      return False
  
  return True

number = int(input("Digite um número: "))
print(f'{number} é primo') if is_prime(number) else print(f'{number} não é primo')
