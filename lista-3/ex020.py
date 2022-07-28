binary = input("Digite um número binário: ")
answer = 0

for index in range(len(binary) - 1, -1, -1):
  answer += int(binary[index]) * 2 ** (len(binary) - index - 1)

print(f'O número binário {binary} corresponde ao número decimal {answer}')