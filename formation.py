from references import *
from bot import FriendlyBot

class Formation:
    """Formation class"""
    def __init__(self):
        """Initializing the formation data"""
        center = (field_width * .75, field_height * .75)
        pygame.draw.circle(screen, GREEN, center, 1, 100)

    def create_formation(defenders_count, midfielders_count, attackers_count, strikers_count):
        """Creates initial formation and positions that the robots will go to"""
        # TODO: account for edge cases (where the inputs do not create a valid formation)
        # TODO: relative to center and ball (adjust width and depth)
        player_list = []
        player_count = 0
        while player_count < 11:
            player_list.append(FriendlyBot())
            player_count += 1

        defense_width = field_width/(defenders_count + 1)
        midfield_width = (field_width/(midfielders_count + 1))
        attack_width = (field_width/(attackers_count + 1))
        strikers_width = (field_width/(strikers_count + 1))
        # Set player initial positions where (0,0) is top left

        # Sweeper Keeper
        player_list[0].update_position((field_width / 2, field_height - 20))

        count = 1
        index = 1
        # Defenders
        while count <= defenders_count:
            player_list[index].update_position((count * defense_width, 840))
            count += 1
            index += 1

        # Midfielders
        count = 1
        while count <= midfielders_count:
            player_list[index].update_position((count * midfield_width, 750))
            count += 1
            index += 1

        # Attackers
        count = 1
        while count <= attackers_count:
            player_list[index].update_position((count * attack_width, 660))
            count += 1
            index += 1

        # Strikers
        count = 1
        while count <= strikers_count:
            player_list[index].update_position((count * strikers_width, 600))
            count += 1
            index += 1

        return player_list
