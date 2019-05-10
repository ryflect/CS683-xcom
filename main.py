from arena import Arena
from agent import HAgent, AAgent
from helper import *
from trainer import qtrainer
from environment import Env
import random
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # init size, num_humans, num_targets, amount of half cover
    # np.random.seed(1234)
    # init environment
    num = [20, 1, 1, 20]
    agents = {}
    targets = {}
    a = Arena(num[0], num[1], num[2])
    a, agents = place_soldiers(num[1], a, agents)
    a, targets, t_pos = place_targets(num[2], a, targets)
    a = place_half_cover(num[3], a)
    env = Env(a, agents, targets, num[1])

    Q, stat = qtrainer(env, 20, t_pos)
    plt.plot(range(20), stat['ep_rewards'])
    plt.xlabel('Episodes')
    plt.ylabel('Reward')
    plt.show()

    env = env.env_reset()

    pass
