from __future__ import division
import random
import numpy as np

def random_x(a,b):
	n=len(a)
	x=np.zeros(n)
	for i in range(n):
		x[i]=a[i]+random.random()*(b[i]-a[i])
	return x

def monte(func,a,b,N):
	sum1 = 0
	sum2 = 0
	vol  = 1
	for i in range(len(a)):
		vol *= (b[i] - a[i])
	for i in range(N):
		f = func(random_x(a,b))
		sum1 += f
		sum2 += np.power(f,2)
	mean  = sum1/N
	sigma = np.sqrt(sum2/N - mean * mean)
	SIGMA = sigma/np.sqrt(N)
	q     = mean * vol
	error   = SIGMA * vol
	return q,error
