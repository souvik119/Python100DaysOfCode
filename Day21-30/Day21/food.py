from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        #accessing turtle class attributes since we inherited
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    
    def refresh(self):
        #leaving some margin
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)