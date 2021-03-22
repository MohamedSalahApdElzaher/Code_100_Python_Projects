from turtle import Turtle, Screen
import random

screen = Screen()

is_on = False
screen.setup(width=500, height=400)
user_predict = screen.textinput(title="Make Your Predict!",prompt="Which turtle will win the race ? Enter a color..")
colors = ["red", "yellow", "orange", "blue", "green", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(new_turtle)

if user_predict:
    is_on = True

while is_on:
    for i in all_turtles:
        if i.xcor() > 230:
            is_on = False
            winner_color = i.pencolor()
            if user_predict == winner_color:
                print(f"You win! The winner color {winner_color}")
            else:
                print(f"You lose! The winner color {winner_color}")
        distance = random.randint(0, 10)
        i.forward(distance)



screen.exitonclick()