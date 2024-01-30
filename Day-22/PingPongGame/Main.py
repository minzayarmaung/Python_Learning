from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# Screen
screen = Screen()
screen.setup(800, 600)
screen.title("Ping Pong")
screen.bgcolor("black")

# To Turn off Paddle Animation moving to the Direction
screen.tracer(0)

# Paddle
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

# Ball
ball = Ball()

# Scoreboard
scoreboard = ScoreBoard()

screen.listen()

# KEY_MOVEMENTS
# For the Right Paddle
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

# For the Left Paddle
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

# To Turn off Paddle Animation moving to the Direction and Update it Manually
# Updating The Screen
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect Collision with the Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # It Needs to Bounce
        ball.bounce_y()

    # Detect Collision with Paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320 or
            ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect Right Paddle Misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    # Detect Left Paddle Misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()
