from __future__ import division
import numpy as np
import search
np.seterr(divide='ignore', invalid='ignore')

def cinterp(p, a):
	return p[1] + 0.5 * a * (p[2] - p[0] + a * (2.0 * p[0] - 5.0*p[1] + 4.0*p[2] - p[3] + a*(3.0*(p[1] - p[2]) + p[3] - p[0])))

def bicubiceval(x,y,p):
	interp = np.zeros((4,4))
	interp[0] = cinterp(p[:,0],y)
	interp[1] = cinterp(p[:,1],y)
	interp[2] = cinterp(p[:,2],y)
	interp[3] = cinterp(p[:,3],y)
	return cinterp(interp,x)
