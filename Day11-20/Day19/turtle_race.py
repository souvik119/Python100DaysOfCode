from turtle import Turtle, Screen
import random

souvik_turtle = Turtle()
souvik_screen = Screen()

#define screen dimension since it is critical for a race
#in this case 500 pixels wide and 400 pixels high
#keyword argument better in this case since otherwise it does not make sense

def screen_setup():
    """Sets a screen based on dimensions"""
    souvik_screen.setup(width=500, height=400)


def screen_popup():
    """Creates the screen popup at the beginning of the race and returns user input"""
    user_bet = souvik_screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color (red/orange/yellow/green/blue/prurple)")
    return user_bet


def turtle_setup():
    """Creates a turtle obeject based on color and returns the dictionary"""
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    turtle_dict = {}
    for color in colors:
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(color)
        new_turtle.penup()
        turtle_dict[color] = new_turtle
    return turtle_dict


def starting_position(turtle_dict):
    """Places turtles at the starting position for race"""
    # x axis will remain constant for all 6 turtles
    # y axis will change to make sure turtles do not overlap
    x_axis = -230
    y_axis_start = -180
    for turtle in turtle_dict:
        turtle_dict[turtle].goto(x=x_axis, y=y_axis_start)
        y_axis_start += 70


def move_forward_random(turtle):
    """Accepts a turtle object and moves it formward by a random amount of pixels between 0 and 10"""
    turtle.forward(random.randint(0, 10))


def main():
    is_race_on = False
    screen_setup()
    user_bet = screen_popup()
    print(user_bet)
    turtle_dict = turtle_setup()
    starting_position(turtle_dict)
    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in turtle_dict:
            if turtle_dict[turtle].xcor() > 230:
                is_race_on = False
                winning_color = turtle_dict[turtle].pencolor()
                if winning_color == user_bet.lower():
                    print(f"You won! the winning color is : {winning_color}")
                else:
                    print(f"You lost! the winning color is : {winning_color}")
            move_forward_random(turtle_dict[turtle])
    souvik_screen.exitonclick()

main()