import turtle

number_sides = int(input('Quantidade de lados do polígono: '))
line_size = int(input('Tamanho da linha: '))

screen = turtle.Screen()
character = turtle.Turtle()

for _ in range(number_sides):
  character.forward(line_size)
  character.right(360 / number_sides)
    
screen.mainloop()
