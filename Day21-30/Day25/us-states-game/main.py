import turtle
import pandas

screen  = turtle.Screen()

def screen_setup():
    screen.title("U.S States Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)


def popup(correct_guess):
    answer_state = screen.textinput(title=f"{correct_guess}/50 States Correct", prompt="What's another state's name? ")
    return answer_state.title()


def find_state(answer):
    df = pandas.read_csv("50_states.csv")
    if answer not in df["state"].to_list():
        return
    else:
        x_cor = int(df[df["state"] == answer]["x"])
        y_cor = int(df[df["state"] == answer]["y"])
        return x_cor, y_cor

def write_state_on_map(answer, x_cor, y_cor):
    t = turtle. Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x_cor, y_cor)
    t.write(answer)


def states_to_learn(correct_guess_states):
    df = pandas.read_csv("50_states.csv")
    states_to_learn = []
    for state in df["state"].to_list():
        if state not in correct_guess_states:
            states_to_learn.append(state)
    new_df = pandas.DataFrame(states_to_learn)
    new_df.to_csv("states-to-learn.csv")

def main():
    screen_setup()
    is_game_on = True
    correct_guess_states = []
    correct_guess = 0
    while is_game_on:
        if correct_guess == 50:
            is_game_on = False
            continue
        answer = popup(correct_guess)
        if answer == "Exit":
            states_to_learn(correct_guess_states)
            break
        if answer not in correct_guess_states:
            if find_state(answer) is not None:
                correct_guess_states.append(answer)
                correct_guess += 1
                x_cor, y_cor = find_state(answer)
                write_state_on_map(answer, x_cor, y_cor)
    #turtle.mainloop()


main()