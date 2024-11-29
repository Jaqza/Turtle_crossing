import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("gray")
screen.listen()
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
screen.onkey(player.move_forward, "w")
car_manager = CarManager()

game_is_on = True

while game_is_on:
    car_manager.creating_cars()
    time.sleep(0.1)
    car_manager.traffic()

    screen.update()

    if player.ycor() >= 280:
        player.go_on_start()
        scoreboard.level_up()
        car_manager.car_speed_up()

    for car in car_manager.cars:
        if car.distance(player) < 22:
            car_manager.run_over()
            scoreboard.game_over()
            game_is_on = False
screen.exitonclick()
