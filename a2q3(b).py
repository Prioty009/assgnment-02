import sympy as sp
x=sp.symbols('x')
y=sp.symbols('y')
f=y**2*sp.cos(x-y)
fx=sp.diff(f,x)
fy=sp.diff(f,y)
fxx=sp.diff(fx,x)
fyy=sp.diff(fy,y)
if fxx+fyy==0:
    print("f satisfy laplace equation")
else:
    print("f is not satisfy laplace equation")