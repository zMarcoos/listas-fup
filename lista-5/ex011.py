def limites(lista: list):
  minimum = maximum = lista[0]

  for elemento in lista:
    if elemento < minimum:
      minimum = elemento
    if elemento > maximum:
      maximum = elemento
  
  return minimum, maximum