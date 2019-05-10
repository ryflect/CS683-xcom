import numpy as np


class Arena(object):

    def __init__(self, n, h, t):
        self.arena = np.array(np.zeros([n, n]), dtype=int)
        self.size = n
        self.humans = h
        self.targets = t
        self.action_space = 3
        self.time = 0
        self.state = 's'

    def game_state(self):
        if self.humans == 0:
            self.state = 'l'  # loss
        elif self.targets == 0:
            self.state = 'w'  # win
        else:
            self.state = 's'  # in progress

    def print_arena(self):
        print(self.arena)
        return

    def remove_agents(self):
        self.arena[self.arena == 1] = 0
        self.arena[self.arena == 2] = 0
        return
