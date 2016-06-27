import numpy as np
import sys
import counter

def rosen(x0):
	x=x0[0]
	y=x0[1]
	return (1-x)*(1-x)+100*(y-x*x)*(y-x*x)

def gradrosen(x0):
	x=x0[0]
	y=x0[1]
	gradr=np.zeros(2)
	gradr[0]=400.*np.power(x,3)-2.*x*(200.*y-1)-2.
	gradr[1]=200.*y-200.*np.power(x,2)
	return gradr

def Hessrosen(x0):
	x=x0[0]
	y=x0[1]
	Hr=np.zeros((2,2))
	Hr[0,0]=1200.*np.power(x,2)-2.*(200.*y-1)
	Hr[0,1]=-400*x
	Hr[1,0]=-400*x
	Hr[1,1]=200.
	return Hr

def himmel(x0):
	x=x0[0]
	y=x0[1]
	return np.power(x*x+y-11, 2) + np.power(x+y*y-7, 2)

def gradhimmel(x0):
	x=x0[0]
	y=x0[1]
	gradh=np.zeros(2)
	gradh[0]=4.*np.power(x,3)+2*x*(2*y-21)+2*(np.power(y,2)-7)
	gradh[1]=4.*np.power(y,3)+2*y*(2*x-21)+2*(np.power(x,2)-11)
	return gradh

def Hesshimmel(x0):
	x=x0[0]
	y=x0[1]
	Hh=np.zeros((2,2))
	Hh[0,0]=12.*np.power(x,2)+2.*(2.*y-21.)
	Hh[0,1]=4.*y+4.*x
	Hh[1,0]=4.*x+4.*y
	Hh[1,1]=12.*np.power(y,2)+2.*(2.*x-13.)
	return Hh
