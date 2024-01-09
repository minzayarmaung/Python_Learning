from turtle import Turtle, Screen

timmy = Turtle()

for i in range(50):
    timmy.speed("fastest")
    timmy.circle(50)
    timmy.right(10)

screen = Screen()
screen.exitonclick()
