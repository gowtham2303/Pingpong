from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


# 1 . Creating screen 
screen = Screen()
screen.setup(height=600 , width=800)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

# 2 .paddle 

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = ScoreBoard()


#3. movement ofpaddle 

screen.listen()
screen.onkey(r_paddle.go_up , "Up")
screen.onkey(r_paddle.go_down , "Down")
screen.onkey(l_paddle.go_up , "w")
screen.onkey(l_paddle.go_down , "s")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    

    # collision with top and bottom 
    if ball.ycor() >280 or ball.ycor() < -280 :
        ball.y_bounce()

    #collision with paddle 
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50  and ball.xcor() > -340 :
        ball.y_bounce()
        ball.x_bounce()

    # crossed the collision with paddle 

    if ball.xcor()> 380:
        ball.reset_positoin ()
        score.l_point()
    
    if ball.xcor()< -380:
        ball.reset_positoin ()
        score.r_point()






    





















screen.exitonclick()