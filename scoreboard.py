from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("yellow")
        self.ht()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(0, 240)
        self.write("Score: {}".format(self.score), False, ALIGNMENT, FONT)

    def ate_food(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.setpos(0, 0)
        self.write("Game over", False, ALIGNMENT, FONT)

    def new_game(self):
        self.reset()


class HighScore(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.color("yellow")
        self.ht()
        self.penup()

    def new_high_score(self, score):
        if score > self.high_score:
            self.high_score = score
        self.update_high_score()

    def update_high_score(self):
        self.clear()
        self.setpos(0, 265)
        self.write("High Score: {}".format(self.high_score), False, ALIGNMENT, FONT)
