import time
from turtle import Screen
from snake import Snake
from food import Food, BetterFood
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
better_food = BetterFood()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.left, "Left")
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend(food.bonus_point)
        scoreboard.increment(food.bonus_point)
        # TODO: appear super food with some conditions (find condition)
        if scoreboard.score % 5 == 0:
            better_food.refresh()
            better_food.appear()

    # Detect collision with better food
    if better_food.isvisible() and snake.head.distance(better_food) < 15:
        better_food.disappear()
        snake.extend(better_food.bonus_point)
        scoreboard.increment(better_food.bonus_point)

    # Detect collision with wall
    current_xcor = snake.head.xcor()
    current_ycor = snake.head.ycor()

    if current_xcor > 280 or current_xcor < -280 or current_ycor > 280 or current_ycor < -280:
        scoreboard.reset()
        snake.reset()
        # is_game_on = False

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if segment.distance(snake.head) < 10:
            scoreboard.reset()
            snake.reset()
            # is_game_on = False

screen.exitonclick()
