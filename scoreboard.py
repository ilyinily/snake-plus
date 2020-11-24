from turtle import Turtle
X_SIZE = 1200
Y_SIZE = 600
FONT = ("Verdana", 12, "bold")


class Scoreboard(Turtle):
    def __init__(self, initial_score=0):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("pink")
        self.setposition(X_SIZE / 2 - 350, Y_SIZE / 2 - 20)
        self.score = initial_score

    def display_score(self, score, steps):
        if score != 1:
            self.write(f"{score} points collected in {steps} steps", align="center", font=FONT)
        else:
            self.write(f"{score} point collected in {steps} steps", align="center", font=FONT)

    def display_final_score(self, score, steps):
        self.setposition(0, 0)
        self.clear()
        if score != 1:
            self.write(f"Game over. You have scored {score} points collected in {steps} steps.", align="center", font=FONT)
        else:
            self.write(f"Game over. You have scored {score} point collected in {steps} steps.", align="center", font=FONT)
