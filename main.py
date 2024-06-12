from turtle import Screen, Turtle
import pandas as pd


FONT = ("Courier", 10, "normal")
ALIGN = "center"

# create screen object
screen = Screen()
screen.title("U.S. States Game")

turtle = Turtle()

# import image of USA
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# create labeller object
labeller = Turtle()
labeller.hideturtle()
labeller.penup()

# import csv of state names and coordinates
states_df = pd.read_csv("50_states.csv")

num_correct = 0
game_on = True
correct_answers = []

# while loop to keep accepting answers
while game_on:
    answer = screen.textinput(f"{num_correct}/50 States Correct", "What's another state name?").title()

    if answer in correct_answers:
        print(f"Already guessed {answer}. Make another guess.")
    elif answer in states_df.state.values:
        # get the x,y coord of the state
        x_corr = states_df[states_df.state == answer].x.values[0]
        y_corr = states_df[states_df.state == answer].y.values[0]
        # print the state on the map
        labeller.goto(x=x_corr, y=y_corr)
        labeller.write(answer, align=ALIGN, font=FONT)
        # track the answers
        num_correct += 1
        correct_answers.append(answer)
    else:
        # something for when they get it wrong
        print('Incorrect. Enter new guess.')

    # some condition for exiting the game early
    if num_correct == 50:
        print("You got them all correct!")
        game_on = False

screen.exitonclick()
