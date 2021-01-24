import pygame

__author__ = "Alex Sohrab"

# Set the window size and title
screen = pygame.display.set_mode([750, 750])
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
        self.radius = 20
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


def start_sim():
    """"Method that starts the simulation"""

    pygame.init()

    running = True

    player_list = []
    player_count = 0

    while player_count < 11:
        player_list.append(FriendlyBot())
        player_count += 1

    defense_width = 175
    midfield_width = 275
    attack_width = 175
    # Set player initial positions where (0,0) is top left
    player_list[0].update((375, 725))
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
