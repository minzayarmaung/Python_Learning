import random
from turtle import Turtle, Screen

colors = ["red", "blue", "DarkGreen", "pink", "brown", "SeaGreen", "IndianRed", "DeepSkyBlue"]

timmy = Turtle()

dot_size = 20
distance = 30
rows = 10
columns = 10


def drawShape():
    for i in range(10):
        timmy.penup()
        timmy.color(random.choice(colors))
        timmy.dot(dot_size)
        timmy.forward(distance)


def goBackward():
    timmy.setheading(90)
    timmy.forward(dot_size * 2)
    timmy.setheading(0)
    timmy.backward(300)


for i in range(10):
    drawShape()
    goBackward()

# for row in range(rows):
#     for columns in range(columns):
#         timmy.penup()
#         timmy.color(random.choice(colors))
#         timmy.dot(dot_size)
#         timmy.forward(distance)
#
#         timmy.setheading(90)
#         timmy.forward(dot_size)
#         timmy.setheading(0)
#
#         timmy.backward(distance * columns)
#         timmy.setheading(0)
#         timmy.forward(distance)


screen = Screen()
screen.exitonclick()
