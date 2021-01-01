#IMPORTING NECESSARY LIBRies
from turtle import Turtle,Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

#screen setup for the game
win = Screen()
win.title("Ini Pong Game")
win.setup(width=800,height=600)
win.bgcolor("blue")
win.tracer(0)


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

#turtle listen to the keypress and make a move
win.listen()
win.onkey(r_paddle.pad_up, "Up")
win.onkey(r_paddle.pad_down, "Down")
win.onkey(l_paddle.pad_up, "w")
win.onkey(l_paddle.pad_down, "s")


game_on = True
while game_on:
    time.sleep(0.1)
    win.update()
    ball.move()


#detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

#detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < - 320:
        ball.bounce_x()


#what happens when the paddle missing
    if ball.xcor() > 380:
        ball.clear_position()
        scoreboard.l_point()


    if ball.xcor() < - 380:
        ball.clear_position()
        scoreboard.r_point()

















win.exitonclick()