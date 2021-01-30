import pygame

__author__ = "Alex Sohrab"

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

background = pygame.Surface((750, 750))


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


def create_formation(defenders, midfielders, attackers):
    player_list = []
    player_count = 0
    while player_count < 11:
        player_list.append(FriendlyBot())
        player_count += 1

    defense_width = 175
    midfield_width = 275
    attack_width = 175
    # Set player initial positions where (0,0) is top left
    player_list[0].update((375.5, 725))
    player_list[1].update((375 - defense_width, 600))
    player_list[2].update((375, 600))
    player_list[3].update((375 + defense_width, 600))
    player_list[4].update((375 - midfield_width, 425))
    player_list[5].update((375 - midfield_width/3, 425))
    player_list[6].update((375 + midfield_width/3, 425))
    player_list[7].update((375 + midfield_width, 425))
    player_list[8].update((375 - attack_width, 250))
    player_list[9].update((375 + attack_width, 250))
    player_list[10].update((375, 125))
    return player_list


def start_sim():
    """"Method that starts the simulation"""

    pygame.init()

    player_list = create_formation(3, 4, 4)
    running = True

    # Game loop
    # TODO : Add click and move functionality
    #        long term add robot response to the movement of others
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            screen.fill((0, 0, 0))

            for player in player_list:
                player.display()

            pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    start_sim()
