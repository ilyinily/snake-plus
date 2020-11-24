from turtle import Turtle
X_SIZE = 1200
Y_SIZE = 600
FONT = ("Verdana", 12, "bold")


class Scoreboard(Turtle):
    def __init__(self, alignment = "right", initial_score=0):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("pink")
        self.alignment = alignment
        if self.alignment == "right":
            self.setposition(X_SIZE / 2 - 350, Y_SIZE / 2 - 20)
        else:
            self.setposition(X_SIZE / 2 - 350, Y_SIZE / 2 - 40)
        self.score = initial_score

    def display_score(self, score, steps):
        if self.alignment == "right":
            self.write(f"Viper scored {score} in {steps} steps", align="center", font=FONT)
        else:
            self.write(f"Serpent scored {score} in {steps} steps", align="center", font=FONT)

    def display_final_score(self, score, steps):
        if self.alignment == "right":
            self.setposition(0, 60)
        else:
            self.setposition(0, -60)
        self.clear()
        if self.alignment == "right":
            self.write(f"Game over. Viper scored {score} collected in {steps} steps.", align="center", font=FONT)
        else:
            self.write(f"Game over. Serpent scored {score} collected in {steps} steps.", align="center", font=FONT)
