from turtle import Turtle


class Scoreboard(Turtle):
    lpoint = 0
    rpoint = 0
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.write_txt()

    def write_txt(self):
        self.clear()
        txt = "Score: "+str(self.lpoint)+":"+str(self.rpoint)
        self.write(txt,align="center",font=("Courier",24,"normal"))

    def l_point(self):
        self.lpoint+=1
        self.write_txt()
    def r_point(self):
        self.rpoint+=1
        self.write_txt()
