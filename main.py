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
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.ycor() >= 280:
        player.go_on_start()
        scoreboard.level_up()

    if scoreboard.level == 2:
        """CHANGE IT WHEN THE COLLISION OCCUR"""
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
