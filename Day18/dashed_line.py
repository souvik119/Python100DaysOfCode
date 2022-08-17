from turtle import Turtle, Screen

souvik_turtle = Turtle()
souvik_screen = Screen()

for _ in range(15):
    souvik_turtle.pendown()
    souvik_turtle.forward(10)
    souvik_turtle.penup()
    souvik_turtle.forward(10)

souvik_screen.exitonclick()