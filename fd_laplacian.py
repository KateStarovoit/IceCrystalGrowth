import scipy


"""
Constructs finite difference laplacian
Input
h - grid spacing
Output
L - fd laplacian
"""
def get_index(i,j,n):
    return int(i+j*n)

def get_cell_indexes(i,j,h):
     return get_index(i,j,1/h), get_index(i+1,j,1/h), get_index(i-1,j,1/h), get_index(i,j-1,1/h), get_index(i,j+1,1/h)

def Fd_laplacian(h):
    n = int(1/h)
    L = scipy.sparse.lil_matrix((n*n, n*n),)

    # constructing L and U
    for i in range(0, n):
        for j in range(0, n):
            mid_index, right_index, left_index, bottom_index, top_index = get_cell_indexes(i, j, h)
            L[(mid_index, mid_index)] = 0
            if (i + 1) < n:
                L[(mid_index, right_index)] = 1
                L[(mid_index, mid_index)] -= 1
            if i > 0:
                L[(mid_index, left_index)] = 1
                L[(mid_index, mid_index)] -= 1
            if j > 0:
                L[(mid_index, bottom_index)] = 1
                L[(mid_index, mid_index)] -= 1
            if (j + 1) < n:
                L[(mid_index, top_index)] = 1
                L[(mid_index, mid_index)] -= 1
    L_ = L/(h*h)
    return L_
