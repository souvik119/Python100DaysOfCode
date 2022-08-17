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

def draw_circle():
    """Draws a circle based on radius"""
    souvik_turtle.circle(100)

def main(size_of_gap):
    souvik_screen.colormode(255)
    souvik_turtle.speed("fastest")
    for _ in range(int(360 / size_of_gap)):
        souvik_turtle.pencolor(random_color())
        draw_circle()
        souvik_turtle.setheading(souvik_turtle.heading() + size_of_gap)

main(5)
souvik_screen.exitonclick()