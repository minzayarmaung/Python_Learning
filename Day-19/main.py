from turtle import Turtle , Screen

timmy = Turtle()

def move_forwards():
    timmy.forward(10)

screen = Screen()
screen.listen()
screen.onkey(key="space" , fun=move_forwards)

screen.exitonclick()