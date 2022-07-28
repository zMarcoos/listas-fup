number = int(input("Digite um número: "))
fibonacci_list = []

if number == 1:
  fibonacci_list += [1]
elif number == 2:
  fibonacci_list += [1, 1]
else:
  fibonacci_list += [1, 1]
  for index in range(2, number):
    fibonacci_list.append(fibonacci_list[index - 1] + fibonacci_list[index - 2])

print(fibonacci_list)