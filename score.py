import turtle

class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed(0)
        self.ScoreValue = 0
        self.penup()
        self.setposition(-350, 250)
        self.write("Score: {}".format(self.ScoreValue), align="left", font=("Arial", 14, "bold"))
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write("Score: {}".format(self.ScoreValue), align="left", font=("Arial", 14, "bold"))

    def increase_score(self, points):
        self.ScoreValue += points
        self.update_score()

