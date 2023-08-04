from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.goto(0, 280)

        self.update_score()

    def update_score(self):
        self.write(
            f"Score: {self.score}",
            move=False,
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(
            f"GAME OVER",
            move=False,
            align=ALIGNMENT,
            font=FONT,
        )
