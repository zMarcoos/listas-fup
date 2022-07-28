a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

print(f"A({a}) é múltiplo de B({b})") if a % b == 0 else print(f"A({a}) não é múltiplo de B({b})")