from turtle import Turtle, Screen
import random

souvik_turtle = Turtle()
souvik_screen = Screen()


def random_color():
    """Returns RGB values between 0 and 255"""
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    return red, green, blue


def draw_shape(sides):
    """Draws a shape based on number of sides"""
    angle = 360 / sides
    for _ in range(sides):
        souvik_turtle.forward(100)
        souvik_turtle.left(angle)


def main():
    """Controls all the functions"""
    souvik_screen.colormode(255)
    for i in range(3, 11):
        souvik_turtle.pencolor(random_color())
        draw_shape(i)


main()
souvik_screen.exitonclick()