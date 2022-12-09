from random import randint
import numpy as np
class signed_distance_function:
    def __init__(self, parent):
        self.parent = parent

    def sdf(self):
        pass
    
    def __call__(self):
        self.sdf()
        return np.array([randint(0,250) for i in range(500 * 4)], dtype="int8")