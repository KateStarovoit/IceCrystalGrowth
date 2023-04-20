from init import *
from heat_solve import *
from phase_field_solve import *
import polyscope as ps
import polyscope.imgui as psim


"""
Simulation
Input
seed - seed coords [x, y]
te - initial T(a constant)
h - size of the grid
alpha - constant
K - latent heat constant
g - constant
j - the degree of anisotropy
eps_ - scaling factor

tay - constant
n_iter - number of iterations
t - timestep
"""
def sim(seed, Te, h, a, alpha, K, g, tay, eps, n_iter = 100, t_step = 0.01):
    #Initizalize T and p
    n = int(1/h)
    T, p = init(seed, n)

    points = np.zeros((n * n, 2))
    for i in range(n):
        for j in range(n):
            points[i + j * n][0] = i * (h + 0.5) / n + h
            points[i + j * n][1] = (j * (h + 0.5)) / n + h
    ps.init()

    P_T = ps.register_point_cloud("Temperature", points)
    P_p = ps.register_point_cloud("Phase field", points)
    P_T.set_radius(0.015)
    P_p.set_radius(0.015)
    for i in range(n_iter):
        T_ = heat_solve(a, T, p, K, h)
        T += T_.transpose() * t_step
        p_ = phase_field_solve(T, p, h, alpha, g, Te, tay, eps)
        p += p_.transpose() * t_step

    ps.PointCloud.add_scalar_quantity(P_T, f"Temperature", T, vminmax = [-1, 1])
    ps.PointCloud.add_scalar_quantity(P_p, f"Phase field", p, vminmax = [0,2])  # ,
    ps.show()

def animate(seed, Te, h, a, alpha, K, g, tay,  eps, n_iter = 100, t_step = 0.01,):
    # Initizalize T and p
    n = int(1 / h)
    T, p = init(seed, n)

    #Initial solve
    T_ = heat_solve(alpha, T, p, K, h)
    T += T_.transpose() * t_step
    p_ = phase_field_solve(T, p, h, alpha, g, Te, tay, eps)
    p += p_.transpose() * t_step

    is_playing = False

    #Animate
    points = np.zeros((n * n, 2))
    for i in range(n):
        for j in range(n):
            points[i + j * n][0] = i * (h + 0.5) / n + h
            points[i + j * n][1] = (j * (h + 0.5)) / n + h

    ps.init()
    P_T = ps.register_point_cloud("Temperature", points)
    P_p = ps.register_point_cloud("Phase field", points)
    P_T.set_radius(0.015)
    P_p.set_radius(0.015)
    ps.PointCloud.add_scalar_quantity(P_T, f"Temperature", T, vminmax = [-1, 1])
    ps.PointCloud.add_scalar_quantity(P_p, f"Phase field", p, vminmax = [0,1])  #
    def callback():
        nonlocal T, p, alpha, g, h, Te, tay, K, t_step, is_playing
        i_ = 0
        if (psim.Button("Iterate")):
            for i in range(1):
                T_ = heat_solve(a, T, p, K, h)
                T += T_.transpose() * t_step
                p_ = phase_field_solve(T, p, h, alpha, g, Te, tay, eps)
                p += p_.transpose() * t_step
            ps.PointCloud.add_scalar_quantity(P_T, f"Temperature", T, vminmax = [-1, 1])
            ps.PointCloud.add_scalar_quantity(P_p, f"Phase field", p, vminmax = [0,1])  # , vminmax = [0,1]
            i_ += 1
        if is_playing:
            i_ = 1
            T_ = heat_solve(a, T, p, K, h)
            T += T_.transpose() * t_step
            p_ = phase_field_solve(T, p, h, alpha, g, Te, tay, eps)
            p += p_.transpose() * t_step
            i_ += 1
            ps.PointCloud.add_scalar_quantity(P_T, f"Temperature", T, vminmax = [-1, 1])
            ps.PointCloud.add_scalar_quantity(P_p, f"Phase field", p, vminmax = [0,1])  # , vminmax = [0,1]

        if (psim.Button("Play")):
            is_playing = True

        if (psim.Button("Paused")):
            is_playing = False
    ps.set_user_callback(callback)
    ps.show()
