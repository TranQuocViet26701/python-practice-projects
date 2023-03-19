from turtle import Turtle
import random


class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        self.bonus_point = 1

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


class BetterFood(Food):

    def __init__(self):
        super().__init__()
        self.color("red")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.disappear()
        self.bonus_point = 2

    def disappear(self):
        self.hideturtle()

    def appear(self):
        self.showturtle()
