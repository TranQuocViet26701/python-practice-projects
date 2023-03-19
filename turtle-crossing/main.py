from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(player.up, "Up")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    # Generate car
    car_manager.generate_car()
    car_manager.move_cars()

    # Detect collision with car
    if car_manager.have_collision(player):
        scoreboard.game_over()
        is_game_on = False

    # Player reach the top edge
    if player.is_reach_top():
        player.refresh()
        car_manager.increase_speed()
        scoreboard.increase_score()

screen.exitonclick()
