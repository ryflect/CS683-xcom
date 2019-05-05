from arena import Arena
from agent import HAgent, AAgent
from helper import place_soldiers, place_targets, place_half_cover

import numpy as np

if __name__ == '__main__':
    # init size, num_humans, num_targets, amount of half cover
    num = [20, 3, 3, 20]

    agents = {}
    targets = {}
    a = Arena(num[0], num[1], num[2])
    a, agents = place_soldiers(num[1], a, agents)
    a, targets = place_targets(num[2], a, targets)
    a = place_half_cover(num[3], a)

    a.print_arena()

    pass
