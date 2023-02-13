from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle(-360)
right_paddle = Paddle(360)
ball = Ball()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")


playing = True
while playing:
    screen.update()
    time.sleep(0.1)

    ball.move()

    if ball.ycor() > 390:
        ball.bounce_down()
    elif ball.ycor() < -390:
        ball.bounce_up()


screen.exitonclick()