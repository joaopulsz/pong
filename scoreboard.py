from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.write(f"{self.left_score} x {self.right_score}", align="center", font=("Arial", 20, "normal"))

    def left_scores(self):
        self.left_score += 1
        self.clear()
        self.write(f"{self.left_score} x {self.right_score}", align="center", font=("Arial", 20, "normal"))

    def right_scores(self):
        self.right_score += 1
        self.clear()
        self.write(f"{self.left_score} x {self.right_score}", align="center", font=("Arial", 20, "normal"))
