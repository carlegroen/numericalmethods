import numpy as np
from findroots import *
from equations import *
from jacobiroots import *
import counter

#Start conditions
eps=1e-12
x0=np.array([1.,-1.])
x1=np.array([-1.,4.])
x2=np.array([2.,-7.])
dx=np.array([1e-8,1e-8])

print "Roots of A*x*y-1 and exp(-x)+exp(-y)-1.-1./A, A=10000"
print "Startpoints=",x0
print "Numerical estimate of the jacobian"
counter.calls=0
res=newtons(eq1, x0, dx, eps)
print "Roots=",res
print "Number of call to function"
print counter.calls
print "\n"

counter.calls=0
res=jacnewtons(eq1, x0, deveq1, eps)
print "User supplied jacobian"
print "Roots=",res
print "Number of call to function"
print counter.calls
print "\n"

counter.calls=0
rosenres=newtons(rosen,x0, dx, eps)
print "Roots of Rosenbrock's valley function"
print "Startpoints=",x1
print "Numerical estimate of the jacobian"
print "Roots=",rosenres
print "Number of call to function"
print counter.calls
print "\n"

counter.calls=0
rosenres=jacnewtons(rosen,x0, devrosen, eps)
print "User supplied jacobian"
print "Startpoints=",x1
print "Roots=",rosenres
print "Number of call to function"
print counter.calls
print "\n"

counter.calls=0
himmelres=newtons(himmel,x0, dx, eps)
print "Roots of Himmelblau function"
print "Startpoints=",x2
print "Numerical estimate of the jacobian"
print "Roots=",himmelres
print "Number of call to function"
print counter.calls
print "\n"

counter.calls=0
himmelres=jacnewtons(himmel,x0, devhimmel, eps)
print "User supplied jacobian"
print "Startpoints=",x2
print "Roots=",himmelres
print "Number of call to function"
print counter.calls
print "\n"
