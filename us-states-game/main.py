from turtle import Turtle, Screen
from state_manager import StateManager
from scoreboard import ScoreBoard

state_manager = StateManager()
scoreboard = ScoreBoard()

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle = Turtle()
turtle.shape(image)


is_guess_all = len(state_manager.state_data) == scoreboard.score
while not is_guess_all:
    answer_state = screen.textinput(title=f"{scoreboard.score}/{len(state_manager.state_data)} States",
                                    prompt="What's another state's name?")
    if not answer_state or answer_state == "exit":
        break

    found_state = state_manager.find(answer_state)
    if not found_state.empty:
        scoreboard.add_answer(found_state)

scoreboard.report(state_manager.state_data.state.to_list())

screen.exitonclick()

