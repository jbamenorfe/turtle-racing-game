"""Turtle_racing_game uses python's turtle module to create a program which allows the user to guess the specific
turtle out of seven, that he/she believes will win a race. The user is given a feedback on his/her guess
depending on the turtle that wins the race"""

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

race_is_on = False

user_guess = screen.textinput("Make your bet", "Which turtle will win the race?\nThe racing turtles are: "
"(red, orange, yellow, green, blue and purple).\n\nEnter a color: ").lower()
turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Create a list of turtles called "turtles" and place individual turtles in it
turtles = []
x_start_position = -230
y_start_position = -100
for turtle_color in turtle_colors:
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(turtle_color)
    new_turtle.goto(x=x_start_position, y=y_start_position)
    y_start_position += 40
    turtles.append(new_turtle)

# Check to see if user made a guess. Start race if user made a guess
if user_guess and user_guess in turtle_colors:
    race_is_on = True
else:
    print("You entered a wrong color! Please choose a color from the list provided")
    race_is_on = False

while race_is_on:
    for turtle in turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            race_is_on = False
            winning_turtle = turtle
            if turtle.pencolor() == user_guess:
                print(f"You Won! The {turtle.pencolor()} turtle is the winner!")
            else:
                print(f"You lost! The {turtle.pencolor()} turtle is the winner!")

screen.exitonclick()