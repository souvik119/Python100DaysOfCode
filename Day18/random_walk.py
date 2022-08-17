from turtle import Turtle, Screen
import random

souvik_turtle = Turtle()
souvik_screen = Screen()

def random_color():
    """Returns RGB values between 0 and 255"""
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    return (red, green, blue)


def random_direction():
    """Points turtle in random direction"""
    directions = [0, 90, 180, 270]
    souvik_turtle.setheading(random.choice(directions))


def main():
    souvik_screen.colormode(255)
    souvik_turtle.pensize(10)
    souvik_turtle.speed("fastest")
    for _ in range(200):
        souvik_turtle.pencolor(random_color())
        souvik_turtle.forward(30)
        random_direction()

main()
souvik_screen.exitonclick()