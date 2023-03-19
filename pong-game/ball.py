from turtle import Turtle


class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(45)
        self.move_speed = 0.1

    def move(self):
        new_xcor = self.xcor() + 10
        new_ycor = self.ycor() + 10
        self.goto(new_xcor, new_ycor)

    def bounce_y(self):
        new_heading = 360 - self.heading()
        self.setheading(new_heading)

    def bounce_x(self):
        new_heading = (360 + (180 - self.heading())) % 360
        self.setheading(new_heading)
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1
