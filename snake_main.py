import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
border = Turtle()

screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.colormode(255)
border.ht()
border.color("red")
border.penup()
border.setpos(-295, -285)
border.pendown()
border.setpos(-295, 295)
border.setpos(285, 295)
border.setpos(285, -285)
border.setpos(-295, -285)
screen.listen()

snake = Snake()
food = Food()
score = Score()

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

new_game = True
while new_game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 16:
        food.refresh()
        score.ate_food()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -280:
        new_game = False
        score.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            new_game = False
            score.game_over()

# TODO: add looping to ask for a new game every time the game is over

screen.mainloop()
