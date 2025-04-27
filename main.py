from turtle import *
from paddle import Racket_Right
from paddle import Racket_Left
from ball import Ball
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
# screen.tracer(0)
racket_r = Racket_Right()
racket_l = Racket_Left()

screen.listen()
onkey(racket_r.up, "Up")
onkey(racket_r.down, "Down")
onkey(racket_l.up, "w")
onkey(racket_l.down, "s")

scoreboard = Scoreboard()


x = 10
y = 10
ball = Ball()
while True:
    def move(self):
        global x,y
        if self.ycor() >= 300:
            y*=-1
        elif self.ycor() <=-300:
            y*=-1
        elif self.xcor() >330 and self.distance(racket_r) < 50:
            x*=-1
        elif self.xcor() <-330 and self.distance(racket_l) < 50:
            x*=-1
        elif self.xcor() >= 400:
            self.reset_position()
            scoreboard.l_point()
        elif self.xcor() <=-400:
            self.reset_position()
            scoreboard.r_point()
        newxcor = self.xcor() + x
        newycor = self.ycor() + y
        self.goto(newxcor, newycor)
    move(ball)
