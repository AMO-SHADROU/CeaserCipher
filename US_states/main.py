import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle2 = turtle.Turtle()
turtle2.hideturtle()
turtle2.penup()


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    user_answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Enter a state: ").title()
    if user_answer == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        pandas.DataFrame(missing_states).to_csv("Stest_to_learn.csv")
        break
    if user_answer in all_states and user_answer not in guessed_states:
        guessed_states.append(user_answer)
        state_data = data[data.state == user_answer]
        turtle2.goto(int(state_data.x.item()), int(state_data.y.item()))
        turtle2.write(state_data.state.item())



