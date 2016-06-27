import numpy as np
from numpy import linalg as LA
import sys
sys.path.append('/Users/carlee/Documents/numeric/linearequations')
from givens import *

def jacnewtons(f, xo, Jacf, eps):
	x=np.copy(xo)
	n=len(x)
	J=np.zeros((n,n))
	while True:
		fx=f(x)
		J=Jacf(x)
		Givens(J)
		Dx = -fx
		solve(J,Dx)
		alpha=2.0
		while True:
			alpha/=2
			y=x+Dx*alpha
			fy=f(y)
			if(LA.norm(fy)<(1-alpha/2)*LA.norm(fx) or  alpha < 0.02):
				break
		x=y
		fx=fy
		if(LA.norm(fx)<eps):
			break
	return x
