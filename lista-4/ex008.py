from turtle import Turtle, Screen

def circle(character, radius, color):
    character.color(color)
    character.pencolor('black')
    character.right(90)
    character.forward(radius)
    character.left(90)
    character.down()
    character.begin_fill()
    character.circle(radius)
    character.end_fill()
    character.up()
    character.left(90)
    character.forward(radius)
    character.right(90)
            
def rings(character, radius, radius_two, sides, color):
    character.color(color)
    character.pencolor('black')
    character.forward(radius_two)
    character.left(90)
    
    for _ in range(sides):
        character.circle(radius_two, extent= 360 / sides)
        
        character.down()
        character.begin_fill()
        character.circle(radius)
        character.end_fill()
        character.up()
        
    character.left(90)
    character.forward(radius_two)
    character.left(180)

def target(character, radius, sides, color, color_two):
    character.pencolor('black')
    
    for index in range(sides, 0, -1):
        
        character.right(90)
        character.forward(radius * index)
        character.left(90)
        
        character.color(color if index % 2 == 0 else color_two)
        character.down()
        character.begin_fill()
        character.circle(radius * index)
        character.end_fill()
        character.up()
        
        character.left(90)
        character.forward(radius * index)
        character.right(90)

screen = Screen()
character = Turtle()
character.speed(0)
character.up()

# circle(c,100,"red")
# rings(c,20,100,32,"red")
# target(character, 10, 20, "red", "white")

screen.mainloop()
