from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        with open("high_score.txt") as f:
            self.high_score = int(f.read())
        print(self.high_score)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increment(self, value=1):
        self.score += value
        self.update_score()

    def reset(self):
        self.high_score = max(self.high_score, self.score)
        with open("high_score.txt", mode="w") as f:
            f.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
