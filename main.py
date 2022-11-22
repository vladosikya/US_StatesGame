import turtle, pandas
from state_checker import StateCheched

GAME = True

screen = turtle.Screen()
screen.tracer(0)
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
checker = StateCheched()
screen.update()

while GAME:
    answer = screen.textinput(title=f"You guessed {len(checker.already_states)}/{checker.count_state} states.", prompt="What other states do you know?").title()
    checker.checker(answer)
    screen.update()
    if len(checker.already_states) == checker.count_state:
        GAME = False
        checker.end_game()

screen.exitonclick()