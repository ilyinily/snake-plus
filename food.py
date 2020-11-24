from turtle import Turtle
import random
X_SIZE = 1200
Y_SIZE = 600


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("yellow")
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        # noinspection PyTypeChecker
        self.setposition(random.randint(- X_SIZE / 2 // 20 + 1, X_SIZE / 2 // 20 - 1) * 20, random.randint(- Y_SIZE / 2 // 20 + 1, Y_SIZE / 2 // 20 - 1) * 20)

    def change_location(self, x_size=120, y_size=600):
        # noinspection PyTypeChecker
        self.setposition(random.randint(- x_size / 2 // 20 + 1, x_size / 2 // 20 - 1) * 20, random.randint(- y_size / 2 // 20 + 1, y_size / 2 // 20 - 1) * 20)

    def move(self):
        if random.randint(0, 20) == 20 and (-1200 / 2 + 20 < self.position()[0] < 1200 / 2 - 20) and (-600 / 2 + 20 < self.position()[1] < 600 / 2 - 20):
            self.setheading(random.randint(0, 3) * 90)
            self.forward(random.randint(0, 1) * 20)
