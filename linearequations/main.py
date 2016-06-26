from QRdecomp import *
import time

start_time = time.time()

A = np.array([[2,3,1],[1,3,4],[1,2,1]])
b = np.array([[7],[15],[22]])

Q,R = QRdec(A)
A1  = np.dot(Q,R)
x   = QRback(Q,R,b)
detA = QRdet(Q,R)
Ain  = QRinverse(Q,R)
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
print "Time elapsed for QR-decomposition:", time.time() - start_time, "to run"
