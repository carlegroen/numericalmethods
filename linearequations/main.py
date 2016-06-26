from QRdecomp import *
import time

start_time = time.time()

A = np.array([[-3,-3,2],[4,1,3],[-9,-4,1],[1,7,0]])
b = np.array([[8],[16],[11],[14]])

Q,R = qrdec(A)
A1  = np.dot(Q,R)
x   = qrback(Q,R,b)
detA = qrdet(Q,R)
Ain  = qrinverse(Q,R)
print("Vector A")
print(A)
print("Vector b")
print(b)
print("Q matrix of matrix A")
print(Q)
print("R matrix of matrix A")
print(R)
print("Solution to A * x = b")
print(x)
print("Absolute value of determinant of A")
print(detA)
print("Inverse matrix of A")
print(Ain)
print "Time elapsed for QR-decomposition", time.time() - start_time, "to run"
