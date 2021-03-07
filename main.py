import math
from formation import Formation
from references import *
from bot import FriendlyBot

__author__ = "Alex Sohrab & Shail Patel"


def start_sim():
    """"Method that starts the simulation"""

    pygame.init()

    formation = Formation(11, field_width)
    formation.set_positions(3, 4, 2, 1)
    player_list = formation.create_formation()
    running = True
    # Test move_center here
    formation.move_center(player_list, (0, 0))

    # stores the last clicked bot
    # we can update this when the user clicks on a bot
    # then the user can use arrow keys to move it
    last_clicked_player = None

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
                    print(mouse_pos[0])
                    # Check if click is within bounds of a bot
                    if math.hypot(dist_x, dist_y) < player.radius:
                        print('collision at ' + str(player.x) + ', ' + str(player.y) + '. The click was ' +
                              str(dist_x) + ', ' + str(dist_y) + ' from the center of the player')
                        player.x += dist_x
                        player.y += dist_y
                        last_clicked_player = player
                        print(last_clicked_player)

        screen.fill((0, 0, 0))
        # Formation center
        pygame.draw.circle(screen, GREEN, formation.center, 3, 80)
        # Halfway line
        pygame.draw.line(screen, WHITE, (0, field_depth / 2), (field_width, field_depth / 2))
        for player in player_list:
            player.display()
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    start_sim()
