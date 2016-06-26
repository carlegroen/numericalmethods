import matplotlib.pyplot as plt
import numpy as np
import interpolation as inter
np.seterr(divide='ignore', invalid='ignore')

data = np.loadtxt('test.dat')

x = data[:,0]
y = data[:,1]
z = np.linspace(x[0],len(x),100)
plt.plot(x,y,'bo',label='Given points')

# linear spline interpolation
f1 = inter.linterp(x,y,z)
plt.plot(z,f1,label='Linear interpolation')

# quadratic spline interpolation
f2 = inter.qinterp(x,y,z)
plt.plot(z,f2,label='Quadratic interpolation')

# move legend to upper left, add shadows
legend = plt.legend(loc='upper left', shadow=True, fontsize='large')

# saving figure
plt.savefig('test.png',format='png')
