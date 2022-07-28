def is_valid(side_one, side_two, side_three):
  return side_one < side_two + side_three and side_two < side_one + side_three and side_three < side_two + side_one

def triangle_type(side_one, side_two, side_three):
  if side_one == side_two == side_three:
      return 'Equilátero'
  elif side_one != side_two and side_two != side_three:
      return 'Escaleno'
  else:
      return 'Isóceles'

side_one = side_two = side_three = 0

while side_one <= 0 or side_two <= 0 or side_three <= 0: 
  side_one = int(input('First side: '))
  side_two = int(input('Second side: '))
  side_three = int(input('Third side: '))
else:
  if is_valid(side_one, side_two, side_three):
    print(triangle_type(side_one, side_two, side_three))