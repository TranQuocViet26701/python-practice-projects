import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle()
l_paddle = Paddle(position=(-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)

    ball.forward(10)
    # Detect collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detect collision with paddle
    if (ball.xcor() >= 320 and ball.distance(r_paddle) < 50) or (ball.xcor() <= -320 and ball.distance(l_paddle) < 50):
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_l()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_r()

screen.exitonclick()
