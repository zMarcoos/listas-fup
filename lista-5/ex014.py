def slice(lista: list, number: int, number_two: int):
  nova_lista = []

  for item in range(number, number_two):
    nova_lista.append(lista[item])
  
  return nova_lista