from references import *


class FriendlyBot:
    """"Class that creates bot units to populate the screen"""

    def __init__(self, position=(0, 0)):
        """Initializing the bot position and color.
        :param position: the requested formation position of the bot.
        Currently stored as tuple, but will be a nparray in codebase"""
        self.x, self.y = position
        # Max radius of SSL robot is 9 cm
        self.radius = 9
        self.color = BLUE
        self.thickness = 100

    def display(self):
        """Display the bot"""
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, self.thickness)

    def update_position(self, new_position):
        """Cleans screen then updates position.

        Need to call display on all other bots after updating.
        """
        screen.blit(background, (0, 0))
        self.x, self.y = new_position

    def get_position(self):
        return self.x, self.y

    def is_offscreen(self):
        """
        :param self: the bot to check
        :return: Bool whether the bot is outside the field"""

        if FIELD_WIDTH < self.x + self.radius or self.x - self.radius < 0:
            return True, 'x'
        elif FIELD_DEPTH < self.y + self.radius or self.y - self.radius < 0:
            return True, 'y'
        else:
            return False
