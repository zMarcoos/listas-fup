def somaDivisores(number):
  total = number

  for i in range(1, number + 1):
    if number % i == 0:
      total += i

      if number // 2 == i: break
      
  return total