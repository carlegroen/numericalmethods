import matplotlib.pyplot as plt
import numpy as np
import bilinearinterpolation as bilin
import bilinear_interpolation as bilinear
np.seterr(divide='ignore', invalid='ignore')




x = np.array([1, 2, 3])
y = np.array([1, 3, 5])
z = np.linspace(x[0],len(x),100)
nx = len(x)
ny = len(y)
F = np.zeros((nx,ny))
n = np.zeros((nx*ny,3))

print n
print("________")
i = 0
j = 0

for i in range(len(x)):
    for j in range(len(y)):
        F[j][i] = x[i]*y[j]

n[0][0] = x[0]





print np.prod(F.shape)
print("________")
print n

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
