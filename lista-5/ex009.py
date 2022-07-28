from random import randint

def numerosAleatorios(amount, minimum, maximum):
  lista = []
  for _ in range(amount):
    lista.append(randint(minimum, maximum))
  return lista

print(numerosAleatorios(5, 10, 30))