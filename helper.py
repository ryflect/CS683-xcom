import numpy as np
from arena import Arena
from agent import HAgent, AAgent


def place_soldiers(n, arena, agents):
    x = 0
    y = 0
    for i in range(n):
        agents[i+1] = HAgent([x, y])
        arena.arena[x, y] = 1
        y += 2
    return arena, agents


def place_targets(n, arena, targets):
    for i in range(n):
        while True:
            x = np.rint(np.array([(arena.size - 1) * np.random.rand(1),
                                  (arena.size - 1) * np.random.rand(1)]))
            if x[0] > 7 and x[1] > 7:
                break
        x = [int(i) for i in x]

        targets[i+1] = AAgent(x)
        arena.arena[x[0], x[1]] = 2

    return arena, targets
