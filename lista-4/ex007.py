from turtle import Turtle, Screen

def square_spiral(character, side_size, squares):
    for index in range(1, squares * 2 + 1):
        for _ in range(2):
            character.forward(side_size * index)
            character.left(90)
            

screen = Screen()
character = Turtle()

square_spiral(character, 15, 5)

screen.mainloop()
