from turtle import Screen
from turtle import Turtle

# Screen
screen = Screen()
screen.setup(800, 600)
screen.title("Ping Pong")
screen.bgcolor("black")

# To Turn off Paddle Animation moving to the Direction
screen.tracer(0)

# Paddle
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

# To Turn off Paddle Animation moving to the Direction and Update it Manually
# Updating The Screen
game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
