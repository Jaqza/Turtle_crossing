from turtle import Turtle
from random import randint, choice
COLORS = ["red", "orange", "yellow", "black", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def creating_cars(self):
        chance = randint(1, 6)
        if chance == 1:
            paint = choice(COLORS)
            generated_y = randint(-260, 260)
            car = Turtle("square")
            car.penup()
            car.shapesize(1, 2)
            car.shape()
            car.color(paint)
            self.cars.append(car)
            car.goto(300, generated_y)

    def traffic(self):
        for car in self.cars:
            car.back(self.car_speed)

    def run_over(self):
        self.car_speed = 0

    def car_speed_up(self):
        self.car_speed += MOVE_INCREMENT
