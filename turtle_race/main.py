import random
import turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race? Enter a color:  ")
rainbow_color = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y_axis = -175
index = 0
for color in rainbow_color:
    new_turtle = turtle.Turtle("turtle")
    new_turtle.color(rainbow_color[index])
    new_turtle.penup()
    new_turtle.goto(-280, y_axis)
    all_turtles.append(new_turtle)
    y_axis += 65
    index += 1

game_is_on = True
while game_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 268:
            if turtle.pencolor() == user_bet:
                print("you won!!!")
                game_is_on = False
            else:
                print(f"{turtle.pencolor()} wins!!!")
                game_is_on = False
        turtle.forward(random.randint(0, 10))


screen.exitonclick()
