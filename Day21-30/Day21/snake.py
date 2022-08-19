from turtle import Turtle

#defining constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        #list that will constain the 3 segments comprising the snake
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        """Creates a snake and positions it at starting position"""
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    
    def move(self):
        """Moves the snake on screen"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    
    def up(self):
        """Changes heading to up"""
        #so it cannot go back on itself
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    
    def down(self):
        """Changes heading to down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    
    def left(self):
        """Changes heading to left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    
    def right(self):
        """Changes heading to right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)