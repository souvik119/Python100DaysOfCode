from turtle import Turtle, Screen

souvik_turtle = Turtle()
souvik_screen = Screen()

def move_forward():
    """Moves the tutle pointer forward by 10 paces"""
    souvik_turtle.forward(10)

souvik_screen.listen()
# when we pass a func as argument, do not use () since we do not want it to execute right then and there
souvik_screen.onkey(key="space", fun=move_forward)
souvik_screen.exitonclick()