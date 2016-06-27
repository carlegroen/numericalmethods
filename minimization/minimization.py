import numpy as np
import counter
import sys
from equations import *
import sys
sys.path.append('/Users/carlee/Documents/numeric/linearequations')
from givens import *
import numpy.linalg as LA



def newtonmini(f, xo, gradf, Hess):
	alpha=1e-5
	eps=1e-10
	x=np.copy(xo)
	n=len(x)
	fx=f(x)
	gf=gradf(x)
	H=np.zeros((n,n))
	while True:
		counter.calls +=1
		H=Hess(x)
		Givens(H)
		Dx = -gf
		solve(H,Dx)
		lamb=2.0
		dot=np.dot(gf,Dx)
		while True:
			lamb/=2.
			y=x+Dx*lamb
			fy=f(y)
			if(fy < fx+alpha*lamb*dot or lamb < 0.002):
				break
		x = y
		fx = fy
		gf=gradf(x)
		if(LA.norm(gf)<eps):
			break
	return x
