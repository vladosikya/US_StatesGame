import turtle
import pandas

class StateCheched:
    def __init__(self):
        self.already_states = []
        self.state_frame = pandas.read_csv("50_states.csv")
        self.count_state = len(self.state_frame.state)

    def checker(self, answer):
        result = self.state_frame[self.state_frame.state == answer]
        result_lst = result.state.tolist()
        if result_lst == []:
            pass
        elif answer in self.already_states:
            pass
        else:
            state_x = int(result.x)
            state_y = int(result.y)
            state = turtle.Turtle()
            state.penup()
            state.goto(state_x, state_y)
            state.hideturtle()
            state.write(arg=answer, align='Center', font=('Arial', 8, 'normal'))
            self.already_states.append(result_lst[0])

    def end_game(self):
        end = turtle.Turtle()
        end.penup()
        end.hideturtle()
        end.write(arg="You won. Congratulations.", align='Center', font=('Arial', 35, 'bold'))


