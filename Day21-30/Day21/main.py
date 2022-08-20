from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

def setup_screen():
    """Sets up screen properties for the game"""
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    screen.listen()
    screen.onkey(fun=snake.up, key="Up")
    screen.onkey(fun=snake.down, key="Down")
    screen.onkey(fun=snake.left, key="Left")
    screen.onkey(fun=snake.right, key="Right")


def main():
    setup_screen()
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        #detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        #detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            scoreboard.game_over()

        #detect collision with tail
        #if head collides with any segment in the tail then initiate game over sequence
        for segment in snake.segments:
            if segment == snake.head:
                continue
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()
    
    screen.exitonclick()

main()