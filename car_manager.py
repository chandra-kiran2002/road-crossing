COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random


class CarManager:
    def __init__(self):
        self.cars = []

    def create(self):
        tim = Turtle()
        tim.penup()
        tim.shape("square")
        tim.shapesize(1, 2)
        tim.color(COLORS[random.randint(0,5)])
        tim.setheading(180)
        tim.goto(300, random.randint(-230, 250))
        self.cars.append(tim)

    def move(self):
        for x in range(0, len(self.cars)):
            self.cars[x].forward(10)

    def remover(self):
        for x in self.cars:
            if x.xcor() < -300:
                self.cars.remove(x)
                x.hideturtle()
            else:
                break

    def detect(self, player):
        for x in self.cars:
            if x.distance(player) < 20:
                return 1
