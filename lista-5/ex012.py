def contaPares(lista: list):
  total = 0

  for elemento in lista:
    if elemento % 2 == 0:
      total += 1
  
  return total