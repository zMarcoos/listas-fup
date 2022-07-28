from turtle import Turtle, Screen

def square(character, side_size):
    character.down()
    
    for _ in range(4):
        character.forward(side_size)
        character.left(90)
        
    character.up()
    
def square_line(character, side_size, squares):
    for _ in range(squares):
        square(character, side_size)
        
        character.forward(side_size * 2)
        
    character.backward(side_size * squares * 2)

def square_grid(character, side_size, squares):
    for i in range(squares):
        square_line(character, side_size, squares)
        
        if (squares - 1 != i):
            character.right(90)
            character.forward(side_size * 2)
            character.left(90)

def square_spiral(character, side_size, squares):
    for _ in range(squares):
        for _ in range(4):
            character.forward(side_size)
            character.left(90)
            
        character.right(360 / squares)
        
screen = Screen()
character = Turtle()
character.speed(0)

# square(character, 100)
# square_line(character, 20, 5)
# square_grid(character, 20, 5)
# square_spiral(character, 50, 16)

screen.mainloop()
