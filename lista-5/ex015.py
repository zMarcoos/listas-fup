def menorFrente(l):
  minimum = l[0]
  for i in l:
      if i < minimum:
          minimum = i
      
  lista = l[:]
  lista.remove(minimum)
  lista.insert(0, minimum)
  
  return lista