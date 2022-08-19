from turtle import Turtle, Screen

souvik_turtle = Turtle()
souvik_screen = Screen()


def move_forward():
    """Moves the turtle pointer forward by 10 paces"""
    souvik_turtle.forward(10)

def move_backward():
    """Moves the turtle pointer backward by 10 paces"""
    souvik_turtle.backward(10)

def turn_left():
    """Moves the turtle pointer counter clockwise by 10 deg"""
    new_heading = souvik_turtle.heading() + 10
    souvik_turtle.setheading(new_heading)

def turn_right():
    """Moves the turtle pointer clockwise by 10 deg"""
    new_heading = souvik_turtle.heading() - 10
    souvik_turtle.setheading(new_heading)

def clear():
    """Clears the screen"""
    souvik_turtle.clear()
    #bring turtle back to the original position
    souvik_turtle.penup()
    souvik_turtle.home()

    
souvik_screen.listen()
# when we pass a func as argument, do not use () since we do not want it to execute right then and there
souvik_screen.onkey(key="w", fun=move_forward)
souvik_screen.onkey(key="s", fun=move_backward)
souvik_screen.onkey(key="a", fun=turn_left)
souvik_screen.onkey(key="d", fun=turn_right)
souvik_screen.onkey(key="c", fun=clear)
souvik_screen.exitonclick()