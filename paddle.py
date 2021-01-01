from turtle import Turtle
from ball import Ball

class Paddle(Turtle):
#creating clas paddle from turtle
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.shapesize(stretch_wid=6,stretch_len=1)
        self.penup()
        self.goto(position)

#movement of the paddle up and down
    def pad_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)


    def pad_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)


