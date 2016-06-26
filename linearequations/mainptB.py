from __future__ import division
from QRdecomp import *
from givens import *
import time
import numpy as np
np.seterr(divide='ignore', invalid='ignore')

print("Test on square matrix")
A = np.array([[2,3,1],[1,3,4],[1,2,1]])
b = np.array([[7],[15],[22]])
Ainv = np.zeros(np.shape(A))
A_norm = np.copy(A)

AGiv = Givens(A)
detA = det(A)

print("Un-changed matrix A ")
print(A_norm)
print("Vector b")
print(b)
print("Givens rotation of matrix A")
print(AGiv)
print("Solution to A * x = b")
solve(A,b)
print(b)
print("Check that A * x = b")
print(np.dot(A_norm,b))
print("|Det(A)|")
print(detA)
print("Inverse matrix of A")
inverseB(A,Ainv)
print(Ainv)
print("Check that A * Ainverse is the identity matrix I")
print(np.dot(A_norm,Ainv))
print("Test on non quadratic matrix")
A1=np.array([[-4.,-4.,2.],[0.,2.,4.],[-3.,-2.,3.],[0.,2.,5.]])
print("Q matrix of A")
print("Matrix A")
print(A1)
Givens(A1)
print("Givens rotation of A")
print(A1)
print("200 x 200 matrix speed-test:")
a2=np.random.random((200, 200))
b2=np.random.random(200)

start_time = time.time()
Q2,R2=QRdec(a2)
x2=QRback(Q2,R2,b2)
print "Gram-Schmidt decomposition solved in:", time.time() - start_time, "seconds"

start_time2 = time.time()
Givens(a2)
solve(a2,b2)
print "Givens solved in:", time.time() - start_time2, "seconds"
