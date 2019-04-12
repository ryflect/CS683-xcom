import numpy as np


class Arena(object):

    def __init__(self, n, h, t):
        self.arena = np.array(np.zeros([n, n]), dtype=int)
        self.size = n
        self.humans = h
        self.targets = t

    def game_state(self):
        if self.humans == 0:
            return 'l'  # loss
        elif self.targets == 0:
            return 'w'  # win
        else:
            return 's'  # in progress

    def print_arena(self):
        print(self.arena)
        return
