from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self, x_size=1200, y_size=600):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("yellow")
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.setposition(random.randint(- x_size / 2 // 20 + 1, x_size / 2 // 20 - 1) * 20, random.randint(- y_size / 2 // 20 + 1, y_size / 2 // 20 - 1) * 20)

    def change_location(self, x_size=120,y_size=600):
        self.setposition(random.randint(- x_size / 2 // 20 + 1, x_size / 2 // 20 - 1) * 20, random.randint(- y_size / 2 // 20 + 1, y_size / 2 // 20 - 1) * 20)