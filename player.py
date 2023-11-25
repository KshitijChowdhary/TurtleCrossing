from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(UP)
        self.goto(STARTING_POSITION)

    def up(self):
        self.forward(MOVE_DISTANCE)
        #new_y = self.ycor() + MOVE_DISTANCE
        #self.goto(self.xcor(), new_y)


    def starting_position(self):
        self.goto(STARTING_POSITION)





