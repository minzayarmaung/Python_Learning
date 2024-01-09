import random
import turtle
from turtle import Turtle, Screen

timmy = Turtle()

colors = ["red", "blue", "DarkGreen", "pink", "brown", "SeaGreen", "IndianRed", "DeepSkyBlue"]
possible_values = [90, 180, 270, 360]
speed = ["slow", "normal", "fast", "fastest"]
pensize = [2, 3, 5, 6, 1, 4]
walk = [8, 15, 25, 20, 10, 5, 30]

for i in range(100):
    timmy.color(random.choice(colors))
    timmy.speed(random.choice(speed))
    timmy.pensize(random.choice(pensize))
    timmy.right(random.choice(possible_values))
    timmy.forward(random.choice(walk))

screen = Screen()
screen.exitonclick()
