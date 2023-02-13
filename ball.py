from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.setheading(300)

    def move(self):
        self.forward(12)

    def bounce_down(self):
        self.setheading(360 - self.heading())

    def bounce_up(self):
        self.setheading(360 - self.heading())
