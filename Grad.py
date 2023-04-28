import scipy

def Grad_matrix(n, p):
    G_x = scipy.sparse.lil_matrix((n * n, n * n))
    for i in range(0, n):
        for j in range(0, n):
            if j > 0:
                G_x[(i * n + j, i * n + j - 1)] += 0.5
            else:
                G_x[(i * n + j, i * n + j + 1)] += 0.5
            if j < n - 1:
                G_x[(i * n + j, i * n + j + 1)] += 0.5
            else:
                G_x[(i * n + j, i * n + j - 1)] += 0.5

    G_y = scipy.sparse.lil_matrix((n * n, n * n))
    for i in range(0, n):
        for j in range(0, n):
            if i > 0:
                G_y[(i * n + j, (i- 1) * n + j)] += 0.5
            else:
                G_y[(i * n + j, (i+ 1) * n + j)] += 0.5
            if i < n - 1:
                G_y[(i * n + j, (i+ 1) * n + j)] += 0.5
            else:
                G_y[(i * n + j, (i- 1) * n + j)] += 0.5
    return G_x, G_y

def Grad(n, p):
    g_x, g_y = Grad_matrix(n, p)
    Gx = p@g_x
    Gy = p@g_y
    G = Gx+Gy
    return Gx, Gy, G
