import turtle

height = int(input('Altura de cada camada: '))
width = int(input('Largura da coluna do topo: '))
amount = int(input('Quantidade de camadas: '))

screen = turtle.Screen()
character = turtle.Turtle()

character.begin_fill()
for index in range(1, amount + 1):
  for _ in range(2):
    character.forward(width * index)
    character.right(90)
    character.forward(height)
    character.right(90)
    
  character.goto(0, -height * index)
character.color('green')
character.end_fill()

screen.mainloop()