import random
import colorgram
from turtle import Turtle, Screen

pacman = Turtle()
screen = Screen()
screen.colormode(255)


def extract_colors(image, number):
    color_list = colorgram.extract(image, number)
    result = []

    for color in color_list:
        rgb = color.rgb
        r, g, b = rgb   
        result.append((r, g, b))

    return result


def jump_row():
    pacman.setheading(90)
    pacman.forward(40)
    pacman.setheading(180)
    for i in range(9):
        pacman.forward(40)
    pacman.setheading(0)


def draw_painting():
    pacman.penup()
    pacman.hideturtle()
    pacman.speed("fastest")
    pacman.setheading(225)
    pacman.forward(300)
    pacman.setheading(0)
    for _ in range(12):
        for _ in range(9):
            random_color = random.choice(colors)
            pacman.dot(20, random_color)
            pacman.forward(40)
        jump_row()


colors = extract_colors("pycharm.jpeg", 10)

draw_painting()
screen.exitonclick()

