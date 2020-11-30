## Inspiration from various environments on gym.openai.com ##
import gym
import sys
from gym import error, spaces, utils
from gym.utils import seeding
from contextlib import closing
from io import StringIO
from gym.envs.toy_text import discrete
import numpy as np

MAP = [
    "Environment",
    "+---------+",
    "|B: : : :S|",
    "+---------+"
]


class Note4Env(gym.Env):
    metadata = {'render.modes': ['human', 'ansi']}
    """chain environment
    This MDP presents moves along a chain of states, with two actions:
     0) forward, which moves forward along the chain but returns no reward
     1) backward, which moves backward along the chain but returns no reward
     
    At the beginning of the chain (State 0) there is a reward of 10 (B).
    At the end of the chain (State 1) there is a reward of 1 (S).
    
    The discount factor is gamma = 0.1
    The transitions are not determistic. If you choose to go forwards, you
    could go backwards with probability "slip" and vice versa.
    
    The observed state is the current state in the chain (0 to n-1).
    
    This MDP is described in CS 188 Note 4 of:
    https://inst.eecs.berkeley.edu/~cs188/fa20/assets/notes/note04.pdf
    """
    def __init__(self, n=5, slip=0.2, small=1, large=10, discount_factor = 0.1):
        self.n = n
        self.slip = slip  # probability of 'slipping' an action
        self.small = small  # payout at the front of the chain
        self.large = large  # payout at end of chain
        self.state = 2  # Start in the middle of the chain
        self.action_space = [0, 1, 2] #0 is forward, 1 is backward, 2 is exit
        self.discount_factor = discount_factor
        self.observation_space = spaces.Discrete(self.n)
        self.seed()

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]
    
    def sample(self):
        return np.random.choice([0, 1, 2])

    def step(self, action):
        # Discount rewards
        self.small = self.discount_factor*self.small
        self.large = self.discount_factor*self.large
        
        assert action in self.action_space
        if self.np_random.rand() < self.slip and action != 2:
            action = not action  # agent slipped, reverse action taken
            
        done = False
        if self.state < self.n - 1 and self.state > 0:
            if action == 0:  # 'backwards'
                reward = 0
                self.state -= 1
            elif action == 1: # 'forwards'
                reward = 0
                self.state += 1
            else: # 'exit'
                reward = 0
        elif self.state == 0:
            if action == 0: # 'backwards'
                reward = 0
            elif action == 1: # 'forwards'
                reward = 0
                self.state += 1
            else: # 'exit'
                reward = self.large
                done = True
        else:
            if action == 0: # 'backwards'
                reward = 0
                self.state -= 1
            elif action == 1: # 'forwards'
                reward = 0
            else: # 'exit'
                reward = self.small
                done = True
            
        return self.state, reward, done, {}

    def reset(self):
        self.state = 2
        self.large = 10
        self.small = 1
        self.slip = 0.2
        self.discount_factor = 0.1
        return self.state
    
    def render(self, mode="human", done=False):
        outfile = StringIO() if mode == 'ansi' else sys.stdout
        desc = np.asarray(MAP, dtype='c')

        out = desc.copy().tolist()
        out = [[c.decode('utf-8') for c in line] for line in out]
        agent_position = self.state

        # out[8][8] = utils.colorize(out[8][8], 'yellow', highlight=True)

        if agent_position <= 5 and not done:
            out[2][2*agent_position + 1] = utils.colorize(out[2][2*agent_position + 1], 'yellow', highlight=True)

        if agent_position <= 5 and done:
            out[2][2*agent_position + 1] = utils.colorize(out[2][2*agent_position + 1], 'green', highlight=True)

        outfile.write("\n".join(["".join(row) for row in out]) + "\n")

        if mode != 'human':
            with closing(outfile):
                return outfile.getvalue()