import random
from turtle import Turtle
COLORS = ["red", "green", "blue", "purple", "pink", "orange", "yellow"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def generate_car(self):
        # Generate car when random chance is 6, decrease frequently car
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            random_color = random.choice(COLORS)
            random_ycor = random.randint(-230, 230)
            new_car = Car(color=random_color, position=(280, random_ycor))
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.move(move_distance=self.move_distance)

    def have_collision(self, player):
        for car in self.cars:
            if car.is_collision(player):
                return True

        return False

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT


class Car(Turtle):

    def __init__(self, color, position):
        super().__init__()
        self.penup()
        self.color(color)
        self.goto(position)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)

    def move(self, move_distance=STARTING_MOVE_DISTANCE):
        self.backward(move_distance)

    def is_collision(self, player):
        return self.distance(player) < 20

