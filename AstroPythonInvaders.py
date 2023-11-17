import turtle
import random
import math
import os
from pygame import mixer
from player import Player
from enemy import Enemy
from bullet import Bullet
from score import Score
import pygame.time

# Constants
BULLET_SPEED = 20
ENEMY_SPEED = 2
ENEMY_DROP_DISTANCE = 25
ENEMY_X_LIMIT = 425

# Get the absolute path of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Initialize the mixer
mixer.init()

# Load the sound files using the correct file paths
sound_files = {
    "laser": os.path.join(script_dir, "SpaceInvaders_laser.wav"),
    "explosion": os.path.join(script_dir, "SpaceInvaders_explosion.wav"),
    "gameover": os.path.join(script_dir, "SpaceInvaders_gameover.wav")
}

# Setting up the screen
scr = turtle.Screen()
scr.setup(1000, 600, 0, 0)
scr.bgcolor("black")
scr.title("Space Invader Game")
scr.bgpic("dp.gif")

# Register the missile GIF as a custom shape
turtle.register_shape("missile.gif")

p = Player()
enemies = [Enemy() for _ in range(8)]
b = Bullet()
b.shape("missile.gif")  # Set the shape of the bullet to the registered missile shape
b.color("white")
b.setheading(90)  # Set the bullet's initial direction to point up
b.speed = BULLET_SPEED  # Set the speed of the bullet
s = Score()

# Function to calculate distance between two objects
def calculate_distance(a, b):
    return math.sqrt(abs(math.pow((a.xcor() - b.xcor()), 2) + math.pow((a.ycor() - b.ycor()), 2)))

# Function to handle bullet firing
def fire_bullet():
    if b.state == "Ready":
        b.state = "Fire"
        mixer.Sound(sound_files["laser"]).play()

        x = p.xcor()
        y = p.ycor() + 30
        b.goto(x, y)
        b.showturtle()

# Function to display menu and handle user input
def display_menu():
    choice = turtle.textinput("Game Over", "Press 'y' to restart or 'n' to quit:")
    if choice.lower() == 'y':
        return True
    elif choice.lower() == 'n':
        turtle.bye()  # Close the turtle graphics window
        return False
    else:
        return display_menu()

# Function to reset the game
def reset_game():
    global game_over
    game_over = False

    # Reset player position
    p.goto(0, -250)
    p.showturtle()

    # Reset enemy positions
    for enemy in enemies:
        x = random.randint(-300, 300)
        y = random.randint(180, 280)
        enemy.goto(x, y)
        enemy.showturtle()

    # Reset score
    s.ScoreValue = 0
    s.pu()
    s.goto(-400, 260)  # Move the score display back to its original position
    s.pd()
    s.clear()
    s.write("Score: {}".format(s.ScoreValue), align="left", font=("Arial", 14, "bold"))
    
    # Reset bullet state
    b.hideturtle()
    b.state = "Ready"

    # Check that the bullet's state has been reset correctly
    assert b.state == "Ready"


# Function to restart the game
def restart_game():
    reset_game()
    turtle.listen()
    turtle.onkey(p.move_left, "Left")
    turtle.onkey(p.move_right, "Right")
    turtle.onkey(fire_bullet, "space")
    turtle.onkey(restart_game, "y")


if __name__ == "__main__":
   # Keybindings
   turtle.listen()
   turtle.onkey(p.move_left, "Left")
   turtle.onkey(p.move_right, "Right")
   turtle.onkey(fire_bullet, "space")
   turtle.onkey(restart_game, "y")

   # Game over flag
   game_over = False

   # Create a clock object to control the frame rate
   clock = pygame.time.Clock()
   clock.tick(7777) # Set the frame rate to 60 FPS

   # Main game loop
   while True:
       restart_game()
       while not game_over:
           for enemy in enemies:
               # Enemy movement
               x = enemy.xcor()
               x += enemy.speedamt
               enemy.setx(x)

               # Movement back and down
               if enemy.xcor() > ENEMY_X_LIMIT or enemy.xcor() < -ENEMY_X_LIMIT:
                  for j in enemies:
                      y = j.ycor()
                      y -= ENEMY_DROP_DISTANCE
                      j.sety(y)
                  enemy.speedamt *= -1

               # Check for collision between bullet and enemy
               if calculate_distance(b, enemy) < 20:
                  b.hideturtle()
                  b.state = "Ready"
                  mixer.Sound(sound_files["explosion"]).play()
                  b.setposition(0, -400)
                  x = random.randint(-300, 300)
                  y = random.randint(180, 280)
                  enemy.setposition(x, y)

                  # Update score
                  s.ScoreValue += 10
                  s.clear()
                  s.write("Score: {}".format(s.ScoreValue), align="left", font=("Arial", 14, "bold"))

               # Check for collision between player and enemy
               if calculate_distance(p, enemy) < 25:
                  for e in enemies:
                      e.hideturtle()
                  p.hideturtle()

                  # Game over
                  s.pu()
                  s.goto(0, 0)
                  s.pd()
                  s.write("Game Over!", align="left", font=("Arial", 14, "bold"))
                  game_over = True
                  break

               if enemy.ycor() <= -200:
                  mixer.Sound(sound_files["gameover"]).play()
                  for j in enemies:
                      j.hideturtle()
                  p.hideturtle()

                  # Game over
                  s.pu()
                  s.goto(0, 0)
                  s.pd()
                  s.write("Game Over!", align="left", font=("Arial", 14, "bold"))
                  game_over = True
                  break

           # Bullet movement
           if b.state == "Fire":
               y = b.ycor()
               y += b.speedamt
               b.sety(y)

               # If bullet has reached the top, reset its state and hide it
               if b.ycor() > 300:
                  b.hideturtle()
                  b.state = "Ready"

       if not display_menu():
           break

   turtle.done()
#reallllll
