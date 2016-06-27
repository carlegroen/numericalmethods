from __future__ import division
from integration import *
import numpy as np
import counter

def f(x):
	f=x*x*x
	return f
a=0.
b=1.
acc=1e-3
eps=1e-3


exact=1/4

qtype=0


Qc,errorc = adapt(f,a,b,acc,eps,qtype)
print 'Integral of x^3 from 0 to 1'
print 'Exact result:\n',exact
print 'The closed sets integral is:\n',Qc
print '# of integrand calls:', counter.calls
print 'Estimated error:\n',errorc


qtype=1
counter.calls=0
Qo,erroro=adapt(f,a,b,acc,eps,qtype)
print 'The open sets integral is:\n',Qo
print '# of integrand calls:', counter.calls
print 'Estimated error:\n',erroro

def f1(x):
	f=4*np.sqrt(1-np.power((1-x),2))
	return f
print '\n'
print 'Integral of 4*sqrt(1-(1-x)^2) from 0 to 1'
qtype = 0
exact1 = np.pi
Qc2,errorc2 = adapt(f1,a,b,acc,eps,qtype)
print 'Exact result:\n',exact1
print 'The closed sets integral is:\n',Qc2
print '# of integrand calls:', counter.calls
print 'Estimated error is\n',errorc2

acc1 = 1e-3
eps1 = 1e-3

qtype=1
counter.calls=0
Qo2,erroro2=adapt(f1,a,b,acc1,eps1,qtype)
print 'The open sets integral is:\n',Qo2
print '# of integrand calls=', counter.calls
print 'Estimated error is\n',erroro2
