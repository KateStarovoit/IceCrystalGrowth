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
def heat_solve(alpha, T, p, K, h):
    L = Fd_laplacian(h)
    sol = scipy.sparse.linalg.spsolve(alpha*L,-T-K*p)
    return sol
