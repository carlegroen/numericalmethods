import matplotlib.pyplot as mp
import numpy as np
import interpolation as inter

x = np.linspace(0,10,10)
y = [0,0,0,0,0,1,1,1,1,1]
z = np.linspace(x[0],len(x),100)
mp.plot(x,y,'bo')


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
mp.savefig('stepwise.png',format='png')

# prints text in command line
print 'Figures saved as .png'
