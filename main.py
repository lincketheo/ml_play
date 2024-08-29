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
        self.adjs = []

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

        costs = []
        adjs = []
        x = random.random() * 0.001

        for _ in range(self.chunk_size):
            # Evaluate
            real = unknown_func(x)
            mine = poly_eval(new_state, x)
            c = (real - mine)**2

            # Save
            costs.append(c)
            adjs.append(new_state[adj])

            # Update
            new_state[adj] = new_state[adj] - 1 * mult

        self.costs.append(costs)
        self.adjs.append(adjs)


"""
Make one random change 
Do 1 thing for n iterations 
Observe
Make decision 
Repeat
"""

"""
Cost Database:
    - |a - b|
    - a can be any parameter, or model output, b is any measurement of the real world
    - Oh hey, this thing is going down as I do this, lets see if that means anything
    - There are lots of costs in the observed 

Fact:
    Observation:
    Model:
        - IDEA:
            - Start out with a small set of numbers 
            - Models have a lifetime based on how well they perform on other tasks in your world
            - Save Random models in a "stack"
        - The data "fits" this model behavior (difference of numbers is same - linear model)
        - Models can be broken

Model Database:
    - Database of facts:
    - Models can be "set in stone" via logic
        - e.g. 
        - If data fit exactly these conditions, I can describe the system _perfectly_
        - Premise: Data fits the model -> conclusion: model outputs
    - Some sort of pipeline for models: 
        - They're bad at first (psychology), then over time get more and more specific and 
        - less ambiguous until they're perfect (math / logic)
        - self describing - all self contained - no magic numbers or constants in the equations
        - (physics is a 1 constant field, Gravity constant)
        - (math is a 0 constant field)

Training algorithm:
    - Generic
        - Make a random perturbation in your "model space"
        - Observe the world 
        - Decide if that perturbation was good or bad 
    - Actualized:
        - pick random perturbation 
        - Run 1000 iterations 
        - observe 
        - repeat
        - (but the fact that I ran 1000 iterations is random, it works well, so 
        - that behavior is a model. E.g. one of my models is "when I run things 1000 times 
        - then observe, I see better performance increases to the cost function of training speed)
        - TODO - capture that idea above in a model? Or not and create a limited set and make 
        - it perform better than 
"""

def func(x):
    return 5 * x**2 + 4 * x + 3 + 9.123 * x**8

b = Brain()

for i in range(10):
    b.chunk(func)

for i in range(len(b.costs)):
    plt.plot(b.adjs[i], b.costs[i])
    plt.show()


