import turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
all_cars = []


class CarManager(turtle.Turtle):
    def __init__(self):
        super().__init__()
        all_cars.append(self)
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(180)
        self.shapesize(stretch_len=2)
        self.goto(300, random.randint(-250, 250))
        self.move_speed = STARTING_MOVE_DISTANCE

    def increase_speed(self):
        self.move_speed = STARTING_MOVE_DISTANCE + MOVE_INCREMENT

    def move_cars(self):
        for car in all_cars:
            car.forward(self.move_speed)
