from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-230, 270)
        self.level_up()

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level:{self.level}", False, "center", font=FONT)
