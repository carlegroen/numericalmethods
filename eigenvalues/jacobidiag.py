from __future__ import division
import math
import numpy as np



def jacobidiag(A):
        n = np.shape(A)[0]
	d = np.zeros(n)
	for i in range(n):
		d[i]=A[i,i]
    	V = np.matrix(np.identity(n))
    	sweeps = 0
    	rotated = True
    	while rotated:
        	rotated = False
        	for i in range(n-1):
            		for j in range(i+1,n):
                		rotated, sweeps=rotate(i,j,n,A,V,d,rotated,sweeps)
    	return d,V,sweeps


def rotate(p,q,n,A,V,d,rotated,sweeps):
	app = d[p]
	aqq = d[q]
	apq = A[p,q]
	phi = 0.5*np.arctan2(2.0*apq,aqq-app)
	c = np.cos(phi)
	s = np.sin(phi)
	App_new = c*c*app+s*s*aqq-2.0*s*c*apq
	Aqq_new = s*s*app+c*c*aqq+2.0*s*c*apq
	if (App_new != app) or (Aqq_new != aqq):
        	rotated = True
        	sweeps += 1
		d[p] = App_new
		d[q] = Aqq_new
		A[p,q] = 0.0
		for i in range(p):
			aip = A[i,p]
			aiq = A[i,q]
			A[i,p] = c*aip-s*aiq
			A[i,q] = c*aiq+s*aip
		for i in range(p+1,q):
			api = A[p,i]
			aiq = A[i,q]
			A[p,i] = c*api-s*aiq
			A[i,q] = c*aiq+s*api
		for i in range(q+1,n):
			api = A[p,i]
			aqi = A[q,i]
			A[p,i] = c*api-s*aqi
			A[q,i] = c*aqi+s*api
		for i in range(n):
			vip = V[i,p]
			viq = V[i,q]
			V[i,p] = c*vip-s*viq
			V[i,q] = c*viq+s*vip

	return rotated, sweeps
