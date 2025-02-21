import sympy as sp
x,y,theta,r,phi,z,t=sp.symbols('x y theta r phi z t') 
F_xy=sp.Matrix([sp.exp(x)-y**3,sp.cos(y)+x**3])
M,N=F_xy[0],F_xy[1]
dN_dx,dM_dy=sp.diff(N,x),sp.diff(M,y)
integrand=dN_dx-dM_dy
integrand_polar=integrand.subs({x:r*sp.cos(theta),y:r*sp.sin(theta)})
w=sp.integrate(integrand_polar*r,(r,0,1),(theta,0,2*sp.pi))
print(f'work done:',w)
#(b)
F_x=x**2
F_thetaphi=F_x.subs({x:sp.sin(theta)*sp.cos(phi)})
ds=sp.sin(theta)
surface_integral=sp.integrate(F_thetaphi*ds,(theta,0,sp.pi),(phi,0,2*sp.pi))
print(f'surface integral:',surface_integral)
#(c)
F_xyz=sp.Matrix([x**3,y**3,z**2])
divergence_F=sp.diff(F_xyz[0],x)+sp.diff(F_xyz[1],y)+sp.diff(F_xyz[2],z)
divergence_Frthetaz=divergence_F.subs({x:r*sp.cos(theta),y:r*sp.sin(theta),z:z})
flux=sp.integrate(sp.integrate(sp.integrate(divergence_Frthetaz*r,(z,0,2)),(r,0,3)),(theta,0,2*sp.pi))
print(f'outsize flux:',flux)
#(d)
F=sp.Matrix([2*z,3*x,5*y])
curl_F=sp.Matrix([sp.diff(F[2],y)-sp.diff(F[1],z),sp.diff(F[0],z)-sp.diff(F[2],x),sp.diff(F[1],x)-sp.diff(F[0],y)])
curl_F_polar=curl_F.subs({x:r*sp.cos(theta),y:r*sp.sin(theta),z:4-x**2-y**2})
print(f'curl:',curl_F_polar)
normal=sp.Matrix([-sp.diff(4-x**2-y**2,x),-sp.diff(4-x**2-y**2,y),1])
normal_polar=normal.subs({x:r*sp.cos(theta),y:r*sp.sin(theta),z:4-x**2-y**2})
surface_integral=sp.integrate(curl_F_polar.dot(normal_polar)*r,(r,0,2),(theta,0,2*sp.pi))
x_p,y_p,z_p=2*sp.cos(t),2*sp.sin(t),0
F_c=F.subs({x:x_p,y:y_p,z:z_p})
dt=sp.Matrix([sp.diff(x_p,t),sp.diff(y_p,t),sp.diff(z_p,t)])
line_integral=sp.integrate(F_c.dot(dt),(t,0,2*sp.pi))
print(f'surface_integral:',surface_integral)
print(f'line_integral:',line_integral)
if surface_integral==line_integral:
    print("stoke's theorem is varify")
else:
     print("stoke's theorem is not varify")




