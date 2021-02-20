from references import *
from bot import FriendlyBot


class Formation:
    """Formation class"""
    def __init__(self):
        """Initializing the formation data"""
        self.player_list = []
        self.center = (field_width * .75, field_height * .75)

    def create_formation(self, defenders_count, midfielders_count, attackers_count, strikers_count):
        """Creates initial formation and positions that the robots will go to

        :param:
        :param strikers_count: number of strikers in the formation
        :param attackers_count: number of attackers in the formation
        :param midfielders_count:  number of midfielders in the formation
        :param defenders_count:  number of defenders in the formation
        """
        # TODO: account for edge cases (where the inputs do not create a valid formation)
        # TODO: relative to center and ball (adjust width and depth)
        player_count = 0
        while player_count < 11:
            self.player_list.append(FriendlyBot())
            player_count += 1

        defense_width = field_width/(defenders_count + 1)
        midfield_width = (field_width/(midfielders_count + 1))
        attack_width = (field_width/(attackers_count + 1))
        strikers_width = (field_width/(strikers_count + 1))
        # Set player initial positions where (0,0) is top left

        # Sweeper Keeper
        self.player_list[0].update_position((field_width / 2, field_height - 20))

        count = 1
        index = 1
        # Defenders
        while count <= defenders_count:
            self.player_list[index].update_position((count * defense_width, 840))
            count += 1
            index += 1

        # Midfielders
        count = 1
        while count <= midfielders_count:
            self.player_list[index].update_position((count * midfield_width, 750))
            count += 1
            index += 1

        # Attackers
        count = 1
        while count <= attackers_count:
            self.player_list[index].update_position((count * attack_width, 660))
            count += 1
            index += 1

        # Strikers
        count = 1
        while count <= strikers_count:
            self.player_list[index].update_position((count * strikers_width, 600))
            count += 1
            index += 1

        return self.player_list

    def get_formation(self):
        """formation getter method

        :return: the list of players
        """
        return self.player_list

    def move_center(self, position=(0, 0)):
        """Moves the center and the bots move to keep in line with it.
        """


