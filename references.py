import pygame
# import numpy as np

# Robocup SSL is played on a 9 m long by 6 m wide field
FIELD_DEPTH = 900
FIELD_WIDTH = int(FIELD_DEPTH * (2 / 3))

# Set the window size and title
# Each unit represents a centimeter
screen = pygame.display.set_mode([FIELD_WIDTH, FIELD_DEPTH])
pygame.display.set_caption("Robot Formation Sim")

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 250, 250)
YELLOW = (255, 255, 0)

# background used to clean drawn objects
background = pygame.Surface((FIELD_WIDTH, FIELD_DEPTH))