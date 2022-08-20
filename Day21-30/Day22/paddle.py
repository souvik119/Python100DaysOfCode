from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        #normal square dimension 20 x 20 but we want 20 x 100
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

    
    def up(self):
        """Moves the paddle up 20 pixels"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    
    def down(self):
        """Moves the paddle down 20 pixels"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)