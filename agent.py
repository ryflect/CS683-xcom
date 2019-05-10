import numpy as np


class HAgent(object):

    def __init__(self, position):
        self.pos = position
        # on normal, base HP of five
        self.health = 5
        # for assault rifle, base ammo of five, using 99 for the simple case
        self.ammo = 99
        self.cover = 0
        self.vision = self.get_vision()
        self.range = self.get_range()
        self.targets = 0
        self.damage = 0
        self.accuracy = 0
        self.moves = 999
        # base movement range is 7 tiles
        self.move_range = 7
        # base aim percentage is 65 pp
        self.aim = 65
        self.base_damage = 3
        # base crit percentage of 10pp
        self.base_crit = 10

    def get_vision(self):
        self.vision = [[i, j] for i in range(self.pos[0] - 20, self.pos[0] + 20) for j in
                       range(self.pos[1] - 20, self.pos[1] + 20) if i >= 0 and j >= 0]
        return self.vision

    def get_range(self):
        self.range = [[i, j] for i in range(self.pos[0] - 10, self.pos[0] + 10) for j in
                      range(self.pos[1] - 10, self.pos[1] + 10) if i >= 0 and j >= 0]
        return self.range


class AAgent(object):

    def __init__(self, position):
        self.pos = position
        # sectoid base hp is 3
        self.health = 3
        # sectoid base ammo is unlimited
        self.ammo = 999
        self.cover = 0
        self.vision = self.get_vision()
        self.range = self.get_range()
        self.targets = 0
        self.damage = 0
        self.accuracy = 0
        self.moves = 999
        # base movement range is 7 tiles
        self.move_range = 7
        # base aim percentage is 65 pp
        self.aim = 65
        self.base_damage = 3
        self.base_crit = 0

    def get_vision(self):
        self.vision = [[i, j] for i in range(self.pos[0] - 20, self.pos[0] + 20) for j in
                       range(self.pos[1] - 20, self.pos[1] + 20) if i >= 0 and j >= 0]
        return self.vision

    def get_range(self):
        self.range = [[i, j] for i in range(self.pos[0] - 20, self.pos[0] + 20) for j in
                      range(self.pos[1] - 20, self.pos[1] + 20) if i >= 0 and j >= 0]

        return self.range
