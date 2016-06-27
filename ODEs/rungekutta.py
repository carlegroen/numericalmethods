import numpy as np
from numpy import linalg as LA

def rk_step(f,t,y,h):
	k0 = f(t,y)
	k12 = f(t+h/2,y+h*k0/2)
	y1  = y + h * k12
	error = LA.norm((k12-k0)*h/2)

	return y1,error

def driver(f,a,b,y0,h,acc,eps):
	t = a
	y = y0
	tlist = [a]
	ylist = [y0]

	while t<b:
		if t+h>b:
			h=b-t
		[y1,dy]=rk_step(f,t,y,h)
		error=LA.norm(dy)
		tol=(LA.norm(y1)*eps+acc)*np.sqrt(h/(b-a))

		if error<tol:
			t+=h
			y=y1
			tlist.append(t)
			ylist.append(y)
		if error>0.:
			h*=np.power(tol/error,0.25)*0.95
	return [tlist,ylist,error]
