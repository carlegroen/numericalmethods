import numpy as np
from numpy import linalg as LA
import sys
sys.path.append('/Users/carlee/Documents/numeric/linearequations')
from givens import *

global calls

def newtons(f, xo, dx, eps):
	x = np.copy(xo)
	n = len(x)
	A = np.zeros((n,n))
	while True:
		fx = f(x)
		for j in range(n):
			x[j] += dx[j]
			df = f(x) - fx
			for i in range(n):
				A[i,j] = df[i]/dx[j]
			x[j] -= dx[j]
		Givens(A)
		Dx = -fx
		solve(A,Dx)
		alpha=2.0
		while True:
			alpha /= 2
			y = x + Dx * alpha
			fy = f(y)
			if(LA.norm(fy)<(1-alpha/2)*LA.norm(fx) or  alpha < 0.02):
				break
		x = y
		fx = fy
		if( LA.norm(Dx)<LA.norm(dx) or LA.norm(fx)<eps):
			break
	return x
