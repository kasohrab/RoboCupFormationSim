import math
from formation import Formation
from references import *

__author__ = "Alex Sohrab"


def start_sim():
    """"Method that starts the simulation"""

    pygame.init()

    player_list = Formation.create_formation(3, 4, 2, 1)
    formation = Formation()
    running = True

    # Game loop
    # TODO : Add click and move functionality
    #        long term add robot response to the movement of others
    while running:
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                # Calculate the x and y distances between the mouse and the center.
                mouse_pos = pygame.mouse.get_pos()

                # Looking at each player in the formation
                for player in player_list:
                    dist_x = mouse_pos[0] - player.x
                    dist_y = mouse_pos[1] - player.y
                    # Check if click is within bounds of a bot
                    if math.hypot(dist_x, dist_y) < player.radius:
                        print('collision at ' + str(player.x) + ', ' + str(player.y) + '. The click was ' +
                              str(dist_x) + ', ' + str(dist_y) + ' from the center of the player')

        screen.fill((0, 0, 0))
        # Halfway line
        pygame.draw.line(screen, WHITE, (0, field_height/2), (field_width, field_height/2))
        for player in player_list:
            player.display()

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    start_sim()
