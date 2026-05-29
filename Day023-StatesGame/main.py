import turtle
import pandas

screen = turtle.Screen()
screen.title("India States Game")
screen.setup(width=800, height=800)   # adjust to your gif size
screen.bgpic("blank_states_img.gif")
data = pandas.read_csv("28_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 28:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/28 States Correct",
        prompt="What's another state's name?"
    )
    if answer_state is None:
        continue

    answer_state = answer_state.title().strip()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(
                int(state_data.x.item()),
                int(state_data.y.item())
            )
            t.write(
                answer_state,
                align="center",
                font=("Arial", 8, "bold")
            )

if len(guessed_states) == 28:
    message = turtle.Turtle()
    message.hideturtle()
    message.penup()
    message.goto(0, 0)
    message.write(
        "Congratulations! You guessed all 28 states!",
        align="center",
        font=("Arial", 16, "bold")
    )
screen.mainloop()