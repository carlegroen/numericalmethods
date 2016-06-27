from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from LSbyQR import *


def f1(x):
	return 1/x
def f2(x):
	return 1
def f3(x):
	return x

f = [f1,f2,f3]

x    = [ 0.100, 0.145, 0.211, 0.307, 0.447, 0.649, 0.944, 1.372, 1.995, 2.900]
y    = [ 12.644, 9.235, 7.377, 6.460, 5.555, 5.896, 5.673, 6.964, 8.896, 11.355]
dy   = [ 0.858, 0.359, 0.505, 0.403, 0.683, 0.605, 0.856, 0.351, 1.083, 1.002]
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
