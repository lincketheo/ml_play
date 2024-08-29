import math
import random
import matplotlib.pyplot as plt
import numpy as np
from typing import List

class Model:
    def __init__(self):
        pass


class Polynomial:
    def __init__(self, coefs):
        self.coefs = coefs


def poly_eval(coefs, x):
    ret = 0
    for i, a in enumerate(coefs):
        ret += a * x**i
    return ret


class Brain:
    def __init__(self, chunk_size=1000, its=100):
        self.chunk_size = chunk_size
        self.its = its
        self.state: List[float] = [random.random() * 10 for _ in range(5)]
        self.costs = []

    def chunk(self, unknown_func):
        # 1 random state change
        adj = None
        new_state = None
        choice = random.randint(0, 2)

        if choice == 0:
            new_state = self.state 
            adj = random.randint(0, len(new_state)-1)
        elif choice == 1:
            new_state = self.state + [random.random() * 10]
            adj = len(new_state) - 1
        elif choice == 2:
            new_state = [random.random() * 10] + self.state
            adj = len(new_state) - 1

        mult = random.choice([-1, 1])

        assert new_state is not None 
        assert adj is not None

        cost = []
        x = random.random() * 0.001

        for _ in range(self.chunk_size):
            real = unknown_func(x)
            mine = poly_eval(new_state, x)
            c = (real - mine)**2

            print(real, mine, c)
            cost.append(c)

            new_state[adj] = new_state[adj] - 1 * mult

        self.costs.append(cost)

def func(x):
    return 5 * x**2 + 4 * x + 3 + 9.123 * x**8

b = Brain()

for i in range(10):
    b.chunk(func)

for c in b.costs:
    plt.plot(c)
    plt.show()


