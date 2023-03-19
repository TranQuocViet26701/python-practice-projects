from turtle import Turtle

import pandas


class ScoreBoard:

    # init method or constructor
    def __init__(self):
        self.correct_list = []
        self.score = 0

    def add_answer(self, state):
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.hideturtle()
        x, y, state_name = state.x.item(), state.y.item(), state.state.item()
        new_turtle.goto(x, y)
        new_turtle.write(f"{state_name}", align="center", font=("Arial", 16, "normal"))
        self.correct_list.append(state_name)
        self.score = len(self.correct_list)

    def report(self, all_states):
        missing_state = [state for state in all_states if state not in self.correct_list]
        df = pandas.DataFrame(missing_state)
        df.to_csv("state_to_learn.csv")
        print(df)
        print(f"score: {self.score}")

