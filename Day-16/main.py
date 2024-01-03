import turtle
import prettytable

from prettytable import PrettyTable
from turtle import Turtle, Screen



timmy = Turtle()
print(timmy)

timmy.shape("turtle")
timmy.color("coral")
timmy.forward(200)
timmy.left(100)
timmy.forward(100)
timmy.right(100)
timmy.forward(100)
timmy.right(10)
timmy.right(20)
timmy.forward(100)
timmy.left(100)
timmy.left(20)

my_screen = Screen()
print(my_screen)
my_screen.exitonclick()