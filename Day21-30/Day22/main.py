from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

def screen_setup():
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong Game!")
    screen.tracer(0)
    screen.listen()
    screen.onkey(fun=r_paddle.up, key="Up")
    screen.onkey(fun=r_paddle.down, key="Down")
    screen.onkey(fun=l_paddle.up, key="w")
    screen.onkey(fun=l_paddle.down, key="s")


def main():
    screen_setup()
    game_is_on = True
    while game_is_on:
        #for better ball visibility
        time.sleep(0.1)
        screen.update()
        ball.move()
    screen.exitonclick()


main()