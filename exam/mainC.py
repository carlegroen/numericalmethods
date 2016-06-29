import matplotlib.pyplot as plt
import numpy as np
import bicubicinterpolation as bicubic
np.seterr(divide='ignore', invalid='ignore')
np.set_printoptions(threshold=np.nan)


x = np.array([0,1,2,3])
y = np.array([0,1,2,3])
nx = len(x)
ny = len(y)
F = np.zeros((nx,ny))
n = np.zeros((nx*ny,3))
steplength = 0.02
interplength = 1.36
kappa = np.zeros((interplength/steplength,interplength/steplength))

i = 0
j = 0

#Define F matrix given a function. Here, it is sqrt(x^2+y^2)

# for i in range(len(x)):
#     for j in range(len(y)):
#         F[j][i] = np.sqrt(x[i]*x[i]+y[j]*y[j])

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
while px < interplength:
    county = 0
    count = 1
    py = 0
    while py < interplength:
        #print count
        count += 1
        kappa[countx,county] = bicubic.bicubiceval(px, py, F)[1]
        county += 1
        py += steplength
    px += steplength
    countx +=1

#Plots interpolated figure
plt.figure(2)
plt.title('Bicubic interpolation')
plt.contourf(np.linspace(min(x),max(x),countx),np.linspace(min(y),max(y),county),kappa,len(kappa))
plt.colorbar()
plt.savefig('interpolatedPartC.png',format='png')
