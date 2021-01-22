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
    """"Class that creates bot units to populate the screen."""
    def __init__(self, position=(0, 0)):
        """Initializing the bot position and color"""
        self.x, self.y = position
        self.radius = 25
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

    # TODO : Set bot positions in loop
    while player_count < 11:
        player_list.append(FriendlyBot())
        player_count += 1


    # Game loop
    # TODO : Add click and move functionality
    #        long term add robot response to the movement of others
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            screen.fill((255, 255, 255))

            # Testing if circles appear correctly in different cases
            one = FriendlyBot((150, 50))
            player_list[1].update((500, 450))

            one.display()

            one.update((150, 200))

            two = FriendlyBot((350, 350))

            two.update((600, 490))

            two.display()
            one.display()
            player_list[1].display()
            pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    start_sim()
