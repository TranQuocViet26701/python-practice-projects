import pandas


class StateManager:

    def __init__(self):
        self.state_data = pandas.read_csv("50_states.csv")
        print(self.state_data)

    def find(self, state):
        """Find state with a state string"""
        formatted_state = state.strip().title()
        return self.state_data[self.state_data.state == formatted_state]

