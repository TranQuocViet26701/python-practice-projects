from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.creat_snake()
        self.head = self.segments[0]

    def creat_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.pensize(width=MOVE_DISTANCE)
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self, value=1):
        for _ in range(value):
            self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            xcor = self.segments[i - 1].xcor()
            ycor = self.segments[i - 1].ycor()
            self.segments[i].goto(xcor, ycor)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() == DOWN:
            return
        self.head.setheading(UP)

    def down(self):
        if self.head.heading() == UP:
            return
        self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() == RIGHT:
            return
        self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() == LEFT:
            return
        self.head.setheading(RIGHT)

    def reset(self):
        # Force segment go outside the screen
        for segment in self.segments:
            segment.goto(1000, 100)
        self.segments.clear()
        self.creat_snake()
        self.head = self.segments[0]
