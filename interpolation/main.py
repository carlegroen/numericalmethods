import matplotlib.pyplot as mp
import numpy as np
import interpolation as inter
np.seterr(divide='ignore', invalid='ignore')

data = np.loadtxt('test.dat')

x = data[:,0]
y = data[:,1]
z = np.linspace(x[0],len(x),100)
mp.plot(x,y,'bo',label='Given points')

# polynomial interpolation
f1 = inter.pinterp(x,y,z)
mp.plot(z,f1,label='Polynomial interpolation')


# linear spline interpolation
f2 = inter.linterp(x,y,z)
mp.plot(z,f2,label='Linear interpolation')


# quadratic spline interpolation
f3 = inter.qinterp(x,y,z)
mp.plot(z,f3,label='Quadratic interpolation')

# move legend to upper left, add shadows
legend = mp.legend(loc='upper left', shadow=True, fontsize='large')

# saving figure
mp.savefig('test.png',format='png')
