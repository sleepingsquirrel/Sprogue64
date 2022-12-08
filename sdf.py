from random import randint
import numpy as np
class signed_distance_function:
    def __init__(self, parent):
        self.parent = parent
    def __call__(self):
        return np.array([randint(0,250) for i in range(500)])