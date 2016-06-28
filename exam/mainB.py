import matplotlib.pyplot as plt
import numpy as np
import bilinearinterpolation as bilin
np.seterr(divide='ignore', invalid='ignore')

x = np.array([0,1,3])
y = np.array([0,1,3])
nx = len(x)
ny = len(y)
F = np.zeros((nx,ny))
n = np.zeros((nx*ny,3))

i = 0
j = 0

for i in range(len(x)):
    for j in range(len(y)):
        F[j][i] = np.sin(x[i]*x[i]+y[j]*y[j])#x[j]*x[j]-y[i]*y[i]

print F

k = 0
l = 0
for k in range(len(x)):
    n[0+len(x)*l:len(x)+len(x)*l,0] = x[l]
    n[0+len(x)*l:len(x)+len(x)*l,1] = y[l]
    l += 1

kappa = np.zeros((150,150))

count = 0
px = 0
countx = 0
while px < 3:
    county = 0
    count = 1
    py = 0
    while py < 3:
        #print count
        count += 1
        kappa[countx,county] = bilin.bilinear(x, y, F, px, py)
        county += 1
        py += 0.02
    px += 0.02
    countx +=1



plt.figure(1)
plt.contourf(x,y,F)
plt.colorbar()
plt.savefig('noninterpolatedPartB.png',format='png')

plt.figure(2)
plt.contourf(np.linspace(0,3,countx),np.linspace(0,3,county),kappa,len(kappa))
plt.colorbar()
plt.savefig('interpolatedPartB.png',format='png')
