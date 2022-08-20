from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

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
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        #detect ball collision with top and bottom wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            #need to bounce
            ball.bounce_y()

        #detect ball collision with paddle
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            #need to bounce
            ball.bounce_x()

        #detect right paddle misses the ball
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.l_point()

        #detect left paddle misses the ball
        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.r_point()

        #first to 5 points wins
        if scoreboard.l_score == 5 or scoreboard.r_score == 5:
            game_is_on = False
            scoreboard.game_over()


    screen.exitonclick()


main()