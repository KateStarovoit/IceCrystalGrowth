import numpy as np

'''
Initialization for ice crystal growth
Input
seed - [x, y] coords of seed
n - size of the grid
'''
def init(seed, n):
    T = np.ones(n*n)
    p = np.zeros(n*n)
    T[seed[0]*seed[1]] = 0
    p[seed[0]*seed[1]] = 1
    return T, p
