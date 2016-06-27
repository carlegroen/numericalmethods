import numpy as np
import counter
from equations import *
from minimization import *

x0 = np.array([-5.,6.])
print "Starting points=",x0
counter.calls=0
rosenmini=newtonmini(rosen, x0, gradrosen, Hessrosen)
print "Minimum of Rosenbrock's valley function:"
print rosenmini
print "steps used:"
print counter.calls
print "\n"

x1=np.array([-4.,8.])
counter.calls=0
print "Starting points=",x1
himmelmini=newtonmini(himmel, x1, gradhimmel, Hesshimmel)
print "Minimum of Himmelblau function:"
print himmelmini
print "steps used:"
print counter.calls
print "\n"
