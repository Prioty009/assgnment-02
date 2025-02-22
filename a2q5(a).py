import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x,y,z=sp.symbols('x y z')
ellipsoid_eq=x**2+4*y**2+z**2-18
#(i)
point=(1,2,1)
grad_f=[sp.diff(ellipsoid_eq,var) for var in (x,y,z)]
normal_vector=[expr.subs({x:point[0],y:point[1],z:point[2]}) for expr in grad_f]
tangent_plane_eq=normal_vector[0]*(x-point[0])+normal_vector[1]*(y-point[1])+normal_vector[2]*(z-point[2])
print("Equation of tangent plane:",tangent_plane_eq)
#(ii)
t=sp.symbols('t')
normal_line=[point[i]+t*normal_vector[i] for i in range(3)]
print("normal line:",normal_line)
#(iii)
angle=sp.acos(abs(normal_vector[2])/sp.sqrt(sum(n**2 for n in normal_vector)))
angle_deg=sp.deg(angle)
print("Angle:",angle_deg.evalf())
#(iv)
fig=plt.figure(figsize=(8,6))
ax=fig.add_subplot(111,projection='3d')
u=np.linspace(0,2*np.pi,50)
v=np.linspace(0,np.pi,50)
X=np.outer(np.cos(u),np.sin(v))*np.sqrt(18)
Y=np.outer(np.sin(u),np.sin(v))*np.sqrt(18)/2
Z=np.outer(np.ones_like(u),np.cos(v))*np.sqrt(18)
ax.plot_surface(X,Y,Z,color='c',alpha=0.6)
#tangent plane
X_t,Y_t=np.meshgrid(np.linspace(-5,5,10),np.linspace(-5,5,10))
Z_t=(normal_vector[0]*(X_t-point[0])+normal_vector[1]*(Y_t-point[1]))/(-normal_vector[2])+point[2]
ax.plot_surface(X_t,Y_t,Z_t,color='r',alpha=0.5)
#normal line
t_vals=np.linspace(-5,5,10)
X_n=point[0]+t_vals*normal_vector[0]
Y_n=point[1]+t_vals*normal_vector[1]
Z_n=point[2]+t_vals*normal_vector[2]
ax.plot(X_n,Y_n,Z_n,'k--',label="Normal Line")
ax.scatter(*point,color='r',s=100,label='Point(1,2,1)')
ax.set_xlabel('X')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
