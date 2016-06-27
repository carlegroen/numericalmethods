import numpy as np
from rungekutta import *
import matplotlib.pyplot as plt

def f(x,y):
	return np.array([y[1],-y[0]])

acc=1e-3
eps=1e-3
step=1e-1
ystart=np.array([0,1])

[t,y,error] = driver(f,0.,10.,ystart,step,acc,eps)
plt.figure()
plt.title('Solution to d^2y/dx^2 = y given y(0) = 0 and y(0) = 1 ')
plt.plot(t,y,'rx',label="numerical")
plt.plot(t,np.cos(t),label="Cos(x)")
plt.plot(t,np.sin(t),'b',label="Sin(x)")
plt.legend(loc=3)
plt.savefig('yplot.png',format='png')

def f(x,y):
	f=np.sin(y)
	return f

[t,y1,error] = driver(f,0.,10.,1.,step,acc,eps)
plt.figure()
plt.title('Solution to dy/dx=sin(y) given y(0)=1')
plt.plot(t,y1,'rx',label="numerical")
plt.legend(loc=4)
plt.savefig('sinplot.png',format='png')
