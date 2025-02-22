import numpy as np
import matplotlib.pyplot as plt
def f(x,y):
    return y**2-2*y*np.cos(x)
x=np.linspace(1,7,100)
y=np.linspace(-5,5,100)
X,Y=np.meshgrid(x,y)
Z=f(X,Y)
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.plot_surface(X,Y,Z,cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(x,y)')
ax.set_title('3D plot of $f(x,y)=y^2-2*y*cos(x)$')
plt.show()


