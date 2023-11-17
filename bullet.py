import turtle

class Bullet(turtle.Turtle):
    def __init__(self):
        super().__init__()
        turtle.register_shape("missile.gif")
        self.penup()
        self.goto(0, -240)
        self.speedamt = 40 #initial speed of the bullet
        self.state = "Ready" 

    def check_collision(self, enemy):
        distance = self.distance(enemy)
        if distance < 20:
            return True
        else:
            return False
