from turtle import *
class Racket_Right(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(6,1,12)
        self.penup()
        self.goto(360,0)
        print(self.xcor(),self.ycor())
    def up(self):
        if self.ycor() < 220:
            newycor = self.ycor()+20
            self.goto(self.xcor(),newycor)
        else:
            print("R's ycor is beyond range")
    def down(self):
        if self.ycor() > -220:
            newycor = self.ycor()-20
            self.goto(self.xcor(),newycor)
        else:
            print("R's ycor is beyond range")


class Racket_Left(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(6,1,12)
        self.penup()
        self.goto(-360,0)
        print(self.xcor(),self.ycor())
    def up(self):
        if self.ycor() < 220:
            newycor = self.ycor()+20
            self.goto(self.xcor(),newycor)
        else:
            print("L's ycor is beyond range")
    def down(self):
        if self.ycor() > -220:
            newycor = self.ycor()-20
            self.goto(self.xcor(),newycor)
        else:
            print("L's ycor is beyond range")
