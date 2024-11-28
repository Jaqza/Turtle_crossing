from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 25 #DAFAULT = 10 ONLY FOR TESTS
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def go_on_start(self):
        """RESET POSITION AFTER CROSSING OVER THE STREET"""
        self.goto(STARTING_POSITION)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)
