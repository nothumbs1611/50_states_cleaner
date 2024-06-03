import pandas
import csv
import turtle
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# determine xy coords for states
# def get_mouse_click(x, y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click)
# turtle.mainloop()

# pull in data
data = pandas.read_csv("50_states.csv")
data.to_csv("test.csv")
# make it a list
all_states = data.state.to_list()
# Record correct guesses in a list

guessed_states = []
# use a loop to allow user to continue guessing
while len(guessed_states) < 50:


    # ask user for an answer, convert to title case to match csv input format
    answer_state = screen.textinput(title=f"{len(guessed_states)} / 50 States Correct", prompt="What's another state's name?").title()

    # compare answer_state to the table to determine if it matches one of them.
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        #missing_states = []
        #for state in all_states:
            #if state not in guessed_states:
                #missing_states.append(state)
        save = pandas.DataFrame(missing_states)
        save.to_csv("States to learn.csv")
        break

    if answer_state in all_states:
         # if answer_state matches state, write it on the state location via turtle
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        #t.write(state_data.state.item())
        t.write(answer_state)

#output a file of states that the user did NOT guess correctly:
# states_to_learn = []
# for state in all_states:
#     if state not in guessed_states:
#         states_to_learn.append(state)
# save = pandas.DataFrame(states_to_learn)
#
# save.to_csv("States to learn.csv")

