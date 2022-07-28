def contaVogais(word: str):
  count = 0

  for letter in word:
    if letter in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
      count += 1
  
  return count