from fd_laplacian import *

def m(T, alpha, g, Te):
    return alpha/np.pi*np.arctan(g * (Te - T))

def phase_field_solve(T,p,h,alpha,g,Te,t):
    L = Fd_laplacian_dense(h)
    return (np.dot(L,p)+np.dot(p,(1-p))*(p-0.5+m(T, alpha, g, Te)))/t
