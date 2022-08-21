import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
player = Player()

def screen_setup():
    screen.setup(width=600, height=600)
    screen.title("Turtle Crossing")
    screen.tracer(0)
    screen.listen()
    screen.onkey(fun=player.go_up, key="Up")


def main():
    screen_setup()
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()

    screen.exitonclick()

main()