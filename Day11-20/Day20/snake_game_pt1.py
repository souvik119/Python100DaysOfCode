from turtle import Turtle, Screen

souvik_screen = Screen()

def screen_setup():
    """Sets up screen based on game requirement"""
    souvik_screen.setup(width=600, height=600)
    souvik_screen.bgcolor("black")
    souvik_screen.title("Snake Game")


def starting_position():
    """Places 3 sqaure turtles at stating position next to each other"""
    # each square is 20 x 20 by default so the offset
    starting_positions = [(0, 0), (-20, 0), (-40, 0)]
    for position in starting_positions:
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.goto(position)


def main():
    screen_setup()
    starting_position()
    souvik_screen.exitonclick()
    
main()