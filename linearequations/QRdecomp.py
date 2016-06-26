from __future__ import division
import math
import numpy as np

def QRdec(A):
    m = np.shape(A)[0]
    n = np.shape(A)[1]
    Q = np.zeros((m,n))
    R = np.zeros((n,n))

    a = []
    for i in range(n):
        a.append(A[:,i])
    q = []
    for i in range(n):
        R[i,i] = np.sqrt(sum(a[i]**2))
        q.append(a[i]/R[i,i])
        for j in range(i+1,n):
            R[i,j] = sum(q[i]*a[j])
            a[j]   = a[j]-q[i]*R[i,j]

    for i in range(n):
        Q[:,i] = q[i]

    return Q,R

def QRback(Q,R,b):
    n = np.shape(Q)[1]
    c = np.zeros(n)
    x = np.zeros(n)
    for i in range(n):
        for j in range(len(b)):
            c[i] += Q[j,i]*b[j]
    for i in reversed(range(n)):
        rx = 0
        for j in range(i+1,n):
            rx += R[i,j]*x[j]
        x[i] = (c[i]-rx)/R[i,i]
    return x

def QRdet(Q,R):
	m = np.shape(Q)[0]
	n = np.shape(Q)[1]
	det = 1
	for i in range(n):
		det *= R[i,i]
		if m != n:
			return "Not a square matrix"
		else:
			detR = np.absolute(det)
	return detR

def QRinverse(Q,R):
	m = np.shape(Q)[0]
	n = np.shape(Q)[1]
	Ainverse = np.zeros(np.shape(Q))
	for i in range(n):
		if m != n:
			return "Non invertible matrix"
		else:
			x = np.zeros(n)
			x[i] = 1
			Ainverse[:,i] = QRback(Q,R,x)
	return Ainverse
