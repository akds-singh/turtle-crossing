import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):

        self.car = None
        self.cars_list = []
        # self.move()

    def create_car(self):
        ran_num = random.randint(1, 6)
        if ran_num == 6:
            self.car = Turtle()
            self.car.shape('square')
            self.car.shapesize(stretch_wid=1, stretch_len=2)

            self.car.penup()
            self.car.color(random.choice(COLORS))
            self.car.setheading(180)
            self.car.goto(290, random.randint(-250, 250))
            self.cars_list.append(self.car)

    def move(self):
        print(len(self.cars_list))
        for c in self.cars_list:
            c.forward(STARTING_MOVE_DISTANCE)
        # while not self.xcor() < -300:
