from turtle import Turtle , Screen

timmy = Turtle()

triangle = 360/3
square = 360/4
pentagon = 360/5
hexagon = 360/6
heptagon = 360/7
octagon = 360/8
nonagon = 360/9
decagon = 360/10

for i in range(3):
    timmy.right(triangle)
    timmy.forward(100)

for i in range(4):
    timmy.right(square)
    timmy.forward(100)

for i in range(5):
    timmy.right(pentagon)
    timmy.forward(100)

for i in range(6):
    timmy.right(hexagon)
    timmy.forward(100)

for i in range(7):
    timmy.right(heptagon)
    timmy.forward(100)

for i in range(8):
    timmy.right(octagon)
    timmy.forward(100)

for i in range(9):
    timmy.right(nonagon)
    timmy.forward(100)

for i in range(10):
    timmy.right(decagon)
    timmy.forward(100)

screen = Screen()
screen.exitonclick()

