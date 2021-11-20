from turtle import Turtle
import random as r

STARTING_POSN = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


# ^^^ constant variable


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        """creates the body of the snake"""
        for i in STARTING_POSN:
            self.add_segment(i)

    def add_segment(self, position):
        """adds a block of the snake at the end of the segment"""
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.snake.append(tim)

    def extend(self):
        """add a block at the end"""
        self.add_segment(self.snake[-1].position())

    def move(self):
        """snake movement"""
        for seg_num in range(len(self.snake) - 1, 0, -1):
            # loops through the length of the snake list starting at the end
            new_x, new_y = self.snake[seg_num - 1].xcor(), self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def snake_up(self):
        if self.head.heading() == 180:
            self.head.right(90)
        else:
            self.head.left(90)

    def snake_down(self):
        if self.head.heading() == 180:
            self.head.left(90)
        else:
            self.head.right(90)

    def snake_left(self):
        if self.head.heading() == 270:
            self.head.right(90)
        else:
            self.head.left(90)

    def snake_right(self):
        if self.head.heading() == 270:
            self.head.left(90)
        else:
            self.head.right(90)
