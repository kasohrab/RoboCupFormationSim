import math

from formation import Formation
from references import *

"""Main references"""
# pygame stores what type of click as integers in event.button
LEFT_CLICK = 1
RIGHT_CLICK = 3

# center radius variable
CENTER_RADIUS = 4


def start_sim():
    """
    Method that starts the simulation
    """

    pygame.init()

    # sample formation structures
    formation3_4_2_1 = Formation(11, FIELD_WIDTH, 300, 3, 4, 2, 1)
    formation4_4_0_2 = Formation(11, FIELD_WIDTH, 300, 4, 4, 0, 2)

    # like a playbook
    formation_book = {0: formation3_4_2_1, 1: formation4_4_0_2}

    curr_formation = formation_book[0]
    curr_formation.build()
    running = True

    # Test move_center here
    curr_formation.increment_center((0, 0))

    # stores the last clicked bot/center
    # we can update this when the user clicks on a bot
    # then the user can use arrow keys/right click to move it
    last_clicked_player = None

    # stores if the user clicked on the center to move it
    click_on_center = False
    # Game loop
    # TODO: long term add robot response to the movement of others
    while running:
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT_CLICK:
                # Calculate the x and y distances between the mouse and the center.
                mouse_pos = pygame.mouse.get_pos()

                # check if user clicked on center
                dist_x = mouse_pos[0] - curr_formation.center[0]
                dist_y = mouse_pos[1] - curr_formation.center[1]
                if math.hypot(dist_x, dist_y) < CENTER_RADIUS:
                    click_on_center = True
                else:
                    click_on_center = False

                # Looking at each player in the formation
                for player in curr_formation:
                    player_check = is_within_bounds(mouse_pos, player)
                    if player_check:
                        last_clicked_player = player
                        break

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
                    # TODO: control whether this resets position or not
                    number = event.key - 48
                    if formation_book.get(number) is not None:
                        curr_formation = formation_book[number]
                        curr_formation.build()

            elif event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT_CLICK:
                # move clicked bot using right click on mouse
                mouse_pos = pygame.mouse.get_pos()
                if click_on_center:
                    curr_formation.move_center(mouse_pos)
                    update_bounds(curr_formation)
                elif last_clicked_player is not None:
                    last_clicked_player.update_position((mouse_pos[0], mouse_pos[1]))

        screen.fill((0, 0, 0))

        # Formation center
        pygame.draw.circle(screen, GREEN, curr_formation.center, CENTER_RADIUS, 80)

        # Halfway line
        pygame.draw.line(screen, WHITE, (0, FIELD_DEPTH / 2), (FIELD_WIDTH, FIELD_DEPTH / 2))

        for player in curr_formation:
            player.display()
        pygame.display.flip()

    pygame.quit()


def is_within_bounds(mouse_pos, bot):
    """
    :param mouse_pos: the mouse position
    :param bot: the bot to check
    :return: Bool whether the bot is within bounds
    """
    dist_x = mouse_pos[0] - bot.x
    dist_y = mouse_pos[1] - bot.y

    return math.hypot(dist_x, dist_y) < bot.radius


def update_bounds(formation: Formation):
    """
    Checks each bot to see if it is out of bounds. If it is then resize the formation.

    :param formation: the current formation in use
    """
    for player in formation:
        if off_check := player.is_offscreen():
            direction = off_check[1]

            if direction == 'x':
                if player.x > 600:
                    # right of the field
                    formation.update_width(2 * (FIELD_WIDTH - formation.center[0]))
                else:
                    # left of the field
                    formation.update_width(2 * formation.center[0])
            else:
                # this comes from 4 rows and the bot having a radius of 9
                # allows to update_depth to get the correct row_separation
                row_constant: int = 36
                if player.y < 0:
                    # north of the field
                    formation.update_depth(2 * (formation.center[1]) - row_constant)
                else:
                    # south of the field
                    formation.update_depth(2 * (FIELD_DEPTH - formation.center[1]) - row_constant)


if __name__ == "__main__":
    start_sim()
