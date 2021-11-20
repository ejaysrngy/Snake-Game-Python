from turtle import Turtle
import random as r


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.change_location()

    def change_location(self):
        self.x_coord = r.randrange(-280, 280, 20)
        self.y_coord = r.randrange(-280, 260, 20)
        self.goto(self.x_coord, self.y_coord)
