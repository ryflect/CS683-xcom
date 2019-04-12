import numpy as np


class HAgent(object):

    def __init__(self, position):
        self.pos = position
        self.health = 100
        self.ammo = 10
        self.cover = 0
        self.vision = self.get_vision()
        self.range = self.get_range()
        self.targets = 0
        self.damage = 0
        self.accuracy = 0

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
        self.health = 50
        self.ammo = 10
        self.cover = 0
        self.vision = self.get_vision()
        self.range = self.get_range()
        self.targets = 0
        self.damage = 0
        self.accuracy = 0

    def get_vision(self):
        self.vision = [[i, j] for i in range(self.pos[0] - 20, self.pos[0] + 20) for j in
                       range(self.pos[1] - 20, self.pos[1] + 20) if i >= 0 and j >= 0]
        return self.vision

    def get_range(self):
        self.range = [[i, j] for i in range(self.pos[0] - 20, self.pos[0] + 20) for j in
                      range(self.pos[1] - 20, self.pos[1] + 20) if i >= 0 and j >= 0]
        return self.range
