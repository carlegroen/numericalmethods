from __future__ import division
import numpy as np
from montecarlo import *
import matplotlib.pyplot as plt

print "Monte Carlo integration:"
pii = np.pi
def f1(x):
	f = 1/((1 - np.cos(x[0]) * np.cos(x[1]) * np.cos(x[2])) * np.power(pii,3))
	return f
a1 = np.array([0,0,0])
b1 = np.array([pii,pii,pii])
N  = np.power(10,7) #long compilation time. no fucks given

vec1,error1 = monte(f1,a1,b1,N)


def f2(x):
	f = np.cos(x[0])*np.power(x[1],2)
	return f
a2 = np.array([0,0,0])
b2 = np.array([pii/2,3,1])
N1 = [10,100,1000,10000,100000,1000000]
n  = 6
t  = list(range(10,1000000))
error2 = np.zeros(n)
vec2=np.zeros(n)
for i in range(n):
	N=np.power(10,i+1)
	vec2[i],error2[i]=monte(f2,a2,b2,N)
print "Calculate the integral cos(x)*y^2 from 0 to pi/2 and 0 to 3"
print "Monte Carlo with N from 10^1 to 10^7:"
print vec2
print "Exact result:", 9
plt.figure()
plt.title("Plot of error as function of N")
plt.loglog(N1,error2,'x',label="error as function of N")
plt.loglog(t,9./np.sqrt(t),label="fit: a/sqrt(N)")
plt.legend(loc=1)
plt.savefig('MonteCarlo.png',format='png')
print "Calculate the integral given in the assignment"
print "Monte carlo with N=10^7:", vec1
print "The result given is", 1.3932039296856768591842462603255
