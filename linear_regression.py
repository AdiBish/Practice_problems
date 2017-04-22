import matplotlib.pyplot as plt
import numpy as np

# takes data points x and y, fits the linear equation y=mx+c to x data points to get y_cal. 
# calculates residual R = (y(xi) - yi)**2 and chi square
# returns chi squared value and plots the fitted data
# prefix s means summation 
def linearregress(x,y): 
    std2 = 1.0/std**2
    S = sum(std2) #summation over 1/sigma**2 for all data points
    
    sx= sum(x) 
    sy= sum(y)
    xy=[]
    xx=[]
    for i in range(len(x)):
        xy.append(x[i]*y[i])
        xx.append(x[i]*x[i])
    sxy= sum(xy)
    sxx= sum(xx)
    sysxx=sy*sxx
    
    ssxx= S*sxx
    ssxy= S*sxy
    sxysx = sxy*sx
    sxsy= sx*sy
    m=(ssxy -sxsy)/(ssxx-sxx)
    c=(sysxx-sxysx)/(ssxx-sxx)
    y_cal =[]
    R= []
    for i in range(len(x)):
        y_cal.append(m*x[i] - c)
        r= (y_cal[i]-y[i])
        rsq= r*r
        R.append(rsq)
    chi_sq= sum(R)/len(x)
    chi= 'chi_sq = '+str(round(chi_sq,2))
    
    observed = plt.scatter(x,y,color='r', label= 'observed')
    expected = plt.plot(x,y_cal,color='b', label = 'expected')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend([observed, expected], ["observed", "expected"])
    plt.text(1,7,chi) 
    plt.grid()
    
    return(chi_sq, m, c, y_cal)
