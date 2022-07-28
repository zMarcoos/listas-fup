import turtle

width = int(input('Tamanho do lado: '))
line_amount = int(input('Quantidade de linhas: '))
columns = int(input('Quantidade de colunas: '))

screen = turtle.Screen()
screen.bgcolor('lightgray')
character = turtle.Turtle()
character.speed(0)
character.up()
character.goto(-screen.window_width() / 2, screen.window_height() / 2)
character.down()

for i in range(line_amount):
  for j in range(columns):
    if j % 2 == 0:
      character.color('black')
    else:
      character.color('white')
    
    character.begin_fill()
    for _ in range(4):
      character.forward(width)
      character.right(90)
    character.end_fill()
    character.forward(width)
    
    if i % 2 == 0:
      character.right(90)
      character.forward(width * 2)
      character.right(90)
    else:
      character.left(180)

screen.mainloop()