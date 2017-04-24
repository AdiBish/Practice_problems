""" root finding by newton raphson
!! this works only for fixed number of iteration. ideally, run it till abs(x0-x01),tol !! """

import sympy as sp

def newtonRoot(f,x1,x2):
    x= sp.Symbol('x')

    if (f.subs(x,x1)*f.subs(x,x2)) <=0:
        x0 = (x1+x2)/2
        i=0
        while i<10  :
            x01 = x0-(f.subs(x,x0)/f.diff(x,1).subs(x,x0))
            x0= x01
            i+=1
    return(x0)
 
## example: 

x=sp.Symbol('x')
f = (x*x*x) - 10*x*x + 5 
x1= 0.6
x2 = 0.8

findroot= newtonRoot(f,x1,x2)
print(findroot)
