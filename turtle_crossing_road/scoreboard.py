import turtle

FONT = ("Courier", 20, "bold")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-270, 250)
        self.level = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"level: {self.level}", font=FONT)

    def add_level(self):
        self.level += 1
        self.write_score()

    def game_over(self):
        self.goto(-60, 0)
        self.write("GAME OVER", font=FONT)
