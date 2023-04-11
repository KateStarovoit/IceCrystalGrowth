from init import *
from heat_solve import *
from phase_field_solve import *

"""
Simulation
Input
seed - seed element position [0,0]
te - initial T(a constant)
h - size of the grid
alpha - constant
K - constant
g - constant
tay - constant
n_iter - number of iterations
t - timestep
"""
def sim(seed, te, h, alpha, K, g,tay,n_iter = 100, t = 0.01):
    #Initizalize T and p
    n = int(1/h)
    T, p = init(seed, n)

    #Simulation
    for i in range(n_iter):
        # solve for T_
        T_ = heat_solve(alpha, T, p, K, h)
        T += T_ * t

        #solve for p_
        p_ = phase_field_solve(T, p, h, alpha, g, te, tay)
        p += p_ * t

    return p, T
