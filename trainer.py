import numpy as np
import itertools
from collections import defaultdict
import sys
import os


def make_eps_greedy(Q, epsilon, num_actions):

    def policy_fn(obs):
        A = np.ones(num_actions, dtype=float) * epsilon / num_actions
        best_action = np.argmax(Q[obs])
        A[best_action] += (1.0 - epsilon)
        return A
    return policy_fn


def qtrainer(env, num_episodes, tpos=None, discount_factor=1.0, alpha=0.5, epsilon=0.1):
    Q = defaultdict(lambda: np.zeros(env.a.action_space))
    stats = {'ep_length': np.zeros(num_episodes),
             'ep_rewards': np.zeros(num_episodes)}
    policy = make_eps_greedy(Q, epsilon, env.a.action_space)
    for i in range(num_episodes):
        # print('Episode: ', i)
        if (i + 1) % 10 == 0:
            print("\rEpisode {}/{}.".format(i + 1, num_episodes), end="")
            sys.stdout.flush()
        state = env.env_reset(tpos).a
        for t in itertools.count():
            # print(t)
            # take step
            action_probs = policy(state)
            action = np.random.choice(np.arange(len(action_probs)), p=action_probs)
            # print('action: ', action)
            next_state, reward, done = env.step(action)
            # print(env.agents[1].pos)

            # sys.stdout.flush()
            # update stats
            stats['ep_length'][i] = t
            stats['ep_rewards'][i] += reward

            # TD update
            best_next_action = np.argmax(Q[next_state])
            td_target = reward + discount_factor * Q[next_state][best_next_action]
            td_delta = td_target - Q[state][action]
            Q[state][action] += alpha * td_delta

            if done:
                break

            state = next_state
            # print(state.arena)

    return Q, stats
