import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x,y,z,lamb=sp.symbols('x y z lamb')
T=8*x**2+4*y*z-16*z+600
g=4*x**2+y**2+4*z**2-16
grad_T=sp.Matrix([sp.diff(T,var) for var in (x,y,z)])
grad_g=sp.Matrix([sp.diff(g,var) for var in (x,y,z)])
equations=[grad_T[i]-lamb*grad_g[i] for i in range(3)]+[g]
solutions=sp.solve(equations,(x,y,z,lamb),dict=True)
max_temp=-np.inf
hottest_point=None
for sol in solutions:
    temp=T.subs(sol)
    if temp>max_temp:
        max_temp=temp
        hottest_point=sol
print("Hottest Point:",hottest_point)
print("Maximum Temperature:",max_temp)