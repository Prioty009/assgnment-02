import numpy as np 
import matplotlib.pyplot as plt
x=np.linspace(-5,5,100)
y=np.linspace(-5,5,100)
X,Y=np.meshgrid(x,y)
Z=4*X**2+Y**2
k=1,4,9,16,25,36
levels=[1,4,9,16,25,36]
plt.contour(X,Y,Z,levels,cmap='viridis')
plt.colorbar()
plt.title(r'Contour Plot of $f(x,y)=4*x**2+y**2$')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()