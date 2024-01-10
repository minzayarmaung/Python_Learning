import random
from turtle import Turtle, Screen

timmy = Turtle()
colors = ["red", "blue", "DarkGreen", "pink", "brown", "SeaGreen", "IndianRed", "DeepSkyBlue"]

for i in range(50):
    timmy.color(random.choice(colors))
    timmy.speed("fastest")
    timmy.circle(50)
    timmy.right(10)

screen = Screen()
screen.exitonclick()
