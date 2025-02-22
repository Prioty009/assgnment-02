import sympy as sp
t=sp.symbols('t')
x=sp.cos(t)
y=sp.sin(t)
z=sp.tan(t)
w=x**2+y**2+z**2
w_prime=w.diff(t).subs(t,3.1416/4)
print(w_prime)