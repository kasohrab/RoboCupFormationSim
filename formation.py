from references import *
from bot import FriendlyBot


class Formation:
    """Formation class"""

    def __init__(self, num_bots, total_width, total_depth, defenders_count,
                 midfielders_count, attackers_count, strikers_count):
        """Initializing the formation data"""

        if num_bots != 11 | num_bots != 6:
            raise ValueError("Only 6 and 11 player formations are supported.")

        self.player_list = []
        player_count = 0
        while player_count < num_bots:
            self.player_list.append(FriendlyBot())
            player_count += 1

        # variables that help define the center of the formation

        # how spaced apart each row of players is
        self.row_separation = total_depth / 4

        self.center = (0, 0)
        self.goalkeeper_depth = FIELD_DEPTH - 20
        self.defense_depth = self.goalkeeper_depth - self.row_separation
        self.midfielders_depth = self.defense_depth - self.row_separation
        self.attackers_depth = self.midfielders_depth - self.row_separation
        self.strikers_depth = self.attackers_depth - self.row_separation

        self.goalkeeper_width = 0
        self.defense_width = 0
        self.midfield_width = 0
        self.attack_width = 0
        self.strikers_width = 0

        self.total_width = total_width

        """Set how many bots in each line"""
        self.defenders_count = defenders_count
        self.midfielders_count = midfielders_count
        self.attackers_count = attackers_count
        self.strikers_count = strikers_count

    def __iter__(self):
        """Makes formation iterable"""
        return iter(self.player_list)

    def build(self):
        """Builds formation and positions that the robots will go to
        """
        # TODO: Make center relative (use center instead of field_... always)

        # set the depth
        self.goalkeeper_depth = FIELD_DEPTH - 20
        self.defense_depth = self.goalkeeper_depth - self.row_separation
        self.midfielders_depth = self.defense_depth - self.row_separation
        self.attackers_depth = self.midfielders_depth - self.row_separation
        self.strikers_depth = self.attackers_depth - self.row_separation
        # set the width of each row
        self.goalkeeper_width = self.total_width / 2
        self.defense_width = self.total_width / (self.defenders_count + 1)
        self.midfield_width = (self.total_width / (self.midfielders_count + 1))
        self.attack_width = (self.total_width / (self.attackers_count + 1))
        self.strikers_width = (self.total_width / (self.strikers_count + 1))
        # Set initial center as the average of all robot positions
        average_depth = (self.goalkeeper_depth + (self.defense_depth * self.defenders_count) +
                         (self.midfielders_depth * self.midfielders_count)
                         + (self.attackers_depth * self.attackers_count)
                         + (self.strikers_depth + self.strikers_count)) / len(self.player_list)

        # add this to allow formation to be adjustable to any width
        shift_left = (FIELD_WIDTH / 2) - (self.total_width / 2)

        # Set player initial positions where (0,0) is top left

        # Sweeper Keeper
        self.player_list[0].update_position((1 * self.goalkeeper_width + shift_left, self.goalkeeper_depth))

        count = 1
        index = 1

        # Defenders
        while count <= self.defenders_count:
            self.player_list[index].\
                update_position((count * self.defense_width + shift_left, self.defense_depth))
            count += 1
            index += 1

        # Midfielders
        count = 1
        while count <= self.midfielders_count:
            self.player_list[index].\
                update_position((count * self.midfield_width + shift_left, self.midfielders_depth))
            count += 1
            index += 1

        # Attackers
        count = 1
        while count <= self.attackers_count:
            self.player_list[index].\
                update_position((count * self.attack_width + shift_left,  self.attackers_depth))
            count += 1
            index += 1

        # Strikers
        #  + self.center[0]/(field_width/self.total_width)
        count = 1
        while count <= self.strikers_count:
            self.player_list[index].\
                update_position((count * self.strikers_width + shift_left, self.strikers_depth))
            count += 1
            index += 1

        # set center to average of positions
        # maybe there is a better place for this?
        self.center = [sum(y) / len(y) for y in zip(*self.get_positions())]

    def get_formation(self):
        """formation getter method

        :return: the list of players
        """
        return self.player_list

    def get_positions(self):
        """Returns a list of the bot positions"""
        pos_list = []
        for bot in self.player_list:
            pos_list.append(bot.get_position())

        return pos_list

    def move_center(self, center=(0, 0)):
        """Moves the center and the bots move to keep in line with it.
        """
        self.increment_center(((center[0] - self.center[0]), (center[1] - self.center[1])))
        self.center = center

    def increment_center(self, increment=(0, 0)):
        """Increments the center based on increment and the bots move to keep in line with it.
        """
        if self.player_list is None:
            self.player_list = []

        for bot in self.player_list:
            bot.update_position(tuple(x + y for x, y in zip((bot.x, bot.y), increment)))

        # Like taking Cartesian product of center & increment then summing each of their values
        # Then the xth sum is stored as xth index in the tuple
        self.center = tuple(x + y for x, y in zip(self.center, increment))

    def factor_center(self, factor, direction):
        """Factor times the center based on factor and the bots move to keep in line with it.
        """
        if self.player_list is None:
            self.player_list = []
        if direction == 'x':
            for bot in self.player_list:
                bot.update_position((bot.x * factor, bot.y))
        else:
            for bot in self.player_list:
                bot.update_position((bot.x, bot.y * factor))

        self.center = [sum(y) / len(y) for y in zip(*self.get_positions())]

    def update_width(self, new_width):
        """Expand or contract the width of the formation depending on the circumstance.
        """
        self.total_width = new_width
        # self.factor_center(self.total_width / field_width, 'x')
        self.build()

    def update_depth(self, new_depth):
        """Push the formation lines up or back the pitch.
        """
        self.row_separation = new_depth / 4
        self.build()

    def update_depth_vars(self):
        """Update the depth vars.
        Eventually should be able to do all rows or individual rows.
        """
        # TODO: do or dont...
        self.goalkeeper_depth = FIELD_DEPTH - 20
        self.defense_depth = self.goalkeeper_depth - self.row_separation
        self.midfielders_depth = self.defense_depth - self.row_separation
        self.attackers_depth = self.midfielders_depth - self.row_separation
        self.strikers_depth = self.attackers_depth - self.row_separation