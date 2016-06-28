import matplotlib.pyplot as plt
import numpy as np
import bilinearinterpolation as bilin
np.seterr(divide='ignore', invalid='ignore')

x = np.array([0,1])
y = np.array([0,1])
nx = len(x)
ny = len(y)
F = np.zeros((nx,ny))
n = np.zeros((nx*ny,3))

i = 0
j = 0

for i in range(len(x)):
    for j in range(len(y)):
        F[j][i] = x[i]*y[j]

k = 0
l = 0
for k in range(len(x)):
    n[0+len(x)*l:len(x)+len(x)*l,0] = x[l]
    n[0+len(x)*l:len(x)+len(x)*l,1] = y[l]
    l += 1

kappa = np.zeros((100,100))

count = 0
px = 0
countx = 0
while px < 1:
    county = 0
    count = 1
    py = 0
    while py < 1:
        #print count
        count += 1
        kappa[countx,county] = bilin.bilinear(x, y, F, px, py)
        county += 1
        py += 0.01
    px += 0.01
    countx +=1

plt.figure(1)
plt.contourf(x,y,F)
plt.colorbar()
plt.savefig('noninterpolated.png',format='png')

plt.figure(2)
plt.contourf(np.linspace(0,1,100),np.linspace(0,1,100),kappa,len(kappa))
plt.colorbar()
plt.savefig('interpolated.png',format='png')
