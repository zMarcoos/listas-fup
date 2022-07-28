# opção 1
def inverte(s):
  word = ''

  for index in range(len(s) - 1, -1, -1):
    word += s[index]

  return word

# opção 2
def inverte2(s):
  return s[::-1]