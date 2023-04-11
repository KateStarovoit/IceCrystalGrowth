import scipy
import numpy as np

def get_index(i,j,n):
    return int(i+j*n)

def get_cell_indexes(i,j,h):
     return get_index(i,j,1/h), get_index(i+1,j,1/h), get_index(i-1,j,1/h), get_index(i,j-1,1/h), get_index(i,j+1,1/h)

def Fd_laplacian_dense(h):
    n = int(1/h)
    L = np.zeros((n, n))
    for i in range(n):
        L[i][i] = -4
        if i > 0:
            L[i - 1][i] = 1
        if i < n-1:
            L[i + 1][i] = 1
    return L
