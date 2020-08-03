import pygame
import random
 
# Define colors
PINK = (0, 0, 0)
BLUE = (255, 255, 255)
 
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BALL_SIZE = 25
 
 
class Ball:
    """
    Class to keep track of a ball's location and vector.
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
         
 
def make_ball():
    """
    Function to make a new, random ball.
    """
    ball = Ball()
    # Starting position of the ball.
    # Take into account the ball size so we don't spawn on the edge.
    ball.x = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
    ball.y = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)
 
    # Speed and direction of rectangle
    ball.change_x = random.randrange(-2, 3)
    ball.change_y = random.randrange(-2, 3)
 
    return ball


    def main():
      pygame.init()

      #Set the height and width of the screen
      size = [SCREEN_WIDTH, SCREEN_HEIGHT]
      screen = pygame.display.setmode(size)

pygame.display.set_caption("Bouncing Balls")

#Loop until user clicks exit button. 
done =False

#manage how fast the screen updates