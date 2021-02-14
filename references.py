import pygame

# Robocup SSL is played on a 9 m long by 6 m wide field
field_height = 900
field_width = int(field_height * (2 / 3))

# Set the window size and title
# Each unit represents a centimeter
screen = pygame.display.set_mode([field_width, field_height])
pygame.display.set_caption("11 Robot Tactics")

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 250, 250)

# background used to clean drawn objects
background = pygame.Surface((field_width, field_height))