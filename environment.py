from agent import HAgent, AAgent
from arena import Arena
from helper import *
import random


class Env(object):

    def __init__(self, arena, agents, targets, num_s):
        self.a = arena
        self.agents = agents
        self.targets = targets
        # self.original = arena
        # self.or_agents = agents
        # self.or_targets = targets
        self.num_s = num_s

    def show_arena(self):
        self.a.print_arena()
        return

    def env_reset(self, orig_pos=None):
        self.a.remove_agents()
        self.a.time = 0
        self.a.state = 's'
        self.a, self.agents = place_soldiers(1, self.a, self.agents)
        self.a, self.targets, orig_pos = place_targets(1, self.a, self.targets, orig_pos)
        return self

    def step(self, action):
        if action == 0:
            # move
            x, y = get_valid_move(self.agents[1])
            # x, y = action[1]
            # print(x, y)
            self.agents[1], self.a = move(self.agents[1], self.a, [x, y])

        elif action == 1:
            # shoot
            # t = int(random.randint(1, 10))
            t = 1
            # print(t)
            self.agents[1], self.a, self.targets[t] = fire(self.agents[1], self.a, self.targets[t])

        elif action == 2:
            # reload
            self.agents[1] = reload(self.agents[1])

        next_state = self.a
        # print(self.a.targets)
        reward = -10 * self.a.targets + 0.1 * self.agents[1].cover + 0.01 * self.agents[1].health - 0.001 * self.a.time
        # print('Reward: ', reward)
        done = False
        # print(self.a.targets, self.a.game_state())
        if self.a.state == 'w':
            done = True
        elif self.a.state == 'l':
            done = True
        elif self.a.time == 500:
            done = True

        return next_state, reward, done
