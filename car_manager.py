from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.new_car()

    def move(self, level=0):
        new_x_pos = self.xcor()
        new_x_pos -= STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * level)
        self.goto(new_x_pos, self.ycor())

    def new_car(self):
        self.penup()
        self.shapesize(1, 2)
        self.shape("square")
        self.goto(320, random.randint(-250, 250))
        self.color(random.choice(COLORS))
