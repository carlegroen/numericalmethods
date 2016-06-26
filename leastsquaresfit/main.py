from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from LSbyQR import *


def f1(x):
	return np.sin(x)
def f2(x):
	return np.cos(x)
def f3(x):
	return np.sqrt(x)
def f4(x):
	return np.exp(x)
def f5(x):
	return x

f = [f1,f2,f3,f4,f5]

#generate 100 random pts to fit with least squares
x    = np.random.rand(30)*10
x.sort()
y    = np.cos(x)+np.sin(x)-np.sqrt(x)+np.exp(x/5)
dy   = np.random.random(len(x))
c1,S1 = lsfit(x,y,dy,f)

pts    = np.linspace(min(x),max(x),100)
fit1   = np.zeros(len(pts))
fit1pc = np.zeros(len(pts))
fit1mc = np.zeros(len(pts))
dc     = np.zeros(len(f))
for k in range(len(f)):
	fit1 += c1[k]*f[k](pts)

for i in range(len(f)):
	dc[i]=np.sqrt(S1[i,i])

for k in range(len(f)):
	fit1pc += (c1[k]+dc[k])*f[k](pts)

for k in range(len(f)):
	fit1mc += (c1[k]-dc[k])*f[k](pts)

plt.errorbar(x,y,yerr=dy,fmt='.',capsize=3,label='Generated data')
plt.plot(pts,fit1,'k',label="Least squares fit")
plt.plot(pts,fit1pc,'r',label="LS-fit + $\Delta$c(x)")
plt.plot(pts,fit1mc,'r',label="LS-fit - $\Delta$c(x)")
plt.title('Least squares fit')
plt.legend(loc=4)
plt.savefig('leastsquares.png',format='png')
