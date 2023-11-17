import unittest
import math  
import turtle
import AstroPythonInvaders
from AstroPythonInvaders import Player
from AstroPythonInvaders import Enemy
from AstroPythonInvaders import calculate_distance
from player import Player
from enemy import Enemy
from bullet import Bullet

# Function to calculate distance between two objects
def calculate_distance(a, b):
    return math.sqrt(abs(math.pow((a.xcor() - b.xcor()), 2) + math.pow((a.ycor() - b.ycor()), 2)))

class TestCollisionDetection(unittest.TestCase):
    def test_bullet_enemy_collision(self):
        # Initialize the game state
        bullet = Bullet()
        enemy = Enemy()
        
        # Simulate the bullet and enemy being at the same position
        bullet.goto(0, 0)
        enemy.goto(0, 0)

        # Check for collision
        distance = calculate_distance(bullet, enemy)
        self.assertTrue(distance < 20)  # Assuming 20 is the collision distance

    def test_player_enemy_collision(self):
        # Initialize the game state
        player = Player()
        enemy = Enemy()
        
        # Simulate the player and enemy being at the same position
        player.goto(0, 0)
        enemy.goto(0, 0)

        # Check for collision
        distance = calculate_distance(player, enemy)
        self.assertTrue(distance < 25)  # Assuming 25 is the collision distance

class TestPlayerMovement(unittest.TestCase):
    def test_move_left(self):
        # Initialize the game state
        player = Player()
        initial_x = player.xcor()

        # Simulate the left arrow key press
        player.move_left()

        # Assert the expected results
        self.assertEqual(player.xcor(), initial_x - player.playerspeed)

    def test_move_right(self):
        # Initialize the game state
        player = Player()
        initial_x = player.xcor()

        # Simulate the right arrow key press
        player.move_right()

        # Assert the expected results
        self.assertEqual(player.xcor(), initial_x + player.playerspeed)

class TestEnemyMovement(unittest.TestCase):
    def test_move_left(self):
        # Initialize the game state
        enemy = Enemy()
        initial_x = enemy.xcor()

        # Simulate the enemy movement to the left
        enemy.move_left()

        # Assert the expected results
        self.assertEqual(enemy.xcor(), initial_x - enemy.speedamt)

    def test_move_right(self):
        # Initialize the game state
        enemy = Enemy()
        initial_x = enemy.xcor()

        # Simulate the enemy movement to the right
        enemy.move_right()

        # Assert the expected results
        self.assertEqual(enemy.xcor(), initial_x + enemy.speedamt)

class TestBulletFiring(unittest.TestCase):
    def test_fire_bullet(self):
        # Initialize the game state
        player = Player()
        bullet = Bullet()
        bullet.state = "Ready"  # Set the initial state of the bullet

        # Simulate firing the bullet
        bullet = player.fire_bullet()

        # Assert the expected results
        self.assertEqual(bullet.state, "Fire")
        self.assertEqual(bullet.ycor(), player.ycor() + 30)

    def test_fire_bullet_multiple_times(self):
        # Initialize the game state
        player = Player()
        bullet = Bullet()
        bullet.state = "Ready"  # Set the initial state of the bullet

        # Simulate firing the bullet multiple times
        for _ in range(5):
            bullet = player.fire_bullet()

        # Assert the expected results
        self.assertEqual(bullet.state, "Fire")
        self.assertEqual(bullet.ycor(), player.ycor() + 30)
# Function to calculate distance between two objects
def calculate_distance(a, b):
    return math.sqrt(abs(math.pow((a.xcor() - b.xcor()), 2) + math.pow((a.ycor() - b.ycor()), 2)))

class TestGameOverCondition(unittest.TestCase):
    def test_player_enemy_collision(self):
        # Initialize the game state
        player = Player()
        enemy = Enemy()
        
        # Simulate the player and enemy being at the same position
        player.goto(0, 0)
        enemy.goto(0, 0)

        # Check if game is over
        distance = calculate_distance(player, enemy)
        is_game_over = distance < 25 or enemy.ycor() <= -200  # Assuming 25 is the collision distance
        self.assertTrue(is_game_over)

    def test_enemy_reaches_bottom(self):
        # Initialize the game state
        enemy = Enemy()
        
        # Simulate the enemy reaching the bottom of the screen
        enemy.goto(0, -200)

        # Check if game is over
        is_game_over = enemy.ycor() <= -200
        self.assertTrue(is_game_over)
        
