from turtle import *

x = 10
y = 10
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(1)
        self.goto(0, 0)
    def reset_position(self):
        self.speed(0)
        self.goto(0,0)
        self.speed(1)
