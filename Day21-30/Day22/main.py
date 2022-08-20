from turtle import Screen
from paddle import Paddle

screen = Screen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

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
        screen.update()
    screen.exitonclick()


main()