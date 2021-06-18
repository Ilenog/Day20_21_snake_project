import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
border = Turtle()

screen.setup(1000, 800)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.colormode(255)
border.ht()
border.color("red")
border.penup()
border.setpos(-495, -385)
border.pendown()
border.setpos(-495, 395)
border.setpos(485, 395)
border.setpos(485, -385)
border.setpos(-495, -385)
screen.listen()

snake = Snake()
food = Food()
score = Score()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

new_game = True
while new_game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 16:
        food.refresh()
        score.ate_food()
        snake.extend()

    if snake.head.xcor() > 480 or snake.head.xcor() < -490 or snake.head.ycor() > 390 or snake.head.ycor() < -380:
        new_game = False
        score.game_over()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            new_game = False
            score.game_over()

screen.mainloop()
