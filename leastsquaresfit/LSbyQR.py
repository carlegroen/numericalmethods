import math
import numpy as np
import sys
sys.path.append('/Users/carlee/Documents/numeric/linearequations')
from QRdecomp import *

def lsfit(x,y,dy,f):

	A = np.zeros((len(x),len(f)))
	b = np.zeros(len(x))

	for i in range(len(x)):
		b[i] = y[i]/dy[i]
		for k in range(len(f)):
			A[i,k] = f[k](x[i])/dy[i]
	Q,R = QRdec(A)
	c = QRback(Q,R,b)
	S = (np.dot(R.T,R))**(-1)
	return c,S
