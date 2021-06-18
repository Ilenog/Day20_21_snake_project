from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_random = random.randint(-480, 480)
        y_random = random.randint(-380, 380)
        self.setpos(x_random, y_random)
