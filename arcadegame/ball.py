from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        self.speed_of_sleep = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move # we are using x_move and y_move variables
        # so that we can use them to reverse in bounce()
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        #y coordinate should reverse
        self.y_move *= -1


    def bounce_x(self):
        self.x_move *= -1
        self.speed_of_sleep *= 0.9


    def reset_position(self):
        #goes to center and opposite direction
        self.goto(0,0)
        self.speed_of_sleep = 0.1
        self.bounce_x()



