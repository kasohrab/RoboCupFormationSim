import math

from formation import Formation
from references import *

__author__ = "Alex Sohrab & Shail Patel"

# pygame stores what type of click as integers in event.button
LEFT_CLICK = 1
RIGHT_CLICK = 3


def start_sim():
    """"Method that starts the simulation"""

    pygame.init()

    # sample formation structures
    formation3_4_2_1 = Formation(11, field_width)
    formation3_4_2_1.set_positions(3, 4, 2, 1)

    formation4_4_0_2 = Formation(11, field_width)
    formation4_4_0_2.set_positions(4, 4, 0, 2)

    # TODO: make formation iterable instead of using player_list
    player_list = formation3_4_2_1.create_formation()
    running = True
    # Test move_center here
    formation3_4_2_1.move_center(player_list, (0, 0))

    formation_book = {0: formation3_4_2_1, 1: formation4_4_0_2}
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
            elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT_CLICK:
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
                        last_clicked_player = player
                        print(last_clicked_player)

            elif event.type == pygame.KEYDOWN:
                # manual bot movement conditionals
                # move clicked bot using arrow keys
                if last_clicked_player is not None:
                    if event.key == pygame.K_LEFT:
                        last_clicked_player.x -= 3
                    elif event.key == pygame.K_RIGHT:
                        last_clicked_player.x += 3
                    elif event.key == pygame.K_UP:
                        last_clicked_player.y -= 3
                    elif event.key == pygame.K_DOWN:
                        last_clicked_player.y += 3

                # change formations mid-match
                # if player clicks a number, choose that numbered formation from the list
                elif 48 <= event.key <= 57:
                    # TODO: change this?
                    number = event.key - 48
                    if formation_book.get(number) is not None:
                        player_list = formation_book[number].create_formation()
                    print(event.key)

            elif event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT_CLICK:
                # move clicked bot using right click on mouse
                mouse_pos = pygame.mouse.get_pos()

                last_clicked_player.update_position((mouse_pos[0], mouse_pos[1]))

        screen.fill((0, 0, 0))
        # Formation center
        pygame.draw.circle(screen, GREEN, formation3_4_2_1.center, 3, 80)
        # Halfway line
        pygame.draw.line(screen, WHITE, (0, field_depth / 2), (field_width, field_depth / 2))
        for player in player_list:
            player.display()
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    start_sim()
