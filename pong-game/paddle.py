from turtle import Turtle
MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, position=(350, 0)):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def vertical_move(self, distance):
        new_ycor = self.ycor() + distance
        self.goto(self.xcor(), new_ycor)

    def go_up(self):
        self.vertical_move(MOVE_DISTANCE)

    def go_down(self):
        self.vertical_move(-MOVE_DISTANCE)

