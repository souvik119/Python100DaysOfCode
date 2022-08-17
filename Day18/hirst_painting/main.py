import colorgram
from turtle import Turtle, Screen
import random

souvik_turtle = Turtle()
souvik_screen = Screen()

def extract_color():
    """Returns a list of rgb tuples of colors extracted from an image"""
    colors = colorgram.extract("C:\\Users\\sghosh\\Documents\\Python100DaysOfCode\\Day18\\hirst_painting\\image.jpg", 30)
    rgb_list = []
    for color in colors:
        rgb_list.append((color.rgb.r, color.rgb.b, color.rgb.g))
    return rgb_list

def draw_dot(rgb_color):
    """Draws a dot of size 20 and specified rgb color"""
    souvik_turtle.dot(20, rgb_color)

def starting_position():
    """Sets the cursor to desirable starting location for better visual appearance"""
    souvik_turtle.setheading(225)
    souvik_turtle.penup()
    souvik_turtle.forward(300)
    souvik_turtle.setheading(0)
    souvik_turtle.pendown()

def main():
    rgb_list = extract_color()
    souvik_screen.colormode(255)
    souvik_turtle.speed("fastest")
    souvik_turtle.hideturtle()
    starting_position()
    for _ in range(10):
        for _ in range(10):
            draw_dot(random.choice(rgb_list))
            souvik_turtle.penup()
            souvik_turtle.forward(50)
            souvik_turtle.pendown()
        souvik_turtle.setheading(90)
        souvik_turtle.penup()
        souvik_turtle.forward(50)
        souvik_turtle.setheading(180)
        souvik_turtle.forward(500)
        souvik_turtle.setheading(0)
        souvik_turtle.pendown()

main()
souvik_screen.exitonclick()