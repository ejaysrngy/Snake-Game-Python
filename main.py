from turtle import Turtle, Screen
from time import *
from snake import Snake
from food import Food
from score import Scoreboard

# screen portion
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()


snake = Snake()
food = Food()
score = Scoreboard()
snake.create_snake()

screen.onkey(snake.snake_up, "w")
screen.onkey(snake.snake_down, "s")
screen.onkey(snake.snake_left, "a")
screen.onkey(snake.snake_right, "d")

game_is_on = True
while game_is_on:

    screen.update()
    sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        snake.extend()
        food.change_location()
        score.clear()
        score.increase_score()

    for j in snake.snake[3:]:
        if snake.head.distance(j) < 15:
            score.high_score()
            game_is_on = False
            score.game_over()

    if snake.head.xcor() == 300 or snake.head.xcor() == (-300) or snake.head.ycor() == 280 or snake.head.ycor() == (-300):
        score.high_score()
        game_is_on = False
        score.game_over()



screen.exitonclick()
