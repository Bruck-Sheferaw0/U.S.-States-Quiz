import turtle
import pandas
screen = turtle.Screen()
screen.setup(725,491)
screen.title("U.S. States Quiz")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")


states_data = pandas.read_csv("50_states.csv")
state_names = states_data.state
state_xcor = states_data.x.to_list()
state_ycor = states_data.y.to_list()
score = 0

state_names_list = states_data.state.to_list()

quiz_on = True
while quiz_on:
    chosen_state = screen.textinput(f"{score}/50 States Correct", "Name a state").title()
    if chosen_state.lower() == "exit":
        states_missed = {
            "State Names":state_names_list
        }
        data = pandas.DataFrame(states_missed)
        data.to_csv("Missed States")
        quiz_on = False

    if chosen_state in state_names.to_list():
        # removes state from state_names_list
        state_names_list.remove(chosen_state)
        # Determining state corrdinates from csv file
        states_list = state_names.to_list()
        x_value = state_xcor[states_list.index(chosen_state)]
        y_value = state_ycor[states_list.index(chosen_state)]
        # Turtle Writes the State Name
        text = turtle.Turtle()
        text.hideturtle()
        text.penup()
        text.speed(0)
        text.goto(x_value,y_value)
        text.write(chosen_state)

        score += 1

        if score == 50:
            quiz_on = False
    else:
        pass




turtle.mainloop()





