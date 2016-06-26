from __future__ import division
import math
import numpy as np
from QRdecomp import *

def Givens(A):
    m = np.shape(A)[0]
    n = np.shape(A)[1]
    for q in range(n):
    	for p in range(q+1,m):
	    phi = np.arctan2(A[p,q],A[q,q])
            for k in range(q,n):
                xq = A[q,k]
               	xp = A[p,k]
               	A[q,k] = xq*np.cos(phi)+xp*np.sin(phi)
               	A[p,k] = -xq*np.sin(phi)+xp*np.cos(phi)
	    A[p,q] = phi



def giv_QT(QR,b):
     m = np.shape(QR)[0]
     n = np.shape(QR)[1]
     for q in range(n):
         for p in range(q+1,m):
             phi = QR[p,q]
             bq  = b[q]
             bp  = b[p]
             b[q]= bq*np.cos(phi)+bp*np.sin(phi)
             b[p]= -bq*np.sin(phi)+bp*np.cos(phi)



def giv_backsub(QR,b):
    n = np.shape(QR)[1]
    for i in reversed(range(n)):
	s = b[i]
        for k in range(i+1,n):
            s -= QR[i,k]*b[k]
        b[i] = s/QR[i,i]

def solve(QR,b):
	giv_QT(QR,b)
	giv_backsub(QR,b)


def det(QR):
	m = np.shape(QR)[0]
	n = np.shape(QR)[1]
	detQR = 1.
	for i in range(n):
		detQR *= QR[i,i]
		if m != n:
			return "Not a square matrix"
		else:
			detQR = np.absolute(detQR)
   	return detQR

def inverseB(QR,Ainv):
	m = np.shape(QR)[0]
	n = np.shape(QR)[1]
	for i in range(n):
		Ainv[i,i] = 1
	for i in range(n):
		if m != n:
			return "Non-invertible matrix"
		else:
			solve(QR,Ainv[:,i])
