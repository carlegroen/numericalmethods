import matplotlib.pyplot as plt
import numpy as np
import bilinearinterpolation as bilin
import bilinear_interpolation as bilinear
np.seterr(divide='ignore', invalid='ignore')

x = np.array([0,1])
y = np.array([0,1])
z = np.linspace(x[0],len(x),100)
nx = len(x)
ny = len(y)
F = np.zeros((nx,ny))
n = np.zeros((nx*ny,3))

i = 0
j = 0

for i in range(len(x)):
    for j in range(len(y)):
        F[j][i] = 2*x[i]*y[j]

Flist = np.ravel(F)

k = 0
l = 0
for k in range(len(x)):
    n[0+len(x)*l:len(x)+len(x)*l,0] = x[l]
    n[0+len(x)*l:len(x)+len(x)*l,1] = y[l]
    l += 1

i = 0
for i in range(len(Flist)):
    n[i][2] = Flist[i]

kappa = np.zeros((100,100))
pxx = np.zeros(600)
pyy = np.zeros(600)

count = 0
px = 0.01

while px < 1:
    count = 1
    py = 0.01
    while py < 1:
        #print count
        count += 1
        kappa[px*100,py*100] = bilin.bilinear(x, y, F, px, py)
        py += 0.01
    px += 0.01

print kappa
# def column(matrix, i):
#     return [row[i] for row in matrix]
#
# xvals = column(n,0)
# yvals = column(n,1)
# Fvals = column(n,2)

plt.figure(1)
plt.contourf(x,y,F)
plt.colorbar()
plt.savefig('noninterpolated.png',format='png')

plt.figure(2)
plt.contourf(np.linspace(0,1,100),np.linspace(0,1,100),kappa,100)
plt.savefig('interpolated.png',format='png')


#
#
#
#
#
# plt.imshow(F)
# plt.savefig('test.png',format='png')
#
# print 'Original Array:'
# print [x,y]
#
# print 'F array'
# print F
#
# print 'Bilinear interpolation'
# print f1
