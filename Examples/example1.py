from simulate import *

seed = [5,5]
alpha = 0.9
K = 1
h = 0.1
n = int(1/h)
tay = 0.003
g = 10
Te = 1
T, p = init(seed, n)

p_s, t_s = sim(seed,Te,h,alpha,K,g,tay,1,0.01)
