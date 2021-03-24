from turtle import Screen, Turtle
from Paddle import Paddle
from ball import ball
import time
from screenboard import board

screen = Screen()

screen.tracer(0)

screen.bgcolor("black")
screen.title("pong")
screen.setup(width=800, height=600)

l = Paddle((-350, 0))
r = Paddle((350, 0))
ball = ball()
board = board()

screen.listen()
screen.onkey(r.move_up, "Up")
screen.onkey(r.move_down, "Down")
screen.onkey(l.move_up, "w")
screen.onkey(l.move_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.distance(r) < 50 and ball.xcor() > 320 or ball.distance(l) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    if ball.xcor() > 380:
        ball.reset_postion()
        board.l_points()


    if ball.xcor() < -380:
        ball.reset_postion()
        board.r_point()

screen.exitonclick()