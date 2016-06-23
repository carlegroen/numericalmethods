from __future__ import division
import numpy as np

#
# BINARY SEARCH
#

def bin(x,z):
	low=0
	high=len(x)-1
	while high-low>1:
		mid=int(round((high+low)/2))
		if z >= x[mid]:	low=mid
		else: high=mid
	return low

#
# POLYNOMIAL INTERPOLATION
#

def pinterp(x,y,z):
	ps=0
	for i in range(len(x)):
		p=1
		for k in range(len(x)):
			if k!=i:
				p*=(z-x[k])/(x[i]-x[k])
		ps+=y[i]*p
	return ps

#
# LINEAR SPLINE INTERPOLATION
#

def linterp(x,y,z):
	ls=np.zeros(len(z))
	dx=np.zeros(len(x))
	dy=np.zeros(len(x))
	for i in range(len(x)-1):
		dx[i] = x[i+1]-x[i]
		dy[i] = y[i+1]-y[i]
	for j in range(len(z)):
		l = search.bin(x,z[j])
		ls[j] = y[l]+(dy[l]/dx[l])*(z[j]-x[l])
	return ls

#
# QUADRATIC SPLINE INTERPOLATION
#

def qinterp(x,y,z):
	qs=np.zeros(len(z))
	dx=np.zeros(len(x))
	dy=np.zeros(len(x))
	a1=np.zeros(len(x))
	a2=np.zeros(len(x))
	a1[0]=0
	a2[-1]=0
	for i in range(len(x)-1):
		dx[i] = x[i+1]-x[i]
		dy[i] = y[i+1]-y[i]
	for j in range(len(x)-1):
		a1[j+1] = 1/dx[j+1]*(dy[j+1]/dx[j+1]-dy[j]/dx[j]-a1[j]*dx[j])
	for j in range(len(x)-3,-1,-1):
		a2[j] = 1/dx[j]*(dy[j+1]/dx[j+1]-dy[j]/dx[j]-a2[j+1]*dx[j+1])
		a=(a1+a2)/2
	for k in range(len(z)):
		l = search.bin(x,z[k])
		qs[k] = y[l] + dy[l]/dx[l]*(z[k]-x[l])+a[l]*(z[k]-x[l])*(z[k]-x[l+1])
	return qs
