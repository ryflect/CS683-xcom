from arena import Arena
from agent import HAgent, AAgent
from helper import place_soldiers, place_targets

import numpy as np

if __name__ == '__main__':
    # init size, num_humans, num_targets
    num = [20, 3, 3]

    agents = {}
    targets = {}
    a = Arena(num[0], num[1], num[2])
    a, agents = place_soldiers(num[1], a, agents)
    a, targets = place_targets(num[2], a, targets)

    a.print_arena()

    pass
