import numpy as np
import matplotlib.pyplot as plt
def f(x,y):
    return np.abs(np.sin(x)*np.cos(y))
x=np.linspace(0,2*np.pi,100)
y=np.linspace(0,2*np.pi,100)
X,Y=np.meshgrid(x,y)
Z=f(X,Y)
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.plot_surface(X,Y,Z,cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(x,y)')
ax.set_title('3D plot of $f(x,y)=|sin(x)cos(y)|$')
plt.show()