import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
screen.title("The Turtle Coordinate System")


def set_position(turtle_instance, x_cor, y_cor):
    turtle_instance.goto(x_cor, y_cor)


def set_turtles(turtle_list):
    for i in range(NUMBER_TURTLES):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[i])
        new_turtle.penup()
        new_turtle.pensize(width=TURTLE_SIZE)
        last_position = - (NUMBER_TURTLES - 1) * DISTANCE_BETWEEN_TURTLES / 2
        x = -250 + TURTLE_SIZE / 2
        y = last_position + DISTANCE_BETWEEN_TURTLES * i
        set_position(new_turtle, x, y)
        turtle_list.append(new_turtle)


def turtle_coordinate_system():
    turtles = []
    is_race_on = False
    user_pet = screen.textinput(title="Choose Pet", prompt=f"Choose your pet from this list {'/'.join(colors)}: ")

    if user_pet:
        is_race_on = True

    set_turtles(turtles)

    while is_race_on:
        for turtle in turtles:
            random_step = random.randint(0, 10)
            turtle.forward(random_step)

            if turtle.xcor() >= 230:
                winner = turtle.color()[0]
                return f"Your pet {'won' if user_pet == winner else 'lost'}. Do you want to play again? (yes/no)"


colors = ["red", "blue", "green", "yellow", "purple", "orange"]
TURTLE_SIZE = 40
DISTANCE_BETWEEN_TURTLES = 40
NUMBER_TURTLES = len(colors)

is_playing = True
while is_playing:
    result = turtle_coordinate_system()
    want_play_again = screen.textinput(title="Play Game Again?", prompt=result)
    if want_play_again == "yes":
        is_playing = True
    else:
        is_playing = False
    screen.clear()
    # TODO: Clear Turtle instance when the race is finished

screen.exitonclick()
