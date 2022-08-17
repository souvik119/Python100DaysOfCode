from turtle import Turtle, Screen

souvik_turtle = Turtle()
souvik_screen = Screen()

def draw_square(length):
    """Draws sqaure of specified length on screen"""
    for _ in range(4):
        souvik_turtle.forward(length)
        souvik_turtle.right(90)


draw_square(200)
souvik_screen.exitonclick()


