import random
import time
from turtle import Screen
from player import Player
import car_manager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = car_manager.CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if random.randint(1, 6) == 1:
        car = car_manager.CarManager()
    car.move_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect if the player has pass this level
    if player.pass_the_line():
        player.goto_start()
        car.increase_speed()
        scoreboard.add_level()

screen.exitonclick()
