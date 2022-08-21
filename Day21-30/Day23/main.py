import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()

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
        carmanager.create_car()
        carmanager.move_cars()

        #detect collision with car
        for car in carmanager.all_cars:
            if car.distance(player) < 20:
                game_is_on = False
                scoreboard.game_over()

        #detect a successful crossing
        if player.is_at_finish_line():
            player.go_to_start()
            carmanager.level_up()
            scoreboard.increase_level()

    screen.exitonclick()

main()