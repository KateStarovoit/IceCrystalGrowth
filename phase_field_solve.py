import math
from fd_laplacian import *

def m(T, alpha, g, Te):
    val = np.zeros(len(T))
    for i in range(len(val)):
        val[i] = math.atan(g*(Te-T[i]))
    M = alpha/math.pi*val
    return M

def phase_field_solve(T,p,h,alpha,g,Te,tay):
    L = Fd_laplacian(h)
    return (L*p+p*(1-p)*(p-0.5+m(T, alpha, g, Te)))/tay
