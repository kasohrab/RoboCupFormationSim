from references import *
from bot import FriendlyBot


class Formation:
    """Formation class"""

    def __init__(self, num_bots):
        """Initializing the formation data"""

        self.player_list = []
        player_count = 0
        while player_count < num_bots:
            self.player_list.append(FriendlyBot())
            player_count += 1

        # variables that help define the center of the formation
        self.center = None
        self.goalkeeper_depth = field_height - 20
        self.defense_depth = 840
        self.midfielders_depth = 750
        self.attackers_depth = 660
        self.strikers_depth = 600

        self.defense_width = 0
        self.midfield_width = 0
        self.attack_width = 0
        self.strikers_width = 0

        # creates class variables that will store the number of bots in each row
        self.defenders_count, self.midfielders_count, self.attackers_count, self.strikers_count = None, None, None, None

    def set_positions(self, defenders_count, midfielders_count, attackers_count, strikers_count):
        """Set how many bots in each line"""
        self.defenders_count = defenders_count
        self.midfielders_count = midfielders_count
        self.attackers_count = attackers_count
        self.strikers_count = strikers_count

        self.defense_width = field_width / (defenders_count + 1)
        self.midfield_width = (field_width / (midfielders_count + 1))
        self.attack_width = (field_width / (attackers_count + 1))
        self.strikers_width = (field_width / (strikers_count + 1))
        # Set initial center as the average of all robot positions
        average_depth = (self.goalkeeper_depth + (self.defense_depth * defenders_count) +
                         (self.midfielders_depth * midfielders_count) + (self.attackers_depth * attackers_count)
                         + (self.strikers_depth + strikers_count)) / len(self.player_list)

        self.center = (field_width / 2, average_depth)

    def create_formation(self):
        """Creates initial formation and positions that the robots will go to
        """

        # TODO: account for edge cases (where the inputs do not create a valid formation)
        # TODO: relative to center and ball (adjust width and depth)

        # Set player initial positions where (0,0) is top left
        print(self.center)
        # Sweeper Keeper
        self.player_list[0].update_position((field_width / 2, field_height - 20))

        count = 1
        index = 1
        # Defenders
        while count <= self.defenders_count:
            self.player_list[index].update_position((count * self.defense_width, 840))
            count += 1
            index += 1

        # Midfielders
        count = 1
        while count <= self.midfielders_count:
            self.player_list[index].update_position((count * self.midfield_width, 750))
            count += 1
            index += 1

        # Attackers
        count = 1
        while count <= self.attackers_count:
            self.player_list[index].update_position((count * self.attack_width, 660))
            count += 1
            index += 1

        # Strikers
        count = 1
        while count <= self.strikers_count:
            self.player_list[index].update_position((count * self.strikers_width, 600))
            count += 1
            index += 1

        return self.player_list

    def get_formation(self):
        """formation getter method

        :return: the list of players
        """
        return self.player_list

    def move_center(self, player_list=None, increment=(0, 0)):
        """Moves the center and the bots move to keep in line with it.
        """
        if player_list is None:
            player_list = []

        for bot in player_list:
            bot.update_position(tuple(x + y for x, y in zip((bot.x, bot.y), increment)))

        # Like taking Cartesian product of center & increment then summing each of their values
        # Then the xth sum is stored as xth index in the tuple
        self.center = tuple(x + y for x, y in zip(self.center, increment))

    def update_width(self, factor):
        """Expand or contract the width of the formation depending on the circumstance.
        """
        # TODO: Fix this
        self.defense_width = (field_width / (self.defenders_count + 1))
        self.midfield_width = (field_width / (self.midfielders_count + 1))
        self.attack_width = (field_width / (self.attackers_count + 1))
        self.strikers_width = (field_width / (self.strikers_count + 1))

    def update_depth(self, factor):
        """Push the formation lines up or back the pitch.
        """
        self.defense_depth *= factor
        self.midfielders_depth *= factor
        self.attackers_depth *= factor
        self.strikers_depth *= factor

