from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.setheading(45)
        self.move_speed = 12

    def move(self):
        self.forward(self.move_speed)

    def increase_speed(self):
        self.move_speed += 2

    def reset_speed(self):
        self.move_speed = 12

    def bounce_down(self):
        self.setheading(360 - self.heading())

    def bounce_up(self):
        self.setheading(360 - self.heading())

    def bounce_left(self):
        self.setheading(180 - self.heading())

    def bounce_right(self):
        self.setheading(180 - self.heading())

    def reset_left(self):
        self.goto(0, 0)
        self.setheading(130)

    def reset_right(self):
        self.goto(0, 0)
        self.setheading(45)