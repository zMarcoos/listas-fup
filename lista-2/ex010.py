operation = int(input('1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\nSelecionar: '))
first_number = float(input ("1° valor: "))
second_number = float(input ("2° Valor: "))
answer = 0

if operation == 1:
    answer = first_number + second_number
elif operation == 2:
    answer = first_number - second_number
elif operation == 3:
    answer = first_number * second_number
else:
    answer = first_number / second_number

print(f'Resultado = {answer}')