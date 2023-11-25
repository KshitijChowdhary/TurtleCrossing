from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 265)
        self.write(f"Level: {self.level}", False, align=ALIGNMENT, font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(-200, 265)
        self.write(f"Level: {self.level}", False, align=ALIGNMENT, font=FONT)
        self.goto(0, 0)
        self.write("Game Over!", False, align = ALIGNMENT, font = FONT)
