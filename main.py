import pygame

__author__ = "Alex Sohrab"

# Set the window size and title
screen = pygame.display.set_mode([750, 750])
pygame.display.set_caption("11 Robot Tactics")

# Colors
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Maybe will make background for each bot as needed instead
background = pygame.Surface((750, 750))


class FriendlyBot:
    """"Class that creates bot units to populate the screen."""
    def __init__(self, position, color, radius):
        """Initializing the bot position and color"""
        self.x, self.y = position
        self.radius = radius
        self.color = color
        self.thickness = 100

    def __hash__(self):
        """Hash function for bots stored in structure"""
        return hash(self.x) ^ hash(self.y)

    def display(self):
        """Display the bot"""
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, self.thickness)

    def update(self, new_position):
        """Cleans screen then updates position.

        Need to call display on all other bots after updating.
        """
        screen.blit(background, (0, 0))
        self.x, self.y = new_position
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, self.thickness)


def start_sim():
    """"Method that starts the simulation"""
    # TODO : Add a data structure that stores all FriendlyBot objects

    pygame.init()

    running = True

    bot_radius = 25

    # Game loop
    # TODO : Add click and move functionality
    #        long term add robot response to the movement of others
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            screen.fill((255, 255, 255))

            one = FriendlyBot((150, 50), BLUE, bot_radius)

            one.display()

            one.update((150, 200))

            two = FriendlyBot((350, 350), BLUE, bot_radius)

            two.display()

            two.update((600, 490))

            one.display()

            pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    start_sim()
