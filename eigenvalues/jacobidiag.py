from __future__ import division
import math
import numpy as np

def jacobi(A):

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
