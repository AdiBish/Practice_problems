""" root finding by bracketing and bisection"""
# this is assuming that the broad interval in which the root lies (x1,x2) is analytially known


import sympy as sp

def root(f,x1,x2,tol):
    x= sp.Symbol('x')

    if (f.subs(x,x1)*f.subs(x,x2)) <=0:
        print(f.subs(x,x1)*f.subs(x,x2))
        while abs(x1-x2) >=tol :  ##
            print(tol)
            x3 = (x1+x2)/2
            print(x3)
            if (f.subs(x,x1)*f.subs(x,x3)) > 0:
                x1=x3
            elif (f.subs(x,x2)*f.subs(x,x3)) >0:
                x2=x3
    return((x1+x2)/2)

## an alternate thing to do here is run a for loop instead till range n 
## where n is the number of iterations calculated as (log(abs(x1-x2)/tol))/log(2)


# example: ( the answer is 0.734600830078125)
x=sp.Symbol('x')
f = (x*x*x) - 10*x*x + 5 
x1= 0.6
x2 = 0.8
tol = 1e-5
findroot= root(f,x1,x2,tol)
