import turtle
from bullet import Bullet

class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        turtle.register_shape("player.gif")
        self.color("blue")
        self.speed(0)
        self.shape("player.gif")
        self.pu()
        self.goto(0, -250)
        self.bullet = None
        # player movement
        self.playerspeed = 40

    def move_left(self):
        x = self.xcor()
        x -= self.playerspeed
        if x < -450:
            x = -450
        self.setx(x)

    def move_right(self):
        x = self.xcor()
        x += self.playerspeed
        if x > 450:
            x = 450
        self.setx(x)

    def fire_bullet(self):
        new_bullet = Bullet()
        new_bullet.goto(self.xcor(), self.ycor() + 30)
        new_bullet.state = "Fire"
        return new_bullet
