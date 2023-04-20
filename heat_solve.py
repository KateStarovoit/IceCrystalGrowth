from fd_laplacian import *

"""
Heat solve
Input
alpha - constant
T - previous T
p - phase field
K - latent heat constant
h - grid size
"""
def heat_solve(a, T, p, k, h):
    L = Fd_laplacian(h)
    return a*a*L@T + k * p
