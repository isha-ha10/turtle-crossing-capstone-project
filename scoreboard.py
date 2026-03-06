from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level_number()
    def level_number(self):
        self.goto(-250, 250)
        self.write(f"Level={self.level}",align="left",font=FONT)
    def new_level(self):
        self.clear()
        self.level+=1
        self.level_number()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)

