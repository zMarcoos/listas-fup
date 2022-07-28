def repeteVogal(word: str):
  new_word = ''

  for letter in word:
    new_word += letter

    if letter in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
      new_word += letter
  return new_word