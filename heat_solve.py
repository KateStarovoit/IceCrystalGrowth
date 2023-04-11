from fd_laplacian import *

"""
Heat solve
Input
alpha - constant
T - previous T
p - phase field
K - constant
h - grid size
"""
def heat_solve(alpha, T, p, k, h):
    L = Fd_laplacian_dense(h)
    return alpha*alpha*np.dot(L, T)+k*p
