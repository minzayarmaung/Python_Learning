from turtle import Turtle, Screen

timmy = Turtle()


def reset():
    timmy.home()
    timmy.clear()


def move_forwards():
    timmy.forward(10)


def move_backwards():
    timmy.backward(10)


def move_left():
    timmy.left(10)


def move_right():
    timmy.right(10)


screen = Screen()
screen.listen()
screen.onkey(key="c", fun=reset)
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d" , fun=move_right)

screen.exitonclick()
