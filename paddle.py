from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_coordinate):
        super().__init__()
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(x_coordinate, 0)

    def up(self):
        y_coordinate = self.ycor()
        self.goto(self.xcor(), y_coordinate + 25)

    def down(self):
        y_coordinate = self.ycor()
        self.goto(self.xcor(), y_coordinate - 25)
