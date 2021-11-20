from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("highscore.txt", mode="r") as self.file:
            self.highscore = int(self.file.read())
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align="center", font=("Arial", 15))

    def high_score(self):
        if self.score > self.highscore:
            with open("highscore.txt", mode="w") as file:
                file.write(f"{self.score}")
                self.highscore = self.score

    def increase_score(self):
        self.score += 1
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align="center", font=("Arial", 15))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 30))
        game_is_on = False
