PI = 22.0 / 7.0

height = float(input('Digite a altura do cilindro: '))
radius = float(input('Digite o raio da base do cilindro: '))

base_area = PI * radius ** 2

print(f'Área da base do cilindro = {base_area}')
print(f'Área lateral do cilindro = {2 * PI * radius * height}')
print(f'Volume do cilindro = {base_area * height}')