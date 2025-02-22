import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
x,y=sp.symbols('x y')
f=4*x*y-x**4-y**4
fx=sp.diff(f,x)
fy=sp.diff(f,y)
fxx=sp.diff(fx,x)
fyy=sp.diff(fy,y)
fxy=sp.diff(fx,y)
cp=sp.solve([fx,fy],[x,y])
D=fxx*fyy-fxy**2
s=[]
max=[]
for i in cp:
    D=D.subs({x:i[0],y:i[1]})
    if D==0:
        s.append(i)
    elif D<0:
        max.append(i)
print(s)
print(max)
f=sp.lambdify((x,y),f,'numpy')
x1=np.linspace(-2,2,100)
y1=np.linspace(-2,2,100)
f_np=f(x1,y1)
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
plt.plot(x1,y1,f_np)
plt.xlabel('X')
plt.ylabel('Y')
ax.set_zlabel('Z')
plt.show()

