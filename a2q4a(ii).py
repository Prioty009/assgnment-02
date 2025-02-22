import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x=np.linspace(-5,5,100)
y=np.linspace(-5,5,100)
X,Y=np.meshgrid(x,y)
z=3
Z=z**2-X**2-Y**2
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.plot_surface(X,Y,Z,cmap='viridis')
ax.set_title(r'3D plot of $f(x,y,z)=z**2-x**2-y**2$ for $z=3$')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(x,y,z)')
plt.show()