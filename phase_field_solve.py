from fd_laplacian import *
import numpy as np

"""
Phase field solve 
Input
T - temperature n x 1 array
p - phase field at prev step. n x 1 array
h - grid size
alpha - constant
g - constant
Te - initial temperature
t - constant
Output
Phase field update dp/dt
"""
def phase_field_solve(T,p,h,alpha,g,Te,tay, eps):
    L = Fd_laplacian(h)
    m = alpha/np.pi*np.arctan(g * (Te - T))

    diffuse_term = eps*eps*L@p
    sourse_term = (p)*(1-p)*(p-0.5+m)
    p_ = (diffuse_term+sourse_term)/tay
    return p_