# Function to calculate distance between two objects
def calculate_distance(a, b):
    return math.sqrt(abs(math.pow((a.xcor() - b.xcor()), 2) + math.pow((a.ycor() - b.ycor()), 2)))

class TestScoringSystem(unittest.TestCase):
    def test_increase_score(self):
        # Initialize the game state
        bullet = Bullet()
        enemy = Enemy()
        score = 0  # Initialize score
        score_increment = 10  # The amount by which the score increases

        # Simulate the bullet and enemy being at the same position (i.e., a hit)
        bullet.goto(0, 0)
        enemy.goto(0, 0)

        # Check for hit and increase score
        distance = calculate_distance(bullet, enemy)
        if distance < 20:  # Assuming 20 is the collision distance
            score += score_increment

        # Assert the expected results
        self.assertEqual(score, score_increment)
class Player(turtle.Turtle):
   def __init__(self):
       super().__init__()
       turtle.register_shape("player.gif")
       self.color("blue")
       self.speed(0)
       self.shape("player.gif")
       self.pu()
       self.goto(0, -250)
       self.bullet = None # Add this line

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
       self.bullet = Bullet()
       self.bullet.goto(self.xcor(), self.ycor() + 30)
       self.bullet.state = "Fire"
       return self.bullet

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

class TestPlayerMethods(unittest.TestCase):
    def setUp(self):
      self.player = Player()
      
    def test_fire_bullet(self):
      # Check the initial state of the player
      self.assertEqual(self.player.bullet, None)

      # Fire a bullet
      self.player.fire_bullet()

      # Check the state of the player after firing a bullet
      self.assertIsInstance(self.player.bullet, Bullet)
      self.assertEqual(self.player.bullet.state, "Fire")
      self.assertEqual(self.player.bullet.ycor(), self.player.ycor() + 30)

class TestCalculateDistance(unittest.TestCase):
    def test_calculate_distance(self):
     # Create two objects at different positions
     obj1 = turtle.Turtle()
     obj1.goto(0, 0)
     obj2 = turtle.Turtle()
     obj2.goto(10, 10)

     # Calculate the distance between the two objects
     distance = calculate_distance(obj1, obj2)

     # Check that the calculated distance is correct
     self.assertAlmostEqual(distance, 14.14, 2)

class TestGameRestart(unittest.TestCase):
   def test_player_position_reset(self):
       # Restart the game
       AstroPythonInvaders.restart_game()

       # Check if the player's position has been reset to the initial position
       self.assertEqual(AstroPythonInvaders.p.xcor(), 0)
       self.assertEqual(AstroPythonInvaders.p.ycor(), -250)

   def test_enemies_position_reset(self):
       # Restart the game
       AstroPythonInvaders.restart_game()

       # Check if the enemies' positions have been reset to random positions
       for enemy in AstroPythonInvaders.enemies:
           self.assertTrue(-300 <= enemy.xcor() <= 300)
           self.assertTrue(180 <= enemy.ycor() <= 280)

   def test_score_reset(self):
       # Restart the game
       AstroPythonInvaders.restart_game()

       # Check if the score has been reset to 0
       self.assertEqual(AstroPythonInvaders.s.ScoreValue, 0)

   def test_bullet_state_reset(self):
       # Restart the game
       AstroPythonInvaders.restart_game()

       # Check if the bullet's state has been reset to "Ready"
       self.assertEqual(AstroPythonInvaders.b.state, "Ready")

class TestEnemyReachBottom(unittest.TestCase):
  def setUp(self):
      self.enemy = Enemy()

  def test_enemy_reach_bottom(self):
      self.enemy.goto(0, -200)
      is_game_over = self.enemy.ycor() <= -200
      self.assertTrue(is_game_over)

class TestPlayerSpeed(unittest.TestCase):
  def setUp(self):
      self.player = Player()

  def test_player_speed(self):
      initial_x = self.player.xcor()
      self.player.move_right()
      self.assertEqual(self.player.xcor(), initial_x + self.player.playerspeed)

if __name__ == '__main__':
    unittest.main()
