import turtle
import random

class Enemy(turtle.Turtle):
    def __init__(self):
        super().__init__()
        turtle.register_shape("/home/keldenpdrac/Desktop/space/enemy.gif")
        self.color("red")
        self.shape("/home/keldenpdrac/Desktop/space/enemy.gif")
        self.pu()
        x = random.randint(-450, 450)
        y = random.randint(180, 250)
        self.goto(x, y)
        self.speedamt = 5

    def move_left(self):
        self.setx(self.xcor() - self.speedamt)

    def move_right(self):
        self.setx(self.xcor() + self.speedamt)

    def check_collision(self, bullet):
        distance = self.distance(bullet)
        if distance < 20:
            return True
        else:
            return False

