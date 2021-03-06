import matplotlib.pyplot as plt
import numpy as np
import bilinearinterpolation as bilin
np.seterr(divide='ignore', invalid='ignore')

x = np.array([0,1,2,3])
y = np.array([0,1,2,3])
nx = len(x)
ny = len(y)
F = np.zeros((nx,ny))
n = np.zeros((nx*ny,3))
steplength = 0.02
kappa = np.zeros((max(x)/steplength,max(y)/steplength))

i = 0
j = 0

#Define F matrix given a function. Here, it is sqrt(x^2+y^2)

for i in range(len(x)):
    for j in range(len(y)):
        F[j][i] = np.sqrt(x[i]*x[i]+y[j]*y[j])

#Defining F after a matrix with known looks
F[0][0] = 1.0
F[1][0] = 3.0
F[2][0] = 6.0
F[3][0] = 4.0
F[0][1] = 1.0
F[1][1] = 2.0
F[2][1] = 3.0
F[3][1] = 5.0
F[0][2] = 2.0
F[1][2] = 4.0
F[2][2] = 3.0
F[3][2] = 1.0
F[0][3] = 5.0
F[1][3] = 3.0
F[2][3] = 2.0
F[3][3] = 3.0


#Starts performing the bilinear interpolation in correct sequence
count = 0
px = 0
countx = 0
while px < max(x):
    county = 0
    count = 1
    py = 0
    while py < max(y):
        #print count
        count += 1
        kappa[countx,county] = bilin.bilinear(x, y, F, px, py)
        county += 1
        py += steplength
    px += steplength
    countx +=1

#Plots non-interpolated figure
plt.figure(1)
plt.contourf(x,y,F)
plt.colorbar()
plt.title('Non-interpolated dataset')
plt.savefig('noninterpolatedPartB.png',format='png')

#Plots interpolated figure
plt.figure(2)
plt.contourf(np.linspace(min(x),max(x),countx),np.linspace(min(y),max(y),county),kappa,len(kappa))
plt.colorbar()
plt.title('Bilinear interpolation')
plt.savefig('interpolatedPartB.png',format='png')
