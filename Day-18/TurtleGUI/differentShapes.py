import random
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

colors = ["red" , "blue" , "yellow" , "pink" , "brown" , "SeaGreen" , "IndianRed" , "DeepSkyBlue"]

for i in range(3):
    timmy.color(random.choice(colors))
    timmy.right(triangle)
    timmy.forward(100)

for i in range(4):
    timmy.color(random.choice(colors))
    timmy.right(square)
    timmy.forward(100)

for i in range(5):
    timmy.color(random.choice(colors))
    timmy.right(pentagon)
    timmy.forward(100)

for i in range(6):
    timmy.color(random.choice(colors))
    timmy.right(hexagon)
    timmy.forward(100)

for i in range(7):
    timmy.color(random.choice(colors))
    timmy.right(heptagon)
    timmy.forward(100)

for i in range(8):
    timmy.color(random.choice(colors))
    timmy.right(octagon)
    timmy.forward(100)

for i in range(9):
    timmy.color(random.choice(colors))
    timmy.right(nonagon)
    timmy.forward(100)

for i in range(10):
    timmy.color(random.choice(colors))
    timmy.right(decagon)
    timmy.forward(100)


screen = Screen()
screen.exitonclick()

