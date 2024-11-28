from turtle import Turtle
FONT = ("Courier", 20, "normal") # 24 was too big for me


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
        """CHANGE DISPLAY OF LEVELS"""
        self.clear()
        self.level += 1
        self.write(f"Level:{self.level}", False, "center", font=FONT)

    def game_over(self):
        """PRINTS A GAME OVER MESSAGE"""
        self.goto(0, 0)
        self.write("Game Over", False, "center", font=FONT)
