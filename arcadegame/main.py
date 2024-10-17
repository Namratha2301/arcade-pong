from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time #using it to make the while loop sleep so that the ball moves more slowly


screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("𝓟𝓸𝓷𝓰")
screen.tracer(0)
scoreboard = Scoreboard()
#will turn off the animation, it is turned on using game_on while loop
#until screen.update() method, everything is created in background and shows when update is called

#object_paddle = Paddle(x_position,y_position)
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #collision with wall conditions : when ball is above 300 in y axis (wall is top and bottom)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y() #up and down

    #detect collision with r_paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() >320
            or ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    #when r_paddle misses
    if ball.xcor() >380:
        ball.reset_postion()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()




screen.exitonclick()