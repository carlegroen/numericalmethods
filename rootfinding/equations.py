import numpy as np
import counter

def eq1(x0):
	x=x0[0]
	y=x0[1]
	A=10000.
	z=np.zeros(2)
	z[0]=A*x*y-1
	z[1]=np.exp(-x)+np.exp(-y)-1.-1./A
	counter.calls += 1
	return z

def deveq1(x0):
	x=x0[0]
	y=x0[1]
	A=10000.
	J=np.zeros((2,2))
	J[0,0]=A*y
	J[0,1]=A*x
	J[1,0]=-np.exp(-x)
	J[1,1]=-np.exp(-y)
	counter.calls += 1
	return J

def rosen(x0):
	x=x0[0]
	y=x0[1]
	z=np.zeros(2)
	z[0]=400*np.power(x,3)-2*x*(200*y-1)-2
	z[1]=200*y-200*np.power(x,2)
	counter.calls += 1
	return z

def devrosen(x0):
	x=x0[0]
	y=x0[1]
	J=np.zeros((2,2))
	J[0,0]=1200.*np.power(x,2)-2*(200*y-1)
	J[0,1]=-400.*x
	J[1,0]=-400.*x
	J[1,1]=200.
	counter.calls += 1
	return J


def himmel(x0):
	x=x0[0]
	y=x0[1]
	z=np.zeros(2)
	z[0]=4*np.power(x,3)+2*x*(2*y-21)+2*(np.power(y,2)-7)
	z[1]=4*np.power(y,3)+2*y*(2*x-13)+2*(np.power(x,2)-11)
	counter.calls += 1
	return z

def devhimmel(x0):
	x=x0[0]
	y=x0[1]
	J=np.zeros((2,2))
	J[0,0]=12*np.power(x,2)+2*(2*y-21)
	J[0,1]=4*x+4*y
	J[1,0]=4*y+4*x
	J[1,1]=12*np.power(y,2)+2*(2*x-13)
	counter.calls += 1
	return J
# def eq1(x0):
# 	x = x0[0]
# 	y = x0[1]
# 	A = 10000.
# 	z = np.zeros(2)
# 	z[0] = A * x * y - 1
# 	z[1] = 1 + 1/A - np.exp(-x) - np.exp(-y)
# 	counter.calls += 1
# 	return z
#
# def deveq1(x0):
# 	x = x0[0]
# 	y = x0[1]
# 	A = 10000.
# 	J = np.zeros((2,2))
# 	J[0,0] = A * y
# 	J[0,1] = A * x
# 	J[1,0] = -np.exp(-x)
# 	J[1,1] = -np.exp(-y)
# 	counter.calls += 1
# 	return J
#
# def rosen(x0):
# 	x = x0[0]
# 	y = x0[1]
# 	z = np.zeros(2)
# 	z[0] = 2*(1-x) - 400 * x * (y - x * x)
# 	z[1] = - 200 * (y - x * x)
# 	counter.calls += 1
# 	return z
#
# def devrosen(x0):
# 	x = x0[0]
# 	y = x0[1]
# 	J = np.zeros((2,2))
# 	J[0,0]= 1200. * np.power(x,2) - 2 * (200 * y - 1)
# 	J[0,1]= -400. * x
# 	J[1,0]= -400. * x
# 	J[1,1]= 200.
# 	counter.calls += 1
# 	return J
#
# def himmel(x0):
# 	x = x0[0]
# 	y = x0[1]
# 	z = np.zeros(2)
# 	z[0] = 4 * x * (x * x + y - 11) + 2 * (x + y * y - 7)
# 	z[1] = -2 * (x * x + y - 11) - 4 * y * (x + y * y - 7)
# 	counter.calls += 1
# 	return z
#
# def devhimmel(x0):
# 	x = x0[0]
# 	y = x0[1]
# 	J = np.zeros((2,2))
# 	J[0,0] = 12 * np.power(x,2) + 2 * (2 * y - 21)
# 	J[0,1] = 4 * x + 4 * y
# 	J[1,0] = 4 * y + 4 * x
# 	J[1,1] = 12 * np.power(y,2) + 2 * (2 * x - 13)
# 	counter.calls += 1
# 	return J
