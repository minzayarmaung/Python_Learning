import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet.", prompt="Which turtle will win the race? Enter a color : ")

is_race_Start = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_Start = True

while is_race_Start:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_Start = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner.")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner.")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# tim = Turtle(shape="turtle")
# tim.penup()
# tim.color(colors[0])
# tim.goto(x=-230, y=100)
#
# tom = Turtle(shape="turtle")
# tom.penup()
# tom.color(colors[1])
# tom.goto(x=-230, y=60)
#
# tomy = Turtle(shape="turtle")
# tomy.penup()
# tomy.color(colors[2])
# tomy.goto(x=-230, y=20)
#
# jim = Turtle(shape="turtle")
# jim.penup()
# jim.color(colors[3])
# jim.goto(x=-230, y=-20)
#
# jimmy = Turtle(shape="turtle")
# jimmy.penup()
# jimmy.color(colors[4])
# jimmy.goto(x=-230, y=-60)
#
# jam = Turtle(shape="turtle")
# jam.penup()
# jam.color(colors[5])
# jam.goto(x=-230, y=-100)


screen.exitonclick()