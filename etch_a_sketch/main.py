import turtle
import random

turtle1 = turtle.Turtle()
screen = turtle.Screen()
screen.listen()


def move_forward():
    turtle1.forward(10)


def move_backward():
    turtle1.backward(10)


def turn_left():
    new_heading = turtle1.heading() + 10
    turtle1.setheading(new_heading)


def turn_right():
    new_heading = turtle1.heading() - 10
    turtle1.setheading(new_heading)


def clear():
    turtle1.clear()
    turtle1.penup()
    turtle1.home()
    turtle1.pendown()


screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=clear, key="c")

screen.exitonclick()
