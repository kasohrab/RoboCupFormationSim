import math
import pygame

__author__ = "Alex Sohrab"

# Set the pygame icon
icon = pygame.image.load('Images/robosim.png')
pygame.display.set_icon(icon)

# Set the window size and title
# Robocup SSL is played on a 9 m long by 6 m wide field
field_height = 900
field_width = int(field_height * (2 / 3))

# Each unit represents a centimeter
screen = pygame.display.set_mode([field_width, field_height])
pygame.display.set_caption("11 Robot Tactics")

# Colors
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 250, 250)

background = pygame.Surface((field_width, field_height))


class FriendlyBot:
    """"Class that creates bot units to populate the screen"""
    def __init__(self, position=(0, 0)):
        """Initializing the bot position and color"""
        self.x, self.y = position
        # Max radius of SSL robot is 9 cm
        self.radius = 9
        self.color = BLUE
        self.thickness = 100

    def display(self):
        """Display the bot"""
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, self.thickness)

    def update(self, new_position):
        """Cleans screen then updates position.

        Need to call display on all other bots after updating.
        """
        screen.blit(background, (0, 0))
        self.x, self.y = new_position


def create_formation(defenders_count, midfielders_count, attackers_count, strikers_count):
    """Creates initial formation and positions that the robots will go to"""
    # TODO: account for edge cases (where the inputs do not create a valid formation)
    player_list = []
    player_count = 0
    while player_count < 11:
        player_list.append(FriendlyBot())
        player_count += 1

    defense_width = field_width/(defenders_count + 1)
    midfield_width = (field_width/(midfielders_count + 1))
    attack_width = (field_width/(attackers_count + 1))
    strikers_width = (field_width / (strikers_count + 1))
    # Set player initial positions where (0,0) is top left

    # Sweeper Keeper
    player_list[0].update((field_width/2, field_height - 20))

    count = 1
    index = 1
    # Defenders
    while count <= defenders_count:
        player_list[index].update((count * defense_width, 840))
        count += 1
        index += 1

    # Midfielders
    count = 1
    while count <= midfielders_count:
        player_list[index].update((count * midfield_width, 750))
        count += 1
        index += 1

    # Attackers
    count = 1
    while count <= attackers_count:
        player_list[index].update((count * attack_width, 660))
        count += 1
        index += 1

    # Strikers
    count = 1
    while count <= strikers_count:
        player_list[index].update((count * strikers_width, 600))
        count += 1
        index += 1

    return player_list


def start_sim():
    """"Method that starts the simulation"""

    pygame.init()

    player_list = create_formation(3, 4, 2, 1)
    running = True

    # Game loop
    # TODO : Add click and move functionality
    #        long term add robot response to the movement of others
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            screen.fill((0, 0, 0))
            # Halfway line
            pygame.draw.line(screen, WHITE, (0, field_height/2), (field_width, field_height/2))
            for player in player_list:
                player.display()

            pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    start_sim()
