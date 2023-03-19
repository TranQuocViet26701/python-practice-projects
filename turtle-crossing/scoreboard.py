from turtle import Turtle
FONT = "Courier", 24, "normal"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
